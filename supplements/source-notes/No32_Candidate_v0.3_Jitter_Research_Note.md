# No.32 candidate v0.3 — A constructive phase-reset jitter barrier

**2026-10-22 | Ryutaro Yonezu / Yonezu Research Lab | EXPLORATION, RELEASE=HOLD**

**Research disposition.** The separate AI audit of No.32 v0.2 reported `PROOF=PASS (restricted model)`, `COMPUTATION=PASS`, `REFERENCES=PARTIAL`, `NOVELTY=INCONCLUSIVE`, `RELEASE=HOLD`. The present **v0.3 is new work, not independently audited**. Its internal algebra, reproducible standard-library calculations, and one separate direct-ODE-vector-field differentiation implementation were checked. **No universal robustness advantage, scholarly novelty, raw-phase sample-complexity improvement, or practical performance is claimed.**

## 1. Exactly what is compared

The underlying zero-frequency, symmetric binary-leaf-edge Kuramoto star is unchanged from No.28/v0.2: `N=m+1>=4`, known hub-leaf couplings, unknown leaf-leaf edges, `k=1/N`, and one scalar observation `h''(0)` at the hub.

Each leaf initial phase is nominally set to `p_i^0`, but may deviate independently by an adversarial `delta_i` with `|delta_i| <= epsilon` **in radians**. The hub remains at zero. **When comparing two possible graphs, they share the same realized phase vector** `p=p^0+delta`; the unknown leaf edges may differ. This is a *same-realized-reset pairwise identifiability* test, and is a deliberately favorable model for the observer. For a practical decoder the realized phases must be known, or its star-only contribution independently calibrated. If jitter is unobserved or the star-only term is calibrated from nominal rather than actual phase values, the present positive-separation certificates do **not** guarantee successful decoding.

Define `W(x,y)=(cos x-cos y)sin(y-x)` and

`h''(0;G,p)=H_star(p)+N^{-2} sum_{i<j} a_ij W(p_i,p_j)`.

For each nominal reset `R` define the **normalized same-realized-phase robust gap**

`gamma_R(epsilon) = inf_{|delta_i|<=epsilon} min_{a12(G1)=1, a12(G0)=0} N^2 |h''(0;G1,p)-h''(0;G0,p)|`.

The star-only term cancels exactly between graphs. `gamma_R>0` proves that two graphs with different target-edge bits are distinguishable from a perfect single jet at the *same known realized preparation*, with jet reading errors smaller than `gamma_R/(2N^2)` provided the decoder uses actual preparation information. `gamma_R=0` provides an explicit impossibility witness for one reset and one jet, even if the realized phases are known. This says **nothing** about several resets or a whole observed time series.

**Compared nominal resets:**

* `R3` (No.28): leaf 1 `pi`, leaf 2 `phi=acos(-1/3)`, all other leaves `0`. Normalized zero-error class gap `b=4sqrt(2)/9=0.6285393611`.
* `R4` (No.32 v0.2): leaf 1 `alpha`, leaf 2 `pi-alpha`, all other leaves `-alpha`, with `alpha=asin(1/sqrt(3))`. Zero-error gap `A=8/(3sqrt(3))=1.5396007178`.

## 2. Constructive exact collision for R3

For `m>=3`, fix **one common realized phase vector**

`p1=pi-e`, `p2=phi`, `pj=e` for `j>=3`, with `0<=e<0.45`.

This satisfies the per-leaf jitter bound epsilon=e. Construct two different graphs:

* `G1`: target edge (1,2) present; **no nuisance edges**.
* `G0`: target edge absent; **all** `(1,j)` for `j>=3` present; no other nuisance edges.

Their normalized jet difference is

`F3_m(e)=W(pi-e,phi) - (m-2) W(pi-e,e)`

`       =W(pi-e,phi) - 4(m-2) sin(e)cos^2(e)`.

At `e=0`, `F3_m(0)=b>0`. It changes sign for a small positive e; a root `e3(m)` forces `h''(0;G1,p)=h''(0;G0,p)`. Therefore `gamma_R3(e3(m))=0`. The smallest root along this specific witness curve behaves as

`e3(m) = [sqrt(2)/9]/(m-2) + O((m-2)^-2)`.

This is an **upper bound** on the true worst-case jitter radius: other graphs/phase deviations may destroy identifiability at a smaller epsilon.

## 3. Constructive exact collision for R4

Fix the common realized vector

`p1=alpha+e`, `p2=pi-alpha-e`, `pj=-alpha+e` for `j>=3`.

Choose `G1` with only the target edge; choose `G0` with **every** `(1,j)` and `(2,j)` for `j>=3`, but without the target. Put `c=cos alpha=sqrt(2/3)`.

The three relevant exact weights are

`W(p1,p2)=4cos^2(alpha+e)sin(alpha+e)`;

`W(p1,pj)=(4/3)c sin(e)`;

`W(p2,pj)=4c sin(e)cos^2(e)`.

Hence the normalized jet difference is

`F4_m(e)=4cos^2(alpha+e)sin(alpha+e) - 4(m-2)c sin(e)[1/3+cos^2(e)]`.

At zero it is `A>0`; it has a small positive root `e4(m)` at which the **same one-jet value** corresponds to target edge 0 or 1. Moreover

`e4(m) = [1/(2sqrt(2))]/(m-2) + O((m-2)^-2)`.

The **particular collision-witness radii** therefore satisfy

`e4(m)/e3(m) -> 9/4 = 2.25` as `m->infinity`.

**Important:** This 2.25 ratio concerns two **constructed upper bounds** on failure radii, **not** a proof that the 4-level reset has a 2.25-fold higher *true* adversarial jitter tolerance. Their exact worst-case radii have not been determined.

## 4. Conservative positive-gap certificates

Each partial derivative of `W(x,y)` has absolute value at most 3, so perturbing both endpoints by at most epsilon changes each edge weight by at most `6 epsilon`.

For two *nuisance leaves* (`j,k>=3`) reset near a common nominal phase `q`, use

`W(x,y)=4sin((x+y)/2)sin^2((y-x)/2)cos((y-x)/2)`

and `|x-y|<=2 epsilon`. When `q=0` (R3), `|W|<=4 epsilon^3`. When `q=-alpha` (R4), `|W|<=4 epsilon^2 (sin(alpha)+epsilon)`.

Writing `Q=(m-2)(m-3)/2` for the number of nuisance-leaf pairs, the difference of any two opposite-bit graph jets at **the same perturbed preparation** is bounded below, after multiplication by `N^2`, by

`L3(m,epsilon) = b - 6(2m-3)epsilon - 4Q epsilon^3`, and

`L4(m,epsilon) = A - 6(2m-3)epsilon - 4Q epsilon^2(sin(alpha)+epsilon)`.

For R3 this relies on the nominal odd-integer lattice gap: `W(pi,phi)=b`, `W(phi,0)=2b`, and all other nuisance weights are 0. For R4 all nominal nuisance weights are 0. The inequalities are intentionally conservative; their constants are not claimed optimal.

If `L_R(m,epsilon)>0` then **every** phase error vector within the cube and **every** pair of opposite-bit graphs under the **same actual reset** retains a strictly positive normalized gap. Denote the roots `ell3(m)`, `ell4(m)`: the actual same-realized-reset collision radius `r_R(m)` obeys

`ell3(m) <= r3(m) <= e3(m)` and `ell4(m) <= r4(m) <= e4(m)`.

As `m->infinity`, the lower certificate roots scale with `1/m`: `m ell3(m)->b/12`, and `m ell4(m)->c4`, where `12c4 + (2/sqrt(3)) c4^2 = A` (`c4≈0.12675405`). Combined with collision witnesses above, this proves **Theta(1/m)** upper/lower scaling for these **two fixed nominal families** in this conditional test. It is not a no-go theorem for every possible reset, every measurement, or adaptive multishot experiments.

## 5. Numerical table and interpretation

Radii below are **radians**. `CERT` means `epsilon < value` gives a provable positive same-preparation class gap. `COLL` means that *at* the displayed epsilon there is an explicit pair of indistinguishable opposite-bit graphs. The unknown actual failure threshold lies between the two numbers, and these are **not confidence intervals**.

| N | R3 CERT | R3 COLL | R4 CERT | R4 COLL |
|--:|--:|--:|--:|--:|
| 4 | 0.034919 | 0.148539 | 0.085533 | 0.295498 |
| 5 | 0.020950 | 0.076403 | 0.051101 | 0.167065 |
| 8 | 0.009523 | 0.031079 | 0.023133 | 0.070006 |
| 16 | 0.003880 | 0.012036 | 0.009404 | 0.027155 |
| 32 | 0.001776 | 0.005408 | 0.004300 | 0.012188 |
| 64 | 0.000852 | 0.002574 | 0.002062 | 0.005796 |
| 128 | 0.000417 | 0.001257 | 0.001010 | 0.002828 |

For `N=8` in degrees the R3 interval is approximately **0.546°–1.781°**, and the R4 interval is approximately **1.325°–4.011°**. These intervals **overlap**, so the comparison does **not** establish a strict robust-tolerance ordering. The two particular collisions differ by about 2.25-fold here, but earlier, different collisions may exist.

## 6. Reproduction and audit boundary

Files `no32_jitter_collision_v03.py` and `No32_Candidate_v0.3_jitter_results.json` cover:

* Bisection of the two exact analytic collision equations at 12 network sizes from `N=4` to `N=1024`;
* Conservative certificate-radius roots and unit checks;
* Equality of the **full, directly differentiated ODE** and `H_star + sum edge weights` for 225 deterministic independently generated phase/graph cases (`m=3..11`), with maximum absolute discrepancy `1.11e-16`;
* Equality of `G0` and `G1` full ODE second jets at the constructed collision phases (floating-point tolerance checked).

Run using Python 3.12 standard library: `python no32_jitter_collision_v03.py`. The output JSON is written next to the script, not to `/mnt/data` or any fixed machine-specific path. All uploaded bundle files have SHA256 hashes in `SHA256SUMS.txt`.

The calculation does **not** independently prove that the bisection roots are globally first along all possible perturbation paths, nor does it exhaust all graphs for large m. The analytic upper/lower statements do not require those global-first-root claims. No human peer review and no independent v0.3 AI audit has been completed.

## 7. Literature and novelty

The broader fields of phase resetting, inverse oscillator networks, single-point probing, and observation-based network recovery have existing results:

* Levnajić & Pikovsky (2011), *Network Reconstruction from Random Phase Resetting*, Phys. Rev. Lett. 107, 034101, DOI: `10.1103/PhysRevLett.107.034101`.
* Delabays & Tyloo (2021), *Network Inference using Sinusoidal Probing*, IFAC-PapersOnLine 54(9), 696–700, DOI: `10.1016/j.ifacol.2021.06.131`, arXiv `2002.00490`.
* Kiran & Pereira (2026), *Unique Reconstruction from Mean-Field Measurements*, SIAM J. Applied Dynamical Systems 25(2), 629–653, DOI: `10.1137/25M1764815`.

These works establish the relevance of the field; they have **not been verified to establish or refute novelty of the narrowly formulated same-reset jitter collision bounds**. The present trigonometric construction is elementary and might be a direct corollary of prior robust identifiability or experimental-design results. `REFERENCES=PARTIAL; NOVELTY=INCONCLUSIVE; RELEASE=HOLD`. Do not publish as an independently novel theorem on this basis.

## 8. Next gate

1. Independent reproduction/proof audit of the v0.3 collision equations and positive-gap certificates.
2. Analyze **different realized error vectors under different hypotheses** (unknown jitter), and raw-hub-phase samples rather than an oracle jet; both could be strictly harder.
3. Attempt *multiple resets* or alternative phase designs, which the present one-shot collision does not exclude.
4. Search for equivalent results in robust system identification, active experiment design, and coding/separation bounds; publish only if a nontrivial residual remains after this audit.

**Decision:** `PROOF=INTERNAL PASS (conditional); COMPUTATION=PASS; EXTERNAL AUDIT=PENDING; REFERENCES=PARTIAL; NOVELTY=INCONCLUSIVE; RELEASE=HOLD`. Existing No.28 and No.32 v0.2 archives are not modified.