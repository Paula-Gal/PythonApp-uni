from datetime import date

from Errors.exceptions import ValidationException, RepositoryException


class Console:

    def __init__(self, srv_student, srv_problema, srv_asignare, srv_notare):
        self.__srv_student = srv_student
        self.__srv_problema = srv_problema
        self.__srv_asignare = srv_asignare
        self.__srv_notare = srv_notare

        self.__comenzi = {'1': self.__adaugareStudent, '2': self.__afisareListaStudenti, '3': self.__stergeStudent,
                          '4': self.__cautareStudentID, '5': self.__modifStNume,
                          '6': self.__modifStGrup, '7': self.__adaugareProblema, '8': self.__afisareListaProbleme,
                          '9': self.__stergereProblema, '10': self.__cautareProblemaID, '11': self.__modifNrLabPb,
                          '12': self.__modifNrPbPb, '13': self.__modifDescrierePb, '14': self.__modifDeadlinePb,
                          '15': self.__asignare_laborator, '16': self.__afisare_asignari,
                          '17': self.__notareLab,
                          '18': self.__afisare_not_lab,
                          '19': self.__afisare_stud_alfabetic, '20': self.__afisare_stud_nota,
                          '21': self.__lista_media_cinci, 'genereaza entitati': self.__genereaza_entitate,
                          '22': self.__iesire, '23': self.__medie_mare_cinci}

    def __adaugareStudent(self):
        """
        Functia care adauga un student citit din consola
        """
        id_student = int(input("ID student: "))
        nume_student = input("Nume student: ")
        grup_student = int(input("Grup student: "))
        self.__srv_student.adaugaStudent(id_student, nume_student, grup_student)
        print("")
        print("Studentul a fost adaugat in lista!")

    def __afisareListaStudenti(self):
        """
        Functia care afiseaza lista de studenti
        """
        lista_studenti = self.__srv_student.getAllStudents()
        if len(lista_studenti) == 0:
            print("Lista de studenti este goala!")
            return
        else:
            print("")
            print("Lista de studenti: ")
        print("ID  Nume  Grup")
        for student in lista_studenti:
            print(student.getID(), " ", student.getNume(), " ", student.getGrup())
        print("")

    def __stergeStudent(self):
        """
        Functia care sterge un student din lista
        """
        lista_studenti = self.__srv_student.getAllStudents()
        if len(lista_studenti) == 0:
            print("Lista de studenti este goala!Nu aveti ce student sa stergeti!")
            return
        else:
            id_student = int(input("ID student: "))
            self.__srv_student.stergeStudent(id_student)
            print("Studentul a fost sters cu succes!")

    def __cautareStudentID(self):
        """
        Functia care cauta un student dupa id ul introdus
        """
        lista_studenti = self.__srv_student.getAllStudents()
        if len(lista_studenti) == 0:
            print("Lista de studenti este goala!Nu aveti ce student sa cautati dupa id!")
            return
        else:
            id_student = int(input("ID student: "))
            stud = self.__srv_student.cautareStudentId(id_student)
            print("Studentul a fost gasit in lista!")
            print("ID  Nume  Grup")
            print(stud.getID(), " ", stud.getNume(), " ", stud.getGrup())
            print("")

    def __modifStNume(self):
        """
        Functia care modifica numele unui student
        """
        id_student = int(input("ID-ul studentului: "))
        nume_nou = input("Nume nou: ")
        self.__srv_student.modificareNumeStud(id_student, nume_nou)
        print("Numele studentului s-a modificat cu succes!")

    def __modifStGrup(self):
        """
        Functia care modifica grupul unui student
        """
        id_student = int(input("ID-ul studentului: "))
        grup_nou = int(input("Grupa noua: "))
        self.__srv_student.modificareGrupStud(id_student, grup_nou)
        print("Grupa studentului s-a modificat cu succes!")

    def __adaugareProblema(self):
        """
        Functia care adauga o problema citita din consola
        """
        id_problema = int(input("ID problema: "))
        nr_lab = int(input("Nr. laborator problema: "))
        nr_pb = int(input("Nr. problema: "))
        desc = input("Descrierea problemei: ")
        zi = int(input("Introduceti ziua: "))
        luna = int(input("Introduceti luna: "))
        an = int(input("Introduceti anul: "))
        deadline = ""
        try:
            deadline = date(an, luna, zi)
        except:
            print("Nu ati introdus o data corecta!")
        self.__srv_problema.adaugaProblema(id_problema, nr_lab, nr_pb, desc, deadline)
        print("")
        print("Problema a fost adaugata in lista!")

    def __afisareListaProbleme(self):
        """
        Functia care afiseaza lista de probleme
        :return:nu returneaza nimic
        """
        lista_probleme = self.__srv_problema.getAllProblems()
        if len(lista_probleme) == 0:
            print("Lista de probleme este goala!")
            return
        else:
            print("")
            print("Lista de probleme: ")
        print("ID  Nr.lab  Nr. pb  Descriere  Deadline")
        for problema in lista_probleme:
            print(problema.getID(), " ", problema.getNrLab(), "      ", problema.getNrPb(), "      ",
                  problema.getDescripion(), "      ", problema.getDline())
        print("")

    def __stergereProblema(self):
        """
        Functia care sterge o problema din lista de probleme
        :return:nu returneaza nimic
        """
        lista_probleme = self.__srv_problema.getAllProblems()
        if len(lista_probleme) == 0:
            print("Lista de probleme este goala!Nu aveti ce problema sa stergeti!")
            return
        else:
            id_pb = int(input("ID problema: "))
            self.__srv_problema.stergeProblema(id_pb)
            print("Problema a fost stearsa cu succes!")

    def __cautareProblemaID(self):
        """
        Functia care cauta o problema dupa ID
        :return: nu returneaza nimic
        """
        lista_probleme = self.__srv_problema.getAllProblems()
        if len(lista_probleme) == 0:
            print("Lista de probleme este goala!Nu aveti ce problema sa cautati dupa id!")
            return
        else:
            id_student = int(input("ID problema: "))
            prob = self.__srv_problema.cautareProblemaId(id_student)
            print("Problema a fost gasit in lista!")
            print("ID  Nr.lab  Nr. pb  Descriere  Deadline")
            print(prob.getID(), " ", prob.getNrLab(), "      ", prob.getNrPb(), "      ",
                  prob.getDescripion(), "      ", prob.getDline())
            print("")

    def __modifNrLabPb(self):
        """
        Functia care modifica nr lab unei probleme
        :return: nu returneaza nimic
        """
        lista_probleme = self.__srv_problema.getAllProblems()
        if len(lista_probleme) == 0:
            print("Lista de probleme este goala!Nu aveti ce sa modificati!")
            return
        else:
            id_problema = int(input("ID-ul problemei: "))
            nr_lab_nou = int(input("Nr. laborator nou: "))
            self.__srv_problema.modificareNrLab(id_problema, nr_lab_nou)
            print("Modificarea nr laboratorului s-a modificat cu succes!")

    def __modifNrPbPb(self):
        """
        Functia care modifica nr pb unei probleme
        :return: nu returneaza nimic
        """
        lista_probleme = self.__srv_problema.getAllProblems()
        if len(lista_probleme) == 0:
            print("Lista de probleme este goala!Nu aveti ce sa modificati!")
            return
        else:
            id_problema = int(input("ID-ul problemei: "))
            nr_pb_nou = int(input("Nr. problema nou: "))
            self.__srv_problema.modificareNrPb(id_problema, nr_pb_nou)
            print("Modificarea nr problemei s-a modificat cu succes!")

    def __modifDescrierePb(self):
        """
        Functia care modifica descrierea unei probleme
        :return: nu returneaza nimic
        """
        lista_probleme = self.__srv_problema.getAllProblems()
        if len(lista_probleme) == 0:
            print("Lista de probleme este goala!Nu aveti ce sa modificati!")
            return
        else:
            id_problema = int(input("ID-ul problemei: "))
            descriere = input("Descriere noua problema: ")
            self.__srv_problema.modificareDescrierePb(id_problema, descriere)
            print("Modificarea descrierii problemei s-a modificat cu succes!")

    def __modifDeadlinePb(self):
        """
        Functia care modifica deadline-ul unei probleme
        :return: nu returneaza nimic
        """
        lista_probleme = self.__srv_problema.getAllProblems()
        if len(lista_probleme) == 0:
            print("Lista de probleme este goala!Nu aveti ce sa modificati!")
            return
        else:
            id_problema = int(input("ID-ul problemei: "))
            zi = int(input("Introduceti ziua: "))
            luna = int(input("Introduceti luna: "))
            an = int(input("Introduceti anul: "))
            deadline = ""
            try:
                deadline = date(an, luna, zi)
            except:
                print("Nu ati introdus o data corecta!")
            self.__srv_problema.modificareDeadlinePb(id_problema, deadline)
            print("Modificarea deadline-ului problemei s-a modificat cu succes!")

    def __genereaza_entitate(self):
        """
        Functia care genereaza o entitate
        :return: nu returneaza nimic
        """
        nr_entitati = int(input("Introduceti nr de entitati: "))
        self.__srv_student.generare_student(nr_entitati)
        self.__srv_problema.generare_problema(nr_entitati)

    def __asignare_laborator(self):
        """
        Functia care asigneaza un laborator unui student
        :return: nu returneaza nimic
        """
        id_student = int(input("ID student: "))
        nr_lab = int(input("Nr laborator: "))
        nr_pb = int(input("Nr problema: "))
        self.__srv_asignare.asignare(id_student, nr_lab, nr_pb)
        print("Laborator asignat cu succes!")

    def __afisare_asignari(self):
        """
        Functia care afiseaza asignarile unui student
        :return: nu returneaza nimic
        """
        lista_asignari = self.__srv_asignare.getAll()
        if len(lista_asignari) == 0:
            print("Lista de asignari este goala!")
            return
        else:
            print("")
            print("Lista de asignari: ")
        print("IDStudent  Nume   Grup    Nr.lab  Nr. pb ")
        for asignare in lista_asignari:
            print(asignare.getStudent(), " ", asignare.getNrLab(), "  ", asignare.getNrPb())
        print("")

    def __notareLab(self):
        """
        Functia care noteaza un laborator
        :return: nu returneaza nimic
        """
        id_student = int(input("ID student: "))
        nr_lab = int(input("Nr laborator: "))
        nota = float(input("Nota: "))
        self.__srv_notare.notare(id_student, nr_lab, nota)
        print("Laborator notat cu succes!")

    def __afisare_not_lab(self):
        """
        Functia care afiseaza notele pe laborator
        :return: nu returneaza nimic
        """
        lista_note = self.__srv_notare.getAllN()
        if len(lista_note) == 0:
            print("Lista de cu notele studentilor este goala!")
            return
        else:
            print("")
            print("Lista cu studentii notati: ")
        print("IDStudent  Nume   Grup    Nr.lab  Nota ")
        for notare in lista_note:
            print(notare.getStudent(), " ", notare.getNrLab(), "      ", notare.getNota())
        print("")

    def __afisare_stud_alfabetic(self):
        """
        Functia care afiseaza lista studentilor si notele lor ordonati alfabetic dupa nume
        :return: nu returneaza nimic
        """
        nr_lab = int(input("Nr lab: "))
        lista_studenti = self.__srv_notare.sortareAlfabetic(nr_lab)
        if len(lista_studenti) == 0:
            print("Lista de studenti notati este goala!")
            return
        else:
            print("")

    def __afisare_stud_nota(self):
        """
        Functia care afiseaza lista studentilor si notele lor ordonati dupa nota
        :return: nu returneaza nimic
        """
        nr_lab = int(input("Nr lab: "))
        lista_studenti = self.__srv_notare.sortareNota(nr_lab)
        if len(lista_studenti) == 0:
            print("Lista de studenti notati este goala!")
            return
        else:
            print("")
            print("Lista de studenti notati dupa nota: ")
        print("IDStudent  Nume   Grup    Nr.lab  Nota ")
        for student in lista_studenti:
            print(student.getStudent(), " ", student.getNrLab(), "      ", student.getNota())
        print("")

    def __lista_media_cinci(self):
        """
        Functia care afiseaza studentii cu media notelor la laborator < 5 (nume student si nota)
        :return: nu returneaza nimic
        """
        lista_stud_sub_cinci = self.__srv_notare.sub_cinci()
        if len(lista_stud_sub_cinci) == 0:
            print("Nu exista studenti sub media 5")
            return
        else:
            print("")

    def __iesire(self):
        """
        Functia de iesire din aplicatie
        :return: nu returneaza nimic
        """
        exit()

    def __medie_mare_cinci(self):
        """
        Functia care afiseaza laboratoarele la care cel putin jumatate din studenti au media > 5
        :return: nu returneaza nimic
        """
        nr_lab = int(input("Nr. laborator: "))
        nr_pb = int(input("Nr. problema"))
        lista_primii_20 = self.__srv_asignare.get20(nr_lab, nr_pb)
        if lista_primii_20 == "":
            print("Nu exista studenti!")
        else:
            nr_afis = 20 * len(lista_primii_20)
            nr_afis = nr_afis // 100
            print("IDStudent  Nume   Grup    Nr.lab")
            for student in lista_primii_20:
                if nr_afis > 0:
                    print(student.getStudent(), "   ", student.getNrLab())
                    nr_afis = nr_afis - 1

    def __printMenu(self):
        """
        Functia care meniul aplicatiei
        """
        print("")
        print("MENIU")
        print("")
        print("Lista de studenti:")
        print("")
        print("1.Adaugare student")
        print("2.Afisare lista de studenti")
        print("3.Stergerea unui student din lista")
        print("4.Cautarea unui student dupa ID")
        print("5.Modificarea numelui unui student.")
        print("6.Modificarea grupei unui student.")
        print("")
        print("Lista de probleme:")
        print("")
        print("7.Adaugarea unei probleme in lista.")
        print("8.Afisarea listei de probleme")
        print("9.Stergerea unei probleme din lista")
        print("10.Cautare problema dupa ID")
        print("11.Modificare nr laborator problema")
        print("12.Modificare nr problema")
        print("13.Modificare descriere problema")
        print("14.Modificare deadline problema")
        print("")
        print("genereaza entitati")
        print("")
        print("15.Asignare laborator")
        print("16.Afisare asignari")
        print("17.Notare laborator")
        print("18.Afisare notari laborator")
        print("19.Lista studenti si notele lor la un laborator ordonati alfabetic dupa nume")
        print("20.Lista studenti si notele lor ordonati dupa nota")
        print("21.Lista studenti cu media notelor de la laborator < 5")
        print("22.Iesire")
        print("23.Afișați cei mai buni 20% studenți pentru un laborator.")

    def run(self):
        """
        Functia de start
        """
        while True:
            self.__printMenu()
            print("")
            comanda = input("Introduceti comanda: ")
            if comanda == "iesire":
                print("Ati ales sa iesiti din aplicatie!")
                return
            if comanda in self.__comenzi:
                try:
                    self.__comenzi[comanda]()
                except ValueError:
                    print("Valoare numerica invalida!")
                except ValidationException as ve:
                    print(ve)
                except RepositoryException as re:
                    print(re)
            else:
                print("Comanda introdusa este invalida!")
