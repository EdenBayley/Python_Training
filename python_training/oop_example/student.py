from python_training.oop_example.person import person


class student(person):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def average_calc(self, grades):
        summery = 0
        for grade in grades:
            summery = summery + grade

        grades_size = len(grades)
        average = summery/grades_size
        print (f'the average grade is {average}')
        return average