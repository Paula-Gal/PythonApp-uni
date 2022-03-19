from Errors.exceptions import ValidationException


class ValidatorNotare:

    def validare_nota(self, nota):
        """
        Functia care valideaza nota
        :return: nu returneaza nimic
        """
        if float(nota) <= 0 or float(nota) > 10:
            raise ValidationException("Nota trebuie sa fie un numar intre 0 si 10")

    def valideazaNotare(self, notare):
        """
        Functia care valideaza o notare
        :notare: entitate de tip notare
        :return: nu returneaza nimic
        """
        erori = ""
        if notare.getNota() == "":
            erori += "Nota invalida!\n"
        if notare.getNrLab() == "":
            erori += "Numar laborator invalid!\n"
        else:
            if notare.getNrLab() < 0:
                erori += "Numar laborator invalid!Introduceti un numar pozitiv!\n"
        if len(erori) > 0:
            raise ValidationException(erori)