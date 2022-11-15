import numpy as np

class Machine():
    def __init__(self, table):
        self.table = list(table)

    def interpret_instruction(self, state, tape, position):
        row = self.table[state-1]
        if tape[position] == 0:
            instruction = row[1]
        elif tape[position] == 1:
            instruction = row[2]
        else:
            print('ERROR')
            return


        if len(instruction) != 3:
            position = -1
            print('HALTED')
            return (state, tape, position)


        (new_value, move, new_state) = tuple(instruction)
        (new_value, move, new_state) = (int(new_value), move, int(new_state))

        tape[position] = new_value

        if move == 'R':
            position +=1
        if move == 'L':
            position -=1

        return (int(new_state), tape, position)

def merge_list_to_string(list):
    list = ''.join(str(x) for x in list)
    return list

def print_output(state, tape, position):
    state = str(state)
    tape = merge_list_to_string(tape)
    print(state + ':' + tape[:position] + '\033[4m' + tape[position] + '\033[0m' + tape[position + 1:])



table = np.loadtxt('table.txt', dtype=str, delimiter=',')
machine = Machine(table)

tape = '011110'
tape = np.array([int(x) for x in list(tape)])


(state, tape, position) = (1, tape, 0)

print('input: ' + merge_list_to_string(tape))
while position > -1:
    print_output(state, tape, position)
    (state, tape, position) = machine.interpret_instruction(state=state, tape=tape, position=position)