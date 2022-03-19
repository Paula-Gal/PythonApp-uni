class Student:

    def __init__(self, studentID, name, group):
        """
        Creeaza un nou student cu id-ul, numele si grupul dat
        :param studentID:i int -  id-ul studentului
        :param name: string - numele studentului
        :param group: int - grupul studentului
        """
        self.__id = studentID
        self.__nume = name
        self.__grup = group

    def getID(self):
        return self.__id

    def getNume(self):
        return self.__nume

    def getGrup(self):
        return self.__grup

    def setName(self, valoare):
        self.__nume = valoare

    def setGroup(self, valoare):
        self.__grup = valoare

    def __eq__(self, stud):
        """
        Functia care verifica egalitatea
        :param student: o entitate student
        :return:True daca studentul curent are acelasi id cu studentul,False in caz contrar
        """
        return self.__id == stud

    def __str__(self):
        """
        Functia care transforma intr-un string un student
        :return:string-ul format
        """
        return str(self.__id) + " " + str(self.__nume) + " " + str(self.__grup)
