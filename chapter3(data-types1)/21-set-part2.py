# ----------1-------------
P = {3, 9, 15, 12, 6, 18}
Q = {12, 6, 18, 10, 4, 16, 2, 8, 14}
print(P - Q)
print(P.difference(Q))
print(P | Q)
print(P.union(Q))
print(P & Q)
print(P.intersection(Q))
print(P ^ Q)
print((P | Q) - (P & Q))
print((P - Q) | (Q - P))
print(P.symmetric_difference(Q))
# ------------2----------------
A = {40, 50, 20, 10, 30, 60}
B = {10, 30, 60}
print(A < B)
print(A > B)
print(A.issubset(B))
print(A.issuperset(B))