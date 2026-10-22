# No.32 candidate v0.2 — Nuisance-Cancelling Reset for Exact Hub-Jet Edge Identification

**2026-10-22 | Ryutaro Yonezu / Yonezu Research Lab | EXPLORATORY CANDIDATE — RELEASE HOLD**

**Independent audit status:** v0.1 restricted-family proof and computation passed a separate AI audit, with two editorial/portability defects. **The stronger v0.2 theorem below has NOT yet been independently audited.** Internal analytic derivation and standard-library numerical checks PASS. **REFERENCES: PARTIAL / NOVELTY: INCONCLUSIVE / PUBLICATION: HOLD.** No claim of scholarly priority or independent human peer review.

## 1. Why v0.2 changes the problem

The v0.1 exact finite-size boundary `N=8` remains true **inside the fixed reset family** (hub and most leaves at 0, leaf 1 at pi, leaf 2 at phi). It is **not a universal boundary** of the hub-star Kuramoto problem. When the allowed phase values are broadened by one additional global level, there exists a size-independent construction that removes **all nuisance leaf-edge contributions** to the single hub's second derivative. This also proves a global one-reset optimality result under the narrowly defined direct-second-jet measurement criterion.

Crucial control complexity distinction: v0.1 uses at most **3 total initial phase levels**, including the hub; v0.2 uses **3 leaf-phase levels, plus the hub at a fourth level**. Do not say the new result holds under the old three-total-level restriction.

## 2. Model and observable

An undirected symmetric Kuramoto star backbone with vertices `0,1,...,m` (`N=m+1>=4`), zero intrinsic frequencies, **known identical hub-leaf edges** and binary unknown leaf-leaf edges `a_ij ∈ {0,1}`. Coupling strength `k=1/N` is known and uniform. Initial phases are exactly preparable; hub phase is set to 0; only `h(t)=theta_0(t)` is measured, and the information model grants direct exact or bounded-error access to `h''(0)` (a time derivative of the hub phase). A single designated target is `a_12`. Other leaf edges are arbitrary.

`theta_i' = k * sum_j a_ij sin(theta_j-theta_i)`.

For any leaf phase vector `p_i=theta_i(0)`, exact differentiation gives

```
h''(0) = H_star(p) + k^2 sum_{1<=i<j<=m} a_ij W(p_i,p_j),
W(x,y) = (cos x - cos y) sin(y-x),
H_star(p) = -k^2 * [sum_i cos(p_i) sin(p_i)
                      + (sum_i sin(p_i)) (sum_i cos(p_i))].
```

`H_star` is computable from known phases and known star backbone, and does not depend on any unknown leaf edge. (The equivalent code computes the hub-only ODE derivative directly.)

The leaf-edge decomposition is elementary and should **not** by itself be presented as a novel network theory.

## 3. Stronger candidate theorem: global one-reset exact-jet margin

Let the between-label separation for a single phase preparation `p` be

`Delta(p) = min_{a_12=0 graph G0, a_12=1 graph G1} |h''(0;G1)-h''(0;G0)|`.

All other unknown leaf edges can vary independently between the two graphs. Then over **all choices of the leaf initial phases** and all assignments to the remaining leaves,

```
max_p Delta(p) = k^2 * 8/(3 sqrt(3))
              = 8 / (3 sqrt(3) N^2).
```

An attaining preparation is

```
alpha = asin(1/sqrt(3))        ≈ 35.26438968°
theta_0(0) = 0,
theta_1(0) = alpha,
theta_2(0) = pi - alpha       ≈ 144.73561032°,
theta_j(0) = -alpha          ≈ -35.26438968°  for all j>=3.
```

For this reset, the hub jet has **exactly** the form

```
h''(0) = H_star(p) + [8/(3 sqrt(3) N^2)] * a_12.
```

It is unaffected by **every other binary leaf-leaf edge**, including edges touching target leaves. Consequently nearest-label decoding under bounded additive jet error `|eta|<4/(3 sqrt(3) N^2)` is guaranteed correct, provided the model and reset angles are exact.

### Proof (internal; independent audit required)

1. For any fixed reset, choose one pair of graphs identical except for their target edge, e.g. take all nuisance edges absent in both. Their jet difference is exactly `k^2 |W(p_1,p_2)|`. Thus `Delta(p) <= k^2 |W(p_1,p_2)|`.
2. Put `t=(p_1+p_2)/2`, `d=(p_2-p_1)/2`. Then `W(p_1,p_2)=4 sin(t) sin^2(d) cos(d)`. As `|sin t|<=1` and, with `z=|cos d|∈[0,1]`, `(1-z^2)z<=2/(3 sqrt 3)`, it follows `|W| <= 8/(3 sqrt 3)` universally.
3. At the stated alpha, `sin(alpha)=1/sqrt(3)`, `cos(alpha)=sqrt(2/3)`. Direct substitution gives target weight `W(alpha,pi-alpha)=8/(3 sqrt(3))`.
4. Every nuisance edge with endpoints at equal `-alpha` has weight zero. For edges `(1,j)` with `j>=3`, `cos(alpha)=cos(-alpha)` yields `W(alpha,-alpha)=0`. For edges `(2,j)`, `(pi-alpha)-(-alpha)=pi`, yielding `W(pi-alpha,-alpha)=0`. Thus **all nuisance edge weights are exactly zero**. This attains the universal upper bound from step 2.

The result is stronger than the v0.1 family optimization but still applies **only** to a perfectly initialized star-backed Kuramoto model with a direct second-jet observable. It does not claim uniform optimality for realistic noisy phase samples, unknown frequencies, resets with jitter, multiple-reset experiments, or non-star topologies.

## 4. Quantitative comparison against No.28

- Original No.28 (`theta_1=pi`, `theta_2=acos(-1/3)`, other leaves 0) normalized cross-class gap: `b=4 sqrt(2)/9 ≈ 0.6285393611` for `N>=4` under the original set-up.
- v0.2 4-global-level reset: `8/(3 sqrt(3)) ≈ 1.5396007178` for **all N>=4**, with no class interleaving.
- Ratio: `sqrt(6) ≈ 2.449489743` (**+144.95%** relative normalized margin). Both actual gaps still scale as `N^-2` owing to `k=1/N`. This is **not** a 2.45x improvement in experimentally measured sample complexity; it measures only worst-case separation in the direct-second-jet channel.
- The v0.1 `N=8` boundary persists **only within the original family**. It cannot be interpreted as a universal transition when an additional phase level is permitted.

## 5. Audit outcome and portability correction

Two defects noted in the independent AI audit of v0.1 have been corrected or explicitly addressed:

1. Correct negative cosine branch proof: for `c<=-1/3`, `sqrt(1-c^2)(1+c)` is increasing over the relevant interval; for `-1/3<=c<=0`, `sqrt(1-c^2)(-2c)` is decreasing. The minimum is maximal at their intersection `c=-1/3`. The individual second factor does **not** attain its standalone global maximum there.
2. The restricted verification script now writes its JSON output **relative to its script directory**, never to an environment-specific `/mnt/data/` path.

The original v0.1 materials remain immutable. Files in this v0.2 package are a distinct candidate revision.

## 6. Reproducible internal computations

- `no32_phase_gap_verifier_v02.py`: direct independent construction of the full ODE vector field and hub second derivative, comparison to the graph-edge decomposition and target-only formula; optional RK4 central-difference phase-trajectory cross-check and dense pair-angle bound sanity test. Python 3.12 stdlib only.
- `no32_restricted_gap_verifier_v02.py`: original v0.1 family verifier updated solely for output path/version.
- Two JSON outputs contain the recorded checks; `SHA256SUMS.txt` covers all files except itself.
- Recorded v0.2 output: 82,728 ODE evaluations; max equation and target-only errors both `5.56e-17`; 60 RK4 independent finite-difference examples (max error `2.42e-8`); 519,841 phase pairs in a numerical bound sanity grid. These are internal reproductions, not external verification.

## 7. Prior work and novelty

Existence and abstracts verified against primary publisher/arXiv pages where possible:

- Z. Levnajić and A. Pikovsky (2011), *Network Reconstruction from Random Phase Resetting*, PRL 107 034101, DOI `10.1103/PhysRevLett.107.034101` (phase resetting for inverse network inference).
- M. J. Panaggio et al. (2019), *Model reconstruction from temporal data for coupled oscillator networks*, Chaos 29 103116, DOI `10.1063/1.5120784` (network reconstruction from oscillator trajectories).
- M. Rosenblum and A. Pikovsky (2023), *Inferring connectivity of an oscillatory network via the phase dynamics reconstruction*, Front. Netw. Physiol. 3 1298228, DOI `10.3389/fnetp.2023.1298228` (review; assumes all network-node outputs in its main method).
- R. Delabays and M. Tyloo, *Network Inference using Sinusoidal Probing*, IFAC-PapersOnLine 54(9), 2021, DOI `10.1016/j.ifacol.2021.06.131` / arXiv:2002.00490 (noteworthy single-node measurement precedent).
- N. Kiran and T. Pereira (2026), *Unique Reconstruction from Mean-Field Measurements*, SIAM JADS 25, 629–653, DOI `10.1137/25M1764815` (aggregated observation and perturbation-based recovery).

No indexed source located in the **bounded searches performed** stated this exact `8/(3sqrt(3))` hub-second-jet nuisance-cancellation construction; however the derivation involves very elementary trigonometrical identities and could be known or implicit in prior identifiability, optimal perturbation, and experiment-design literature. **NOVELTY=INCONCLUSIVE**. A claim that this is the first such result would be unsupported.

## 8. Next research gate

The promising residual question is **initialization-error robustness**: when each phase reset is perturbed by up to `epsilon`, nuisance edge weights no longer vanish exactly, potentially accumulating with graph size. Compare rigorous worst-case margins and real raw-phase sample budgets for optimized 3-total-level versus 4-total-level resets under a common jitter model. The present v0.2 theorem must first pass independent proof and reference-equivalence review. Keep **No.32 RELEASE=HOLD**, and do not overwrite or revise the already published No.28 archival record.