# Speaker Notes — 10-Minute Final Presentation

> **Narrative owner:** Josmar (Role 4 — Narrative & Data Storytelling Lead)
> **Timing owner:** Jesus (Role 5 — QA & Integration Lead)
> **Presentation date:** November 24, 2026
> **Format:** 10 minutes, all 5 members speaking (~2 minutes each)

**Story arc:** Setup → Conflict/Insight → Resolution

---

## 1. Timing plan

| Window | Speaker | Role | Section | Focus |
|--------|---------|------|---------|-------|
| 00:00 – 02:00 | **Edwing** | Role 1 — Data Architect & Wrangler | Setup & Data Pipeline | Business challenge, dataset scope, cleaning, schema |
| 02:00 – 04:00 | **Laura** | Role 3 — Python Visualization Specialist | Exploratory & Statistical Depth | Distributions, KDE, confidence intervals, correlation matrix |
| 04:00 – 06:00 | **Neyzer** | Role 2 — BI Dashboard Lead | Interactive Dashboard | Slicers, cross-filtering, drill-down walkthrough |
| 06:00 – 08:00 | **Josmar** | Role 4 — Narrative & Data Storytelling Lead | Conflict & Resolution | Core anomaly and 3 data-backed recommendations |
| 08:00 – 10:00 | **Jesus** | Role 5 — QA & Integration Lead | Accessibility, QA & Conclusion | Colorblind safety, 0-baseline, reproducibility, Q&A transition |

> Keep 10–15 seconds of buffer between speakers. The hard stop is **10:00**.

---

## 2. Opening (Edwing, 0:00 – 0:15)

**Hook (one sentence):**

> “A $2.3M business is quietly giving away its profit: nearly 1 in 5 order lines loses money,
> and most of that loss comes from discounts above 20%. Today we show where, why, and what to do.”

**Agenda (one sentence):**

> “We will cover the data pipeline, the statistical evidence, the interactive dashboard, and
> the three decisions we recommend.”

---

## 3. Speaker scripts

### 3.1 Edwing — Setup & Data Pipeline (0:00 – 2:00)

**Key points**
- Business context and the core question.
- Dataset: Superstore, ~9,994 rows × 21 columns, 2014–2017 (verify).
- Four field types: continuous, categorical, temporal, geospatial.
- Cleaning: null audit, date parsing, whitespace, duplicates, imputation.
- Output: one reproducible `clean_dataset.csv` consumed by the notebook and dashboard.

**Numbers to say out loud**
- Rows: 9,994 order lines
- Columns: 21 raw → 27 processed (6 derived fields)
- Missing cells handled: 0 found (full audit passed)
- Duplicates removed: 0 found

**Transition to Laura:**
> “With a trustworthy dataset in place, Laura will show what the distributions and correlations
> reveal.”

---

### 3.2 Laura — Exploratory & Statistical Depth (2:00 – 4:00)

**Key points**
- Distribution of `Sales` / `Profit`: skewness and outliers (KDE + box/violin).
- Uncertainty: 95% confidence interval band for the monthly trend.
- Correlation heatmap: strongest positive/negative relationships.
- Interactive Plotly scatter: discount vs. profit, colored by category.

**Insight to land**
> “Sales are heavily right-skewed, and the correlation matrix shows discount moving against
> profit — the first warning sign that we will confirm with the dashboard.”

**Transition to Neyzer:**
> “The dashboard makes these patterns explorable for a non-technical audience.”

---

### 3.3 Neyzer — Interactive Dashboard (4:00 – 6:00)

**Live demo sequence (rehearse exactly)**
1. Executive Overview: Total Sales, Total Profit, Profit Margin %.
2. Filter by Region → point out the change in margin.
3. Drill Category → Sub-Category → Product.
4. Show the loss-making products and the discount pattern.
5. Reset filters and return to the overview.

**Key points**
- 0-baseline on every bar chart.
- Sequential palette for volume; diverging palette centered at 0 for profit/loss.
- Cross-filtering and date slicing.

**Transition to Josmar:**
> “So what does this mean for the business? Josmar will connect the evidence to decisions.”

---

### 3.4 Josmar — Conflict & Resolution (6:00 – 8:00)

**Key points**
- **Conflict:** $2.30M sales, $286.4K profit (12.5% margin), but 1,871 lines (18.7%) lose money.
- **Anomaly:** margin turns negative once discount > 20% (+29.5% at 0% → −10.0% at 21–30% → −119.2% at >50%); 1,393 lines >20% discount = −$135.4K (86.7% of all losses), 96.8% of them lose money.
- **Concentration:** Furniture = 32.3% of sales but 6.4% of profit (2% margin); worst sub-categories: Tables (−$17.7K), Bookcases (−$3.5K), Supplies (−$1.2K).
- **3 recommendations (data-backed):**
  1. Cap discounts by sub-category (approval >20%; >30% almost always a loss) → addresses $135.4K of losses.
  2. Fix or exit loss-making sub-categories (reprice/delist Tables, Bookcases; review Supplies) → turns worst sub-categories profitable.
  3. Scale the profitable mix (Home Office 14%, West 15%, East 14%) → grows revenue without diluting margin.
- **Impact note:** recovering half of $156K lost moves margin from 12.5% toward ~16% without selling extra units.

**Preattentive choices**
- One accent color (orange) for loss; teal for positive margin.
- Bold only the key number/recommendation headline.
- No redundant legends or secondary tables on conflict slides.

**Transition to Jesus:**
> “Finally, Jesus will cover the quality and accessibility checks that make this analysis
> trustworthy and presentation-ready.”

---

### 3.5 Jesus — Accessibility, QA & Conclusion (8:00 – 10:00)

**Key points**
- **0-baseline:** every bar/column chart starts at zero (no visual distortion).
- **Color:** colorblind-safe palettes (Viridis / blue-orange); no red-green encoding.
- **Reproducibility:** notebook runs from `Kernel → Restart & Run All`; script reruns cleanly.
- **Dashboard integrity:** `.pbix` opens and refreshes without broken sources.
- **Access:** repository and deck links open in incognito (“Everyone with the link”).
- **Conclusion:** restate the core finding and the three recommendations in one sentence.

**Closing line**
> “The data is reproducible, the visuals are accessible, and the recommendation is clear:
> cap discounts above 20%, fix the loss-making sub-categories, and scale the profitable mix.”

**Q&A transition**
> “Thank you — we are happy to take questions.”

---

## 4. Rehearsal log

| Rehearsal | Date | Planned | Actual | Over/under | Main fix |
|-----------|------|---------|--------|------------|----------|
| 1 | TBD | 10:00 | TBD | TBD | TBD |
| 2 | TBD | 10:00 | TBD | TBD | TBD |
| 3 (dress) | TBD | 10:00 | TBD | TBD | TBD |

**Per-speaker timing**

| Speaker | Target | Rehearsal 1 | Rehearsal 2 | Final |
|---------|--------|-------------|-------------|-------|
| Edwing | 2:00 | TBD | TBD | TBD |
| Laura | 2:00 | TBD | TBD | TBD |
| Neyzer | 2:00 | TBD | TBD | TBD |
| Josmar | 2:00 | TBD | TBD | TBD |
| Jesus | 2:00 | TBD | TBD | TBD |
| **Total** | **10:00** | TBD | TBD | TBD |

---

## 5. Q&A preparation

Likely questions and assigned responder:

| Question | Responder | Key answer |
|----------|-----------|------------|
| How did you handle missing values? | Edwing | TBD |
| Why is this dataset representative? | Edwing | TBD |
| Is the correlation causal? | Laura | No — association only; confounders such as discount and category |
| Why use a confidence interval? | Laura | Shows uncertainty of the mean estimate, not just a point value |
| Why does the dashboard use a diverging palette? | Neyzer | Profit and loss diverge from a meaningful zero midpoint |
| How did you choose the 3 recommendations? | Josmar | Ranked by profit impact and feasibility: discount cap addresses 86.7% of losses; sub-category fixes are local and fast; mix scaling is upside with no new cost |
| How do you know the analysis is reproducible? | Jesus | Clean script + executed notebook + documented environment |
| Are the colors accessible? | Jesus | Viridis/blue-orange, contrast checked, no red-green pairing |

---

## 6. Presentation-day checklist

- [ ] Deck PDF on a USB drive **and** in the cloud.
- [ ] Dashboard `.pbix` opens on the presentation laptop.
- [ ] Notebook already executed (do not run live unless necessary).
- [ ] Interactive HTML plots open locally.
- [ ] All links tested on the presentation network.
- [ ] Clicker / keyboard navigation tested.
- [ ] Water and printed backup notes.
- [ ] Timer visible to the speaker on the left.
- [ ] Every member knows their exact start time and transition line.

---

## 7. Change log

| Date | Author | Change |
|------|--------|--------|
| 2026-11-06 | Jesus (Role 5) | Initial template created |
| 2026-11-23 | Josmar (Role 4) | Narrative, evidence, and recommendations completed |
| TBD | Jesus (Role 5) | Timed rehearsal results recorded |
