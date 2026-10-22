# No.28 — Technical Appendix A
## Reset-Phase Lemmas and Preparation-Error Identifiability in a Restricted Hub–Star Kuramoto Network

**Ryutaro Yonezu — Yonezu Research Lab**  
**Technical appendix draft v0.1 | 2026-10-22 | Not a new numbered paper**

**Parent record:** No.28, *Restricted Hub-Star Phase Reconstruction: A Conditional Research Record on Ternary Resets and Noise Scaling* (archival v1.0, 2026-10-17).  
**Source of the appended results:** the formerly independent **No.32 exploratory candidate v0.1–v0.4**, now **reclassified as supplemental lemmas of No.28**. These are supporting calculations, **not independent scholarly novelty claims**.

**Evidence state:** Conditional mathematical proof checks: **PASS in a separate AI audit** for v0.1–v0.4, within the narrowly specified models. Computation and integrity checks: **PASS** as reported and rechecked in those audits. Bibliography verification: **PARTIAL**. Scholarly novelty: **INCONCLUSIVE**. Human peer review: **none**. Publication as a new No.32 paper: **not authorized / CLOSED AS A SEPARATE PAPER**. This appendix is a **draft technical supplement**, not an announced update to any existing GitHub/Zenodo release or DOI.

### A.1. Model and normalization

Let `N=m+1 >= 4`, with hub 0 and leaves `1,...,m`, a known unit-weight undirected hub–leaf star, unknown **binary** undirected leaf–leaf edges `a_ij`, zero intrinsic frequencies, and known coupling `k=1/N`. The hub starts at phase 0. The leaf initial phase vector is `p=(p_1,...,p_m)` and the network obeys

\[
\dot\theta_i=k\sum_j a_{ij}\sin(\theta_j-\theta_i).
\]

Unless a lemma explicitly changes the uncertainty model, the observable is **the exact hub second derivative at time zero**, not a noisy trajectory or a practically available derivative estimate. The designated target edge is `a_12` and all other leaf–leaf edges are nuisance variables. Define

\[
\begin{aligned}
T(p,G)&:=N^2 h''(0;p,G),\\
C(p)&=\sum_i\cos p_i,\quad S(p)=\sum_i\sin p_i,\\
Z(p)&=\sum_i\cos p_i\sin p_i,\\
H(p)&=-Z(p)-C(p)S(p),\\
W(x,y)&=(\cos x-\cos y)\sin(y-x),\\
U(p,G)&=\sum_{1\le i<j\le m}a_{ij}W(p_i,p_j).
\end{aligned}
\]

**Lemma A.1 (exact second-jet decomposition).** For the stated Kuramoto model,

\[
\boxed{T(p,G)=H(p)+U(p,G).}
\]

**Proof.** Differentiate the hub equation once, use `h'(0)=k S(p)` and each leaf's derivative from the complete ODE, and collect hub-star contributions into `H` and each unordered leaf edge's pair of terms into `W`. This is an elementary identity, not presented as a new dynamical principle. □

### A.2. Selective suppression of all nuisance edges (formerly No.32 v0.2)

For any fixed phase vector define opposite-target-bit separation, with all nuisance edges freely varying between hypotheses, by

\[
\Delta(p)=\min_{a_{12}(G_0)=0,\ a_{12}(G_1)=1}|h''(0;p,G_1)-h''(0;p,G_0)|.
\]

**Lemma A.2 (restricted single-jet margin and an attaining reset).** With unrestricted exact leaf-phase preparation in the stated model,

\[
\boxed{\max_p\Delta(p)=\frac{8}{3\sqrt3\,N^2}.}
\]

It is attained by

\[
\alpha=\arcsin(1/\sqrt3),\qquad
p_1=\alpha,\ p_2=\pi-\alpha,\ p_j=-\alpha\ (j\ge3).
\]

At that preparation,

\[
h''(0)=N^{-2}H(p)+\frac{8}{3\sqrt3\,N^2}a_{12},
\]

so the unknown nuisance edges do **not** contribute to the observed second jet. A jet observation error less than `4/(3√3 N²)` in absolute magnitude permits nearest-class decoding when the preparations and model are exact.

**Proof.** Compare two graphs differing only at target edge `(1,2)`: for any `p`, `Δ(p) ≤ N⁻² |W(p_1,p_2)|`. Writing `t=(p_1+p_2)/2`, `d=(p_2-p_1)/2` gives `W=4 sin(t) sin²(d) cos(d)`. Maximizing `(1-z²)z` for `z=|cos d| ∈ [0,1]` yields `|W|≤8/(3√3)`. The displayed reset makes the target weight attain the bound; every nuisance edge has weight zero by equal cosine, equal endpoint phase, or phase difference `π`. Thus the upper bound is attained. □

**Scope warning.** The reset has **four distinct total phase levels, counting the hub**, versus three for the original No.28 construction. A maximum direct-second-jet separation is **not** a minimum actual sample budget, a robust-optimality claim, or proof of independent novelty.

### A.3. Phase-perturbation collisions for two fixed resets (formerly v0.3)

Define two fixed nominal reset families:

- `R3` (original No.28): `p=(π, φ, 0,...,0)`, `φ=acos(-1/3)`, nominal *normalized* target-bit class gap `g_3=b=4√2/9`.
- `R4` (Lemma A.2): `p=(α, π-α, -α,...,-α)`, nominal normalized gap `g_4=A=8/(3√3)`.

In this section **both opposing graph hypotheses share exactly the same realized phase vector** `p=p⁰+δ`, with `|δ_i|≤ε`; the vector may be unknown to the reader, but positive-gap decoding may require actual-phase information or calibration. Define `r_same(R,m)` as the infimum perturbation bound allowing an opposite-target-bit graph pair to collide in the **same** exact second-jet reading at a **common realized** reset.

**Lemma A.3 (fixed-family error-radius order).** For each `R∈{R3,R4}`, there are explicit positive-gap certificates `ell_R(m)` and collision witnesses `e_R(m)` for which

\[
\ell_R(m)\le r_{\rm same}(R,m)\le e_R(m),\qquad
\boxed{r_{\rm same}(R,m)=\Theta(m^{-1})}.
\]

Let `Q=(m-2)(m-3)/2`, `s=1/√3`. A sufficient positive-gap certificate is

\[
\begin{aligned}
L_3(m,\varepsilon)&=b-6(2m-3)\varepsilon-4Q\varepsilon^3>0,\\
L_4(m,\varepsilon)&=A-6(2m-3)\varepsilon-4Q\varepsilon^2(s+\varepsilon)>0.
\end{aligned}
\]

The explicit nuisance-edge collision constructions satisfy

\[
 e_3(m)=\frac{\sqrt2}{9(m-2)}+O(m^{-2}),\qquad
 e_4(m)=\frac{1}{2\sqrt2(m-2)}+O(m^{-2}).
\]

**Proof outline.** Each target-adjacent edge weight changes by at most `6ε`; nuisance–nuisance edge weights contribute at most `4ε³` for R3 and `4ε²(s+ε)` for R4. This proves the positive-gap certificates. Conversely, change target-leaf and nuisance-leaf phases along the one-parameter paths detailed in the frozen v0.3 evidence. For R3 take `(π-e,φ,e,...,e)` and compare a target-only graph with a graph carrying every edge `(1,j)`. For R4 take `(α+e,π-α-e,-α+e,...,-α+e)` and compare a target-only graph with all edges `(1,j),(2,j)`. The exact trigonometric difference functions have roots with the stated asymptotics. □

**Important:** `e_4/e_3→9/4` is a ratio of **these specific collision witnesses**, **not** the ratio of the actual worst-case tolerances. A universal superiority ordering of R3 and R4 has **not** been proved.

### A.4. Antipodal paired resets and cancellation (formerly v0.4)

Let `1` denote the all-ones leaf vector. The **matched antipodal protocol** consists of first realizing a phase vector `p=p⁰+δ`, then resetting to **precisely `p+π1`** with the same unknown preparation errors on every leaf. The hub remains at zero, and the unknown graph is held fixed.

**Lemma A.4 (exact antipodal cancellation).** Under this **matched preparation assumption**,

\[
\boxed{\frac{T(p,G)+T(p+\pi\mathbf 1,G)}2=H(p)},
\qquad
\boxed{\frac{T(p,G)-T(p+\pi\mathbf1,G)}2=U(p,G)}.
\]

**Proof.** Adding π on all leaf phases negates `C` and `S` but preserves `Z`, hence `H(p+π1)=H(p)`. It negates each cosine without changing leaf–leaf phase differences, hence `W(x+π,y+π)=-W(x,y)` and `U(p+π1,G)=-U(p,G)`. Substitute into Lemma A.1. □

The cancellation removes the **star contribution** even though the actual leaf phases are unknown. It does **not** remove phase error in `U`, does not guarantee the relative π shift can be implemented physically, and is not a real-noise-cancellation result.

### A.5. Error-model dependence of the two-jet gain (formerly v0.4)

For a protocol, define the **collision radius** as the infimum ε for which **two graph hypotheses with opposite target bits**, each allowed its own nuisance graph and phase errors within its specified uncertainty set, yield **the same complete observation vector**. In the single-run and unmatched settings, the nuisance phase vector may be *different between graph hypotheses*; in the matched protocol each graph's two runs must retain the *same* errors (but errors need not agree across the two competing graphs). Three protocols are considered:

1. `one`: one exact normalized second-jet reading with unknown bounded phase errors;
2. `unmatched`: two nominally antipodal readings with separately drifting/adversarial errors in each run;
3. `matched`: two readings with the **exact shared-error antipodal relation** of Lemma A.4.

**Lemma A.5 (two-jet conditional error-scaling distinction).** For each *fixed nominal preparation family* R3 or R4, as `m→∞`,

\[
\boxed{r_{\rm one}(R,m)=\Theta(m^{-2})},\quad
\boxed{r_{\rm unmatched}(R,m)=\Theta(m^{-2})},\quad
\boxed{r_{\rm matched}(R,m)=\Theta(m^{-1})}.
\]

**Proof outline.** For any graph, `|T(p⁰+δ,G)-T(p⁰,G)|≤(5m²-2m)ε`, so the one-run collision radius is at least `g_R/[2(5m²-2m)]`. With only the target edge in one graph and no leaf–leaf edges in the other, shifting all nuisance-leaf phases by a common `t=O(m⁻²)` in the second graph changes the star term `H` by exactly `g_R`, giving an equal reading. Thus the one-run radius is `Θ(m⁻²)`.

For the matched pair, Lemma A.4 reduces the informative difference to `U`. Its positive class-gap certificate is `g_R-2E_R(m,ε)` with

\[
E_3=6(2m-3)\varepsilon+4Q\varepsilon^3,\qquad
E_4=6(2m-3)\varepsilon+4Q\varepsilon^2(s+\varepsilon),
\]

so separation holds at least for a constant times `1/m`. The common-realized-phase collision witnesses of Lemma A.3 make **both** antipodal jets coincide at `O(1/m)`, proving the matched `Θ(m⁻¹)` result.

For the unmatched pair, the second run may suffer a *different* error. Shift the nuisance leaf phases by a small negative `t_+` in one run and a positive `t_-` in the other, so the same star-only graph mimics the target-only graph's positive and negative target contributions in the two components. The shifts are `O(m⁻²)`, and the one-jet separation certificate supplies the lower bound. □

**Scope warning.** This is a **worst-case adversarial** model, not a random-jitter distribution. The `Θ(m⁻¹)` gain is across **measurement protocols**, not proof of R4's superiority over R3. An arbitrary multi-reset protocol is not ruled out by the unmatched example; results assume a fixed designated edge, exact jet, and specific reset families.

### A.6. Historical restricted observation (formerly v0.1)

Within the **original one-parameter, three-total-phase-level reset family only**, the maximum nominal direct-second-jet class gap uses a different cosine for `4≤N≤7`, and returns to the original No.28 setting `cos φ=-1/3` for `N≥8`. This finite-size switch is **not universal**: Lemma A.2 enlarges the allowed phase family and eliminates that constraint. The derivation is archived with the v0.1 candidate and is not recommended as a headline result.

### A.7. Limitations and prior-work status

These lemmas concern exact second jets of a restricted **binary hub-star Kuramoto ODE**. They establish neither robust inference from noisy finite-time raw-phase samples nor an optimal measurement budget; two-jet differencing may amplify measurement noise. Intrinsic-frequency uncertainty, weighted unknown edges, realistic reset feasibility, correlated *stochastic* jitter, adaptive many-step procedures and recovery of all edges are outside scope. Known areas of relevant prior work include phase-reset network reconstruction, sinusoidal single-node probing, mean-field reconstruction, differential/common-mode cancellation and experimental design. **REFERENCES=PARTIAL; NOVELTY=INCONCLUSIVE** remain appropriate; none of the elementary trigonometric identities is claimed as an original discovery.

### A.8. Provenance and preservation policy

- No.28's original published preprint, DOI, original evidence ZIP, audit status and citation metadata remain **unchanged**.
- The former No.32 v0.1–v0.4 evidence bundles remain available as **traceable historical audit artifacts**; their earlier HOLD decisions are preserved. No.32 is **closed as a separate publication candidate**, not deleted.
- This appendix is a **draft** intended to accompany No.28 as supporting material. Attaching it to an already published record may require a separate supplement or a new formally labeled version. Do **not** silently replace the No.28 PDF or Zenodo record, or claim its existing DOI automatically covers this new document.
- The separate AI audit reports supplied for v0.1–v0.4 support the **conditional** pass statements; they are not human peer review and do not certify novelty.

### A.9. Archived audit source files

For exact formulas, graph-pair witnesses, calculations and full scope statements, consult the versioned bundles archived alongside this appendix:

- `No32_Candidate_v0.1_Exploration_Bundle.zip`
- `No32_Candidate_v0.2_Audit_Bundle.zip`
- `No32_Candidate_v0.3_Jitter_Audit_Bundle.zip`
- `No32_Candidate_v0.4_Antipodal_Pair_Audit_Bundle.zip`

**Final disposition:** `No.28 APPENDIX DRAFT = READY FOR EDITORIAL REVIEW`; `PROOF = CONDITIONAL AI-AUDITED PASS`; `COMPUTATION = PASS`; `REFERENCES = PARTIAL`; `NOVELTY = INCONCLUSIVE`; `No.32 INDEPENDENT RELEASE = CLOSED / NOT PURSUED`.
