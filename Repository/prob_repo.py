from Errors.exceptions import RepositoryException


class ProblemRepository:

    def __init__(self):
        self.__lista_probleme = []

    def size(self):
        """
        Functia care da nr de probleme din lista
        :return: int -  returneaza nr de probleme
        """
        return len(self.__lista_probleme)

    def adaugare(self, problem):
        """
        Functia care adauga un element in lista
        raise RepositoryException daca avem deja un student cu acelasi ID
        """
        if problem.getID() in self.__lista_probleme:
            raise RepositoryException("Problema deja existenta!\n")
        self.__lista_probleme.append(problem)

    def getAll(self):
        """
        Functia care returneaza studentii
        :return: lista de studenti
        """
        return self.__lista_probleme[:]

    def stergereProblema(self, id_problema):
        """
        Functia care sterge o problema din lista de probleme
        :id_problema: int - id-ul problemei
        :return: nu returneaza nimic
        """
        if id_problema not in self.__lista_probleme:
            raise RepositoryException("Aceasta problema nu exsita in lista!\n")
        for i in range(0, len(self.__lista_probleme)):
            if i < len(self.__lista_probleme):
                if self.__lista_probleme[i] == id_problema:
                    del self.__lista_probleme[i]

    def findById(self, id_prob):
        """
        Functia care cauta o problema dupa ID
        :id_prob: int - id-ul problemei
        :return: problema gasita
        """
        if id_prob not in self.__lista_probleme:
            raise RepositoryException("Problema nu exista in lista!\n")
        for pb in self.__lista_probleme:
            if pb == id_prob:
                return pb
        return None

    def update(self, problema):
        """
        Functia care face update la o problema
        :problema: entitate de tip problema
        :return: nu returneaza nimic
        """
        if problema not in self.__lista_probleme:
            raise RepositoryException("Problema inexistenta!\n")
        for i in range(len(self.__lista_probleme)):
            if self.__lista_probleme[i] == problema:
                self.__lista_probleme[i] = problema
                return
