class Compare:
    def check(self, a, b, c):
        if a.isalpha() or b.isalpha() or c.isalpha():
            return self.check(input("??1"), input("??2"), input("??3"))
        else:
            a = int(a)
            b = int(b)
            c = int(c) 
            MAX = 0
            ME = 0
            MIN = 0
            if a > b:  
                if b > c:
                    MAX = a
                    ME = b
                    MIN = c     
                elif c > a:
                    MAX = c
                    ME = a
                    MIN = b
                else:
                    MAX = a
                    ME = c
                    MIN = b   
            elif b > a:
                if a > c:
                    MAX = b
                    ME = a
                    MIN = c
                elif c > b:
                    MAX = c
                    ME = b
                    MIN = a
                else:
                    MAX = b
                    ME = c
                    MIN = a
        print(MAX, ME, MIN)