from Domain.entitate_problema import Problema
from Domain.validators_problem import ValidatorProblem
from Errors.exceptions import ValidationException, RepositoryException
from Repository.prob_repo import ProblemRepository


class TesteProblema:

    def __problema_repository_tests(self):
        """
        Functia care testeaza functiile de pe repository de problema
        :return: nu returneaza nimic,ridica exceptie
        """
        problema = Problema(1, 12, 123, "abcd", "10/10/2016")
        repoProblema = ProblemRepository()
        assert repoProblema.size() == 0
        repoProblema.adaugare(problema)
        assert repoProblema.size() == 1
        id_problema = Problema(1, None, 0, 0, 0)
        result = repoProblema.findById(id_problema)
        assert (problema.getNrLab() == result.getNrLab())
        assert (problema.getNrPb() == result.getNrPb())
        assert (problema.getDescripion() == result.getDescripion())
        assert (problema.getDline() == result.getDline())
        problema1 = Problema(1, None, 1, 1, "10/12/2021")
        problema2 = Problema(13, None, 1, 1, "10/12/2021")
        try:
            repoProblema.adaugare(problema1)
            assert False
        except RepositoryException as re:
            assert (str(re) == "Problema deja existenta!\n")
        try:
            repoProblema.stergereProblema(problema2)
            assert False
        except RepositoryException as re:
            assert (str(re) == "Aceasta problema nu exsita in lista!\n")

        result1 = repoProblema.findById(id_problema)
        modif1 = Problema(1, 12, 0, 0, 0)
        repoProblema.update(result1)
        assert (result1.getNrLab() == modif1.getNrLab())
        modif2 = Problema(1, 12, 12, 0, 0)
        assert (result1.getNrLab() == modif2.getNrLab())
        modif3 = Problema(1, 12, 12, "abcd", 0)
        assert (result1.getNrLab() == modif3.getNrLab())
        modif4 = Problema(1, 12, 12, "abcd", "10/12/2021")
        assert (result1.getNrLab() == modif4.getNrLab())
        try:
            repoProblema.stergereProblema(123)
            assert False
        except RepositoryException as re:
            assert (str(re) == "Aceasta problema nu exsita in lista!\n")
        repoProblema.stergereProblema(1)
        assert repoProblema.size() == 0

    def __problema_validator_test(self):
        """
        Functia care testeaza functiile de validare
        :return: nu returneaza nimic
        """
        validator = ValidatorProblem()

        pb1 = Problema("", "", "", "", "")
        try:
            validator.valideazaProblema(pb1)
            assert False
        except ValidationException as ex:
            assert len(ex.getErrors()) > 0

        pb2 = Problema(12, "", "", "", "")
        try:
            validator.valideazaProblema(pb2)
            assert False
        except ValidationException as ex:
            assert len(ex.getErrors()) > 0

        st3 = Problema(1, 12, 123, "abcd", "10/20/2020")
        try:
            validator.valideazaProblema(st3)
            assert True
        except ValidationException as ex:
            assert False

    def __problemaDomainTests(self):
        """
        Functi cate testeaza functiile din domain
        :return: nu returneaza nimic
        """
        id_problema = 1
        nr_lab = 12
        nr_pb = 123
        descriere = "abcd"
        deadline = "12/12/2021"
        problema = Problema(id_problema, nr_lab, nr_pb, descriere, deadline)
        assert (problema.getID() == 1)
        assert (problema.getNrLab() == 12)
        assert (problema.getNrPb() == 123)
        assert (problema.getDescripion() == "abcd")
        assert (problema.getDline() == "12/12/2021")
        problema1 = Problema(id_problema, 0, 0, 0, 0)
        assert (problema == problema1)

    def ruleaza_toate_testele(self):
        """
        Functia care ruleaza toate testele
        """
        # teste problema
        self.__problema_repository_tests()
        self.__problema_validator_test()
        self.__problemaDomainTests()
