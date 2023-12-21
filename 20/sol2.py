import re
from dataclasses import dataclass
from dataclasses import field
import queue
import sys

file = open("20/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

@dataclass
class Module():
    targets: list[str]
    type: int # 0 -> broadcast, 1 -> flipflop, 2 -> conjuction
    state: dict[str,int] # 'd will mean default mode in all the other types
    connected_moduels: set[str] = field(default_factory=set) # only usefull for conjuctions
    def receive_pulse(self,pulse,pulse_queue):
        match self.type:
            case 0:
                for t in self.targets:
                    pulse_queue.put((pulse[0],t,pulse[1]))
            case 1:
                if pulse[0] == 0:
                    if self.state['d'] == 0:
                        self.state['d'] = 1
                        for t in self.targets: pulse_queue.put((1,t,pulse[1]))
                    else:
                        self.state['d'] = 0
                        for t in self.targets: pulse_queue.put((0,t,pulse[1]))
            case 2:
                self.state[pulse[2]] = pulse[0]
                if all((self.state[i] == 1 for i in self.state)):
                    for t in self.targets: pulse_queue.put((0,t,pulse[1]))
                else:
                    for t in self.targets: pulse_queue.put((1,t,pulse[1]))

modules: dict[str,Module] = dict()
conjuctions = set()
for l in lines:
    mod_name, mod_targets = l.split('->')
    mod_targets = mod_targets.split(',')
    mod_targets = [i.strip() for i in mod_targets]
    if mod_name[0] == 'b':
        mod = Module(mod_targets,0,dict())
        modules[mod_name[:-1]] = mod
    elif mod_name[0] == '%':
        mod = Module(mod_targets,1,{'d':0})
        modules[mod_name[1:-1]] = mod
    else:
        mod = Module(mod_targets,2,dict())
        modules[mod_name[1:-1]] = mod
        conjuctions.add(mod_name[1:-1])

for m in modules:
    if m in conjuctions: continue
    for t in modules[m].targets:
        if t in conjuctions:
            modules[t].connected_moduels.add(m)

for m in conjuctions:
    for c in modules[m].connected_moduels:
        modules[m].state[c] = 0

def test_print(module,deep):
    a = '\t'
    print(f"{a*deep}{modules[module].state}")
    for m in modules[module].state:
        if m in conjuctions:
            test_print(m,deep+1)

# print(modules)
high_pulses = 0
low_pulses = 0
pulse_queue = queue.Queue()
key_modules = {
    'rt':[0,0],
    'sl':[0,0],
    'fv':[0,0],
    'gk':[0,0],
}
for i in range(10000):
    pulse_queue.put((0,'broadcaster','button'))
    stop = False
    while pulse_queue.qsize() != 0:
        pulse = pulse_queue.get()
        if pulse[0] == 0 and (pulse[2] in key_modules) and i != key_modules[pulse[2]][1]:
            key_modules[pulse[2]][0] = i - key_modules[pulse[2]][1]
            key_modules[pulse[2]][1] = i
            print(i,pulse[2])
            # if all(key_modules[j] != 0 for j in key_modules):
            #     stop = True
            #     break
        # print(pulse)
        if pulse[0] == 0: 
            low_pulses +=1 
        else: 
            high_pulses +=1
        if pulse[1] == 'rx':
            continue
        else:
            modules[pulse[1]].receive_pulse(pulse,pulse_queue)
tot = 1
print(key_modules)
for j in key_modules:
    tot *= key_modules[j][0]
print(tot)