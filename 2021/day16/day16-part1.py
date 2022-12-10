import sys

class Packet:
    def __init__(self,id = None):
        self.id = id
        self.version = None
        self.op = None
        self.subPackets = []

    def eval(self):
        if self.id == 4:
            return self.version

        sum = self.version
        for p in self.subPackets:
            sum += p.eval()
        return sum

    def parse(self, bits, spot = 0):
        version = ''
        start = spot

        if spot > len(bits) - 3:
            return len(bits)

        while spot < start + 3:
            version += bits[spot]
            spot += 1
        self.version = binStringToDec(version)

        packetID = ''
        while spot < start + 6:
            packetID += bits[spot]
            spot += 1
        self.id = binStringToDec(packetID)

        if self.id == 4:
            literal = ''

            while bits[spot] == '1':
                spot += 1
                numStart = spot
                while numStart < spot + 4:
                    literal += bits[numStart]
                    numStart += 1
                spot = numStart

            spot += 1
            numStart = spot
            while numStart < spot + 4:
                literal += bits[numStart]
                numStart += 1
            spot = numStart
            self.op = binStringToDec(literal)
        else:
            self.op = binStringToDec(packetID)
            lengthID = bits[spot]
            spot += 1
            if lengthID == '0':
                packetLength = bits[spot:spot+15]
                spot+=15

                packetLength = binStringToDec(packetLength)
                nb = 0
                while nb < packetLength:
                    p = Packet()
                    before = spot
                    spot = p.parse(bits, spot)
                    nb += (spot-before)
                    if p.version != None:
                        self.subPackets.append(p)
            else:
                packetLength = expandBits[spot:spot+11]
                spot += 11
                packetLength = binStringToDec(packetLength)
                for i in range(packetLength):
                    p = Packet()
                    spot = p.parse(bits,spot)
                    if p.version != None:
                        self.subPackets.append(p)
        return spot

    def __str__(self):
        rtn = '--- START ---\n'
        rtn += 'Version: ' + str(self.version) + '\n'
        rtn += 'ID: ' + str(self.id) + '\n'
        if self.id == 4:
            rtn += 'Literal: ' + str(self.op) + '\n'
        else:
            rtn += 'Operator:' + str(self.op) + '\n'
            rtn += '----- SUB of '+str(self.version)+ ' ------\n'
            for p in self.subPackets:
                rtn += str(p)
        rtn += '--- END ---\n'
        
        return rtn


def binStringToDec(s):
    rtn = 0

    power = len(s) - 1
    spot = 0
    while spot < len(s):
        if s[spot] == '1':
            rtn += pow(2, power)
        spot += 1
        power -= 1
    return rtn

convert = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'
}

with open('input','r') as f:
    line = f.readline().strip()

    expandBits = ''
    for letter in line:
        expandBits += convert[letter]

    start = 0
    packet = Packet()
    start = packet.parse(expandBits, start)
    sum = packet.eval()
    print(sum)
