# Created by Leon Hunter at 12:10 PM 12/08/2020
class Lister(object):
    def get_integer_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
        '''
        if step != 0:
            result= []
            for value in range(start, stop+1, step):
                result.append(value)
            return result
        return [0]


    def get_even_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are divisible by 2
        '''
        if step != 0:
            result= []
            for value in range(start, stop+1, step):
                if value % 2==0:
                    result.append(value)
            return result
        return [0]



    def get_odd_list(self, start, stop, step):
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are not divisible by 2
        '''
        if step != 0:
            result= []
            for value in range(start, stop+1, step):
                if value % 2==1:
                    result.append(value)
            return result
        return []
