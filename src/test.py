from models.demo import Demo
from common.op import Operation

p = r"C:/Users/Jess/Documents/My Demos/CodePipeline with Multi-Account Architectures [ R1 - V1 ].demo"
d = Demo(path=p)
print(d)
for i, sect in enumerate(d.iter_sect()):
    for j, step in enumerate(sect):
        print(i, step.idx)
        if step.idx == 0:
            print("NEW SECT")
            print("Sect " + str(i) + ", Step " + str(j))