import random
import string
from datetime import date

from Domain.entitate_problema import *


class ProblemService:

    def __init__(self, valProblem, repoProblem, repoAsignare):
        self.__valProblem = valProblem
        self.__repoProblem = repoProblem
        self.__repoAsignare = repoAsignare

    def adaugaProblema(self, id, nr_lab, nr_pb, desc, dline):
        """
        Functia care adauga o problema
        raise RepositoryExeption - daca problema exista deja in lista de probleme
        raise ValidationException - daca proprietatile problemei sunt invalide
        :param id: int - identificator unic problema
        :param nr_lab: int -  numarul laboratorului din care face parte progrmul
        :param nr_pb: int - numarul problemei
        :param desc: string - descrierea problemei
        :param dline: datetime - deadline ul problemei
        :return: entitate de tip problema
        """
        # creeaza un obiect de tipul problema
        problema = Problema(id, nr_lab, nr_pb, desc, dline)
        # valideaza problema utilizand un obiect de tip validator
        self.__valProblem.valideazaProblema(problema)
        # salvez problema utilizand un obiect de tip repository
        self.__repoProblem.adaugare(problema)

        return problema

    def getAllProblems(self):
        """
        Functia care returneaza lista de probleme
        """
        return self.__repoProblem.getAll()

    def stergeProblema(self, ide):
        """
        Functia care sterge o problema dupa id
        raise RepositoryExeption - daca problema nu exista in lista
        raise ValidationException - daca proprietatile problemei sunt invalide
        :param ide: int - id ul problemei de sters
        """
        # valideaza id-ul utilizand un obiect de tip validator
        self.__valProblem.valideazaID(ide)
        # sterg studentul utilizand un obiect de tip repository
        lista_probleme = self.__repoProblem.getAll()
        lista_asignari = self.__repoAsignare.getAll()
        for problema in lista_probleme:
            if problema.getID() == ide:
                nr_pr = problema.getNrPb()
                for asignare in lista_asignari:
                    if asignare.getNrPb() == nr_pr:
                        self.__repoAsignare.stergereAsignare(asignare.getStudent())
        self.__repoProblem.stergereProblema(ide)

    def cautareProblemaId(self, id_problema):
        """
        Functia care cauta o problema dupa id in lista de probleme
        :param id_problema: int - id-ul problmei de cautat
        :return: problema gasita
        """
        # valideaza id-ul utilizand un obiect de tip validator
        self.__valProblem.valideazaID(id_problema)
        # caut studentul utilizand un obiect de tip repository
        return self.__repoProblem.findById(id_problema)

    def modificareNrLab(self, id_problema, nr_lab_nou):
        """
        Functia care modifica nr laboratorului unei probleme
        :param id_problema: int - id-ul problemei
        :param nr_lab_nou: int - nr noului laborator
        :return: nu returneaza nimic
        """
        problema = self.__repoProblem.findById(id_problema)
        problema.setNrLab(nr_lab_nou)
        self.__valProblem.valideazaProblema(problema)
        self.__repoProblem.update(problema)

    def modificareNrPb(self, id_problema, nr_pb_nou):
        """
         Functia care modifica nr problemei unei probleme
        :param id_problema: int - id-ul problemei
        :param nr_pb_nou: int - nr nou al problemei
        :return: nu returneaza nimic
        """
        problema = self.__repoProblem.findById(id_problema)
        problema.setNrPb(nr_pb_nou)
        self.__valProblem.valideazaProblema(problema)
        self.__repoProblem.update(problema)

    def modificareDescrierePb(self, id_problema, descriere):
        """
        Functia care modifica descrierea unei probleme
        :param id_problema: int - id-ul problemei
        :param descriere: string - descrierea noua
        :return: nu returneaza nimic
        """
        problema = self.__repoProblem.findById(id_problema)
        problema.setDescription(descriere)
        self.__valProblem.valideazaProblema(problema)
        self.__repoProblem.update(problema)

    def modificareDeadlinePb(self, id_problema, deadline):
        """
        Functia care modifica deadline-ul unei probleme
        :param id_problema: int - id-ul problemei
        :param deadline: DateTime - deadline nou
        :return: nu returneaza nimic
        """
        problema = self.__repoProblem.findById(id_problema)
        problema.setDline(deadline)
        self.__valProblem.valideazaProblema(problema)
        self.__repoProblem.update(problema)

    def generare_problema(self, nr_probleme):
        """
        Functia care genereaza un student
        :return: nu returneaza nimic
        """
        letters = string.ascii_letters
        deadline = ""
        for i in range(0, nr_probleme):
            id_problema = random.randint(1, 20000)
            nr_lab = random.randint(1, 999)
            nr_pb = random.randint(1, 999)
            descriere = "".join(random.choice(letters) for j in range(10))
            zi = random.randint(1, 31)
            luna = random.randint(1, 12)
            an = random.randint(2020, 4000)
            problema = ""
            try:
                deadline = date(an, luna, zi)
            except:
                i = i - 1
            try:
                problema = Problema(id_problema, nr_lab, nr_pb, descriere, deadline)
            except:
                i = i - 1
            try:
                self.__valProblem.valideazaProblema(problema)
            except:
                i = i - 1
            try:
                self.__repoProblem.adaugare(problema)
            except:
                i = i - 1

        print(self.__repoProblem.size())
