# No.32 candidate v0.4 — Antipodal paired resets and preparation-error identifiability

**Ryutaro Yonezu / Yonezu Research Lab | 2026-10-22 | exploratory audit candidate, not for release**

**STATUS:** v0.3 externally AI-audited `PROOF=PASS (conditional); COMPUTATION=PASS; REFERENCES=PARTIAL; NOVELTY=INCONCLUSIVE; RELEASE=HOLD`. This document is **new v0.4 work with INTERNAL checks only**, and has **not** undergone independent v0.4 mathematical or literature audit. The exact antipodal cancellation and the asymptotic claims below are candidates for such audit. They are **not** assertions of scholarly novelty, physical reset feasibility, or real-sensor superiority.

## 1. The deliberately narrow dynamical model

Let `N=m+1`, `m>=3`: one hub 0, leaves 1,...,m, known hub–leaf edges, arbitrary *binary undirected* leaf–leaf edges `a_ij`. The zero-intrinsic-frequency Kuramoto dynamics are

```
θ_i' = k Σ_j a_ij sin(θ_j-θ_i),  k=1/N,  θ_0(0)=0.
```

At leaf phase vector `p=(p_1,...,p_m)`, only the **exact hub second derivative** `h''(0)` is observed. There is no measurement noise, no phase wrapping ambiguity for the mathematical jet, no reset-cost constraint, and no dynamics/process noise.

Define the normalized jet `T(p,G)=N² h''(0;p,G)` and

```
C(p)=Σ_i cos p_i,  S(p)=Σ_i sin p_i,  Z(p)=Σ_i cos p_i sin p_i,
H(p)= -Z(p)-C(p)S(p),
W(x,y)=(cos x-cos y)sin(y-x),
U(p,G)=Σ_{1<=i<j<=m} a_ij W(p_i,p_j).
```

Direct differentiation of the full ODE gives the exact identity

```
T(p,G)=H(p)+U(p,G).                                      (1)
```

Target edge is `a_12` (Python indices `0,1`). Every nuisance leaf–leaf edge may be present or absent. The unknown graph is fixed across the two experiments.

The two nominal leaf reset families are frozen from earlier research:

- `R3`: `p=(π, φ, 0,...,0)`, `φ=acos(-1/3)`. Nominal opposite-target-bit class gap `g3=b=4sqrt(2)/9` because `U=b(a_12+2d)` with integer `d`.
- `R4`: `p=(α, π-α, -α,...,-α)`, `α=asin(1/sqrt3)`. Nominal class gap `g4=A=8/(3sqrt3)` because `U=A a_12` with zero nuisance-edge contributions.

These statements rely on **binary edges**, the exact model and preparation geometry, and a single target bit.

## 2. Two different preparation-error models (essential)

Every nominal initial phase is realized within independent *adversarial bounds* `|δ_i|<=ε`; this is a deterministic uncertainty set, **not** a statement about statistically independent random errors. When comparing graph hypotheses, their actual realized phase vectors may differ. The hub is held fixed at zero. We distinguish:

1. **One jet with unknown jitter**: one preparation, and `p` may differ between the two candidate graphs.
2. **Unmatched two jets**: nominal preparations `p0` and `p0+π1`, but each is allowed its *own* unconstrained jitter vector `δ^(1)`, `δ^(2)`. They need not agree.
3. **Matched antipodal two jets**: a single realized but *unknown* vector `p=p0+δ` is used in the first run and **exactly `p+π1`** in the second run. All m leaf phases receive an exact relative π shift, and the hub does not shift. For each separate candidate graph this matched δ may be different.

The crucial matched-pair assumption (3) is strictly stronger than just specifying two nominal resets. Nothing here proves that hardware can establish such error correlation.

## 3. Exact antipodal baseline cancellation

For all p, directly from trigonometry,

```
C(p+π1)=-C(p), S(p+π1)=-S(p), Z(p+π1)=Z(p),
H(p+π1)=H(p),
W(p_i+π,p_j+π)=-W(p_i,p_j),
U(p+π1,G)=-U(p,G).
```

Consequently, if the second preparation is **exactly** the first realized preparation shifted by π on all leaves,

```
T(p,G)=H(p)+U(p,G),
T(p+π1,G)=H(p)-U(p,G),
D := [T(p,G)-T(p+π1,G)]/2 = U(p,G).                (2)
```

Equation (2) isolates unknown *inter-leaf* contributions without requiring knowledge of actual p or a separate star-only baseline calibration. It does **not** eliminate the effect of phase errors on U, and is not an estimate of U with physical sample noise.

## 4. Unknown preparation: a one-jet Θ(1/m²) separation limit for both R3 and R4

Define the **collision radius** for any observation protocol to be the infimum ε for which some two graphs with opposite `a_12`, and admissible (possibly different) realized initial phase vectors, produce exactly the same entire observation vector. Full class separation for ε smaller than this collision radius is guaranteed. Boundary equality need not be attained by the infimum; all statements below are asymptotic.

**Positive separation lower certificate.** Each normalized star response partial derivative satisfies

```
|∂H/∂p_i| = |cos(2p_i) - sin(p_i) S + cos(p_i) C| <= 1+2m.
```

Each W changes by at most `6ε` when both phases move by ≤ε (both partial derivatives bounded by 3), and at most `m(m-1)/2` graph edges are present. Hence, for any one graph,

```
|T(p0+δ,G)-T(p0,G)| <= [m(1+2m)+3m(m-1)] ε
                            = (5m²-2m) ε := K_m ε.
```

Thus two **opposite-bit** graphs with unrelated jitter vectors have normalized jet separation at least `g_R-2K_m ε`, with `g_R=b` for R3 and `A` for R4. In particular, the one-jet collision radius is at least

```
r_one(R,m) >= g_R/[2(5m²-2m)] = Ω(m^-2).                 (3)
```

**Explicit one-jet collision.** Compare G1 containing only edge (1,2), realized at nominal `p0`, against G0 with no leaf–leaf edges but with all nuisance leaves (3,...,m) uniformly shifted by an amount t. The exact normalized G1 jet is `H(p0)+g_R`. For G0 it is `H(p0+t1_nuisance)`.

For R3:

```
(d/dt) H(π,φ,t,...,t)|_{t=0}=-(m-2)(m-7/3).
```

For R4:

```
H(α,π-α,-α+t,...,-α+t)
  = -(m-2) cos(t-α)[ 2sinα + (m-1)sin(t-α) ],
(d/dt)H|_{t=0}=-(m-2)(m+1)/3.
```

Both derivatives are negative for `m>=3`. By continuity and Taylor expansion, for all sufficiently large m there are small negative shifts with

```
H(p0+t1_nuisance)-H(p0)=g_R,
|t_R(m)|= { b/m²+O(m^-3)          for R3,
            3A/m²+O(m^-3)         for R4 }.             (4)
```

The two different graphs thereby have *exactly equal full single-jet readings*, even with no nuisance edges. Combining (3) and (4): for each **fixed** nominal family R3, R4 under **unknown unrelated errors between hypotheses**,

```
r_one(R,m)=Θ(m^-2).                                    (5)
```

This is a theorem only about *these nominal preparations* and the exact second jet. It is not a universal lower bound across arbitrary experiments or all possible reset geometries.

## 5. Matched antipodal pair restores Θ(1/m) despite unknown actual p

Each candidate graph may have its own phase error δ, but within each candidate's two runs the exact same δ must be carried into the antipodal preparation. Then the *observable* D in (2) equals U(p,G).

Let `Q=(m-2)(m-3)/2` be nuisance–nuisance pairs, and `s=sinα=1/sqrt3`.

At R3, each perturbed graph's U differs from its nominal U by at most

```
E3(m,ε)=6(2m-3) ε + 4Q ε³.
```

At R4 the counterpart is

```
E4(m,ε)=6(2m-3) ε + 4Q ε²(s+ε).
```

Reason: `2m-3` edges touch leaves 1 or 2, each varying by ≤6ε; for the Q nuisance–nuisance edges the |W| bound is respectively `4ε³` (nominal 0) or `4ε²(s+ε)` (nominal -α). These bounds apply to **each** graph individually, so even if hypotheses have *different* actual δ vectors,

```
min opposite-bit |D(G1,p1)-D(G0,p0)| >= g_R-2E_R(m,ε).
```

Hence the matched two-jet observation vector separates target-bit classes whenever `2E_R(m,ε)<g_R`. For fixed R3/R4, the positive-certificate root scales as Ω(1/m). (In the R4 case, with ε=c/m, the limit condition is `24c+4s c²<A`; R3 is `24c<b`.)

**Full two-observation collision at O(1/m):** v0.3 contains explicit *same actual phase* R3/R4 graph pairs with opposite target bits and equal U at phase error radius `e3(m)~sqrt(2)/(9(m-2))`, or `e4(m)~1/(2sqrt2(m-2))`. Because H is also identical under the same actual phase, eqs. (1)–(2) show that **both** raw second-jet readings of the matched pair coincide for these graphs. Thus the *full matched two-jet* collision radius is upper bounded by these witnesses, proving

```
r_matched_pair(R,m)=Θ(m^-1)  (for R3 and R4 separately).  (6)
```

The construction does *not* claim the full matched model collision threshold equals the named witness e3/e4: they are only upper bounds.

## 6. Two nominally antipodal resets with independently drifting errors FAIL to improve the order

If the second realized reset is not constrained to `p+π1` with exactly the *same* δ, eq. (2) does not apply. An explicit indistinguishable pair exists with ε=O(m^-2):

- Graph G1 has only target edge (1,2); use nominal `p0` and `p0+π1` in the two runs. Its full normalized observation vector is `(H(p0)+g_R, H(p0)-g_R)`.
- Graph G0 has no leaf edges; in the **first run**, shift all its nuisance phases by `t_plus<0` such that `H(p0+t_plus 1_nuisance)=H(p0)+g_R`. In its **second run**, instead shift nuisance phases by `t_minus>0` such that `H(p0+t_minus 1_nuisance)=H(p0)-g_R`, and add π to all leaves.

Both shifts exist with `|t_±|=O(m^-2)` by the nonzero derivative calculated in §4. Because `H(p+π1)=H(p)`, the entire **two-component observation vectors coincide exactly** despite opposite target-edge bits. Any additional fixed number of repetitions of *these same two nominal preparations* with unrelated errors can be spoofed the same way.

Combining this collision upper bound with one-jet positive separation certificate (3) gives, in the **adversarial independent-reset-error model**,

```
r_unmatched_pair(R,m)=Θ(m^-2).                      (7)
```

This is not a no-go theorem for arbitrary multi-reset or adaptive designs, nor for stochastic independent errors with a specified distribution.

## 7. Numerical reproduction and example radii

`no32_antipodal_v04.py` (Python 3.12 standard library) separately evaluates `T=H+U` and the full Kuramoto ODE vector-field time derivative, and verifies exact antipodal cancellation for **495** seeded arbitrary graph/phase examples (`m=3,...,11`); maximum absolute normalized discrepancy **7.11e-15**. It also checks one-jet and matched/unmatched two-jet collision witnesses at 7 sizes per family, where the maximum full-vector witness error is printed in the JSON (`<2e-9` with ordinary double precision; generally much smaller).

`no32_rk4_independent_v04.py` separately time-integrates the original ODE using RK4 and estimates the *actual hub second jet* using a fourth-order centered difference on the hub velocity. The **168** seeded cases (`m=3,...,9`, both nominal patterns and antipodal counterparts with random jitter/graph) have max raw h'' error **2.51e-12**.

The example values below are **radians**, and are purposely not presented as exact collision radii. `CERT` = ε below this value is guaranteed to separate target bits. `COLL` = a specific explicit pair collides at this value. The exact threshold lies somewhere between bounds. For one-jet `COLL`, the witness uses empty-vs-target-only graphs and different realized jitter; for matched pair `COLL`, the witness uses the v0.3 nuisance-edge graph pair with the *same realized jitter*.

| N | Family | One unknown CERT | One unknown COLL | Matched pair CERT | Matched pair COLL |
|---:|---|---:|---:|---:|---:|
| 16 | R3 | 0.000287 | 0.003817 | 0.001940 | 0.012036 |
| 16 | R4 | 0.000703 | 0.023535 | 0.004727 | 0.027155 |
| 64 | R3 | 0.0000159 | 0.0001698 | 0.0004258 | 0.002574 |
| 64 | R4 | 0.0000390 | 0.0011869 | 0.001037 | 0.005796 |
| 128 | R3 | 0.00000391 | 0.00004033 | 0.0002087 | 0.001257 |
| 128 | R4 | 0.00000958 | 0.0002889 | 0.0005081 | 0.002828 |

The actual exact figures, independent-unmatched-pair witnesses and all tested sizes are in `No32_Candidate_v0.4_results.json`. All scripts write to their own directory; there is no hard-coded `/mnt/data` path.

**IMPORTANT:** The lower certificate is quite conservative. In particular, no comparison of the **optimal numerical constants** or universal R3-vs-R4 robustness follows from these bounds. The key difference is `m^-2` vs. `m^-1` **between uncertainty protocols**, not a ranking of the two reset geometries.

## 8. Hard limits and novelty prior-art gate

- The cancellation is elementary algebra; it may already be known in phase cycling, differential measurement, symmetry reduction, common-mode rejection, experimental design, or oscillator-network inference. **Scholarly novelty is NOT ESTABLISHED.** Before a separate No.32 paper, inspect mathematical equivalences rather than looking solely for the phrase "antipodal Kuramoto reset".
- The method assumes two **exact second-order hub derivatives**; extracting them from noisy short trajectories may be poorly conditioned, and subtraction can amplify observational noise. No lower/sample complexity analysis is presented.
- The matched two-reset **preparation-error correlation is strong and unverified** physically: an exact π offset on every leaf after the first experiment while reproducing the same unknown error vector. Unknown error cancellation does not follow merely from similar nominal control settings.
- Each construction recovers **one prespecified leaf–leaf target bit**; it does not reduce the number of target edges, and does not establish efficiency for full graph reconstruction.
- No nonzero known/unknown intrinsic frequencies, stochastic jitter distribution, unknown hub offsets, weighted edges, wrapped phase, or non-Kuramoto dynamics are covered.
- Contrasting unmatched and matched regimes is a model sensitivity finding, **not a claim of a new general no-go bound for multi-step methods**.

**Primary literature verified at metadata/abstract level:**

1. Z. Levnajić, A. Pikovsky (2011), *Network Reconstruction from Random Phase Resetting*, Phys. Rev. Lett. 107, 034101, DOI 10.1103/PhysRevLett.107.034101. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.107.034101
2. R. Delabays, M. Tyloo (2021), *Network Inference using Sinusoidal Probing*, IFAC-PapersOnLine 54(9), 696–700, DOI 10.1016/j.ifacol.2021.06.131. https://www.sciencedirect.com/science/article/pii/S2405896321006169
3. N. Kiran, T. Pereira (2026), *Unique Reconstruction from Mean-Field Measurements*, SIAM J. Applied Dynamical Systems 25(2), 629–653, DOI 10.1137/25M1764815. https://epubs.siam.org/doi/10.1137/25M1764815
4. T. Berry, T. Sauer (2025), *Reconstruction of Network Dynamics from Partial Observations*, SIAM JADS 24(1), 633–654, DOI 10.1137/24M1655780. https://epubs.siam.org/doi/10.1137/24M1655780
5. *Assessing the role of initial conditions in the local structural identifiability of large dynamic models* (2021), PMC8376890. https://pmc.ncbi.nlm.nih.gov/articles/PMC8376890

They support that phase-reset network reconstruction, single-point probing, partial observability, and initial-condition-sensitive identifiability already have substantive antecedents. The exact equivalence or nonequivalence of the v0.4 restricted two-reset cancellation and preparation-correlation threshold has **not** been audited from full texts. `REFERENCES=PARTIAL`, `NOVELTY=INCONCLUSIVE`.

## 9. Decision and next independent audit

- **Mathematics:** INTERNAL PASS **subject to verifying** all model quantifiers, errors across hypotheses vs between runs, exact π-pair requirement, asymptotic root existence, and class gap in R3.
- **Computation:** INTERNAL PASS with pure-standard-library reproduction. `no32_antipodal_v04.py`, `no32_rk4_independent_v04.py`, and both deterministic JSON result files. `SHA256SUMS.txt` lists all included files except itself.
- **Novelty:** INCONCLUSIVE; **RELEASE HOLD**. No.28 and v0.3 frozen originals remain unchanged.

**Independent audit instruction:** Seek minimal failures first: a graph pair and two matched antipodal vectors at ε smaller than the positive gap certificate; a counterexample to `H(p+π1)=H(p)` in the stated model; an algebraic inconsistency in the unmatched independent-jitter collision construction; or an earlier paper proving the same separation-order statement. Do not approve scholarly novelty on a solely trigonometric demonstration. If novelty remains weak, retain these findings as No.28 technical supplement rather than publishing an independent numbered paper.
