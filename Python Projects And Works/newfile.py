def python():
        x = ("python")
        y = ("Is ")
        z = (" amazing?(Y/N)     ")
        a = str(input(y + x + z ))
        if a ==  'Y' or a == 'y':
                print('yes python is amazing!!!!!')
        elif a == 'n' or a == 'N':
                print("no! python is amazing")
        elif a != 'y' or 'Y' or 'n' or 'N':
                python()
python()
