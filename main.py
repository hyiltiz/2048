   
import random

class array(object):
    def __init__(self, length):
        """
        Constructor methods for creating a new array.
        """
        self.lst = [0]*length
        self.score = 0
        for it in random.sample(range(length),2):
            self.lst[it] = 2
            
    def __repr__(self):
        return ' '.join(map(str, self.lst)) + '   |   score = ' + str(self.score)
    
    def move(self, d = 'left'):
        if d == 'left':
            elems = filter(lambda x:x != 0, self.lst)
            self.lst[:len(elems)] = elems
            self.lst = [self.lst[i] if i < len(elems) else 0 for i in range(len(self.lst))]
        else:
            elems = filter(lambda x:x != 0, self.lst)
            self.lst[-len(elems):] = elems
            self.lst = [self.lst[i] if i > len(self.lst) - len(elems) - 1 else 0 for i in range(len(self.lst))]            
            
    def merge(self, d = 'left'):
        if d == 'left':
            for i in xrange(len(self.lst)-1):
                if self.lst[i] == 0:
                    break
                if self.lst[i] == self.lst[i+1]:
                    self.lst[i] = self.lst[i] + self.lst[i+1]
                    self.score += self.lst[i]
                    self.lst.pop(i+1)
                    self.lst.extend([0])
        else:
            for i in xrange(len(self.lst)-1, 0, -1):
                if self.lst[i] == 0:
                    break
                if self.lst[i] == self.lst[i-1]:
                    self.lst[i] = self.lst[i] + self.lst[i-1]
                    self.score += self.lst[i]
                    self.lst.pop(i-1)
                    self.lst.insert(0, 0)
                    
    def add(self, d = 'left'):
        if d == 'left':
            self.lst[-1] = 2
        else:
            self.lst[0] = 2

def main():
    a = array(21)
    while True:
        d = raw_input("The direction")
        a.move(d)
        a.merge(d)
        a.add(d)
        print a
    
    
if __name__ == '__main__':
    main()