from Errors.exceptions import ValidationException


class ValidatorAsignare:

    def valideazaAsignare(self, asignare):
        """
        Functia care valideaza o asignare
        :asignare: entitate de tip asignare
        :return: nu returneaza nimic
        """
        erori = ""
        if asignare.getNrPb() == "":
            erori += "Numar prolema invalid!\n"
        else:
            if asignare.getNrPb() < 0:
                erori += "Numar problema invalid!Introduceti un nr pozitiv!\n"
        if asignare.getNrLab() == "":
            erori += "Numar laborator invalid!\n"
        else:
            if asignare.getNrLab() < 0:
                erori += "Numar laborator invalid!Introduceti un numar pozitiv!\n"
        if len(erori) > 0:
            raise ValidationException(erori)