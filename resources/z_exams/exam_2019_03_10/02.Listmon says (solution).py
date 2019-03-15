from functools import  reduce

listmon_data = list(map(int, input().split()))
data = input()
count_rounds = 0

while not data == 'exhausted':
    count_rounds += 1

    command = data.split()[0]
    my_playground_list = []

    if command == 'set':
        if len(listmon_data) == len(set(listmon_data)):
            print("It is a set")
        else:
            my_playground_list = sorted(set(listmon_data), key=listmon_data.index)
    elif command == 'filter':
        number = 0
        if data.split()[1] == 'odd':
            number = 1
        my_playground_list = list(filter(lambda x: x%2 == number, listmon_data))
    elif command == 'multiply':
        number = int(data.split()[1])
        my_playground_list = list(map(lambda x: x * number, listmon_data))
    elif command == 'reduce':
        my_playground_list = reduce(lambda a,b: a+b, listmon_data)
        print(f'Reduced - {my_playground_list}')
    elif command == 'divide':
        number = int(data.split()[1])
        if number == 0:
            print('ZeroDivisionError caught')
        else:
            my_playground_list = list(map(lambda x: x/number, listmon_data))
    elif command == 'slice':
        index_1 = int(data.split()[1])
        index_2 = int(data.split()[2])
        if (index_1 > len(listmon_data)-1 or index_1 < 0) or ((index_2 > len(listmon_data)-1 or index_2 < 0)):
            print('IndexError caught')
        else:
            print(listmon_data[index_1:index_2+1])
    elif command == 'sort':
        my_playground_list = sorted(listmon_data)
    elif command == 'reverse':
        my_playground_list = list(reversed(listmon_data))

    if my_playground_list:
        print(my_playground_list)
    data = input()

print(f'I beat It for {count_rounds} rounds!')