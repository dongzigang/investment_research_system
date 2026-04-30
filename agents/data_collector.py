import random
from .base_agent import BaseAgent
from config import COMPANIES, DATA_DIR
import json
import os

class DataCollectorAgent(BaseAgent):
    def __init__(self):
        super().__init__("数据采集Agent")
    
    def process(self, data: dict) -> dict:
        stock_code = data.get("stock_code", "000001")
        company_name = COMPANIES.get(stock_code, "未知公司")
        
        self.logger.info(f"采集 {company_name}({stock_code}) 的数据")
        
        # 模拟采集财务数据
        financial_data = {
            "stock_code": stock_code,
            "company_name": company_name,
            "revenue": random.randint(1000000, 10000000),
            "profit": random.randint(100000, 1000000),
            "assets": random.randint(5000000, 50000000),
            "liabilities": random.randint(2000000, 20000000),
            "roe": round(random.uniform(0.05, 0.25), 4),
            "debt_ratio": round(random.uniform(0.3, 0.7), 4),
            "growth_rate": round(random.uniform(-0.1, 0.3), 4)
        }
        
        # 模拟采集市场数据
        market_data = {
            "current_price": round(random.uniform(10, 200), 2),
            "pe_ratio": round(random.uniform(5, 50), 2),
            "pb_ratio": round(random.uniform(0.5, 5), 2),
            "market_cap": random.randint(1000000000, 10000000000)
        }
        
        # 模拟采集公告数据
        announcements = [
            {"date": "2026-04-25", "type": "年报", "title": f"{company_name}2025年年度报告"},
            {"date": "2026-04-20", "type": "季报", "title": f"{company_name}2026年第一季度报告"},
            {"date": "2026-04-15", "type": "分红", "title": f"{company_name}关于2025年度利润分配预案的公告"}
        ]
        
        collected_data = {
            "financial": financial_data,
            "market": market_data,
            "announcements": announcements,
            "data_source": "模拟数据源"
        }
        
        # 保存到文件
        output_file = os.path.join(DATA_DIR, f"{stock_code}_raw_data.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(collected_data, f, ensure_ascii=False, indent=2)
        
        self.logger.info(f"数据已保存到 {output_file}")
        
        return {
            "stock_code": stock_code,
            "company_name": company_name,
            "collected_data": collected_data,
            "raw_data_file": output_file
        }
