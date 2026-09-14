# Erdős 396 — binomial divisibility witnesses

This repository is the focused home for a computational/structural program around Erdős problem 396:

> for which `k` does there exist `n` such that
> `n(n-1)...(n-k)` divides `C(2n,n)`?

The core tool is Kummer's theorem: `v_p(C(2n,n))` equals the number of carries when adding `n+n` in base `p`. That turns the divisibility test into an exact prime-by-prime calculation.

## Verified finite frontier

The recovered search establishes the following least witnesses:

| k | least n | witnesses below 60,000 |
|---:|---:|---:|
| 1 | 2 | 701 |
| 2 | 2480 | 72 |
| 3 | 8178 | 8 |
| 4 | 45153 | 1 |

In particular,

- `8178*8177*8176*8175 | C(16356,8178)`;
- `45153*45152*45151*45150*45149 | C(90306,45153)`.

All factors in those two consecutive blocks are composite. This matters because a historical nonexistence argument silently needed a prime in the short window `(n-k,n]`; its much larger stated prime interval does not supply the claimed negative valuation.

## Correction carried with the result

The source archive contained a `PROVED` row asserting a prime in `(2n/3,n]` forces the relevant valuation obstruction. The exact Kummer computation shows those primes can all have valuation zero. The obstruction only works when a prime occurs in the final `k+1` integers themselves.

The repository therefore preserves both the positive witnesses and the failed proof mechanism.

## Files

- [`ERDOS-396-WITNESS.md`](ERDOS-396-WITNESS.md) — full mathematical write-up recovered from the ore review.
- [`erdos396_witness.py`](erdos396_witness.py) — exact Kummer-based search and verification program.
- [`PROVENANCE.md`](PROVENANCE.md) — source locations and authority boundary.

## Reproduce

```bash
python erdos396_witness.py
```

The script uses `sympy` for exact factorization/primality. Finite search results are finite statements; this repository does not claim a general classification of all `k`.

## Author

Jared Wilder
