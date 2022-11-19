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
            return None

        if instruction == 'BLANK':
            position = -2
            print('HALTED')
            return (state, tape, position)

        (new_value, move, new_state) = (instruction[0], instruction[1], instruction[2:])
        (new_value, move, new_state) = (int(new_value), move, int(new_state))

        tape[position] = new_value

        if move == 'R':
            position +=1
        elif move == 'L':
            position -=1
        else:
            print('INVALID INSTRUCTION')
            return None

        return (int(new_state), tape, position)

    def print_output(self, state, tape, position):
        state = str(state).rjust(max([len(x[0]) for x in self.table]), ' ')
        tape = merge_list_to_string(tape)
        print(state + ':' + tape[:position] + '\033[4m' + tape[position] + '\033[0m' + tape[position + 1:])


def merge_list_to_string(list):
    list = ''.join(str(x) for x in list)
    return list




filename = 'ps2_q3b.txt'
table = np.loadtxt(filename, dtype=str, delimiter=',')
machine = Machine(table)

tape = '011011'
tape = tape.ljust(8,'0')
tape = np.array([int(x) for x in list(tape)])

(state, tape, position) = (1, tape, 0)

print(filename.rstrip('.txt'))
print('input: ' + merge_list_to_string(tape))
while position > -1:
    machine.print_output(state, tape, position)
    (state, tape, position) = machine.interpret_instruction(state=state, tape=tape, position=position)
if position == -1:
    print('CRASHED')