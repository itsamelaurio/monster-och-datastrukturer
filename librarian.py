from observer import Observer
from novel import Novel

class Librarian(Observer):

	#__novel: Novel

	def __init__(self):
		pass

	def setNovel(self, novel: Novel) -> None:
		self.__novel = novel
		self.__novel.addObserver(self)
	
	def update(self) -> None:
		print("Jag uppdaterar bokens metadata.")
		print("Titel: " + self.__novel.getTitle())
		print("Författare: " + self.__novel.getAuthor())
		print("År: " + str(self.__novel.getYear()))
