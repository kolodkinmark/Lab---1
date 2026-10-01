from time import sleep
import os


YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'
RED = '\u001b[41m'
BLUE = '\u001b[44m'
END = '\u001b[0m'
GAP = '  '




def flag():
    print("Флаг Литвы\n")
    shir = 50
    vusot = 12
    for i in range(vusot):
        
        if i < 4:
            print(f'{YELLOW}{" " * shir}{END}')
        elif i < 8:
            print(f'{GREEN}{" " * shir}{END}')
        else:
            print(f'{RED}{" " * shir}{END}')
    
# Фигура e
pattern_e = [
    '##          ##',
    '  ##      ##  ',
    '    ##  ##    ',
    '      ##      ',
    '      ##      '
]

def pattern(strings=3, down=3):
    print("Узор e:\n")
    for l in range(down):
        for r in pattern_e:
            line = ''
            for c in r * strings:
                if c == '#':
                    line += f'{GREEN}  {END}'
                else:
                    line += '  '
            print(line)


def animate():
    colors = [YELLOW, GREEN, RED] 
    for m in range(2): 
        for color in colors:
            #очистка консоли
            os.system('cls')
            for r in pattern_e:
                line = ''
                for c in r:
                    if c == '#':
                        line += f'{color}  {END}'
                    else:
                        line += '  '
                print(line)
            sleep(1)


def sequence():
    file = open('sequence.txt')
    chetpoz = [] 
    nechetpoz = []  
    index = 0
    for line in file:
        num = abs(float(line))
        if index % 2 == 0:
            chetpoz.append(num)
        else:
            nechetpoz.append(num)
        index += 1
    file.close()

    sredchet = sum(chetpoz) / len(chetpoz)
    srednechet = sum(nechetpoz) / len(nechetpoz)
    sume = sredchet + srednechet
    answerchet = (sredchet / sume) * 100
    answernechet = (srednechet / sume) * 100
    
    print(f'{YELLOW}{" " * int(answerchet / 2)}{END} {answerchet:.1f}%')
    print(f'{GREEN}{" " * int(answernechet / 2)}{END} {answernechet:.1f}%')



def function():
    print("График функции y = |x|:\n")
    print("  ^ y")
    for y in range(12, 0, -1):
        if y > 9:
            print(f"{y}|{' ' * (y * 2 - 1)}{RED}+{END}")
        else:
            print(f" {y}|{' ' * (y * 2 - 1)}{RED}+{END}")

    print(f" 0{RED}+{END}-----------------------> x")
    print("    1 2 3 4 5 6 7 8 9 10 11 12")
    

animate()
function()
sequence()
flag()
pattern()