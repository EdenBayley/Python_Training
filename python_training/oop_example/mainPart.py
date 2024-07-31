from python_training.oop_example.driver import driver
from python_training.oop_example.lecture import lecture
from python_training.oop_example.student import student


class mainPart():
    print('test start')

    lecture_history = lecture('history')
    lecture_english = lecture('english')
    student_1 = student('Eden', 'Bayley')
    student_2 = student('Hannah', 'Bailey')
    driver_1 = driver("a")

    driver_1.print_speed(60)
    student_1.age_calculator(23)
    student_2.age_calculator(21)
    student_1.average_calc([67,67,90,100])

    student_1.age_printing_into_person(34)

    print('test end')
