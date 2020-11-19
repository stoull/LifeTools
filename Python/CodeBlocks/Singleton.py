
# using a metaclass to create Singleton

class Singleton(type):
	"""docstring for Singleton"""
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class Computer(metaclass = Singleton):
	"""docstring for Computer"""
	def __init__(self, model = 'Unkown'):
		super(Computer, self).__init__()
		self.model = model

class AutoVehicles(Computer, metaclass = Singleton):
	"""docstring for AutoVehicles"""
	def __init__(self, version = 'R'):
		super(AutoVehicles, self).__init__()
		self.version = version
		
		
		
if __name__ == "__main__":
	c1 = Computer(model = "Dell")
	c2 = Computer(model = "Lenovo")
	c3 = Computer(model = "Mi")
	print(f"c1: {c1}	model: {c1.model}")
	print(f"c2: {c2}	model: {c2.model}")
	print(f"c3: {c3}	model: {c3.model}")

	auto_ve1 = AutoVehicles()
	auto_ve2 = AutoVehicles(version = "K")
	auto_ve3 = AutoVehicles(version = "S")
	print(f"auto_ve1: {auto_ve1}	version: {auto_ve1.version}")
	print(f"auto_ve2: {auto_ve2}	version: {auto_ve2.version}")
	print(f"auto_ve3: {auto_ve3}	version: {auto_ve3.version}")

