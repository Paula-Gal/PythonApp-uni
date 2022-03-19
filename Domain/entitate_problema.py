class Problema:

    def __init__(self, id_prob, nr_lab, nr_pb, desc, dline):
        """
        Creeaza o noua problema
        :param id_prob: int -  id-ul problemei
        :param nr_lab: int - nr laboratorului din care face parte problema
        :param nr_pb: int - numarul problemei
        :param desc: string - descrierea problemei
        :param dline: datetime -deadline ul problemei
        """
        self.__id_prob = id_prob
        self.__nr_lab = nr_lab
        self.__nr_pb = nr_pb
        self.__desc = desc
        self.__dline = dline

    def getID(self):
        return self.__id_prob

    def getNrLab(self):
        return self.__nr_lab

    def getNrPb(self):
        return self.__nr_pb

    def getDescripion(self):
        return self.__desc

    def getDline(self):
        return self.__dline

    def setNrLab(self, valoare):
        self.__nr_lab = valoare

    def setNrPb(self, valoare):
        self.__nr_pb = valoare

    def setDescription(self, valoare):
        self.__desc = valoare

    def setDline(self, valoare):
        self.__dline = valoare

    def __eq__(self, problema):
        """
        Functia care verifica egalitatea
        :param problema: o entitate problema
        :return:True daca problema curenta are acelasi id cu problema,False in caz contrar
        """
        return self.__id_prob == problema

    def __str__(self):
        """
        Functia care transforma intr-un string o problema
        :return: returneaza string-ul format
        """
        return str(self.__id_prob) + " " + str(self.__id_prob) + " " + str(self.__id_prob)
