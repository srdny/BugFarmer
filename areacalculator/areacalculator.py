import math

#Square	area=side**2
def square(v_side):
    return v_side**2

#Rectangle	area=length∗width
def reqtangle(v_length,v_width):
    return v_length*v_width

#Triangle	area=(height∗base)/2
def triangle(v_height,v_base):
    return (v_height*v_base)/2

#Circle	area=π∗radius 
def circle(v_radius):
    return math.pi*v_radius

def calculator():
    is_calculator_off = False
    total = 0
    
    while not is_calculator_off:
        print('==================')
        print('Area Calculator 📐')
        print('==================')

        print('1) Triangle')
        print('2) Rectangle')
        print('3) Square')
        print('4) Circle')
        print('5) Quit')

        shape = int(input('Which shape: '))

        if shape == 5 :
            is_calculator_off = True
            total = 0
        elif shape == 1:
            v_height = int(input('Height: '))
            v_base = int(input('Base: '))
            total = triangle(v_height,v_base)
        elif shape == 2:
            v_length = int(input('Length: '))
            v_width = int(input('Width: '))
            total = reqtangle(v_length,v_width)
        elif shape == 3:
            v_side = int(input('Side: '))
            total = square(v_side)
        elif shape == 4:
            v_radius = int(input('Radius: '))
            total = circle(v_radius)
        
        if total > 0:
            print(f'Your Total: {total}') 
            not_repeat = False
            #again = input('Again ? [Y/N]: ')
            while not not_repeat:
                ask = input('Again ? [Y/N]: ').upper()
                if ask == 'N': 
                    not_repeat = True
                    is_calculator_off = True
                elif ask == 'Y': 
                    not_repeat = True
                    is_calculator_off = False
 
 #start
calculator()