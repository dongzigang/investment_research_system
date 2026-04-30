from .base_agent import BaseAgent

class RiskAssessorAgent(BaseAgent):
    def __init__(self):
        super().__init__("风险评估Agent")
    
    def process(self, data: dict) -> dict:
        extracted_info = data.get("extracted_info", {})
        analysis_result = data.get("analysis_result", {})
        company_name = data.get("company_name", "未知公司")
        
        self.logger.info(f"对 {company_name} 进行多维度风险评估")
        
        key_metrics = extracted_info.get("key_metrics", {})
        risk_flags = extracted_info.get("risk_flags", [])
        
        # 风险评估矩阵
        risk_assessment = {
            "财务风险": self._assess_financial_risk(key_metrics),
            "市场风险": self._assess_market_risk(key_metrics),
            "经营风险": self._assess_operation_risk(key_metrics, analysis_result),
            "综合风险等级": ""
        }
        
        # 计算综合风险等级
        risk_scores = {
            "低风险": 1,
            "中风险": 2,
            "高风险": 3
        }
        
        total_risk = sum([
            risk_scores.get(risk_assessment["财务风险"], 2),
            risk_scores.get(risk_assessment["市场风险"], 2),
            risk_scores.get(risk_assessment["经营风险"], 2)
        ])
        
        if total_risk <= 3:
            risk_assessment["综合风险等级"] = "低风险"
        elif total_risk <= 6:
            risk_assessment["综合风险等级"] = "中风险"
        else:
            risk_assessment["综合风险等级"] = "高风险"
        
        # 风险缓解建议
        mitigation_suggestions = []
        if risk_assessment["财务风险"] == "高风险":
            mitigation_suggestions.append("关注公司债务结构和现金流状况")
        if risk_assessment["市场风险"] == "高风险":
            mitigation_suggestions.append("注意市场波动，设置止损位")
        if risk_assessment["经营风险"] == "高风险":
            mitigation_suggestions.append("密切关注行业竞争和公司战略调整")
        
        if not mitigation_suggestions:
            mitigation_suggestions.append("当前风险可控，建议持续跟踪")
        
        self.logger.info(f"风险评估完成，综合风险等级: {risk_assessment['综合风险等级']}")
        
        return {
            "stock_code": data.get("stock_code"),
            "company_name": company_name,
            "risk_assessment": risk_assessment,
            "mitigation_suggestions": mitigation_suggestions,
            "analysis_result": analysis_result,
            "extracted_info": extracted_info,
            "reasoning": data.get("reasoning", []),
            "raw_data_file": data.get("raw_data_file")
        }
    
    def _assess_financial_risk(self, metrics):
        debt_ratio = metrics.get("偿债能力", {}).get("资产负债率", 0)
        roe = metrics.get("盈利能力", {}).get("ROE", 0)
        
        if debt_ratio > 0.6 or roe < 0.08:
            return "高风险"
        elif debt_ratio > 0.5 or roe < 0.12:
            return "中风险"
        else:
            return "低风险"
    
    def _assess_market_risk(self, metrics):
        pe = metrics.get("估值指标", {}).get("市盈率", 0)
        pb = metrics.get("估值指标", {}).get("市净率", 0)
        
        if pe > 40 or pb > 4:
            return "高风险"
        elif pe > 25 or pb > 3:
            return "中风险"
        else:
            return "低风险"
    
    def _assess_operation_risk(self, metrics, analysis):
        growth = metrics.get("成长性", {}).get("营收增长率", 0)
        rating = analysis.get("综合评级", "持有")
        
        if growth < 0 or rating == "卖出":
            return "高风险"
        elif growth < 0.1 or rating == "持有":
            return "中风险"
        else:
            return "低风险"
