def hello():
    print('Hello User!')

def pack(a,b,c):
    return([a,b,c])

# ATTEMPT - NESTED LOOP WON'T WORK.
# def eat_lunch(my_list):
#     if my_list == []:
#         print('My lunchbox is empty!')
#     else:
#         for i in my_list:
#             print(f'first I eat {my_list[0]}.')
#             for x in range(len(my_list)):
#                 print(f'next I eat {my_list[x]}')

def eat_lunch(my_list):
    if len(my_list) == 0:
        print('My lunchbox is empty!')
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f'first I eat {my_list[0]}')
            else:
                print(f'then I eat {my_list[i]}')


hello()
pack('toothpaste', 'toothbrush', 'cups')
eat_lunch(['Ham', 'Cheese'])