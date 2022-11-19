import numpy as np
from machine import Machine
from misc_functions import merge_list_to_string


filename = 'ps2_q3b.txt'
table = np.loadtxt('machines/' + filename, dtype=str, delimiter=',')
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