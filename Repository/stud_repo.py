from Errors.exceptions import RepositoryException


class StudentRepository:

    def __init__(self):
        self.__lista_studenti = []

    def adaugare(self, student):
        """
        Functia care adauga un element in lista
        raise RepositoryException daca avem deja un student cu acelasi ID
        :param: entitate de tip student
        """
        if student.getID() in self.__lista_studenti:
            raise RepositoryException("Student deja existent!\n")
        self.__lista_studenti.append(student)

    def findById(self, id_student):
        """
        Functia care cauta un student dupa ID
        :param: int - id_student - id-ul studentului
        :return: studentul gasit
        """
        if id_student not in self.__lista_studenti:
            raise RepositoryException("Studentul nu exista in lista!\n")
        for student in self.__lista_studenti:
            if student == id_student:
                return student

    def stergereStudent(self, id_student):
        """
        Functia care sterge un student din lista de studenti
        :param: int - id_student - id-ul studentului
        :return: nu returneaza nimic
        """
        if id_student not in self.__lista_studenti:
            raise RepositoryException("Acest student nu exsita in lista!\n")
        for i in range(0, len(self.__lista_studenti)):
            if i < len(self.__lista_studenti):
                if self.__lista_studenti[i] == id_student:
                    del self.__lista_studenti[i]

    def update(self, student):
        """
        Functia care face update la un student
        :param: entitate de tip student
        :return: nu returneaza nimic
        """
        if student not in self.__lista_studenti:
            raise RepositoryException("Student inexistent!\n")
        for i in range(len(self.__lista_studenti)):
            if self.__lista_studenti[i] == student:
                self.__lista_studenti[i] = student
                return

    def getAll(self):
        """
        Functia care returneaza studentii
        :return: lista de studenti
        """
        return self.__lista_studenti[:]

    def size(self):
        """
        Functia care da nr de studenti din lista
        :return: returneaza un nr intreg
        """
        return len(self.__lista_studenti)
