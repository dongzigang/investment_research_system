import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# 模拟的上市公司列表
COMPANIES = {
    "000001": "平安银行",
    "600519": "贵州茅台",
    "000858": "五粮液",
    "601318": "中国平安",
    "600036": "招商银行"
}

# Agent配置
AGENT_CONFIG = {
    "data_collector": {"timeout": 30, "retry": 3},
    "info_extractor": {"model": "simple-nlp"},
    "logic_analyzer": {"reasoning_depth": 3},
    "risk_assessor": {"risk_threshold": 0.7},
    "report_generator": {"format": "markdown"}
}
