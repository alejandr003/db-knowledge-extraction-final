# Canva Build Guide — Executive Presentation

> **Owner:** Josmar (Role 4 — Narrative & Data Storytelling Lead)
> **Purpose:** Rebuild the same 18-slide deck in Canva, 1:1 with `Executive_Presentation.pptx`.
> **Deck length:** 18 slides · 16:9 widescreen · ~10 minutes
> **Story arc:** Setup → Insight → Conflict → Resolution

This guide lets you recreate the deck in Canva by copy-paste. The PowerPoint/PDF version
(`presentation/Executive_Presentation.pptx` / `.pdf`) is already finished and matches every
slide below. Use Canva only if the professor wants a public "Everyone with the link" deck.

---

## 1. Canva setup

1. Create a design → **Presentation (16:9)** → **1920 × 1080 px**.
2. Set the **theme colors** (Canva → Styles → Colors → + Add):
   - Navy `#1F3A5F`
   - Navy dark `#142844`
   - Orange `#E4572E`
   - Teal `#2A9D8F`
   - Gray `#4A5568`
   - Light `#F1F5F9`
   - Line `#E2E8F0`
3. Set the **fonts**:
   - Titles: **Montserrat** (Bold) — closest to the PPTX Arial Bold
   - Body: **Open Sans** (Regular) — or Arial to match exactly
4. Upload the images in `presentation/assets/` to Canva once, then reuse them.

**Global rules**
- White background on content slides; full navy background on the 4 section dividers and the closing.
- Every content slide has a **thin navy bar at the very top** and a **small orange vertical bar** left of the kicker.
- Kicker (small, orange, letter-spaced) above the title; title in navy bold.
- Footer: left = "Enterprise Multi-Modal Data Visualization & Storytelling", right = slide number.
- Top-right gray tag = the speaker who owns that slide.

---

## 2. Slide-by-slide

### Slide 1 — Title
- **Background:** navy `#1F3A5F`, with an orange `#E4572E` vertical bar on the far left and a short orange block top-right.
- **Kicker:** `DATABASE KNOWLEDGE EXTRACTION · FINAL PROJECT` (orange, letter-spaced)
- **Title:** `Enterprise Multi-Modal` / `Data Visualization & Storytelling` (white, bold, ~2 lines)
- **Orange rule** under the title.
- **Subtitle:** `Turning a raw sales CSV into three decisions that protect profit.` (light gray)
- **Team:** `Edwing · Neyzer · Laura · Josmar · Jesus` (white, bold)
- **Bottom:** `Presented November 24, 2026 · 10 minutes`

### Slide 2 — Four questions (Agenda)
- **Kicker:** `OVERVIEW` · **Tag:** `Josmar · Role 4`
- **Title:** `Four questions, one dataset, one decision`
- **Line:** `A retailer has four years of order data but no clear read on profitability.`
- **4 cards** (light `#F1F5F9`, colored top edge):
  1. `Where do we make money?` (navy edge)
  2. `Where do we lose money?` (navy edge)
  3. `What is causing the profit leak?` (orange edge)
  4. `What should we do about it?` (teal edge)
- **Navy strip** at bottom with 4 labels: `SETUP · Trust the data` / `INSIGHT · See the evidence` / `CONFLICT · Name the anomaly` / `RESOLUTION · Act on it`

### Slide 3 — Divider 01 · SETUP
- **Full navy background.** Giant faint `01` top-left, orange kicker `SETUP`, white title `The data behind the story`, sub `A reproducible pipeline turns a raw CSV into one trusted source of truth.`

### Slide 4 — Dataset & pipeline
- **Kicker:** `SETUP · DATA` · **Tag:** `Edwing · Role 1`
- **Title:** `Superstore sales: 9,994 order lines, four years, one source`
- **Left panel** (light, titled `THE PIPELINE`): 4 numbered circles
  1. `Raw CSV` — 9,994 rows × 21 columns
  2. `clean_data.py` — audit · clean · type-cast · impute
  3. `Processed CSV` — 9,994 rows × 27 columns
  4. `Consumers` — Notebook + Power BI dashboard (orange circle)
- **Right column** titled `FOUR FIELD TYPES (RUBRIC)`:
  - `Temporal` — Order Date · Ship Date
  - `Continuous` — Sales · Profit · Discount · Quantity
  - `Categorical` — Segment · Category · Sub-Category · Ship Mode
  - `Geospatial` — Country · Region · State · City · Postal Code
- **Navy pill** bottom-right: `2014–2017 · United States · USD · one row per order line`

### Slide 5 — Data quality
- **Kicker:** `SETUP · QUALITY` · **Tag:** `Edwing · Role 1`
- **Title:** `Six derived fields make the raw data decision-ready`
- **Line:** `The cleaning script documents every change, so anyone can reproduce the same CSV.`
- **6 cards** (3×2): `Order Year` (Trend by year) · `Order Month` (Seasonality) · `Order Quarter` (Quarterly view) · `Shipping Days` (Fulfilment speed) · `Profit Margin` (Efficiency ratio) · `Is Loss` (Loss flag)
- **Italic note:** `Null audit · date parsing · whitespace trim · duplicate check · documented imputation → documented in data/DATA_DICTIONARY.md`
- Fact to say: 0 duplicates, 0 missing cells, 0 parse failures.

### Slide 6 — Divider 02 · INSIGHT
- **Full navy.** Giant `02`, kicker `INSIGHT`, title `What the evidence shows`, sub `Statistics and an interactive dashboard agree on the same pattern.`

### Slide 7 — KPI snapshot
- **Kicker:** `INSIGHT · KPIS` · **Tag:** `Neyzer · Role 2`
- **Title:** `The business sells $2.30M — but nearly 1 in 5 lines loses money`
- **6 KPI cards:** `$2.30M` Total sales · `$286.4K` Total profit · `12.5%` Profit margin (teal) · `5,009` Orders · `15.6%` Average discount · `18.7%` Loss-making lines (orange)
- **Navy strip:** `The opportunity is not more volume — it is protecting the margin we already earn.`

### Slide 8 — Statistical evidence (Python)
- **Kicker:** `INSIGHT · PYTHON` · **Tag:** `Laura · Role 3`
- **Title:** `Sales are skewed and discount tracks lower profit`
- **Two images side by side:** `distribution_kde.png` (left) + `correlation_heatmap.png` (right)
- **Captions:** left `Distribution of sales is heavily right-skewed: many small orders, few large ones.` · right `Correlation matrix: discount moves against profit — the first warning sign.`

### Slide 9 — Uncertainty & outliers
- **Kicker:** `INSIGHT · UNCERTAINTY` · **Tag:** `Laura · Role 3`
- **Title:** `Confidence bands and outliers keep us honest`
- **Images:** `uncertainty_ci.png` (left) + `boxplot_profit.png` (right)
- **Captions:** left `95% confidence band: the monthly trend is real, not a single-point fluke.` · right `Boxplot of profit by category: Furniture carries the widest downside tail.`

### Slide 10 — Dashboard
- **Kicker:** `INSIGHT · DASHBOARD` · **Tag:** `Neyzer · Role 2`
- **Title:** `The same story, explorable in Power BI`
- **Images:** `dashboard_executive_overview.png` (left) + `dashboard_drilldown.png` (right)
- **Captions:** left `Executive Overview: KPIs, map, trend, sales by category, slicers.` · right `Operational Drill-Down: Category → Sub-Category → Product, discount vs profit.`

### Slide 11 — Divider 03 · CONFLICT
- **Full navy.** Giant `03`, kicker `CONFLICT`, title `The profit leak has a name: discounting`, sub `86.7% of all losses come from order lines discounted above 20%.`

### Slide 12 — The discount paradox (HERO)
- **Kicker:** `CONFLICT · CORE ANOMALY` · **Tag:** `Josmar · Role 4`
- **Title:** `Discounts above 20% turn profit negative`
- **Big image:** `insight_discount_margin.png` (left, ~60% width)
- **Right rail** titled `AT A GLANCE`:
  - `+29.5%` margin with no discount (teal)
  - `−10.0%` margin at 21–30% discount (orange)
  - `96.8%` of >20% lines lose money (orange)
  - `$135.4K` lost on >20% discount lines (orange)

### Slide 13 — Where losses live
- **Kicker:** `CONFLICT · CONCENTRATION` · **Tag:** `Josmar · Role 4`
- **Title:** `Furniture and three sub-categories carry the damage`
- **Left top:** `insight_category_margin.png` · **Left bottom:** `insight_loss_subcategories.png`
- **Right:** `insight_loss_donut.png` (18.7% loss rate)
- **Callout:** `Furniture = 32% of sales, only 6% of profit.`

### Slide 14 — Divider 04 · RESOLUTION
- **Full navy.** Giant `04`, kicker `RESOLUTION`, title `Three decisions that protect margin`, sub `Ranked by profit impact and feasibility, each grounded in the data.`

### Slide 15 — Recommendations
- **Kicker:** `RESOLUTION · ACTIONS` · **Tag:** `Josmar · Role 4`
- **Title:** `Three actions, each with evidence and impact`
- **3 rows**, each with a numbered colored block, a title, a body, and an "EXPECTED IMPACT" box:
  1. `01` **Cap discounts by sub-category** — Require approval for any discount above 20%; above 30% is almost always a loss. → *Addresses $135K of losses (86.7% of the total).* (orange)
  2. `02` **Fix or exit loss-making sub-categories** — Reprice or delist Tables (−$17.7K) and Bookcases (−$3.5K); review Supplies. → *Turns the three worst sub-categories profitable.* (orange)
  3. `03` **Scale the profitable mix** — Grow high-margin Home Office (14%) and West region (15%) playbook. → *Grows revenue without diluting margin.* (teal)

### Slide 16 — Impact & monitoring
- **Kicker:** `RESOLUTION · IMPACT` · **Tag:** `Josmar · Role 4`
- **Title:** `What changes if we act — and how we track it`
- **Left panel** `THE PRIZE`: big `$156K` (orange) "of annual profit currently lost"; `Recovering even half` → `≈ $78K` (teal) → `moves the overall margin from 12.5% toward ~16% — without selling a single extra unit.`
- **Right column** `CONTINUOUS MONITORING` (teal bars):
  - Weekly KPI review — Sales, profit, margin, loss rate on the dashboard.
  - Discount guardrail — Alert when a sub-category's avg discount > 20%.
  - Sub-category watchlist — Track Tables, Bookcases, Supplies monthly.
  - Region / segment mix — Protect West & Home Office margins while scaling.

### Slide 17 — QA & reproducibility
- **Kicker:** `TRUST · QA` · **Tag:** `Jesus · Role 5`
- **Title:** `The story is only as good as the pipeline behind it`
- **4 cards:** `0-baseline` (Every bar chart starts at zero — no visual distortion.) · `Colorblind-safe` (Blue/orange & Viridis; no red-green encoding.) · `Reproducible` (Notebook runs Restart & Run All; script reruns cleanly.) · `Consistent` (Dashboard and notebook read the same processed CSV.)
- **Navy strip:** `Clean data → correct visuals → a recommendation you can defend.`
- **Italic:** `Repository: github.com/alejandr003/db-knowledge-extraction-final · Public access verified`

### Slide 18 — Closing
- **Full navy**, orange left bar.
- **Kicker:** `THE BOTTOM LINE`
- **Title:** `The risk is not too few sales.` / `It is too much discount.` (white, bold)
- **Orange rule** + line: `Cap discounts above 20%, fix the loss-making sub-categories, and scale the profitable mix.`
- `Thank you — we are happy to take questions.`
- `Edwing · Neyzer · Laura · Josmar · Jesus` + `Database Knowledge Extraction · Final Project · November 24, 2026`

---

## 3. Publish checklist (Canva)

1. **Share → See all → Anyone with the link → Can view.**
2. Copy the link and paste it into `presentation/LINKS.md` (row "Executive deck (Canva)").
3. Open the link in an **incognito window** to confirm it opens without login.
4. Optional: **Present → Presenter view** to check speaker notes; download a **PDF backup** to a USB drive.

---

## 4. Image inventory (already in `presentation/assets/`)

| File | Used on slide |
|------|---------------|
| `distribution_kde.png` | 8 |
| `correlation_heatmap.png` | 8 |
| `uncertainty_ci.png` | 9 |
| `boxplot_profit.png` | 9 |
| `dashboard_executive_overview.png` | 10 |
| `dashboard_drilldown.png` | 10 |
| `insight_discount_margin.png` | 12 (hero) |
| `insight_category_margin.png` | 13 |
| `insight_loss_subcategories.png` | 13 |
| `insight_loss_donut.png` | 13 |
