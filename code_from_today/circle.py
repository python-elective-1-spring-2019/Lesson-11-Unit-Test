from math import pi

def area(r): 
    
    if type(r) not in [int, float]:
        raise TypeError('Radius should be of numeric value ')

    if r < 0:
        raise ValueError('Radius can not be a negativ number')

    return pi * r**2


def main():

   # while True:
   #     inp = int(input('Radius of circle: '))    
   #     print(area(inp))

    radius = [1, 0, -3, True, 'Hello', [1, 2]]
    
    for r in radius:
        try:
            print(f'Area of circle with {r} is {area(r)}')
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()







