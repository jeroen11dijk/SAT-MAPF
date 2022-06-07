import errno
import functools
import itertools
import os
import signal
import psutil
from func_timeout import func_set_timeout
from tqdm import tqdm

from MAXSATSolverColored import SATSolverColored
from WMStar.mstar import Mstar
from problem_classes import BaseProblem, MAPFW


class TimeoutError(Exception):
    pass


def timeout(seconds, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrapper

    return decorator

@timeout(180)
def mMstar(problem):
    matches = []
    for team in range(len(problem.starts)):
        a = problem.starts[team]
        b = problem.goals[team]
        combinations = [list(zip(comb, b)) for comb in list(itertools.permutations(a, len(b)))]
        matches.append(combinations)
    problems = []
    distances = {}
    tsp_cache = {}
    for match in list(itertools.product(*matches)):
        new_problem = MAPFW()
        new_problem.update(problem, match)
        try:
            new_problem.get_heuristic(distances)
            problems.append(new_problem)
        except:
            pass
    problems.sort(key=lambda x: x.heuristic)
    res = float("inf")
    opt_path = None
    for i, problem in enumerate(problems):
        if problem.heuristic > res:
            break
        waypoints = ((),) * problem.n_agents
        path, cost = Mstar(problem.graph, tuple(problem.starts), waypoints,
                           tuple(problem.goals), tsp_cache).solve()
        if cost < res:
            res = cost
            opt_path = path
    return opt_path, res


@timeout(180)
def SATColoredCNF(problem):
    return SATSolverColored(problem).solve_cnf()


@timeout(180)
def MaxSATColoredCNF(problem):
    return SATSolverColored(problem).solve_cnf(True)


@timeout(180)
def MaxSATColoredCNFInflated(problem):
    return SATSolverColored(problem, inflation=1.25).solve_cnf(True)


if __name__ == '__main__':
    res = {"MaxSATColoredCNF": 0, "MaxSATColoredCNFInflated": 0, "mMstar": 0, "SATColoredCNF": 0}
    file = ""
    done = set()
    ten = 0
    extra = []
    extra_inflated = []
    graph = 'grid_random_3t_64n_8b_8g_10.0r.graph'
    for scene in tqdm(sorted(os.listdir('test/'), key=lambda x: int(x.split('_')[7][0:-1]))):
        main_problem = BaseProblem(graph, 'grid_random_3t_64n_8b_8g_10.0r/' + scene)
        ten += 1
        costs = {"MaxSATColoredCNF": -1, "MaxSATColoredCNFInflated": -1, "mMstar": -1, "SATColoredCNF": -1}
        solvers = [MaxSATColoredCNFInflated]
        for func in solvers:
            print(func.__name__)
            if func.__name__ not in done:
                try:
                    costs[func.__name__] = func(main_problem)[1]
                    res[func.__name__] += 1
                except Exception as e:
                    print(e)
                    pass
        if costs["MaxSATColoredCNF"] > costs["SATColoredCNF"]:
            extra.append(((costs["MaxSATColoredCNF"] - costs["SATColoredCNF"]) / costs["SATColoredCNF"]) * 100)
        if costs["MaxSATColoredCNFInflated"] > costs["SATColoredCNF"]:
            extra_inflated.append(
                ((costs["MaxSATColoredCNFInflated"] - costs["SATColoredCNF"]) / costs["SATColoredCNF"]) * 100)
        if ten == 10:
            print("\n" + str(scene.split('_')[7][0:-1]) + ": " + str(res))
            print(extra)
            print(extra_inflated)
            process = psutil.Process(os.getpid())
            print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
            print(vars())
            file += str(scene.split('_')[7][0:-1]) + ": " + str(res) + '\n'
            for key in res.keys():
                if res[key] == 0:
                    done.add(key)
            res = {"MaxSATColoredCNF": 0, "MaxSATColoredCNFInflated": 0, "mMstar": 0, "SATColoredCNF": 0}
            ten = 0
    file += str(extra) + "\n"
    file += str(extra_inflated)
    open("coloredGrid8.txt", "w").write(file)
