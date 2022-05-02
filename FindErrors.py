import random

from main import solver1, solver3
from problem_classes import BaseProblem

if __name__ == '__main__':
    for i in range(1000):
        print(i)
        main_problem = BaseProblem(random.randint(2, 8), 1, random.randint(5, 10), random.uniform(0, 0.3))
        try:
            res0 = solver1(main_problem)
            res1 = solver3(main_problem)
            if res0[1] != res1[1]:
                print("=======================================")
                print(res0)
                print(res1)
                print(main_problem.graph)
                print(main_problem.starts)
                print(main_problem.goals)
                print("=======================================")
        except:
            pass
