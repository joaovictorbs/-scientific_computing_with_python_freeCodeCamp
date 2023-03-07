def arithmetic_arranger(problems, answers=''):
    first_numbers_list = []
    last_numbers_list = []
    operators_list = []
    results_list = []
    line_list = []

    first_numbers_string = ''
    last_numbers_string = ''
    line_string = ''
    results_string = ''
    separator_first = ' ' * 6
    separator_last = ' ' * 4

    count = 0

    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems

    for i in problems:
        numbers = i.strip()
        numbers = numbers.split(' ')
        number_one = numbers[0]
        number_two = numbers[2]

        left_whitespace = 0
        operator_whitespace = 0

        if numbers[1] not in ('+', '-'):
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems

        if numbers[0].isdigit() != True or numbers[2].isdigit() != True:
            arranged_problems = 'Error: Numbers must only contain digits.'
            return arranged_problems

        if len(numbers[0]) > 4 or len(numbers[2]) > 4:
            arranged_problems = 'Error: Numbers cannot be more than four digits.'
            return arranged_problems

        if count < 1:
            if len(number_one) == len(number_two):
                left_whitespace = 2; operator_whitespace = 1
            elif len(number_one) in (2, 3) and len(number_one) > len(number_two):
                left_whitespace = 2
                if len(number_one) == 2 and len(number_two) == 1:
                    operator_whitespace = 2
                elif len(number_one) == 3 and len(number_two) == 1:
                    operator_whitespace = 3
                else:
                    operator_whitespace = 2
            elif len(number_one) == 4 and len(number_one) > len(number_two):
                left_whitespace = 2
                if len(number_two) == 1:
                    operator_whitespace = 4
                elif len(number_two) == 2:
                    operator_whitespace = 3
                else:
                    operator_whitespace = 2

            if len(number_two) in (2, 3) and len(number_one) < len(number_two):
                if len(number_two) == 2 and len(number_one) == 1:
                    left_whitespace = 3; operator_whitespace = 3
                elif len(number_two) == 3 and len(number_one) == 1:
                    left_whitespace = 4; operator_whitespace = 1
                else:
                    left_whitespace = 3; operator_whitespace = 1
            elif len(number_two) == 4 and len(number_one) < len(number_two):
                operator_whitespace = 1
                if len(number_one) == 1:
                    left_whitespace = 5
                elif len(number_two) == 2:
                    left_whitespace = 4
                else:
                    left_whitespace = 3


        else:
            if len(number_one) == len(number_two):
                left_whitespace = 0; operator_whitespace = 1
            elif len(number_one) in (2, 3) and len(number_one) > len(number_two):
                left_whitespace = 0
                if len(number_one) == 2 and len(number_two) == 1:
                    operator_whitespace = 2
                elif len(number_one) == 3 and len(number_two) == 1:
                    operator_whitespace = 3
                else:
                    operator_whitespace = 2
            elif len(number_one) == 4 and len(number_one) > len(number_two):
                left_whitespace = 0
                if len(number_two) == 1:
                    operator_whitespace = 4
                elif len(number_two) == 2:
                    operator_whitespace = 3
                else:
                    operator_whitespace = 2

            if len(number_two) in (2, 3) and len(number_one) < len(number_two):
                if len(number_two) == 2 and len(number_one) == 1:
                    left_whitespace = 3; operator_whitespace = 3
                elif len(number_two) == 3 and len(number_one) == 1:
                    left_whitespace = 4; operator_whitespace = 1
                else:
                    left_whitespace = 3; operator_whitespace = 1
            elif len(number_two) == 4 and len(number_one) < len(number_two):
                operator_whitespace = 1
                if len(number_one) == 1:
                    left_whitespace = 3
                elif len(number_two) == 2:
                    left_whitespace = 2
                else:
                    left_whitespace = 1

                # inserting space
        left_whitespace = ' ' * left_whitespace
        operator_whitespace = ' ' * operator_whitespace

        first_numbers_list.append(f'{left_whitespace}{numbers[0]}')
        operators_list.append(f'{numbers[1]}{operator_whitespace}')
        last_numbers_list.append(f'{numbers[2]}')

        # create "---"
        line_list.append('-' * int(len(numbers[1] + operator_whitespace + numbers[2])))

        # results
        if answers == True:

            if numbers[1] == '+':
                result = str(int(numbers[0]) + int(numbers[2]))
            else:
                result = str(int(numbers[0]) - int(numbers[2]))

            whitespace_answer = ' ' * int(len(numbers[1] + operator_whitespace + numbers[2]) - int(len(result)))
            results_list.append(f'{whitespace_answer}{result}')

        count += 1

    for i in first_numbers_list:
        first_numbers_string += i + separator_first

    for o, n in zip(operators_list, last_numbers_list):
        operator_number = f'{o}{n}'
        last_numbers_string += operator_number + separator_last

    for l in line_list:
        line_string += l + separator_last

    for r in results_list:
        results_string += r + separator_last

    if answers == True:
        arranged_problems = f'{first_numbers_string.rstrip()}\n{last_numbers_string.rstrip()}\n{line_string.rstrip()}\n{results_string.rstrip()}'
    else:
        arranged_problems = f'{first_numbers_string.rstrip()}\n{last_numbers_string.rstrip()}\n{line_string.rstrip()}'

    return arranged_problems