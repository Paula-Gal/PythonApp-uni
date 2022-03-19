class Asignare:

    def __init__(self, student, nr_lab, nr_pb, nota):
        """
        Creeaza o noua asignare cu id-ul, nr_lab si nr_pb date
        :param student: int -  id-ul studentului
        :param nr_pb: int - numarul problemei
        :param nr_lab: int - numarul laboratorului
        """
        self.__student = student
        self.__nr_lab = nr_lab
        self.__nr_pb = nr_pb
        self.__nota = nota

    def getStudent(self):
        return self.__student

    def getNota(self):
        return self.__nota

    def getNrPb(self):
        return self.__nr_pb

    def getNrLab(self):
        return self.__nr_lab

    def setNrLab(self, valoare):
        self.__nr_lab = valoare

    def setNrPb(self, valoare):
        self.__nr_pb = valoare

    def __eq__(self, asignare):
        """
        Functia care verifica egalitatea
        :param asignare: o entitate asignare
        :return:True daca asignarea curenta are acelasi id cu asignarea,False in caz contrar
        """
        return self.__student == asignare

    def __str__(self):
        """
        Functia care transforma intr-un string o asignare
        :return:string-ul format
        """
        return str(self.__student) + " " + str(self.__nr_lab) + " " + str(self.__nr_pb)
