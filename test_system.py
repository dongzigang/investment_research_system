"""测试脚本 - 批量分析多只股票"""
from coordinator import ResearchCoordinator
from config import COMPANIES
import time

def test_single_stock(stock_code):
    print(f"\n{'='*60}")
    print(f"分析股票: {stock_code} - {COMPANIES.get(stock_code, '未知')}")
    print('='*60)
    
    coordinator = ResearchCoordinator()
    start = time.time()
    result = coordinator.run_research(stock_code)
    elapsed = time.time() - start
    
    if result["status"] == "success":
        summary = result["result"]["report_summary"]
        print(f"✅ 完成 ({elapsed:.2f}秒)")
        print(f"   评级: {summary['评级']} | 风险: {summary['风险等级']}")
        return True
    else:
        print(f"❌ 失败: {result.get('error')}")
        return False

def test_all_stocks():
    print("\n开始批量测试所有股票...\n")
    results = []
    for stock_code in COMPANIES.keys():
        success = test_single_stock(stock_code)
        results.append((stock_code, success))
        time.sleep(0.5)  # 避免输出混乱
    
    print(f"\n{'='*60}")
    print("测试汇总")
    print('='*60)
    success_count = sum(1 for _, success in results if success)
    print(f"总计: {len(results)} 只股票")
    print(f"成功: {success_count} 只")
    print(f"失败: {len(results) - success_count} 只")

if __name__ == "__main__":
    test_all_stocks()
