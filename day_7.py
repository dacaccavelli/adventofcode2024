
equations: list[list[int]] = []

with open('data/day_7.txt', 'r') as f:
    for line in f:
        split_line = line.split(' ')
        split_line[0] = split_line[0].replace(":", "")
        split_line[-1] = split_line[-1].replace("\n", "")
        int_line = [int(x) for x in split_line]
        equations.append(int_line)

# equations = [[11884578, 0, 0, 0, 0, 0, 11884578], [10, 5, 2], [190, 10, 19], [3267, 81, 40, 27], [292, 11, 6, 16, 20]]

total_calibration_result = 0
for equation in equations:
    total = equation[0]
    value_list = []
    value_list.append(equation[1])
    equation = equation[2:]

    for next_value in equation:
        for value in reversed(value_list):
            value_list.append(value*next_value)
            value_list.append(value+next_value)
            value_list.append(int(str(value)+str(next_value)))
            value_list.remove(value)

    if total in value_list:
        total_calibration_result += total
        print(total)

print(total_calibration_result)








###########################################################
# # FAILED because too much recursion
# # make a list that tracks mult or add
# # pass original equation
# # check when work list is n-2 if equal, else remove last added mult. When all popped, it fails.
# def calibrate(equation: list, operators: list | int = [], running_total: int = None) -> int:

#     def _backtrack(operators: list) -> list:
#         print(f'backtrack: {operators}')
#         if len(operators) == 0:
#             return 0
#         if operators[-1] == 'mult':
#             operators[-1] = 'add'
#             return operators
#         else:
#             del operators[-1]
#             return _backtrack(operators)

#     print(equation, operators, running_total)

#     # break out if all operator combinations failed
#     if isinstance(operators, int):
#         return 0

#     # Recalculate running total if it had to backtrack
#     if not running_total:
#         # print(equation)
#         # print(operators)
#         running_total = equation[1]
#         count = 2
#         for operator in operators:
#             if operator == 'mult':
#                 running_total *= equation[count]
#             else:
#                 running_total += equation[count]
#             # print(f'Recalculate: {running_total}')
#             count +=1


#     remaining_operators = len(equation) - 2 - len(operators)

#     # Final check logic
#     if remaining_operators == 0:

#         if running_total == equation[0]:
#             return equation[0]
#         else:
#             new_operators = _backtrack(operators)
#             return calibrate(equation, new_operators, None)

#     # Build the operator list
#     else:
#         print(running_total)
#         if running_total * equation[-remaining_operators] <= equation[0] and running_total * equation[-remaining_operators] > 0:
#             # print(operators)
#             # print(f'In mult: {running_total}')
#             # print(f'In mult: {equation[-remaining_operators]}')
#             running_total *= equation[-remaining_operators]
#             operators.append('mult')
#         elif running_total + equation[-remaining_operators] <= equation[0]:
#             running_total += equation[-remaining_operators]
#             operators.append('add')
#         else:
#             new_operators = _backtrack(operators)
#             return calibrate(equation, new_operators, None)
#         # print(operators)
#         return calibrate(equation, operators, running_total)


# def test():
#     print(calibrate([189170, 7, 269, 76, 698, 93, 3]))

# test()

# total_calibration_result = 0

# for equation in equations:
#     print(total_calibration_result)
#     total_calibration_result += calibrate(equation, [], None)
####################################################
