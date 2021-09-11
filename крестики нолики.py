pole = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
cnt = 1

def draw_pole():
    print('  0 1 2')
    print('0', *pole[0])
    print('1', *pole[1])
    print('2', *pole[2])

draw_pole()

def pobeda(pole):
    if pole[0] == ['X', 'X', 'X'] or pole[1] == ['X', 'X', 'X'] or pole[2] == ['X', 'X', 'X'] or (
            pole[0][0] == 'X' and pole[1][0] == 'X' and pole[2][0] == 'X') or (
            pole[0][1] == 'X' and pole[1][1] == 'X' and pole[2][1] == 'X') or (
            pole[0][2] == 'X' and pole[1][2] == 'X' and pole[2][2] == 'X') or (
            pole[2][0] == 'X' and pole[1][1] == 'X' and pole[0][2] == 'X') or (
            pole[0][0] == 'X' and pole[1][1] == 'X' and pole[2][2] == 'X'):
        print("X win")
        return True
    elif pole[0] == ['0', '0', '0'] or pole[1] == ['0', '0', '0'] or pole[2] == ['0', '0', '0'] or (
                pole[0][0] == '0' and pole[1][0] == '0' and pole[2][0] == '0') or (
                     pole[0][1] == '0' and pole[1][1] == '0' and pole[2][1] == '0') or (
                     pole[0][2] == '0' and pole[1][2] == '0' and pole[2][2] == '0') or (
                     pole[2][0] == '0' and pole[1][1] == '0' and pole[0][2] == '0') or (
                     pole[0][0] == '0' and pole[1][1] == '0' and pole[2][2] == '0'):
        print("0 win")
        return True
    else:
        return False

def true_hod(x):
    global cnt
    if 0 < x[0] > 2 or 0 < x[1] > 2:
        print("неправильный ход")
        cnt -=1
        hod()

    elif pole[x[0]][x[1]] != '-':
        print("неправильный ход")
        cnt-=1
        hod()
    else:
        return x

def hod():
    global cnt
    if cnt % 2 == 0:
        cnt += 1
        x = list(map(int, input('ход 0, введи y,x через пробел: ').split()))
        if true_hod(x):
            pole[x[0]][x[1]] = "0"
            draw_pole()
            return pole, cnt
    else:
        cnt += 1
        x = list(map(int, input('ход Х, введи y,x через пробел: ').split()))
        if true_hod(x):
            pole[x[0]][x[1]] = "X"
            draw_pole()
            return pole, cnt

while not pobeda(pole):
    hod()





