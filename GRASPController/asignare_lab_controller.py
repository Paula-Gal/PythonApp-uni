from Domain.entitate_asignare import *
from Errors.exceptions import RepositoryException


class AsignareService:

    def __init__(self, valStudent, repoStudent, valProblema, repoProblema, valAsignare, repoAsignare):
        self.__valStudent = valStudent
        self.__repoStudent = repoStudent
        self.__valProblema = valProblema
        self.__repoProblema = repoProblema
        self.__valAsignare = valAsignare
        self.__repoAsignare = repoAsignare

    def asignare(self, st_id, nr_lab, nr_pb):
        """
        Asignare nr_lab si nr_pb unui student
        :param: st_id - int - id-ul studentului
        :param: nr_lab - int  - nr laborator
        :param: nr_pb - int - nr problema
        nr_lab si nr_pb se salveaza
        return nr_lab si nr_pb
        raise ValidationException for invalid nr_lab
        """
        # caut studentul cu id ul introdus
        student = self.__repoStudent.findById(st_id)

        # creez nota cu studentul,disciplina si nota
        asignare = Asignare(student, nr_lab, nr_pb, 0)

        # validez asignarea creata
        self.__valAsignare.valideazaAsignare(asignare)

        lista_probleme = self.__repoProblema.getAll()
        ok1 = False
        for problema in lista_probleme:
            if problema.getNrLab() == nr_lab:
                ok1 = True

        if not ok1:
            raise RepositoryException("Acest nr de laborator nu apare in lista de probleme!")

        ok2 = False
        for problema in lista_probleme:
            if problema.getNrPb() == nr_pb:
                ok2 = True

        if not ok2:
            raise RepositoryException("Aceasta problema nu apare in lista de probleme!")

        # adaug asignarea
        self.__repoAsignare.adaugare(asignare)

        return asignare

    def getAll(self):
        """
        Functia care returneaza lista de asignari
        """
        return self.__repoAsignare.getAll()

    def get20(self, nr_lab, nr_pb):
        """
        Functia care
        :param nr_lab: int  - nr laboratorului
        :param nr_pb: int - nr problema
        :return: nu returneaza nimic
        """
        lista_note = []
        lista_notari = self.__repoAsignare.getAll()
        for notare in lista_notari:
            if notare.getNrLab() == nr_lab and notare.getNrPb() == nr_pb:
                lista_note.append(notare)

        lista_sortata = sorted(lista_note, key=lambda studNota: studNota.getNota(), reverse=False)
        return lista_sortata
