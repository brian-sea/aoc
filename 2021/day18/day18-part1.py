import sys
import math

class SnailNumber:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.parent = None

    def parse(self, s, spot = 0):
        
        if s[spot].isdigit():
            self.value = int(s[spot])
            return spot + 1
        else:
            self.left = SnailNumber()
            self.left.parent = self
            spot = self.left.parse(s, spot+1)

            self.right = SnailNumber()
            self.right.parent = self
            spot = self.right.parse(s, spot+1)

            return spot + 1

    def add(self, left):
        if left == None:
            return self
        
        newNum = SnailNumber()
        newNum.parent = self.parent 
        left.parent = self.parent = newNum

        newNum.left = left
        newNum.right = self

        return newNum

    def magnitude(self):
        if self.value != None:
            return self.value
        
        return 3*self.left.magnitude() + 2*self.right.magnitude()

    def __str__(self):
        if self.value != None:
            return str(self.value)
        
        rtn = '['
        rtn += str(self.left) + ','
        rtn += str(self.right) + ']'

        return rtn
        
def explode(num, depth = 0):
    if( num == None ):
        return False

    if depth == 4 and num.value == None:
        curr = num.parent
        if num == curr.left:

            v = curr.right
            while v.left != None:
                v = v.left
            v.value += num.right.value
            
            p = curr.parent
            while p != None and p.left == curr:
                curr = p
                p = p.parent

            if p != None:            
                curr = p.left
                while curr.right != None:
                    curr = curr.right
                
                curr.value += num.left.value
        else:
            if curr.left != None:
                curr.left.value += num.left.value
            
            p = curr.parent
            while p != None and p.right == curr:
                curr = p
                p = p.parent
            
            if p != None:
                curr = p.right
                while curr.left != None:
                    curr = curr.left
                curr.value += num.right.value
        num.value = 0
        num.left = num.right = None
        return True
    
    didExplode = explode(num.left, depth+1)
    if not didExplode:
        didExplode = explode(num.right, depth+1)
    return didExplode

def split(num):
    if num == None:
        return False

    if num.value != None:
        if num.value >= 10:
            num.left = SnailNumber()
            num.right = SnailNumber()


            num.left.parent = num.right.parent = num

            num.left.value = math.floor(num.value/2)
            num.right.value = math.ceil(num.value/2)
            num.value = None
            return True
    else:    
        didSplit = split(num.left)
        if not didSplit:
            didSplit = split(num.right)
        return didSplit



number = None
with open('input', 'r') as f:
    for line in f:
        line = line.strip()

        num = SnailNumber()
        num.parse(line)

        number = num.add(number)

        didSplit = True
        while didSplit:
            while(explode(number)):
                pass
            didSplit = split(number)
    print(number.magnitude())       

