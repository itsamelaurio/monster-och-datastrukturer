from observable import Observable

class Novel(Observable):

	#__title: str
	#__author: str
	#__year: int
	#__content: str

	def __init__(self, title: str, author: str):
		super().__init__()
		self.__title: str = title
		self.__author: str = author
		self.__year = 0
		self.__content = ""
	
	def getTitle(self) -> str:
		return self.__title
	
	def setTitle(self, title: str) -> None:
		self.__title = title
		self.notifyObservers()
	
	def getAuthor(self) -> str:
		return self.__author
	
	def setAuthor(self, author: str) -> None:
		self.__author = author
		self.notifyObservers()

	def getYear(self) -> int:
		return self.__year
	
	def setYear(self, year: int) -> None:
		self.__year = year
		self.notifyObservers()

	def getContent(self) -> str:
		return self.__content
	
	def setContent(self, content: str) -> None:
		self.__content = content
		self.notifyObservers()
