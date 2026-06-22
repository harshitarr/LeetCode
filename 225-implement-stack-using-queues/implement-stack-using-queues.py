class MyStack(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []
        

    def push(self, x):
        self.q1.append(x)
        
    def pop(self):

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        ans = self.q1.pop(0)

        self.q1, self.q2 = self.q2, self.q1

        return ans
        

    def top(self):

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        ans = self.q1[0]

        self.q2.append(self.q1.pop(0))

        self.q1, self.q2 = self.q2, self.q1

        return ans
        

    def empty(self):
        return len(self.q1) == 0
    