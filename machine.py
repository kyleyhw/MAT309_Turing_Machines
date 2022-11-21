from misc_functions import merge_list_to_string
from pandas import DataFrame

class Machine():
    def __init__(self, table):
        self.table = list(table)
        self.states = [x[0] for x in self.table]
        self.zero_instructions = [x[1] for x in self.table]
        self.one_instructions = [x[2] for x in self.table]
        for i in range(len(table)):
            if self.zero_instructions[i] == 'BLANK':
                self.zero_instructions[i] = ' '
            if self.one_instructions[i] == 'BLANK':
                self.one_instructions[i] = ' '

    def print_machine_table(self, name):
        d = {'0':self.zero_instructions, '1':self.one_instructions}
        dframe = DataFrame(data=d, index=self.states)
        dframe.columns.name = name
        print(dframe)

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

    def print_output(self, state, tape, position, show_triple = False):
        state = str(state).rjust(max([len(x[0]) for x in self.table]), ' ')
        tape = merge_list_to_string(tape)
        print(state + ':' + tape[:position] + '\033[4m' + tape[position] + '\033[0m' + tape[position + 1:], end='\t \t \t')

        if show_triple == True:
            position = str(position)
            print('( ' + state + ' , ' + position + ', ' + tape + '... )', end='')

        print()