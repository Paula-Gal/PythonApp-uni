import random
import string

from Domain.entitate_student import *


class StudentService:

    def __init__(self, valStudent, repoStudent):
        self.__valStudent = valStudent
        self.__repoStudent = repoStudent

    def adaugaStudent(self, id, nume, grup):
        """
        Functia care adauga un student
        raise RepositoryExeption - daca studentul exista deja in lista de studenti
        raise ValidationException - daca proprietatile studentului sunt invalide
        :param id: int - identificator unic student
        :param nume: string - numle studentului
        :param grup: int - grupul din care face parte studentul
        :return: entitate de tip student
        """
        # creeaza un obiect de tipul student
        student = Student(id, nume, grup)
        # valideaza studentul utilizand un obiect de tip validator
        self.__valStudent.valideazaStudent(student)
        # salvez studentul utilizand un obiect de tip repository
        self.__repoStudent.adaugare(student)

        return student

    def stergeStudent(self, ide):
        """
        Functia care sterge un student dupa id
        raise RepositoryExeption - daca studentul nu exista in lista
        raise ValidationException - daca proprietatile studentului sunt invalide
        :param ide: int -  id ul studentului de sters
        """
        # valideaza id-ul utilizand un obiect de tip validator
        self.__valStudent.valideazaID(ide)
        # sterg studentul utilizand un obiect de tip repository
        self.__repoStudent.stergereStudent(ide)

    def getAllStudents(self):
        """
        Functia care returneaza lista de studenti
        """
        return self.__repoStudent.getAll()

    def cautareStudentId(self, id_student):
        """
        Functia care cauta un student dupa id in lista de studenti
        :param id_student:  int - id-ul studentului de cautat
        :return: studentul gasit
        """
        # valideaza id-ul utilizand un obiect de tip validator
        self.__valStudent.valideazaID(id_student)
        # caut studentul utilizand un obiect de tip repository
        return self.__repoStudent.findById(id_student)

    def modificareNumeStud(self, id_stud, nume_nou):
        """
        Functia care modifica numele unui student
        :param id_stud: int - id-ul studentului
        :param nume_nou: string - numele nou
        :return: nu returneaza nimic
        """
        # validez numele si id-ul introdus de la tastatura
        self.__valStudent.valideazaID(id_stud)
        self.__valStudent.valideazaNume(nume_nou)

        # iau studentul cu id-ul introdus
        student = self.__repoStudent.findById(id_stud)
        student.setName(nume_nou)

        self.__repoStudent.update(student)

    def modificareGrupStud(self, ide_student, grup_nou):
        """
        Functia care modifica grupul unui student
        :param ide_student: int - id ul studentului
        :param grup_nou: int - nr grupului nou
        :return: nu returneaza nimic
        """
        self.__valStudent.valideazaID(ide_student)
        self.__valStudent.valideazaGrup(grup_nou)

        student = self.__repoStudent.findById(ide_student)
        student.setGroup(grup_nou)

        self.__repoStudent.update(student)

    def generare_student(self, nr_studenti):
        """
        Functia care genereaza un student
        :return: nu returneaza nimic
        """
        self.__valStudent.valdeazaNrEntitati(nr_studenti)
        letters = string.ascii_letters
        student = ""
        for i in range(0, nr_studenti):
            id_student = random.randint(1, 2000)
            nume_student = "".join(random.choice(letters) for j in range(15))
            grup_student = random.randint(1, 2000)
            try:
                student = Student(id_student, nume_student, grup_student)
            except:
                i = i - 1
            try:
                self.__valStudent.valideazaStudent(student)
            except:
                i = i - 1
            try:
                self.__repoStudent.adaugare(student)
            except:
                i = i - 1
