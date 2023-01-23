import time
seq = [0,1]
globalNumber = 0
def fibonacci_sequence(number, inital):
    global x 
    if inital == True: x = number
    if number < len(seq): return seq[number]
    else:
        seq.append(fibonacci_sequence(number -1, False) + fibonacci_sequence(number - 2, False))
        return seq[number]
    x = number
start = time.time()
final = fibonacci_sequence(34, True)
print("fib(" + str(x) + ") = " + str(final))
end = time.time()
print("fib(" + str(x) + ") took " +  str(start-end)  + " seconds")