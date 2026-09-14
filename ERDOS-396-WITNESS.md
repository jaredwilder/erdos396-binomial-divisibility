# Erdős 396: a four-factor witness at n = 8178, and the proof that said it couldn't exist

The question: for which `k` does `n(n−1)⋯(n−k)` divide `C(2n,n)` for some `n`?

---

## The tool

By **Kummer's theorem**, `v_p(C(2n,n))` is the number of carries when adding `n + n` in base `p`.
So the divisibility is decidable prime-by-prime with no big-integer arithmetic at all: compute the
factorization of the product and compare each exponent against a carry count.

## k = 2 — exactly two witnesses below 4000

```
n = 2480 :  2480·2479·2478 = 15,234,545,760  |  C(4960,2480)
n = 3478 :  3478·3477·3476 = 42,035,288,856  |  C(6956,3478)
```

Verified prime by prime. For n = 2480 the product needs `2⁵·3·5·7·31·37·59·67` and the binomial
supplies `2⁶·3⁴·5⁴·7·31·37·59²·67²` — every exponent clears.

## k = 3 — a witness the corpus's own search could not reach

```
n = 8178 :  8178·8177·8176·8175  |  C(16356,8178)
```

**The only one below 30,000.** The corpus searched `n < 6000` and reported none.

| factor | factorization | prime? |
|---|---|---|
| 8178 | 2 · 3 · 29 · 47 | no |
| 8177 | 13 · 17 · 37 | no |
| 8176 | 2⁴ · 7 · 73 | no |
| 8175 | 3 · 5² · 109 | no |

Required exponents against what the binomial supplies:

```
prime     2   3   5  7  13 17 29 37 47 73 109
needed    5   2   2  1   1  1  1  1  1  1   1
supplied 11   5   4  2   1  1  1  1  1  1   2
```

Every one clears, several with room to spare.

## k = 4 — and one more level down

```
n = 45153 :  45153·45152·45151·45150·45149  |  C(90306,45153)
```

The only witness below 60,000, and again every factor is composite:

| factor | factorization |
|---|---|
| 45153 | 3² · 29 · 173 |
| 45152 | 2⁵ · 17 · 83 |
| 45151 | 163 · 277 |
| 45150 | 2 · 3 · 5² · 7 · 43 |
| 45149 | 13 · 23 · 151 |

The exponent comparison clears at every prime — `2` needs 6 and gets 7, `3` needs 3 and gets 6,
and the eleven large primes each need 1.

### The least witness per level

| k | least n | count below 60,000 |
|---|---:|---:|
| 1 | 2 | 701 |
| 2 | **2480** | 72 |
| 3 | **8178** | 8 |
| 4 | **45153** | 1 |

Witness density drops by roughly an order of magnitude per level — which is what the
all-factors-composite requirement predicts, and why each level needed a search an order of
magnitude longer than the last.

*(A mining pass reports the k = 5 least witness as n = 3,648,841. Not independently recomputed
here — treat as a lead.)*

---

## The row that says this is impossible

The corpus files, as **PROVED**:

> for n ≥ 9 a prime `p ∈ (2n/3, n]` gives `v_p((2n)!(n−3)!/n!³) = −1`, so `n(n−1)(n−2)` never
> divides `C(2n,n)`

**The gap is exactly locatable.** The valuation is `−1` only for `p ∈ (n−3, n]` — a window of
three integers, not the interval `(2n/3, n]`. So the argument tacitly requires **one of n, n−1,
n−2 to be prime**.

At n = 2480 none of 2480, 2479, 2478 is prime. And all **108** primes in `(2n/3, n]` give
valuation **0**, not −1. The mechanism is silent exactly where the witnesses live — which is why
the witnesses are large and composite in all their top factors.

That also explains the shape of the answer: a witness must have `n, n−1, …, n−k` *all* composite,
which is why the smallest k=3 example sits above 8000.

---

## A second finding from the same batch: a kernel receipt that certifies `True`

A Lean file in the `KERNEL_CHECKED` set carries the docstring

> *"This certifies: every graph on 6 vertices has a triangle or an independent triple, i.e.
> R(3,3) ≤ 6."*

Its core definition is

```lean
triCase x y z := x || y || z || (!x && !y && !z)
```

That is `P ∨ ¬P`. Its truth table is `True` in all eight rows — the proposition is a tautology and
the receipt establishes nothing about graphs.

Worse, the argument the docstring describes uses **vertex 0 plus four others** — five vertices.
`C₅` has no triangle and no independent triple.

`R(3,3) ≤ 6` is of course true — this is about what the receipt proves, which is `True`.

---

## Reproduce

`erdos396_witness.py` runs the Kummer test, finds the witnesses, prints the exponent comparison
for n = 8178, checks that none of its four factors is prime, confirms the valuation-0 fact at
n = 2480, and evaluates the `triCase` truth table. Exits 0.
