import sys

def my_func(num_1,num_2):
    return int(num_1) + int(num_2)

if (__name__ == '__main__'):
    print(my_func(sys.argv[1],sys.argv[2]))
