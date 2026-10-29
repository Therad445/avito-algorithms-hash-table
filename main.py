import sys


def hash_str(s):
    h = 0
    for c in s:
        h = (h * 131 + c) % 1000000007
    return h


class Table:
    def __init__(self):
        self.a = [None] * 8
        self.n = 0

    def grow(self):
        old = self.a
        self.a = [None] * (len(old) * 2)
        for b in old:
            if b is not None:
                for p in b:
                    i = p[2] % len(self.a)
                    if self.a[i] is None:
                        self.a[i] = []
                    self.a[i].append(p)

    def put(self, s, x):
        h = hash_str(s)
        i = h % len(self.a)
        b = self.a[i]
        if b is None:
            b = []
            self.a[i] = b
        for p in b:
            if p[0] == s:
                p[1] = x
                return

        b.append([s, x, h])
        self.n += 1
        if self.n * 4 > len(self.a) * 3:
            self.grow()

    def get(self, s):
        i = hash_str(s) % len(self.a)
        b = self.a[i]
        if b is not None:
            for p in b:
                if p[0] == s:
                    return p[1]
        return None

    def delete(self, s):
        i = hash_str(s) % len(self.a)
        b = self.a[i]
        if b is None:
            return None
        for j in range(len(b)):
            if b[j][0] == s:
                x = b[j][1]
                b.pop(j)
                self.n -= 1
                return x
        return None


input = sys.stdin.buffer.readline
q = int(input())
t = Table()
ans = []

for _ in range(q):
    a = input().split()
    if a[0] == b'put':
        t.put(a[1], int(a[2]))
    elif a[0] == b'get':
        x = t.get(a[1])
        ans.append(str(x) if x is not None else 'Error')
    elif a[0] == b'del':
        x = t.delete(a[1])
        ans.append(str(x) if x is not None else 'Error')
    else:
        ans.append(str(t.n))

sys.stdout.write('\n'.join(ans))
