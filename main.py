from coordinator import ResearchCoordinator
from config import COMPANIES
import sys

def main():
    print("\n" + "="*60)
    print("智能投研 Agent 系统")
    print("基于多Agent协作的自动化投资分析")
    print("="*60 + "\n")
    
    coordinator = ResearchCoordinator()
    
    # 显示可分析的股票
    print("可分析的股票列表：")
    for code, name in COMPANIES.items():
        print(f"  {code} - {name}")
    print()
    
    # 获取用户输入
    if len(sys.argv) > 1:
        stock_code = sys.argv[1]
    else:
        stock_code = input("请输入股票代码 (默认 000001): ").strip() or "000001"
    
    if stock_code not in COMPANIES:
        print(f"警告: {stock_code} 不在预设列表中，将使用模拟数据进行分析")
    
    # 运行分析
    result = coordinator.run_research(stock_code)
    
    if result["status"] == "success":
        print("\n✅ 分析完成！")
        print(f"工作流: {result['workflow']}")
        print(f"\n📊 分析结果:")
        summary = result["result"]["report_summary"]
        print(f"  公司: {summary['公司']}({summary['股票代码']})")
        print(f"  评级: {summary['评级']}")
        print(f"  风险: {summary['风险等级']}")
        print(f"\n📄 报告已生成:")
        print(f"  {result['result']['report_file']}")
    else:
        print(f"\n❌ 分析失败: {result.get('error', '未知错误')}")

if __name__ == "__main__":
    main()
