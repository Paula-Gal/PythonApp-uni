from Errors.exceptions import ValidationException


class ValidatorStudent:

    def valideazaStudent(self, student):
        """
        Functia care valideaza un student
        :student: entitate de tip student
        :return: nu returneaza nimic
        """
        erori = ""
        if student.getID() == "":
            erori += "ID student invalid!\n"
        else:
            if student.getID() < 0:
                erori += "ID student invalid! Introduceti un nr pozitiv!\n"
        if student.getNume() == "":
            erori += "Nume invalid!\n"
        if student.getGrup() == "":
            erori += "Grup invalid!\n"
        if len(erori) > 0:
            raise ValidationException(erori)

    def valideazaID(self, ide):
        """
        Functia care valideaza id ul unui student
        :param ide: int -  id ul studentului
        :return: nu returneaza nimic
        """
        erori = ""
        if ide == "":
            erori += "ID student invalid!\n"
        else:
            if ide < 0:
                erori += "ID student invalid! Introduceti un nr pozitiv!\n"
        if len(erori) > 0:
            raise ValidationException(erori)

    def valideazaNume(self, nume):
        """
        Functia care valideaza numele introdus
        :param nume:string - numele introdus
        :return: nu returneaza nimic
        """
        erori = ""
        if nume == "":
            erori += "Numele este nul!Introduceti un nume valid!\n"
        if len(erori) > 0:
            raise ValidationException(erori)

    def valideazaGrup(self, grup):
        """
        Functia care valideaza grupul introdus
        :param grup: int - nr grupului din care face parte studentul
        :return: nu returneaza nimic
        """
        erori = ""
        if grup == "":
            erori += "Grupul e nul!Introduceti un grup valid!\n"
        else:
            if grup < 0:
                erori += "Grup invalid!Introduceti un nr pozitiv!\n"

    def valdeazaNrEntitati(self, nr):
        """
        Functia care valideaza nr de entitati de generat introdus
        :param nr: int -  nr de entitati
        :return: nu returneaza nimic
        """
        erori = ""
        if nr == "":
            erori += "Nr entitati invalid!\n"
        else:
            if nr < 0:
                erori += "Nr entitati invalid! Introduceti un nr pozitiv!\n"
        if len(erori) > 0:
            raise ValidationException(erori)