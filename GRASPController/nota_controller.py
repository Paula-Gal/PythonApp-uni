from Domain.enitate_nota import *
from Errors.exceptions import RepositoryException


class NotaService:

    def __init__(self, valStudent, repoStudent, valProblema, repoProblema, valAsignare, repoAsignare, valNota, repoNota):
        self.__valStudent = valStudent
        self.__repoStudent = repoStudent
        self.__valProblema = valProblema
        self.__repoProblema = repoProblema
        self.__valAsignare = valAsignare
        self.__repoAsignare = repoAsignare
        self.__valNota = valNota
        self.__repoNota = repoNota

    def notare(self, st_id, nr_lab, nota):
        """
        Asignare nr_lab si nr_pb unui student
        :param: st_id - int - id-ul studentului
        :param: nr_lab - int  - nr laborator
        :param: nota - int - nota laloratorului
        nr_lab si nota se salveaza
        return nr_lab si nr_pb
        """
        # caut studentul cu id ul introdus
        student = self.__repoStudent.findById(st_id)

        # creez nota cu studentul,disciplina si nota
        notare = Nota(student, nr_lab, nota)

        # validez notarea creata
        self.__valNota.validare_nota(nota)
        self.__valNota.valideazaNotare(notare)

        # verific daca exista o asignare
        exista_asignare = self.__repoAsignare.find(student, nr_lab)
        lista_probleme = self.__repoProblema.getAll()
        ok1 = False
        for problema in lista_probleme:
            if problema.getNrLab() == nr_lab:
                ok1 = True

        if not ok1:
            raise RepositoryException("Acest nr de laborator nu apare in lista de probleme!")

        if exista_asignare is not None:
            # adaug notare
            self.__repoNota.adaugare(notare)
            return notare
        else:
            raise RepositoryException("Asignare pentru laboratorul introdus nu exista!\n")

    def getAllN(self):
        """
        Functia care returneaza lista de asignari
        """
        return self.__repoNota.getAll()

    def sortareAlfabetic(self, nr_lab):
        """
        Functia care sorteaza alfabetic dupa nume studentii
        :return: lista sortata
        """
        lista_stud = []
        lista_nume = []
        lista_all = self.__repoNota.getAll()  # lista cu toti studentii si notele
        # lista_asignari = self.__repoAsignare.getAll() #lista de asignari
        for notare in lista_all:
            if notare.getNrLab() == nr_lab:
                lista_stud.append(notare.getStudent())

        lista_sortata = sorted(lista_stud, key=lambda numeST: numeST.getNume(), reverse=False)

        print("Lista de studenti ordonati alfabetic dupa nume este:")
        for stud in lista_sortata:
            for elem in lista_all:
                if elem.getStudent() == stud:
                    print(stud.getNume(), elem.getNota())
        # print(lista_sortata)
        return lista_sortata

    def sortareNota(self, nr_lab):
        """
        Functia care sorteaza  dupa nota studentii
        :return: lista sortata
        """
        lista_stud = []
        lista_all = self.__repoNota.getAll()  # lista cu toti studentii si notele
        for notare in lista_all:
            if notare.getNrLab() == nr_lab:
                lista_stud.append(notare)

        lista_sortata = sorted(lista_stud, key=lambda studNota: studNota.getNota(), reverse=False)
        return lista_sortata

    def sub_cinci(self):
        """
        Functia care afiseaza studentii cu media notelor de la laborator < 5
        :return: lista gasita
        """
        lista_stud_medii_sub_cinci = []
        # media_stud = suma_notelor/nr_notelor
        lista_all_stud = self.__repoStudent.getAll()
        list_all = self.__repoNota.getAll()
        suma = 0
        media = 0
        nr_note = 0
        print("IDStudent  Nume   Grup    Nr.lab  Nota ")
        for student in lista_all_stud:
            suma = 0
            nr_note = 0
            for stud in list_all:
                if student == stud.getStudent():
                    suma = suma + stud.getNota()
                    nr_note = nr_note + 1
            try:
                media = float(float(suma) / float(nr_note))
            except ZeroDivisionError:
                media = 0
            if 5 > media > 0:
                print(student, media)
                lista_stud_medii_sub_cinci.append(student)

        return lista_stud_medii_sub_cinci
