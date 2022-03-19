from Errors.exceptions import RepositoryException


class NotaRepository:

    def __init__(self):
        self.__lisa_note = []

    def adaugare(self, notare):
        """
        Functia care adauga un element in lista
        raise RepositoryException daca avem deja o notare cu acelasi ID
        :param: entitate de tip notare
        """
        if self.__find(notare.getStudent(), notare.getNrLab()) is not None:
            raise RepositoryException("Laboratorul acesta a fost deja notat!\n")

        self.__lisa_note.append(notare)

    def __find(self, st, nr_lab):
        """
          Lookup a grade for a given student and discipline
          st - student
          disc - discipline
          return Grade or None if there is no grade in the repository
        """
        for notare in self.__lisa_note:
            if notare.getStudent() == st and notare.getNrLab() == nr_lab:
                return notare
        return None

    def getAll(self):
        """
        Functia care returneaza asignarile
        :return: lista de  asignari
        """
        return self.__lisa_note[:]

