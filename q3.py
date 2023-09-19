class Powerset:
    def __init__(self):
        self.s = []

    def g(self, n):
        self.s = []
        self._g(n, [], 0)
        return self.s

    def _g(self, n, c, i):
        if i == len(n):
            self.s.append(c[:])
            return

        c.append(n[i])
        self._g(n, c, i + 1)

        c.pop()
        self._g(n, c, i + 1)

def u():
    i = input("Enter a set seperated by spaces:")
    e = i.split()
    s = set(e)
    return s

if __name__ == "__main__":
    us = u()
    p = Powerset()
    r = p.g(list(us))
    print("The powerset is: ", r)
