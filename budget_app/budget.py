class Category:
    def __init__(self, category):

        self.category = category
        self.ledger = list()
        self.balance = list()
        self.list_description = list()
        self.list_values = list()
        self.print = list()
        self.deposit_amount = 0
        self.negative_amount = 0
        self.count = 0
        self.characters = 30

    def get_category_name(self):
        return self.category

    def get_balance(self):
        try:
            return self.balance[-1]
        except:
            return False

    def check_funds(self, value):
        self.value = float(value)
        try:
            if self.value > self.balance[-1]:
                return False
            else:
                return True
        except:
            return 'Error'

    def deposit(self, amount, description=''):

        self.deposit_amount = amount
        self.deposit_description = description

        self.ledger.append({"amount": self.deposit_amount, "description": self.deposit_description})
        if len(self.balance) < 1:
            self.balance.append(float(self.deposit_amount))
        else:
            self.balance.append(float(self.balance[-1]) + float(self.deposit_amount))

        return self.ledger

    def withdraw(self, amount, description=''):
        self.negative_amount = amount
        self.negative_description = description

        if self.check_funds(self.negative_amount) == True:
            self.ledger.append({"amount": -abs(self.negative_amount), "description": self.negative_description})
            self.balance.append(float(self.balance[-1]) - float(self.negative_amount))
            return True
        else:
            return False

    def transfer(self, amount, category_transfer):

        self.transfer_amount = amount
        self.category_transfer = str(category_transfer.get_category_name())
        self.negative_amount = self.transfer_amount

        if self.withdraw(self.transfer_amount, f'Transfer to {self.category_transfer}') != False:
            category_transfer.deposit(self.transfer_amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def ledger_list(self):
        return self.ledger

    def __str__(self):
        self.letters_count_category = len(self.get_category_name())
        characters_quantity = self.characters - self.letters_count_category
        characters_quantity = characters_quantity / 2
        asterisk = '*' * int(characters_quantity)

        for line in self.ledger:
            for k, v in line.items():
                self.count += 1
                if (self.count % 2) == 0:
                    self.list_description.append(v)
                else:
                    self.list_values.append(v)

        for description, values in zip(self.list_description, self.list_values):
            description = description[:23]
            values = f'{float(values):.2f}'[:7]

            total_len = len(description) + len(values)
            whitespace = self.characters - total_len
            if len(description) == 23:
                whitespace = 1
            whitespace = ' ' * int(whitespace)

            line_string = f'{description}{whitespace}{values}\n'
            self.print.append(line_string)

        title = f'{asterisk}{self.get_category_name()}{asterisk}'
        description_values = ''.join(self.print)
        total = f'Total: {sum(self.list_values)}'

        self.result = f'{title}\n{description_values}{total}'
        return self.result


def create_spend_chart(categories):
    if len(categories) > 4:
        return 'Inform a maximum of 4 categories'

    percentage_dictionary = dict()
    new_list_word = dict()
    word_dictionary = dict()
    categories_names = list()
    percentage_print_list = list()
    word_dictionary_print_list = list()
    list_withdraw = list()

    percentage_dictionary = {new_list: [] for new_list in range(0, 101, 10)}

    count = -1
    category_number = -1
    amount = 0
    total_amount = 0
    left_whitespace = ' ' * 4
    right_whitespace = ' ' * 2
    quantity_categories = len(categories)
    line = '-' * ((quantity_categories * 3) + 1)

    for category in categories:
        categories_names.append(category.get_category_name())

        amount = 0
        for line_item in category.ledger:
            for k, v in line_item.items():
                count += 1
                if (count % 2) == 0:
                    if float(v) < 0:
                        amount += abs(float(v))
        list_withdraw.append(amount)
        total_amount += amount

    for i in list_withdraw:
        percentage_list = list(map(lambda amount: int((((amount / total_amount) * 10) // 1) * 10), list_withdraw))

    # general percentage
    for category in categories:

        # append "o" space
        if categories_names.index(category.get_category_name()) == 0:
            append_string = f' o'
        else:
            append_string = f'o'

        category_number += 1

        # percentage "o"
        for k in percentage_dictionary:
            right_whitespace = ' ' * 2
            if percentage_list[category_number] >= k:
                if categories_names[-1] != category.get_category_name(): right_whitespace = ' '
                percentage_dictionary[k].append(append_string + right_whitespace)
            else:
                if categories_names.index(category.get_category_name()) == 0 or categories_names[
                    -1] == category.get_category_name(): right_whitespace = ' ' * 3
                percentage_dictionary[k].append(right_whitespace)

                # name of each category ------------------------------------------------------------------------------------------
            new_dict_word = {new_list_word: [] for new_list_word in range(len(category.get_category_name()))}
            word_dictionary.update(new_dict_word)
            # ----------------------------------------------------------------------------------------------------------

    # percentage string ------------------------------------------------------------------------------------------
    for k, v in percentage_dictionary.items():
        value = ' '.join(v)
        if k == 0:
            k = f' {k}|'
        else:
            k = f'{k}|'
        percentage_print_list.append(f'{k}{value}\n')
    percentage_print_list.reverse()
    # --------------------------------------------------------------------------------------------------------

    # category string ------------------------------------------------------------------------------------------
    count = -1
    empty_space = ' '
    right_whitespace = ' ' * 2

    for category in categories:
        count += 1

        for k in word_dictionary:
            try:
                if count > 0:
                    word_dictionary[k].append(f'{empty_space}{category.get_category_name()[k]}')
                else:
                    word_dictionary[k].append(f'{category.get_category_name()[k]}')
            except:
                if count > 0:
                    word_dictionary[k].append(f'  ')
                else:
                    word_dictionary[k].append(f' ')

    for k, v in word_dictionary.items():
        value = ' '.join(v)
        if k == 0: value = f' {value}'
        word_dictionary_print_list.append(f'{left_whitespace}{value}{right_whitespace}\n')
    # ----------------------------------------------------------------------------------------------------

    # final strings ------------------------------------------------------------------------------------------
    percentage_string = ' '.join(percentage_print_list)
    line = f'{left_whitespace}{line}'
    vertical_words = ' '.join(word_dictionary_print_list)
    # ----------------------------------------------------------------------------------------------------

    final_string = (f'Percentage spent by category\n{percentage_string}{line.rstrip()}\n{vertical_words.rstrip()}  ')
    return final_string
