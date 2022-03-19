from Domain.validators_asignare import ValidatorAsignare
from Domain.validators_notare import ValidatorNotare
from GRASPController.asignare_lab_controller import AsignareService
from GRASPController.nota_controller import NotaService
from Repository.asignare_repo import AsignareRepository
from Repository.nota_repo import NotaRepository
from Tests.teste_stud import TesteStudent
from Tests.teste_prob import TesteProblema
from Domain.validators_student import ValidatorStudent
from Domain.validators_problem import ValidatorProblem
from Repository.stud_repo import StudentRepository
from Repository.prob_repo import ProblemRepository
from GRASPController.student_controller import StudentService
from GRASPController.problem_controller import ProblemService
from GRASPController.nota_controller import NotaService

from UI.console import Console

if __name__ == '__main__':
    teste_stud = TesteStudent()
    teste_stud.ruleaza_toate_testele()
    teste_prob = TesteProblema()
    teste_prob.ruleaza_toate_testele()
    valid_student = ValidatorStudent()
    repo_studenti = StudentRepository()
    valid_problema = ValidatorProblem()
    repo_problem = ProblemRepository()
    valid_asignare = ValidatorAsignare()
    repo_asignare = AsignareRepository()
    valid_nota = ValidatorNotare()
    repo_nota = NotaRepository()
    controller_student = StudentService(valid_student, repo_studenti)
    controller_problem = ProblemService(valid_problema, repo_problem, repo_asignare)
    controller_asignare = AsignareService(valid_student, repo_studenti, valid_problema, repo_problem, valid_asignare, repo_asignare)
    controller_notare = NotaService(valid_student, repo_studenti, valid_problema, repo_problem, valid_asignare, repo_asignare, valid_nota, repo_nota)
    cons = Console(controller_student, controller_problem, controller_asignare, controller_notare)
    cons.run()
