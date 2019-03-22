from calculater import Calculater


def main():
    calc = Calculater()

    while True:

        inp = input(calc)

        if '+' in inp:
            temp = inp.split('+')
            calc.add(int(temp[-1]))
        elif '-' in inp:
            calc.subtrack()
        elif '/' in inp:
            calc.devide()
        elif '*' in inp:
            calc.multiply()
        else:
            pass


if __name__ == "__main__":
    main()
