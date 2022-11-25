import numpy as np
from machine import Machine
from misc_functions import merge_list_to_string


filename = 'example_12_2.txt'
table = np.loadtxt('machines/' + filename, dtype=str, delimiter=',')
machine = Machine(table)

tape = '0110111'
zeros_on_end = 5
tape = tape.ljust(len(tape) + zeros_on_end, '0')
tape = np.array([int(x) for x in list(tape)])

(state, position, tape) = (1, 0, tape)

machine_name = filename.rstrip('.txt')
machine.print_machine_table(machine_name)
print()
print('input: ' + merge_list_to_string(tape))

while position > -1:
    machine.print_output(state, position, tape, show_triple=False)
    (state, position, tape) = machine.interpret_instruction(state=state, position=position, tape=tape)
if position == -1:
    print('CRASHED')