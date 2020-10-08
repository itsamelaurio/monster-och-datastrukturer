from observer import Observer
from novel import Novel

class Printer(Observer):

	#__novel: Novel

	def __init__(self):
		self.__novel = ""
		
	def setNovel(self, novel: Novel) -> None:
		self.__novel = novel
		self.update()
	
	def update(self) -> None:
		print("Här är romanens innehåll:")
		if (self.__novel.getContent() == ""):
			print("--text saknas--")
		else:
			print(self.__novel.getContent())
		print()
