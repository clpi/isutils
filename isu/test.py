from dataclasses import dataclass, fields
from models.demo.demo import Demo
from models.operation import Op, ShellOp, InsertOp, get_op
from enum import Enum, auto

class OpKind(Enum):
    Shell = auto()
    Insert = auto()
    Section = auto()
    Audio = auto()
    Crop = auto()

#p = r"C:/Users/Jess/Documents/My Demos/CodePipeline with Multi-Account Architectures [ R1 - V1 ].demo"
#d = Demo(path=p)
#print(d)
"""
for i, sect in enumerate(d.iter_sect()):
    for j, step in enumerate(sect):
        print(i, step.idx)
        if step.idx == 0:
            print("NEW SECT")
            print("Sect " + str(i) + ", Step " + str(j))
"""

def print_ops(op: Op):
    print(op.apply_to)
    print(op.all_steps)
    print(fields(op))

if __name__ == "__main__":
    print(get_op(1))
    op = Op()
    sop = ShellOp()
    print(type(op))
    print(type(sop))
    print_ops(op)
    print_ops(sop)