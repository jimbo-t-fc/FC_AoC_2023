def find_first_number(line, find):
    read_char = 0
    search_list = []
    while read_char < len(line):
        # read next character in the line
        char = line[read_char]

        # add new search to the search list
        search_list.append(find)

        # compare the new character to each search list
        for index, search in enumerate(search_list):
            # if the new character matches the next character in the search then keep the search as a potential
            potentials = [x for x in search if x[0].startswith(char)]

            # if the potentials has been narrowed down to one then return
            # else remove matched char from the list of potentials ready for comparing the next char
            if len(potentials) == 1 and len(potentials[0][0]) == 1:
                return potentials[0][1]
            else:
                search_list[index] = [(x[0][1:],x[1]) for x in potentials]
        
        # remove searches that have no potentials from the list (not really needed)
        search_list = [x for x in search_list if x!=[]]
        
        # increment character to read in
        read_char += 1

    return
    

if __name__ == '__main__':
    # Read the input file
    with open("2023/Day 1/input.txt",'r') as f:
        lines = [x for x in f.read().split('\n') if x!='']

    find = ['1','2','3','4','5','6','7','8','9','one','two','three','four','five','six','seven','eight','nine']
    convert = {
        'one': '1'
        ,'two': '2'
        ,'three': '3'
        ,'four': '4'
        ,'five': '5'
        ,'six': '6'
        ,'seven': '7'
        ,'eight': '8'
        ,'nine': '9'
        ,'1': '1'
        ,'2': '2'
        ,'3': '3'
        ,'4': '4'
        ,'5': '5'
        ,'6': '6'
        ,'7': '7'
        ,'8': '8'
        ,'9': '9'
    }
    calval = []
    for line in lines:
        n = find_first_number(line, list(zip(find,[convert[x] for x in find])))
        n += find_first_number(line[::-1], list(zip([x[::-1] for x in find],[convert[x] for x in find])))
            
        calval.append(int(n))
    print(sum(calval))

    pass




    
#     calval = []
#     for line in lines:
#         line_numbers = ''
#         for character in line:
#             if character.isdigit():
#                 line_numbers+=character

#         if len(line_numbers) == 1:
#             coord = int(line_numbers+line_numbers)
#         elif len(line_numbers) > 2:
#             coord = int(line_numbers[0]+line_numbers[-1])
#         else:
#             coord = int(line_numbers)
#         calval.append(coord)
#     print(sum(calval))


    #rev_lines = [x[::-1] for x in lines]