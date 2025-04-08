def prodmat(A, B): # produit matriciel
    n, p = len(A), len(B[0])
    m = len(B)
    result = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += A[i][k] * B[k][j]
    return result

def det(A): # déterminant
    if len(A) == 1:
        return A[0][0]
    elif len(A) == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    else:
        d = 0
        for j in range(len(A)):
            minor = [row[:j] + row[j+1:] for row in A[1:]]
            d += ((-1)**j) * A[0][j] * det(minor)
        return d

def com(A): # comatrice
    n = len(A)
    cof = [] # cofacteur
    for i in range(n):
        row = []
        for j in range(n):
            minor = [A[x][:j] + A[x][j+1:] for x in range(n) if x != i]
            row.append(((-1)**(i+j)) * det(minor))
        cof.append(row)
    return cof

def transpose(M):
    return [list(row) for row in zip(*M)]

def inverse(A):
    d = det(A)
    if d == 0:
        print("Matrice non inversible")
    comat = com(A)
    adj = transpose(comat)
    return [[adj[i][j]/d for j in range(len(A))] for i in range(len(A))]

def main():
    A = [
        [1, 0, -2],
        [2, 1, 1],
        [-1, 0, 1]
    ]
    B = [
        [-1, 0, 1],
        [2, 1, -1],
        [0, 3, 1]
    ]

    print("\n" + "Produit matriciel :" + "\n")
    for i in range(3):
        print(prodmat(A, B)[i])

    print("\n" + "Déterminant :" + "\n")
    print(det(A))
    
    print("\n" + "Comatrice :" + "\n")
    for i in range(3):
        print(com(A)[i])

    print("\n" + "Inverse :" + "\n")
    for i in range(3):
        print(inverse(A)[i])

main()