from .base_agent import BaseAgent
import json

class InfoExtractorAgent(BaseAgent):
    def __init__(self):
        super().__init__("信息抽取Agent")
    
    def process(self, data: dict) -> dict:
        collected_data = data.get("collected_data", {})
        company_name = data.get("company_name", "未知公司")
        
        self.logger.info(f"从 {company_name} 的采集数据中提取关键信息")
        
        financial = collected_data.get("financial", {})
        market = collected_data.get("market", {})
        announcements = collected_data.get("announcements", [])
        
        # 提取关键财务指标
        key_metrics = {
            "盈利能力": {
                "ROE": financial.get("roe", 0),
                "利润率": round(financial.get("profit", 0) / max(financial.get("revenue", 1), 1), 4)
            },
            "偿债能力": {
                "资产负债率": financial.get("debt_ratio", 0),
                "资产规模": financial.get("assets", 0)
            },
            "成长性": {
                "营收增长率": financial.get("growth_rate", 0)
            },
            "估值指标": {
                "市盈率": market.get("pe_ratio", 0),
                "市净率": market.get("pb_ratio", 0),
                "股价": market.get("current_price", 0)
            }
        }
        
        # 提取公告要点
        announcement_summary = []
        for ann in announcements:
            announcement_summary.append({
                "日期": ann.get("date"),
                "类型": ann.get("type"),
                "标题": ann.get("title")
            })
        
        # 识别关键风险点（简单规则）
        risk_flags = []
        if financial.get("debt_ratio", 0) > 0.6:
            risk_flags.append("资产负债率偏高")
        if financial.get("roe", 0) < 0.1:
            risk_flags.append("ROE偏低，盈利能力不足")
        if market.get("pe_ratio", 0) > 30:
            risk_flags.append("市盈率较高，估值偏贵")
        
        extracted_info = {
            "key_metrics": key_metrics,
            "announcement_summary": announcement_summary,
            "risk_flags": risk_flags,
            "data_quality": "高"
        }
        
        self.logger.info(f"提取完成，发现 {len(risk_flags)} 个风险点")
        
        return {
            "stock_code": data.get("stock_code"),
            "company_name": company_name,
            "extracted_info": extracted_info,
            "raw_data_file": data.get("raw_data_file")
        }
