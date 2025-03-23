import logging

class Logger(logging.Logger):
	def __init__(self,name:str, console:bool,file:bool, level ,filename = None):
		super().__init__(name=name,level=level)
		formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
		if console:
			console_handler = logging.StreamHandler()
			console_handler.setFormatter(formatter)
			self.addHandler(console_handler)
		if file:
			file_handler = logging.FileHandler(f"{filename or name}.log")
			file_handler.setFormatter(formatter)
			self.addHandler(file_handler)