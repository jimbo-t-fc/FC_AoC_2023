def check_num(array, y, x, direction):
    num=''
    loop=True
    """ if direction == 'foward':
        while loop:
            digit_last=False
            char = array[symbol_y+y][symbol_x+x]
            if char.isnumeric():
                num = char+num
                digit_last = True

            if x < -1 and not digit_last:
                loop=False
                if num != '':
                    sum+=int(num)
            elif 
            else:
                x-=1 """

def sum_engine_parts(array,symbol_y,symbol_x):
    sum=0
    """ for y in (-1,0,1):
        num=''
        loop=True
        x = 1
        while loop:
            digit_last=False
            char = array[symbol_y+y][symbol_x+x]
            if char.isnumeric():
                num = char+num
                digit_last = True

            if x < -1 and not digit_last:
                loop=False
                if num != '':
                    sum+=int(num)
            elif 
            else:
                x-=1
        

        sum+=int(num) """
    return sum


if __name__ == '__main__':
    # Read the input file
    with open("2023/Day 3/input.txt",'r') as f:
        array = [list(line) for line in f.read().split('\n') if line!='']
    
    sum=0
    for y, row in enumerate(array):
        for x, column in enumerate(row):
            if not array[y][x].isalnum() and array[y][x] != '.':
                sum+=sum_engine_parts(array,y,x)
    
    print(f"Part 1: {sum}")

    pass