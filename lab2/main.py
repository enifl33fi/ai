from nio import Io
from parser import Parser
from solver import Solver

ioInst: Io = Io()
parserInst: Parser = Parser()
solverInst: Solver = Solver()

ioInst.start()
while True:
    req: str = ioInst.get_value()
    data: tuple = parserInst.parse(req)
    if data is None:
        ioInst.error()
        continue
    try:
        print(f'The answer is {solverInst.solve(data)}')
    except:
        ioInst.error()
