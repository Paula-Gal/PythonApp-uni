from Errors.exceptions import ValidationException

class ValidatorProblem:

    def valideazaProblema(self, problema):
        """
        Functia care valideaza o problema
        :problema: entitate de tip problema
        :return: nu returneaza nimic
        """
        erori = ""
        if problema.getID() == "":
            erori += "ID problema invalid!\n"
        else:
            if problema.getID() < 0:
                erori += "ID problema invalid! Introduceti un nr pozitiv!\n"
        if problema.getNrPb() == "":
            erori += "Numar prolema invalid!\n"
        else:
            if problema.getNrPb() < 0:
                erori += "Numar problema invalid!Introduceti un nr pozitiv!\n"
        if problema.getNrLab() == "":
            erori += "Numar laborator invalid!\n"
        else:
            if problema.getNrLab() < 0:
                erori += "Numar laborator invalid!Introduceti un numar pozitiv!\n"
        if problema.getDescripion() == "":
            erori += "Descriere invalida!Introduceti o descriere problemei!\n"
        if problema.getDline() == "":
            erori += "Deadline invalid!\n"
        if len(erori) > 0:
            raise ValidationException(erori)


    def valideazaID(self, ide):
        """
        Functia care valideaza id ul unei probleme
        :param ide: int -  id ul problemei
        :return: nu returneaza nimic
        """
        erori = ""
        if ide == "":
            erori += "ID problema invalid!\n"
        else:
            if ide < 0:
                erori += "ID problema invalid! Introduceti un nr pozitiv!\n"
        if len(erori) > 0:
            raise ValidationException(erori)

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