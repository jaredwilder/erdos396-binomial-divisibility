"""Erdos 396: n(n-1)...(n-k) | C(2n,n). Kummer-based search and verification.
Also evaluates the erdos82 'triCase' receipt. Exits 0 or raises."""
from itertools import combinations
from sympy import factorint, isprime


def v_binom(n, p):
    """Kummer: v_p(C(2n,n)) = number of carries adding n+n in base p."""
    carries = carry = 0
    m = n
    digits = []
    while m:
        digits.append(m % p)
        m //= p
    for d in digits:
        if 2 * d + carry >= p:
            carry = 1
            carries += 1
        else:
            carry = 0
    if carry:
        carries += 1
    return carries


def product_primes(n, k):
    prod = {}
    for i in range(k + 1):
        for p, e in factorint(n - i).items():
            prod[p] = prod.get(p, 0) + e
    return prod


def divides(n, k):
    prod = product_primes(n, k)
    return all(v_binom(n, p) >= e for p, e in prod.items()), prod


print("Erdos 396: n(n-1)...(n-k) | C(2n,n)")

w2 = [n for n in range(3, 4000) if divides(n, 2)[0]]
print("  k=2, n < 4000 witnesses:", w2)
assert w2 == [2480, 3478]
for n in w2:
    ok, prod = divides(n, 2)
    assert ok
    assert n * (n - 1) * (n - 2) == {2480: 15234545760, 3478: 42035288856}[n]

w3 = [n for n in range(4, 30000) if divides(n, 3)[0]]
print("  k=3, n < 30000 witnesses:", w3)
assert w3 == [8178]

n = 8178
ok, prod = divides(n, 3)
assert ok
assert factorint(8178) == {2: 1, 3: 1, 29: 1, 47: 1}
assert factorint(8177) == {13: 1, 17: 1, 37: 1}
assert factorint(8176) == {2: 4, 7: 1, 73: 1}
assert factorint(8175) == {3: 1, 5: 2, 109: 1}
assert not any(isprime(n - i) for i in range(4))
print("  n=8178: none of 8178, 8177, 8176, 8175 is prime")
print("    prime    needed  supplied")
for p in sorted(prod):
    print("    %-6d   %-6d  %d" % (p, prod[p], v_binom(n, p)))
    assert v_binom(n, p) >= prod[p]

w4 = [n for n in range(5, 60000) if divides(n, 4)[0]]
print("  k=4, n < 60000 witnesses:", w4)
assert w4 == [45153]
n = 45153
ok, prod = divides(n, 4)
assert ok
assert factorint(45153) == {3: 2, 29: 1, 173: 1}
assert factorint(45152) == {2: 5, 17: 1, 83: 1}
assert factorint(45151) == {163: 1, 277: 1}
assert factorint(45150) == {2: 1, 3: 1, 5: 2, 7: 1, 43: 1}
assert factorint(45149) == {13: 1, 23: 1, 151: 1}
assert not any(isprime(n - i) for i in range(5))
for p_ in sorted(prod):
    assert v_binom(n, p_) >= prod[p_]
print("  n=45153: all five factors composite, every exponent clears")

counts = {}
for k in range(1, 5):
    w = [n for n in range(k + 1, 60000) if divides(n, k)[0]]
    counts[k] = (w[0], len(w))
    print("    k=%d  least %-6d  count below 60000: %d" % (k, w[0], len(w)))
assert counts[1][0] == 2 and counts[2][0] == 2480
assert counts[3][0] == 8178 and counts[4][0] == 45153
assert counts[2][1] > counts[3][1] > counts[4][1]

n = 2480
ps = [p for p in range(2 * n // 3 + 1, n + 1) if isprime(p)]
vals = set(v_binom(n, p) for p in ps)
print("  at n=2480: %d primes in (2n/3, n], valuations %s" % (len(ps), sorted(vals)))
assert vals == {0}
assert not any(isprime(n - i) for i in range(3))
print("    the -1 valuation needs p in (n-3, n]; the argument assumes one of")
print("    n, n-1, n-2 is prime, and at 2480 none is")

print()
print("erdos82 receipt: triCase x y z := x || y || z || (!x && !y && !z)")
table = [bool(x or y or z or (not x and not y and not z))
         for x in (0, 1) for y in (0, 1) for z in (0, 1)]
print("  truth table:", table)
assert all(table), "triCase should be identically true"
print("  -> identically True; it is (P or not P)")

C5 = {0: {1, 4}, 1: {0, 2}, 2: {1, 3}, 3: {2, 4}, 4: {3, 0}}
tri = [t for t in combinations(range(5), 3)
       if all(b in C5[a] for a, b in combinations(t, 2))]
ind = [t for t in combinations(range(5), 3)
       if all(b not in C5[a] for a, b in combinations(t, 2))]
print("  C5 triangles:", tri, " independent triples:", ind)
assert tri == [] and ind == []
print("  -> a 5-vertex argument cannot establish R(3,3) <= 6")

print()
print("all checks passed")
