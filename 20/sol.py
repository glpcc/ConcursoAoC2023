import re
from dataclasses import dataclass
from dataclasses import field
import queue

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


# print(modules)
high_pulses = 0
low_pulses = 0
pulse_queue = queue.Queue()
for i in range(1000):
    pulse_queue.put((0,'broadcaster','button'))
    while pulse_queue.qsize() != 0:
        pulse = pulse_queue.get()
        # print(pulse)
        if pulse[0] == 0: 
            low_pulses +=1 
        else: 
            high_pulses +=1
        if pulse[1] in modules:
            modules[pulse[1]].receive_pulse(pulse,pulse_queue)

print(low_pulses,high_pulses,low_pulses*high_pulses)