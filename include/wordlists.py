from itertools import product

class Wordlist:
    def __init__(self,filename,length=3,cb=None):
        self.filename = filename
        self.length = length
        self.file = open(filename,'w')
        self.x = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1','2','3','4','5','6','7','8','9']
        self.cb = cb
        self.base = ['a' for i in range(length)]

    def generate(self):
        for i in range(1,self.length + 1):
            for t in product(self.x,repeat=i):
                new = "".join(t)
                new += "\n"
                self.file.write(new)
            if self.cb: self.cb()