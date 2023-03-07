class Rectangle:
    def __init__(self, width, height):

        self.set_width(width)
        self.set_height(height)

    def __str__(self):

        self.str = f'Rectangle(width={self.width}, height={self.height})'

        return self.str

    def set_width(self, width):

        self.width = width
        if str(self.__class__.__name__).upper() == 'SQUARE':
            self.side = self.width

        return self.width

    def set_height(self, height):

        self.height = height

        return self.height

    def class_name(self):

        self.name = str(__class__.__name__)

        return self.name

    def get_area(self):

        self.area = self.width * self.height

        return self.area

    def get_perimeter(self):

        self.perimeter = 2 * self.width + 2 * self.height

        return self.perimeter

    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return self.diagonal

    def get_picture(self):

        count = 0
        line = list()
        message_big_picture = "Too big for picture."

        if self.height > 50 or self.width > 50: return message_big_picture

        try:
            if self.side != '':
                self.asterisk = '*' * self.side
        except:
            self.side = ''

        self.asterisk = '*' * self.width

        while count < self.height:
            count += 1
            line.append(f'{self.asterisk}\n')
        line = ''.join(line)

        self.picture = line

        return self.picture

    def get_amount_inside(self, object):

        self.shape = object.class_name()
        if self.shape.upper() == 'SQUARE':
            self.shape_area = object.get_area()
        else:
            self.shape_area = object.get_area()

        self.amount_inside = int(self.get_area() / self.shape_area)
        return self.amount_inside


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.set_side(side)

    def __str__(self):
        self.str_square = f'Square(side={self.side})'

        return self.str_square

    def set_side(self, side):
        self.side = side
        self.set_width(side)
        self.set_height(side)

        return self.side

    def class_name(self):
        self.name = str(__class__.__name__)

        return self.name