import matplotlib.pyplot as plt

pi = 3.141592653589793

def transpose(M):
    return [list(row) for row in zip(*M)]

def ligne(n, xmin, xmax):
    W = []
    dx = (xmax - xmin) / (n - 1)
    for x in range(n):
        W.append([xmin + x * dx, 0, 0])
    return transpose(W)

def carre_vide(n, a):
    W = []
    for i in range(n):
        t = i / (n - 1)
        W.append([a * t, 0, 0])
        W.append([a, a * t, 0])
        W.append([a * (1 - t), a, 0])
        W.append([0, a * (1 - t), 0])
    return transpose(W)

def carre_plein(n, a):
    W = []
    c = sqrt(n)
    for i in range(int(c)):
        for j in range(int(c)):
            W.append([a * i / (c - 1), a * j / (c - 1), 0])
    return transpose(W)

def pave_plein(n, a, b, c):
    W = []
    root = int(round(n ** (1/3)))
    for i in range(root):
        for j in range(root):
            for k in range(root):
                W.append([
                    a * i / (root - 1),
                    b * j / (root - 1),
                    c * k / (root - 1)
                ])
    return transpose(W)

def sqrt(x, epsilon=1e-10):
    if x < 0:
       print("e")
    r = x
    while abs(r * r - x) > epsilon:
        r = (r + x / r) / 2
    return r


def factoriel(n):
    if n == 0 or n == 1:
        return 1
    return n * factoriel(n - 1)

def cosinus(x):
    cosx = 0
    for k in range(10):
        cosx += ((-1)**k * x**(2*k)) / factoriel(2*k)
    return cosx

def sinus(x):
    sinx = 0
    for k in range(10):
        sinx += ((-1)**k * x**(2*k + 1)) / factoriel(2*k + 1)
    return sinx

def cercle_plein(n, R):
    W = []
    for i in range(n):
        for j in range(n):  
            r = R * i / (n - 1)
            theta = 2 * pi * j / (n - 1)
            x = r * cosinus(theta)
            y = r * sinus(theta)
            z = 0
            W.append([x, y, z])
    return transpose(W)

def cylindre_plein(n, R, h):
    W = []
    for i in range(n):
        z = h * i / (n - 1)
        for r_ratio in range(n):
            r = R * r_ratio / (n - 1)
            for j in range(n):
                theta = 2 * pi * j / (n - 1)
                x = r * cosinus(theta)
                y = r * sinus(theta)
                W.append([x, y, z])
    return transpose(W)


def afficher_3D(W, titre=''):
    x, y, z = W
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z, c=z, cmap='plasma')
    ax.set_title(titre)
    plt.show()

# W = ligne(20, -5, 5)
# W = carre_vide(20, 2)
# W = carre_plein(100, 2)
# W = pave_plein(1000, 2, 2, 2)
# W = cercle_plein(50, 2)
W = cylindre_plein(16, 2, 3)

afficher_3D(W, titre='Cylindre')
