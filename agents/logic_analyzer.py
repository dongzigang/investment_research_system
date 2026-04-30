from .base_agent import BaseAgent

class LogicAnalyzerAgent(BaseAgent):
    def __init__(self):
        super().__init__("逻辑推理Agent")
    
    def process(self, data: dict) -> dict:
        extracted_info = data.get("extracted_info", {})
        company_name = data.get("company_name", "未知公司")
        
        self.logger.info(f"对 {company_name} 进行多维度逻辑推理分析")
        
        key_metrics = extracted_info.get("key_metrics", {})
        risk_flags = extracted_info.get("risk_flags", [])
        
        # 多维度交叉验证分析
        analysis_result = {
            "财务健康度": self._analyze_financial_health(key_metrics),
            "估值合理性": self._analyze_valuation(key_metrics),
            "成长性评估": self._analyze_growth(key_metrics),
            "综合评级": ""
        }
        
        # 综合评级逻辑
        score = 0
        if analysis_result["财务健康度"] == "良好":
            score += 2
        elif analysis_result["财务健康度"] == "一般":
            score += 1
        
        if analysis_result["估值合理性"] == "合理":
            score += 2
        elif analysis_result["估值合理性"] == "偏高":
            score += 0
        
        if analysis_result["成长性评估"] == "优秀":
            score += 2
        elif analysis_result["成长性评估"] == "良好":
            score += 1
        
        if score >= 5:
            analysis_result["综合评级"] = "买入"
        elif score >= 3:
            analysis_result["综合评级"] = "持有"
        else:
            analysis_result["综合评级"] = "卖出"
        
        # 逻辑推理解释
        reasoning = []
        reasoning.append(f"财务健康度: {analysis_result['财务健康度']}")
        reasoning.append(f"估值合理性: {analysis_result['估值合理性']}")
        reasoning.append(f"成长性评估: {analysis_result['成长性评估']}")
        reasoning.append(f"基于以上分析，综合评级为: {analysis_result['综合评级']}")
        
        self.logger.info(f"逻辑推理完成，综合评级: {analysis_result['综合评级']}")
        
        return {
            "stock_code": data.get("stock_code"),
            "company_name": company_name,
            "analysis_result": analysis_result,
            "reasoning": reasoning,
            "extracted_info": extracted_info,
            "raw_data_file": data.get("raw_data_file")
        }
    
    def _analyze_financial_health(self, metrics):
        debt_ratio = metrics.get("偿债能力", {}).get("资产负债率", 0)
        roe = metrics.get("盈利能力", {}).get("ROE", 0)
        
        if debt_ratio < 0.5 and roe > 0.15:
            return "良好"
        elif debt_ratio < 0.6 and roe > 0.1:
            return "一般"
        else:
            return "较差"
    
    def _analyze_valuation(self, metrics):
        pe = metrics.get("估值指标", {}).get("市盈率", 0)
        pb = metrics.get("估值指标", {}).get("市净率", 0)
        
        if pe < 15 and pb < 2:
            return "合理"
        elif pe < 25 and pb < 3:
            return "偏高"
        else:
            return "过高"
    
    def _analyze_growth(self, metrics):
        growth = metrics.get("成长性", {}).get("营收增长率", 0)
        
        if growth > 0.2:
            return "优秀"
        elif growth > 0.1:
            return "良好"
        elif growth > 0:
            return "一般"
        else:
            return "负增长"
