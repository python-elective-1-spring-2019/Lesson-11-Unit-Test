""" Calculater class that can add, subtrack, multiply and devide """

# https://stackify.com/unit-testing-basics-best-practices/

class Calculater:

    """ init takes 0 arguments """

    def __init__(self):

        # you should here create two instance variables
        # total and error_msg

        self.total = 0
        self.error_msg = ''

    def add(self, num):
        """ Add takes 1 argument an 'int' or 'float', 
            the number to add to 'total' """

        # Think of possible errors that could happen, 
        # and make tests for these errors
        
        self.total += num

    def subtrack(self):
        pass

    def multiply(self):
        pass

    def devide(self):
        pass

    def __str__(self):
        """ Returns 'total' or 'Error message' """

        if self.error_msg != '':
            self.temp = self.error_msg
            self.error_msg = ''
            return self.temp

        return str(self.total)
    
    
    def display(self):
        """ Returns 'total' or 'Error message' """
        return str(self.total)
