#
#Author: Adrian Martinez
#Description: takes a few inputs on CPU specs and organizes them accordingly
#
#

cpu_ghz = float(input('Enter CPU gigahertz:\n')) #input for CPU specs
cpu_core = int(input('Enter CPU core count:\n'))
cpu_hyper = input('Enter CPU hyperthreading (True or False):\n')
print()

if cpu_core >= 20:
    print('That is a high-performance CPU.')
    exit(0)

if (cpu_hyper == "True") or (cpu_hyper == 'true'): #setting bool for hyperthreading spec
    cpu_hyper = True
elif (cpu_hyper == 'False') or (cpu_hyper == 'false'):
    cpu_hyper = False
else:
    print('Please enter True or False for hyperthreading')
    exit(0)

if cpu_hyper: #CPUs with hyperthreading
    if (cpu_ghz >= 2.7) and (cpu_core >= 6):
        print ('That is a high-performance CPU.')
        exit(0)
    elif (cpu_ghz >= 2.4) and (cpu_core >= 4):
        print('That is a medium-performance CPU.')
        exit(0)
    elif (cpu_ghz >= 1.9) and (cpu_core >= 2):
        print('That is a low-performance CPU.')
        exit(0)
else: #CPUs without hyperthreading
    if (cpu_ghz >= 3.2) and (cpu_core >= 8):
        print('That is a high-performance CPU.')
        exit(0)
    elif (cpu_ghz >= 2.8) and (cpu_core >= 6):
        print('That is a medium-performance CPU.')
        exit(0)
    elif (cpu_ghz >= 2.4) and (cpu_core >= 2):
        print('That is a low-performance CPU.')
        exit(0)
# everything else
print('That CPU could use an upgrade.')