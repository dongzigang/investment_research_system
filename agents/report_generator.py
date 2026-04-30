from .base_agent import BaseAgent
from config import REPORT_DIR
import json
import os
from datetime import datetime

class ReportGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("报告生成Agent")
    
    def process(self, data: dict) -> dict:
        company_name = data.get("company_name", "未知公司")
        stock_code = data.get("stock_code", "")
        
        self.logger.info(f"为 {company_name} 生成结构化投资分析报告")
        
        # 生成Markdown格式报告
        report_content = self._generate_markdown_report(data)
        
        # 保存报告
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = os.path.join(REPORT_DIR, f"{stock_code}_{timestamp}_report.md")
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        # 同时保存JSON格式的完整数据
        json_file = os.path.join(REPORT_DIR, f"{stock_code}_{timestamp}_data.json")
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        self.logger.info(f"报告已生成: {report_file}")
        
        return {
            "stock_code": stock_code,
            "company_name": company_name,
            "report_file": report_file,
            "json_file": json_file,
            "report_summary": self._get_summary(data)
        }
    
    def _generate_markdown_report(self, data):
        company_name = data.get("company_name", "")
        stock_code = data.get("stock_code", "")
        extracted_info = data.get("extracted_info", {})
        analysis_result = data.get("analysis_result", {})
        risk_assessment = data.get("risk_assessment", {})
        reasoning = data.get("reasoning", [])
        mitigation = data.get("mitigation_suggestions", [])
        
        report = f"""# {company_name}({stock_code}) 投资分析报告

**生成时间**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

## 一、核心财务指标

"""
        
        key_metrics = extracted_info.get("key_metrics", {})
        for category, metrics in key_metrics.items():
            report += f"### {category}\n"
            for metric, value in metrics.items():
                if isinstance(value, float):
                    report += f"- **{metric}**: {value:.4f}\n"
                else:
                    report += f"- **{metric}**: {value}\n"
            report += "\n"
        
        report += """---

## 二、逻辑推理分析

"""
        for item in reasoning:
            report += f"{item}\n\n"
        
        report += f"""---

## 三、风险评估

### 综合风险等级: **{risk_assessment.get('综合风险等级', '未知')}**

#### 细分风险:
- 财务风险: {risk_assessment.get('财务风险', '未知')}
- 市场风险: {risk_assessment.get('市场风险', '未知')}
- 经营风险: {risk_assessment.get('经营风险', '未知')}

#### 风险缓解建议:
"""
        for suggestion in mitigation:
            report += f"- {suggestion}\n"
        
        report += f"""
---

## 四、投资建议

**综合评级**: {analysis_result.get('综合评级', '未知')}

### 关键风险点:
"""
        risk_flags = extracted_info.get("risk_flags", [])
        if risk_flags:
            for flag in risk_flags:
                report += f"- ⚠️ {flag}\n"
        else:
            report += "- ✅ 未发现明显风险点\n"
        
        report += f"""
---

## 五、公告摘要

"""
        announcements = extracted_info.get("announcement_summary", [])
        for ann in announcements:
            report += f"- **{ann.get('日期')}** [{ann.get('类型')}] {ann.get('标题')}\n"
        
        report += f"""
---

*本报告由智能投研Agent系统自动生成，仅供参考，不构成投资建议。*
"""
        
        return report
    
    def _get_summary(self, data):
        return {
            "公司": data.get("company_name"),
            "股票代码": data.get("stock_code"),
            "评级": data.get("analysis_result", {}).get("综合评级"),
            "风险等级": data.get("risk_assessment", {}).get("综合风险等级")
        }
