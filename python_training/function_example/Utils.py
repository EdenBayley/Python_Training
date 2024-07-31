
class Utils():

#example of function that getting parameters and return variable

    def summery_calc(num1, num2):
        summery = num1 + num2
        print (f'summery found the value is {summery}')
        if (summery > 0):
            print (f'the summery of {num1} and {num2} is higher than 0')

        return summery

#example of function that getting parameters only

    def print_string(string_to_print):
        print (string_to_print)

#example of function without parameters and didn't return variables



    def find_length_of_word(word):
        length = len(word)
        print ('action done')
        if (length < 10)
            word = word + 'suffix'
            print ('the updated word is {word}')
        return length

