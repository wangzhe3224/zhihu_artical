import hashlib

def hash(s):
    m = hashlib.sha256()
    m.update(s)
    res = m.hexdigest()
    return res

print(hash(b"11111"))
print(hash(b"11112"))

def pow(s: str, difficulty: int=2) -> int:
    p = 0
    while True:
        m = hashlib.sha256()
        m.update((s + str(p)).encode())
        h = m.hexdigest()

        if h[:difficulty] == "0" * difficulty:
            return p 
        else:
            p += 1

            
s = "This is a message!"
diff = 4
p = pow(s, diff)
print(p)

m = hashlib.sha256()
s = "This is a message!"
# p = 667
m.update((s + str(p)).encode())
h = m.hexdigest()
print(h)


import time
import matplotlib.pyplot as plt

message = "This is a message!"
x = []
y = []
ps = []
for diff in range(1, 7):
    _s = time.time()   
    p = pow(message, diff)
    ps.append(p)
    _e = time.time()
    dur = _e - _s
    print(f"难度：{diff} - {dur}:.6f")
    x.append(diff)
    y.append(dur)

plt.plot(x, y)