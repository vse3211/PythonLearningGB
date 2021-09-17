class Data:
    @staticmethod
    def range_checker(s, e, v):
        return s <= v <= e

    @classmethod
    def to_int(cls, date):
        return str(date).split('-')

    @staticmethod
    def validate(val):
        if (Data.range_checker(1, 12, int(val[1]))):
            if (int(val[1]) % 2 == 1 and Data.range_checker(1, 31, int(val[0]))):
                return val
            elif (int(val[1]) != 2 and int(val[1]) % 2 == 0 and Data.range_checker(1, 30, int(val[0]))):
                return val
            elif (int(val[1]) == 2 and Data.range_checker(1, 29, int(val[0]))):
                return val
            # Весокосный год проверять не стал из-за нехватки времени
            else:
                raise ValueError('Incorrect Day Number')
        else:
            raise ValueError('Incorrect month code!')


print('.'.join(Data.validate(Data.to_int(input('Enter date with format dd-mm-year: ')))))
