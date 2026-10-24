def find_largest(numbers): 
    maxlen = 0
    for str in test_strings: 
        if len(str) > maxlen:
            maxlen = len(str)
    return maxlen

test_strings = [
"Hello world!", 
"How are you doing", 
"four score and seven years ago",
 "life moves pretty fast. if you dont stop and look around every once in a whiledasdasdasfsdfadsfasdf"
]


print(find_largest(test_strings))