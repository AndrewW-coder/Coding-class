class reverse(object):
    def __init__(self, s):
        self.s = s
    def talk(self):
        # l = self.s.split()
        # for i in range(0, len(l)):
        #     m = len(l[i])
        #     for m in range(m, -1):
        #         l.append(l[i][m])
        l = []
        for i in range(0, len(self.s)):
            l.append(self.s[i])
        l = l.reverse()
        
        print(l)

        
test = reverse('Hi i like pie')
test.talk()



