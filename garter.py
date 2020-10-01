# ============================================================================
import os, glob

selfname = os.path.basename(__file__)

targets = glob.glob('*.py')
targets.remove(selfname)

f = open(targets[0], 'r')
targetfile = f.readlines()

f2 = open(selfname, 'r')
selffile = f2.readlines()

for line in targetfile:
    # Since each line has '\n' character, remove it
    print(line.replace('\n', ''))

for line in selffile:
	print(line.replace('\n', ''))

print(selfname)
print(targets)
print(targetfile)
