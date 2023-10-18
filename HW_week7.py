capacity = 100
array = [None] * capacity
size = 0


def isEmpty():
    if size == 0:
        return True
    else:
        return False


def isFull():
    return size == capacity


def insert(pos, e):
    global size
    if not isFull() and 0 <= pos <= size:
        for i in range(size, pos, -1):
            list[i] = list[i - 1]
        list[pos] = e
        size += 1
    else:
        print("list overflow or invalid pos for insert")


def isFull():
    return size == capacity


capacity = 10  # list 용량
list = [None] * capacity  # 크기가 10인 list 생성
size = 0  # 현재 엘리먼트 개수 및 상단 인덱스


def append(e):
    global size
    list[size] = e
    size += 1


def removeItem(e):
    global size
    for i in range(size - 1):
        list[i] = list[i - 1]
        size -= 1


capacity = 10  # list 용량
list = [None] * capacity  # 크기가 10인 list 생성
size = 0  # 현재 엘리먼트 개수 및 상단 인덱스
append(5)
append(10)
print(list[:size])
insert(0, 35)
insert(0, 40)
insert(1, 15)
print(list[:size])
removeItem(5)


def removeIndex(pos):
    global size
    if not isEmpty() and 0 <= pos < size:
        e = list[pos]
        for i in range(pos, size - 1):
            list[i] = list[i + 1]
        size -= 1
    else:
        print("리스트 underflow 또는 유효하지 않은 삽입 삭제")
        exit()


def getItem(pos):
    e = list[pos]
    return (e)


def find(e):
    for i in range(size - 1):
        if list[i] == e:
            return i
        else:
            return -1


def delete(pos):
    global size
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size - 1):
            array[i] = array[i + 1]
        size = -1
        return e
    else:
        print("리스트 underflow 또는 유효하지 않은 삽입 삭제")
        exit()


