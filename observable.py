from observer import Observer

class Observable:

	#__observers: List[Observer]
	
	def __init__(self):
		self.__observers = []
	
	def addObserver(self, observer: Observer) -> None:
		self.__observers.append(observer)
	
	def removeObserver(self, observer: Observer) -> None:
		self.__observers.remove(observer)
	
	def notifyObservers(self) -> None:
		for observer in self.__observers:
			observer.update()
