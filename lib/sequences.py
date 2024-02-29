#!/usr/bin/env python3

def print_fibonacci(length):
    fibionacci_sequence = [0,1]
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    else:
        for i in range(2,length):
                next_number = fibionacci_sequence[-1] + fibionacci_sequence[-2]
                fibionacci_sequence.append(next_number)
        print(fibionacci_sequence )

    