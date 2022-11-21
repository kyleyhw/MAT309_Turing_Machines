import numpy as np
from machine import Machine
from misc_functions import merge_list_to_string


filename = 'ps2_q3c.txt'
table = np.loadtxt('machines/' + filename, dtype=str, delimiter=',')
machine = Machine(table)

tape = '011011'
zeros_on_end = 5
tape = tape.ljust(len(tape) + zeros_on_end, '0')
tape = np.array([int(x) for x in list(tape)])

(state, tape, position) = (1, tape, 5)

machine_name = filename.rstrip('.txt')
machine.print_machine_table(machine_name)
print()
print('input: ' + merge_list_to_string(tape))

while position > -1:
    machine.print_output(state, tape, position, show_triple=True)
    (state, tape, position) = machine.interpret_instruction(state=state, tape=tape, position=position)
if position == -1:
    print('CRASHED')