# Erdős #396 — binomial divisibility witnesses

For which `k` does there exist `n` such that

\[
n(n-1)\cdots(n-k)\mid {2n\choose n}?
\]

This repository gives exact finite witnesses and a Kummer-theoretic search for the problem.

## Least witnesses found below 60,000

| `k` | least `n` | witnesses below 60,000 |
|---:|---:|---:|
| 1 | 2 | 701 |
| 2 | 2480 | 72 |
| 3 | 8178 | 8 |
| 4 | 45153 | 1 |

In particular,

\[
8178\cdot8177\cdot8176\cdot8175\mid {16356\choose8178},
\]

and

\[
45153\cdot45152\cdot45151\cdot45150\cdot45149\mid {90306\choose45153}.
\]

All factors in these two consecutive blocks are composite.

## Method

Kummer's theorem identifies

\[
v_p\!\left({2n\choose n}\right)
\]

with the number of carries in the base-`p` addition `n+n`. The verifier factors the consecutive block and checks the required `p`-adic inequalities prime by prime.

The computation also exposes a failed historical obstruction: a prime in the much wider interval `(2n/3,n]` need not contribute the required negative valuation. The elementary obstruction works only when the relevant prime actually occurs in the final `k+1` factors.

## Files

- [`ERDOS-396-WITNESS.md`](ERDOS-396-WITNESS.md) — mathematical write-up.
- [`erdos396_witness.py`](erdos396_witness.py) — exact Kummer-based search and verifier.
- [`PROVENANCE.md`](PROVENANCE.md) — source history.

## Reproduce

```bash
python erdos396_witness.py
```

The script uses `sympy` for exact factorization and primality testing. The table is a finite result; no classification for all `k` is asserted.

Author: Jared Wilder.
