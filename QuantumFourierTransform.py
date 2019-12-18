from QuantumComputer import QuantumComputer
from QuantumGate import QuantumGate
from Complex import *
from State import State

def Rk(k):
    return QuantumGate("",[[Complex(1,0), Complex(0,0)],
                        [Complex(0,0), ComplexA((2*math.pi) / (2**k))]])

computer = QuantumComputer(3)
computer.gatearray = [[computer.universal_gate_set["I"] ,computer.universal_gate_set["H"] ,Rk(2)                           ,Rk(3)                            ,computer.universal_gate_set["I"],computer.universal_gate_set["I"] ,computer.universal_gate_set["I"],computer.universal_gate_set["P"] ,computer.universal_gate_set["X"],computer.universal_gate_set["P"] ],
                      [computer.universal_gate_set["I"] ,computer.universal_gate_set["I"] ,computer.universal_gate_set["P"],computer.universal_gate_set["I"] ,computer.universal_gate_set["H"],Rk(2)                            ,computer.universal_gate_set["I"],computer.universal_gate_set["I"] ,computer.universal_gate_set["I"],computer.universal_gate_set["I"] ],
                      [computer.universal_gate_set["X"] ,computer.universal_gate_set["I"] ,computer.universal_gate_set["I"],computer.universal_gate_set["P"] ,computer.universal_gate_set["I"],computer.universal_gate_set["P"] ,computer.universal_gate_set["H"],computer.universal_gate_set["X"] ,computer.universal_gate_set["P"],computer.universal_gate_set["X"] ]]

computer.compute()
computer.display_current_state()
