class Calculator:
    name = 'Good calculator'
    price = 18

    def add(self, x, y):
        print(self.name)
        result = x + y
        print(result)

    def minus(self, x, y):
        result = x / y
        result = x*y
        print(result)

    def times(self, x, y):
        print(x * y)


calculator = Calculator()
calculator.name = 'hhhh'
calculator.add(1, 2)
calculator.minus(0,2)
