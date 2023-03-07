import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **arguments):

        self.arguments = arguments
        self.contents = list()

        if len(self.arguments) < 1:
            return print('Inform at least 1 value')

        for k, v in self.arguments.items():
            balls_number = 0
            while balls_number < v:
                balls_number += 1
                self.contents.append(k)

    def __str__(self):
        return str(self.contents)

    def draw(self, balls):
        count = 0
        self.variable_index = ''
        self.draw_balls = list()

        if balls > len(self.contents):
            return self.contents

        while count < balls:
            count += 1
            self.variable_index = random.choice(range(len(self.contents)))
            self.draw_balls.append(self.contents.pop(self.variable_index))

        return self.draw_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_experiments = 0
    count_exact_balls = 0
    exact_balls_expected = dict()

    while count_experiments < num_experiments:
        count_experiments += 1
        equal_balls = 0
        exact_balls_expected = dict()
        contents_copy = copy.deepcopy(hat)
        total_balls = contents_copy.draw(num_balls_drawn)

        try:
            for i in total_balls:
                if i in exact_balls_expected:
                    exact_balls_expected[i] += 1
                else:
                    exact_balls_expected[i] = 1

            for k, v in exact_balls_expected.items():
                if k in expected_balls and v >= expected_balls[k]:
                    equal_balls += 1

            if equal_balls == len(expected_balls):
                count_exact_balls += 1

        except:
            continue

    experiment_probability = float(count_exact_balls) / num_experiments

    return experiment_probability








