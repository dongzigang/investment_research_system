from agents import (
    DataCollectorAgent,
    InfoExtractorAgent,
    LogicAnalyzerAgent,
    RiskAssessorAgent,
    ReportGeneratorAgent
)
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MainCoordinator")

class ResearchCoordinator:
    def __init__(self):
        self.data_collector = DataCollectorAgent()
        self.info_extractor = InfoExtractorAgent()
        self.logic_analyzer = LogicAnalyzerAgent()
        self.risk_assessor = RiskAssessorAgent()
        self.report_generator = ReportGeneratorAgent()
        
    def run_research(self, stock_code: str) -> dict:
        logger.info(f"开始对股票 {stock_code} 进行智能投研分析")
        logger.info("="*50)
        
        # 1. 数据采集
        step1_result = self.data_collector.run({"stock_code": stock_code})
        if step1_result["status"] == "error":
            return step1_result
        data = step1_result["data"]
        
        # 2. 信息抽取
        step2_result = self.info_extractor.run(data)
        if step2_result["status"] == "error":
            return step2_result
        data = step2_result["data"]
        
        # 3. 逻辑推理
        step3_result = self.logic_analyzer.run(data)
        if step3_result["status"] == "error":
            return step3_result
        data = step3_result["data"]
        
        # 4. 风险评估
        step4_result = self.risk_assessor.run(data)
        if step4_result["status"] == "error":
            return step4_result
        data = step4_result["data"]
        
        # 5. 报告生成
        step5_result = self.report_generator.run(data)
        if step5_result["status"] == "error":
            return step5_result
        
        logger.info("="*50)
        logger.info(f"智能投研分析完成！")
        logger.info(f"股票: {step5_result['data']['company_name']}({step5_result['data']['stock_code']})")
        logger.info(f"评级: {step5_result['data']['report_summary']['评级']}")
        logger.info(f"风险等级: {step5_result['data']['report_summary']['风险等级']}")
        logger.info(f"报告文件: {step5_result['data']['report_file']}")
        logger.info("="*50)
        
        return {
            "status": "success",
            "workflow": "数据采集→信息抽取→逻辑推理→风险评估→报告生成",
            "result": step5_result["data"]
        }
