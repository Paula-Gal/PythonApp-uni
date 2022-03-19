from Errors.exceptions import RepositoryException


class AsignareRepository:

    def __init__(self):
        self.__lista_asignari = []

    def adaugare(self, asignare):
        """
        Functia care adauga un element in lista
        raise RepositoryException daca avem deja o asignare cu acelasi ID
        :param: entitate de tip asignare
        """
        if self.find(asignare.getStudent(), asignare.getNrLab()) is not None:
            raise RepositoryException("Asignare pentru laboratorul introdus deja existenta!\n")

        self.__lista_asignari.append(asignare)

    def find(self, st, nr_lab):
        """
          Lookup a grade for a given student and discipline
          st - student
          disc - discipline
          return Grade or None if there is no grade in the repository
        """
        for asignment in self.__lista_asignari:
            if asignment.getStudent() == st and asignment.getNrLab() == nr_lab:
                return asignment
        return None


    def getAll(self):
        """
        Functia care returneaza asignarile
        :return: lista de  asignari
        """
        return self.__lista_asignari[:]

    def stergereAsignare(self, id_asignare):
        """
        Functia care sterge o problema din lista de probleme
        :id_problema: int - id-ul problemei
        :return: nu returneaza nimic
        """
        if id_asignare not in self.__lista_asignari:
            raise RepositoryException("Aceasta asignare nu exsita in lista!\n")
        for i in range(0, len(self.__lista_asignari)):
            if i < len(self.__lista_asignari):
                if self.__lista_asignari[i] == id_asignare:
                    del self.__lista_asignari[i]
