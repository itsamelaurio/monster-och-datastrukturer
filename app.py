from novel import Novel
from printer import Printer
from librarian import Librarian

novel = Novel("1984", "George Orwell")

librarian = Librarian()
novel.addObserver(librarian)
librarian.setNovel(novel)

printer = Printer()
novel.addObserver(printer)
printer.setNovel(novel)

# Uppdatera årtalet
novel.setYear(1949)

#uppdatera innehållet
novel.setContent("Freedom is the freedom to say that two plus two make four. If that is granted, all else follows.")
