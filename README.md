# 智能投研 Agent 系统

基于多 Agent 协作的自动化投资分析系统，能够自主完成从数据采集到报告生成的完整投研流程。

## 系统架构

```
数据采集Agent → 信息抽取Agent → 逻辑推理Agent → 风险评估Agent → 报告生成Agent
```

## 功能特性

- **数据采集**: 模拟采集财报、公告和市场数据
- **信息抽取**: 提取关键财务指标和风险点
- **逻辑推理**: 多维度交叉验证分析
- **风险评估**: 财务/市场/经营三维风险评估
- **报告生成**: 自动生成结构化Markdown报告

## 快速开始

### 运行单个股票分析
```bash
cd E:\agent-sys\investment_research_system
python main.py
# 或指定股票代码
python main.py 600519
```

### 批量测试所有股票
```bash
python test_system.py
```

## 内置股票列表

| 代码 | 名称 |
|------|------|
| 000001 | 平安银行 |
| 600519 | 贵州茅台 |
| 000858 | 五粮液 |
| 601318 | 中国平安 |
| 600036 | 招商银行 |

## 输出说明

运行后会在 `reports/` 目录生成：
- `XXXXXX_YYYYMMDD_HHMMSS_report.md` - Markdown格式分析报告
- `XXXXXX_YYYYMMDD_HHMMSS_data.json` - JSON格式完整数据

## 报告内容

生成的报告包含：
1. 核心财务指标
2. 逻辑推理分析
3. 风险评估（综合风险等级）
4. 投资建议（买入/持有/卖出）
5. 关键风险点
6. 公告摘要

## 技术栈

- Python 3.x
- 标准库（无需额外依赖）
- 模块化 Agent 设计
- 日志追踪

## 扩展说明

当前使用模拟数据。如需接入真实数据源，修改 `agents/data_collector.py` 中的数据采集逻辑即可。
