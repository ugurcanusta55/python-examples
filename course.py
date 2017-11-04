
LOOK_UP = 1
ADD = 2
ALL_REC = 3
QUIT = 4

def main():
    course_inf = {'cs101':['3004','haynes','8:00 am'],'cs102':['4501','alvarado','9:00 am'],
                  'cs103':['6755','rich','10:00 am']}
    counter = 0
    while counter != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(course_inf)
        elif choice == ADD:
            add(course_inf)
        elif choice == ALL_REC:
            all_rec(course_inf)






def get_menu_choice():
    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a birtday: ')
    print('2. Add a birtday: ')
    print('3. All Records')
    print('4.Quit the program: ')
    print()

    choice = int(input('Enter your choice'))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))
    return choice

def look_up(course_inf):
    course_numer = input('Enter course number: ')
    cs,rm,ins = course_inf[course_numer]
    print(cs)
    print(rm)
    print(ins)

def all_rec(course_inf):
    for cs,ins,mt in course_inf.values():
        print(cs,ins,mt)


def add(course_inf):
    course_number = input('course number: ')
    room_number = input('room number: ')
    instructor = input('Instructor : ')
    meeting_time = input('meeting time: ')
    if course_number not in course_inf:
        course_inf[course_number] = room_number, instructor, meeting_time
    else:
        print('That entry already exist.')


main()
