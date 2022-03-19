from Domain.entitate_student import Student
from Domain.validators_student import ValidatorStudent
from Errors.exceptions import ValidationException, RepositoryException
from Repository.stud_repo import StudentRepository


class TesteStudent:

    def __student_repository_tests(self):
        """
        Functia care testeaza functiile de pe repository de student
        :return: nu returneaza nimic,ridica exceptie
        """
        student = Student(1, "Alex", 12)
        repoStudent = StudentRepository()
        assert repoStudent.size() == 0
        repoStudent.adaugare(student)
        assert repoStudent.size() == 1
        id_student = Student(1, None, 0)
        result = repoStudent.findById(id_student)
        assert (student.getNume() == result.getNume())
        assert (student.getGrup() == result.getGrup())
        student1 = Student(1, None, 0)
        student2 = Student(13, None, 1)
        try:
            return repoStudent.adaugare(student1)
            assert False
        except RepositoryException as re:
            assert (str(re) == "Student deja existent!\n")
        try:
            repoStudent.stergereStudent(student2)
            assert False
        except RepositoryException as re:
            assert (str(re) == "Acest student nu exsita in lista!\n")

        result1 = repoStudent.findById(id_student)
        modif1 = Student(1, None, 0)
        repoStudent.update(modif1)
        assert (result1.getNume() == modif1.getNume())
        modif2 = Student(1, 12, 15)
        assert (result1.getGrup() == modif2.getGrup())
        try:
            repoStudent.stergereStudent(123)
            assert False
        except RepositoryException as re:
            assert (str(re) == "Acest student nu exsita in lista!\n")
        repoStudent.stergereStudent(1)
        assert repoStudent.size() == 0

    def __testEqual(self):
        """
        Functia care testeaza functia de verificare a egalitatii
        """
        stud1 = Student("1", "Ana", "201")
        stud2 = Student("1", "Ana", "210")
        assert stud1 == stud2

    def __testValideazaStudent(self):
        """
        Functia care testeaza validarea unui student
        """
        validator = ValidatorStudent()

        st = Student("", "", "")
        try:
            validator.valideazaStudent(st)
            assert False
        except ValidationException as ex:
            assert len(ex.getErrors()) > 0

        st = Student(12, "", "")
        try:
            validator.valideazaStudent(st)
            assert False
        except ValidationException as ex:
            assert len(ex.getErrors()) > 0

        st = Student(1, "Ion", "12")
        try:
            validator.valideazaStudent(st)
            assert True
        except ValidationException as ex:
            assert False

    def __student_domain_tests(self):
        """
        Functia care testeaza functiile din domain
        :return: nu returneaza nimic
        """
        id = 1
        nume = "Ana"
        grupa = 123
        student = Student(id, nume, grupa)
        assert (student.getID() == 1)
        assert (student.getNume() == "Ana")
        assert (student.getGrup() == 123)
        student1 = Student(id, 0, 0)
        assert (student == student1)


    def __testValideazaID(self):
        """
        Functia care testeaza validarea unui id
        """
        validator = ValidatorStudent()
        id1 = ""
        try:
            validator.valideazaID(id1)
            assert False
        except ValidationException as ex:
            assert len(ex.getErrors()) > 0

        id2 = -1
        try:
            validator.valideazaID(id2)
            assert False
        except ValidationException as ex:
            assert len(ex.getErrors()) > 0


    def ruleaza_toate_testele(self):
        """
        Functia care ruleaza toate testele
        """
        #teste student
        self.__testValideazaStudent()
        self.__student_domain_tests()

