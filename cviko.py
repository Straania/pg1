
def my_range(start, stop, step=1):
    result = []
    value = start
    while value < stop:
        result.append(value)
        value += step
    return result


def my_enumerate(iterable):
    result = []
    index = 0
    for value in iterable:
        result.append((index, value))
        index += 1
    return result

def my_zip(*iterables):
    results = []
    lenght = len(iterables[0])
    for i in range(0, lenght):
        subresult = []
        for iterable in iterables:
            subresult.append(iterable[i])
        results.append(tuple(subresult))
    return results             

if __name__ == "__main__":
    print(my_enumerate("ahoj"))
    print (my_range(1,10,2))