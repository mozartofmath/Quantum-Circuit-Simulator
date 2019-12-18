from Complex import Complex
from State import State
class QuantumGate:
    def __init__(self,name,matrix):
        self.name = name
        self.matrix = matrix
    def tensor(self, othergate):
        resulting_matrix = []
        for i in range(len(self.matrix) * len(othergate.matrix)):
            resulting_matrix.append([])
            for j in range(len(self.matrix) * len(othergate.matrix)):
                resulting_matrix[i].append(Complex(0,0))

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                for k in range(len(othergate.matrix)):
                    for l in range(len(othergate.matrix)):
                        resulting_matrix[i*len(othergate.matrix) + k][j*len(othergate.matrix) + l] = self.matrix[i][j].multiply(othergate.matrix[k][l])
                        
        return QuantumGate("",resulting_matrix)
    def dot(self, state):
        result = []
        for i in range(len(self.matrix)):
            temp = Complex(0,0)
            for j in range(len(self.matrix)):
                temp = temp.add(self.matrix[i][j].multiply(state.state_vector[j]))
                #temp.print()
            result.append(temp)
        return State(result)






























