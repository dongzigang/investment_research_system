from abc import ABC, abstractmethod
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(name)
    
    @abstractmethod
    def process(self, data: dict) -> dict:
        pass
    
    def run(self, data: dict) -> dict:
        self.logger.info(f"开始执行 {self.name}")
        start_time = time.time()
        try:
            result = self.process(data)
            elapsed = time.time() - start_time
            self.logger.info(f"{self.name} 完成，耗时 {elapsed:.2f}秒")
            return {"status": "success", "data": result, "agent": self.name}
        except Exception as e:
            self.logger.error(f"{self.name} 执行失败: {str(e)}")
            return {"status": "error", "error": str(e), "agent": self.name}
