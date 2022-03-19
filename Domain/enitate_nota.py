class Nota:

    def __init__(self, student, nr_lab, nota):
        """
        Creeaza o noua nota cu unui student pe un anumit laborator
        :param student: entitatea student
        :param nota: float - nota pe laborator
        :param nr_lab: int - numarul laboratorului
        """
        self.__student = student
        self.__nr_lab = nr_lab
        self.__nota = nota

    def getStudent(self):
        return self.__student


    def getNota(self):
        return self.__nota

    def getNrLab(self):
        return self.__nr_lab

    def setNrLab(self, valoare):
        self.__nr_lab = valoare

    def setNota(self, valoare):
        self.__nota = valoare

    def __eq__(self, nota):
        """
        Functia care verifica egalitatea
        :param nota: o entitate nota
        :return:True daca nota curenta are acelasi id cu nota,False in caz contrar
        """
        return self.__student == nota

    def __str__(self):
        """
        Functia care transforma intr-un string o nota
        :return:string-ul format
        """
        return str(self.__student) + " " + str(self.__nr_lab) + " " + str(self.__nota)
