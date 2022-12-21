import math

class LList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add(self, val):
        n = LList.Node(val)
        if self.head == None:
            self.head = self.tail = n
            n.next = n.prev = n
        else:
            n.next = self.tail.next
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
            self.head.prev = self.tail
        self.len += 1
        return n

    def __len__(self):
        return self.len

    def __str__(self):
        s = '['
        i = self.head
        spot = 0
        while spot < len(self):
            s += str(i.val)+", "
            i = i.next
            spot += 1
        s += ']'
        return s

zeroNode = None
mixer = []
lst = LList()
f = open('inputfinal')
for line in f:
    num = int(line)
    mixer.append(lst.add(num))
    if num == 0:
        zeroNode = mixer[-1]


for e in mixer:
    v = e.val    

    if v == 0:
        continue

    moveTo = e.prev

    if e == lst.head:
        lst.head = e.next
    if e == lst.tail:
        lst.tail = e.prev

    e.prev.next = e.next
    e.next.prev = e.prev    

    while v < 0:
        moveTo = moveTo.prev
        v += 1
    while v > 0:
        moveTo = moveTo.next
        v -= 1

    e.next = moveTo.next
    e.prev = moveTo
    e.next.prev = e.prev.next = e

n = zeroNode
scorePlaces = [1000,2000,3000]
score = 0
count = 0
for i in scorePlaces:
    while count < i:
        n = n.next
        count += 1
    score += n.val
print(score)

# Guess: -3329
# Guess: 25966
# Guess: -1335