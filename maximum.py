def enter():
    print('Enter some numbers')
    print('press q to stop')
    a_list = []
    while True:
        n = (input())
        if n == 'q':
            break
        a_list.append(int(n))
    return a_list

def find_max(a_list):
    if not a_list:
        return 0
    max_num = a_list[0]
    for num in a_list:
        if num >= max_num:
            max_num = num
    return max_num

def main():
    a_list = enter()
    num = find_max(a_list)
    print(a_list)
    print('the maximum is', num)

main()


