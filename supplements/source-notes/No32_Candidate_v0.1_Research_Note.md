# No.32 candidate v0.1 — A Finite-Size Decoding Transition in Ternary Kuramoto Resets

**2026-10-22 | Ryutaro Yonezu / Yonezu Research Lab | RESEARCH CANDIDATE — HOLD**

**Status:** MODEL-RESTRICTED PROOF: internally checked; COMPUTATION: PASS; REFERENCES: PARTIAL; NOVELTY: INCONCLUSIVE; RELEASE: HOLD. This is not a certified new theorem, peer-reviewed research, or a claim of priority. A genuinely independent mathematical and prior-art audit is needed before a numbered paper is approved.

## Question

The published No.28 restricted hub-star Kuramoto record uses one reset with leaf phases `(pi, acos(-1/3), 0, ..., 0)` and reconstructs an unknown target leaf edge from the hub's exact second time derivative. Within this *same one-parameter family of three-level resets*, is the prescribed angle best if the observation is disturbed by an unknown bounded additive error? Does the answer depend on network size?

**The answer in this precisely stated model is yes, and the best angle changes at N=8.** This is a finite-jet separation result, not a claim about the optimality of noisy time-series sampling or unknown graph generalization.

## Restricted setup

There are `N=m+1` nodes: hub `0` and leaves `1,...,m`, with m>=3. Hub-to-leaf edges are present and all leaf-to-leaf edges are unknown undirected binary variables. The Kuramoto ODE is

`theta_i'(t) = k sum_j A_ij sin(theta_j(t)-theta_i(t))`, with `k=1/N`; frequencies are set to zero.

Set `theta_0(0)=0, theta_1(0)=pi, theta_2(0)=phi`, and `theta_j(0)=0` for j>=3. Choose phi in (0,pi) and put `c=cos(phi)`, `s=sin(phi)>0`. Write `a=A_12` (target edge) and `d=sum_{j=3}^m A_2j` (nuisance degree). The nuisance index takes **every** integer in `[0,D]` independently of a, where `D=m-2=N-3`.

**Direct vector-field calculation, not an interpolation assumption:**

`h''(0) = k^2 s [3-m-2c + (1+c)a + (1-c)d]`, where `h=theta_0`.

The unknown edges not incident to node 2 do not contribute to this second jet.

## Finite-class separation and exact optimum

Define the smallest possible difference between hub second-jet readings from graphs with `a=0` and graphs with `a=1`, over all nuisance graphs:

`Delta_N(c) = k^2 g_D(c)`,

`g_D(c) = sqrt(1-c^2) min_{j=0,...,D} |(1+c)-j(1-c)|`.

The signed nuisance difference may be negative, but because both coefficients are nonnegative on `[-1,1]`, the nearest candidate is at j>=0. A worst-case bounded additive second-jet error less than `Delta_N(c)/2` is guaranteed to preserve the target-edge label by nearest-class decoding; at error `Delta_N(c)/2`, opposite-class ambiguity can occur. This is a *geometric separation criterion for direct jets*, not a raw-phase sampling guarantee.

### Main candidate theorem

Let `b=4 sqrt(2)/9 ≈ 0.6285393611`. Define

`c_D = [(D-1) + sqrt((D-1)^2 + 8(D+1)^2)] / [4(D+1)]`,

`f_D = [(D+1)c_D-(D-1)] sqrt(1-c_D^2)`.

For m>=3 (D>=1), the **global maximizer of g_D over -1<=c<=1** is

- `c=c_D` when `1<=D<=4` (N=4,5,6,7), with margin `f_D`;
- `c=-1/3` when `D>=5` (N>=8), with margin `b`.

In particular, for N=4..7 the optimal label decoder distinguishes two disjoint intervals (threshold mechanism), whereas for N>=8 the optimal reset uses *interleaved classes* with a parity/lattice mechanism, reproducing the No.28 reset angle. Thus the observation design has a sharp finite-size switch in a restricted family.

### Proof outline (complete for this optimization statement, pending independent review)

1. Differentiate the hub equation: `h''=k sum_{j=1}^m cos(theta_j-theta_0)(theta_j'-theta_0')`. Insert reset angles and `theta'_i` to derive the displayed affine expression. The target a and nuisance degree d are independent binary edge selections, so all pairs in `{0,1} x {0,...,D}` are attained.
2. For `c<=0`, the minimum in `g_D` occurs at `j=0` or `j=1`, hence `g_D(c)=sqrt(1-c^2) min(1+c,-2c)`. Both pieces achieve their maximum at `c=-1/3`, attaining `b`.
3. For `0<=c<=(D-1)/(D+1)` (an empty interval except c=0 if D=1), put `r=(1+c)/(1-c)`. Then `1<=r<=D`. Some integer `j in {1,...,D}` is at most 1/2 away from r, giving `g_D(c) <= (1-c)s/2 <= 1/2 < b`.
4. For `(D-1)/(D+1) <= c<=1`, we have `r>=D`, so `g_D(c)=[(D+1)c-(D-1)]sqrt(1-c^2)`. Differentiate: its sole interior positive maximum has `2(D+1)c^2-(D-1)c-(D+1)=0`, giving c_D above.
5. Direct evaluation gives `f_1=1`, `f_2≈0.840154844`, `f_3≈0.738017460`, `f_4≈0.665738454`, all greater than b. For every D>=5, the positive branch is pointwise bounded above by the D=5 branch (for 0<=c<=1). Its maximum is `f_5≈0.611177383 < b`; an exact check uses `f_5^2=(169-38 sqrt(19))/9 < 32/81=b^2` (equivalent after rearrangement to `1489^2 < 342^2*19`). This proves the stated global switch.

There is no dependence on graph symmetry or typical/random graphs; this is a worst-case combinatorial margin over all binary nuisance edges. The optimization family and jet-level noise model are the key restrictions.

## Exact numbers

| N (all nodes) | D=N-3 | Optimal cos(phi) | Optimal phi (degrees) | Normalized gap g_D | Gain over No.28 |
|---:|---:|---:|---:|---:|---:|
| 4 | 1 | 0.7071067812 | 45.0000 | 1.0000000 | +59.10% |
| 5 | 2 | 0.7953336454 | 37.3132 | 0.8401548 | +33.67% |
| 6 | 3 | 0.8430703308 | 32.5342 | 0.7380175 | +17.42% |
| 7 | 4 | 0.8728416147 | 29.2094 | 0.6657385 | +5.92% |
| >=8 | >=5 | -1/3 | 109.4712 | 0.6285394 | 0.00% |

For the actual hub second derivative, multiply the tabulated normalized gap by `k^2=N^-2`.

## Computational audit

`no32_phase_gap_verifier.py` uses Python 3.12 *standard library only*. It computes the ODE vector field directly, differentiates the observable hub velocity by the chain rule, and compares with the reduced formula.

- All leaf graphs with m=3,4,5,6 were tested exhaustively: 8+64+1024+32768 = **33,864** graphs, at four reset angles per graph.
- For m=7,8,9: **20,000 pseudorandom graphs per m**, again at four reset angles.
- **375,456** exact-formula versus directly differentiated ODE numerical comparisons. Maximum absolute error: **4.163336342344337e-17** (floating-point rounding).
- For D=1..12: full finite `(a,d)` class-set separation equals `g_D(c*)`; the derived optimizer is never beaten by a **40,001-angle mesh**.
- Machine-readable details in `No32_Candidate_v0.1_verification.json`. SHA256 manifest in bundled archive.

**Independent review status:** Not yet externally confirmed. Dense-grid agreement is a check, not a proof of global optimality; the analytic argument is the proof candidate.

## Prior work and novelty limits (bounded literature exploration, 2026-10-22)

- Levnajić and Pikovsky, *Network Reconstruction from Random Phase Resetting* (2011), DOI `10.1103/PhysRevLett.107.034101`: phase-reset network inference; original method assumes observation of the initial instantaneous frequencies of all oscillators, rather than a hub-only second jet.
- Panaggio et al., *Model reconstruction from temporal data for coupled oscillator networks* (2019), DOI `10.1063/1.5120784` (verified via PubMed): coupled-oscillator network reconstruction from multivariate time series (requires transient observations of each oscillator in the reported method).
- Rosenblum and Pikovsky, *Inferring connectivity of an oscillatory network via the phase dynamics reconstruction* (2023), DOI `10.3389/fnetp.2023.1298228`: review of network phase inference; explicitly assumes observations of all network-node outputs for the featured technique.
- Kiran and Pereira, *Unique Reconstruction from Mean-Field Measurements* (2026), DOI `10.1137/25M1764815`: partial/aggregated observations, localized perturbations, sparse recovery and uniqueness guarantees.
- *Network Inference using Sinusoidal Probing* (IFAC-PapersOnLine 2021), DOI `10.1016/j.ifacol.2021.06.131`: network identification with single-node measurements via probing, a particularly relevant related line.
- Broader optimal perturbation/experimental design and coding theory can subsume the elementary max-min separation argument. No direct exact counterpart to this N=8 threshold was found during these searches, but this is **not evidence that it is unpublished or nontrivial in the literature**.

**Novelty verdict: INCONCLUSIVE.** It may be a small exercise following No.28 rather than a genuinely new paper. No priority or full-literature-coverage assertion is warranted.

## Explicit negative and open claims

- Not optimal among *all* ternary resets, multiple resets, arbitrary phase assignments or measurement schedules.
- No result for unknown coupling k, unknown intrinsic frequencies, heterogeneous/weighted edges, phase wrapping, reset jitter, process noise, or non-star models.
- Does not improve or refute No.28's fixed-horizon raw-phase sample-complexity lower bound; direct-jet margin and noisy raw-phase sample counts must not be conflated.
- No measured traffic or academic impact can be inferred from the GitHub/Zenodo statistics.

## Next gate

Independent proof audit (particularly the class-distance and c>0 branch); adversarial non-family reset challenge; prior-art equivalence search in active experimental design and network tomography; then GO/FAIL/INCONCLUSIVE decision for public No.32. **Do not create a public repository or Zenodo record on this exploratory result alone.**