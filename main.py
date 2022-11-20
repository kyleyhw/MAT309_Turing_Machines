import numpy as np
from machine import Machine
from misc_functions import merge_list_to_string


filename = 'ps2_q3d.txt'
table = np.loadtxt('machines/' + filename, dtype=str, delimiter=',')
machine = Machine(table)

tape = '011111'
tape = tape.ljust(len(tape) + 2,'0')
tape = np.array([int(x) for x in list(tape)])

(state, tape, position) = (1, tape, 0)

print(filename.rstrip('.txt'))
print('input: ' + merge_list_to_string(tape))
while position > -1:
    machine.print_output(state, tape, position, show_triple=False)
    (state, tape, position) = machine.interpret_instruction(state=state, tape=tape, position=position)
if position == -1:
    print('CRASHED')