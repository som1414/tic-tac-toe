def build_field(f):
    print(f"   {' '.join(str(i) for i in range(1, len(f) + 1))}")
    for r in range(len(f)):
        print(str(r + 1), end=' ')
        for c in range(len(f)):
            print(f'|{f[r][c]}', end='')
        print('|')


def users_motion(f, n):
    while True:
        motion = input(f'{n} ведите координаты хода: ')
        if len(motion) != 2:
            print('Введите две координаты')
            continue
        if not (motion[0].isdigit() and motion[1].isdigit()):
            print('Координаты должны быть числами')
            continue
        x, y = map(int, list(motion))
        if not (x >= 1 and x <= size and y >= 1 and y <= size):
            print(f'Вы вышли из диапазона доступных координат, введите числа от 1 до {size}')
            continue
        if f[x - 1][y - 1] != '-':
            print('Ход уже сделан, ходите в другую клетку')
            continue
        break
    return x, y


def who_victory(f, user):
    return [f[i][i] for i in range(len(f))].count(user) == len(f) or \
           [f[len(f) - i - 1][i] for i in range(len(f))].count(user) == len(f) or \
           any([c.count(user) == len(f) for c in f]) or \
           any([c.count(user) == len(f) for c in [list(r) for r in zip(*f)]])


flag = True
while flag:
    print("Игра - 'крестики-нолики'")
    size = int(input('Введите размеры игрового поля: '))
    field = [['-'] * size for _ in range(size)]
    name = [input(f'Здравствуйте, введите имя {i + 1} игрока ') for i in range(2)]
    while True:
        priority = int(input(f'{name[0]} хотите ходить первым? Решите это с {name[1]}; 1 = первым, 2 = вторым\n')) - 1
        if str(priority) not in '01':
            print('Введите 1 или 2')
            continue
        break
    count = 1
    while True:
        if count % 2 != 0:
            user = f'\033[31m{"x"}\033[0m'
        else:
            user = f'\033[32m{"o"}\033[0m'
        build_field(field)
        if count <= size ** 2:
            gamer = name[priority]
            x, y = users_motion(field, gamer)
            field[x - 1][y - 1] = user
            priority = not priority
        if count > size ** 2:
            print('Вы сыграли вничью')
            if input('Сыграете еще раз? д = да, н = нет\n') != 'д':
                flag = False
            break
        if who_victory(field, user):
            build_field(field)
            field[x - 1][y - 1] = user
            print(f'Выйграл {gamer}')
            if input('Сыграете еще раз? д = да, н = нет\n') != 'д':
                flag = False
            break
        count += 1
