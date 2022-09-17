import time

def fibo_gen(limit: int):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            if n1 >= limit: break
            yield n1
        elif counter == 1:
            counter += 1
            if n2 >= limit: break
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux   
            counter += 1
            if aux >= limit: break
            yield aux

if __name__ == "__main__":
    fibonacci = fibo_gen(8)

    for element in fibonacci:
        print(element)
        time.sleep(1)