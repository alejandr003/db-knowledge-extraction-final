# Enterprise Multi-Modal Data Visualization and Storytelling

**Course:** Database Knowledge Extraction
**Project:** Final Project — Enterprise Multi-Modal Data Visualization and Storytelling
**Deadline:** November 24, 2026 · 11:59 PM
**Live presentation:** November 24, 2026 · 10 minutes · all 5 members speaking

This repository is the single source of truth for the team's final project. It combines a
reproducible Python data pipeline, an interactive BI dashboard, programmatic statistical
visualizations, and an executive data story built on the **Setup → Conflict/Insight →
Resolution** framework.

---

## Team roster and ownership

| # | Role | Member | Owns | Main deliverables |
|---|------|--------|------|-------------------|
| 1 | Data Architect & Wrangler | **Edwing** | `data/`, `src/` | Raw dataset, `clean_data.py`, processed CSV, data dictionary |
| 2 | BI Dashboard Lead | **Neyzer** | `dashboard/` | `.pbix` dashboard, theme, screenshots, dashboard guide |
| 3 | Python Visualization Specialist | **Laura** | `notebooks/`, `assets/plots/` | Executed `final_visualizations.ipynb`, PNG/SVG/HTML assets |
| 4 | Narrative & Data Storytelling Lead | **Josmar** | `presentation/` | Executive deck (PDF/PPTX), Canva link, speaker narrative |
| 5 | QA & Integration Lead | **Jesus** | Root files, `presentation/` | `.gitignore`, `requirements.txt`, `README.md`, links, QA audit, rehearsal |

> Each member should only modify the folders they own. Coordinate in the team chat before
> changing shared files at the repository root.

---

## Repository structure

```text
db-knowledge-extraction-final/
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   │   ├── .gitkeep
│   │   └── superstore_raw.csv                # Role 1 — original dataset (CSV)
│   ├── processed/
│   │   ├── .gitkeep
│   │   └── clean_dataset.csv                 # Role 1 — cleaned dataset (CSV)
│   └── DATA_DICTIONARY.md                    # Role 1 — field definitions and quality log
├── src/
│   └── clean_data.py                         # Role 1 — cleaning and transformation script
├── dashboard/
│   ├── .gitkeep
│   ├── README.md                             # Role 2 — dashboard guide and measures
│   ├── enterprise_dashboard.pbix             # Role 2 — Power BI dashboard
│   ├── theme.json                            # Role 2 — accessible report theme
│   └── screenshots/
│       ├── .gitkeep
│       ├── dashboard_executive_overview.png
│       └── dashboard_drilldown.png
├── notebooks/
│   └── final_visualizations.ipynb            # Role 3 — statistical and interactive visuals
├── assets/
│   └── plots/
│       ├── .gitkeep
│       ├── boxplot_profit.png / .svg
│       ├── correlation_heatmap.png / .svg
│       ├── distribution_kde.png / .svg
│       ├── uncertainty_ci.png / .svg
│       └── interactive_scatter.html
└── presentation/
    ├── LINKS.md                              # Role 4/5 — submission links and access checks
    └── SPEAKER_NOTES.md                      # Role 4/5 — 10-minute script and timing
```

---

## Dataset (CSV used in this project)

The project uses the **Superstore Sales Dataset** as the enterprise dataset for the full
pipeline (cleaning, dashboard, notebook, and storytelling).

| Item | Value |
|------|-------|
| Dataset name | Superstore Sales Dataset |
| Source (Kaggle) | [Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) |
| Raw CSV mirror | [sample-superstore.csv](https://raw.githubusercontent.com/datasets/sample-superstore/master/data/sample-superstore.csv) |
| Raw CSV (repo) | `data/raw/superstore_raw.csv` |
| Processed CSV (repo) | `data/processed/clean_dataset.csv` |
| Original rows / columns | 9,994 rows × 21 columns |
| Processed columns | 27 (includes 6 derived fields) |
| Time range | 2014-01-03 → 2017-12-30 |
| Geographic scope | United States |
| Currency | USD |
| Granularity | One row per order line (product within an order) |

**Field mix (rubric requirement):**

- **Temporal:** `Order Date`, `Ship Date`
- **Continuous:** `Sales`, `Profit`, `Discount`, `Quantity`
- **Categorical:** `Segment`, `Category`, `Sub-Category`, `Ship Mode`
- **Geospatial:** `Country`, `Region`, `State`, `City`, `Postal Code`

**Derived fields added by `src/clean_data.py`:** `Order Year`, `Order Month`,
`Order Quarter`, `Shipping Days`, `Profit Margin`, `Is Loss`.

Full field definitions, null rates, imputation log, and quality checks are documented in
[`data/DATA_DICTIONARY.md`](data/DATA_DICTIONARY.md).

---

## Data pipeline

```text
data/raw/superstore_raw.csv
        │
        ▼
src/clean_data.py  (audit → clean → type casting → imputation)
        │
        ▼
data/processed/clean_dataset.csv
        │
        ├──▶ notebooks/final_visualizations.ipynb  →  assets/plots/*.png / *.svg / *.html
        └──▶ dashboard/enterprise_dashboard.pbix   →  presentation/Executive_Presentation.pdf
```

---

## Quick start

```bash
# 1. Clone the repository
git clone https://github.com/alejandr003/db-knowledge-extraction-final.git
cd db-knowledge-extraction-final

# 2. Create and activate a virtual environment
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS / Linux
# source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the cleaning pipeline (raw CSV already included in this repo)
python src/clean_data.py

# 5. Open the notebook
jupyter notebook notebooks/final_visualizations.ipynb
```

> On Windows, if PowerShell blocks activation, run
> `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first.

---

## How to upload your part

1. **Sync before working** to avoid conflicts:
   ```bash
   git pull --rebase origin main
   ```
2. **Add only your own files** (replace the paths with your deliverables):
   ```bash
   git add data/ src/clean_data.py
   git commit -m "feat(data): add cleaned Superstore dataset and data dictionary"
   git push origin main
   ```
3. **Large deliverables** (`.pbix`, executed notebook, deck PDF) are easier to review through
   a branch and a pull request:
   ```bash
   git checkout -b feature/role-2-dashboard
   git add dashboard/
   git commit -m "feat(dashboard): add executive overview and drill-down pages"
   git push -u origin feature/role-2-dashboard
   ```
   Then open a pull request on GitHub and ask the QA lead (Jesus) to review it.
4. **Never commit** virtual environments, `.ipynb_checkpoints/`, `__pycache__/`, or temp files;
   they are already excluded by `.gitignore`.
5. **Do not overwrite another member's folder.** If a shared file must change, announce it first.

### Suggested commit prefixes

| Prefix | Use |
|--------|-----|
| `feat(role):` | New deliverable or feature |
| `fix(role):` | Correction to an existing deliverable |
| `docs(role):` | Documentation only |
| `chore(repo):` | Repository maintenance (QA lead) |

---

## Deliverables checklist

### Role 1 — Data Architect & Wrangler (Edwing)
- [x] `data/raw/superstore_raw.csv`
- [x] `src/clean_data.py` (documented and runnable)
- [x] `data/processed/clean_dataset.csv`
- [x] `data/DATA_DICTIONARY.md` (types, ranges, null rates, imputation log)

### Role 2 — BI Dashboard Lead (Neyzer)
- [x] `dashboard/enterprise_dashboard.pbix`
- [x] Executive Overview: KPIs, map, time-series trend
- [x] Operational Drill-Down: Category → Sub-Category → Product
- [x] `dashboard/README.md` updated with measures, model, and filters
- [x] `dashboard/theme.json` and dashboard screenshots

### Role 3 — Python Visualization Specialist (Laura)
- [x] `notebooks/final_visualizations.ipynb` executed with markdown commentary
- [x] `assets/plots/distribution_kde.png`
- [x] `assets/plots/correlation_heatmap.png`
- [x] `assets/plots/uncertainty_ci.png`
- [x] `assets/plots/interactive_scatter.html`
- [x] Extra assets: `boxplot_profit.png/svg` and SVG exports

### Role 4 — Narrative & Data Storytelling Lead (Josmar)
- [ ] `presentation/Executive_Presentation.pdf` (or `.pptx`)
- [ ] Setup → Conflict/Insight → Resolution narrative
- [ ] Public Canva/PowerPoint link registered in `presentation/LINKS.md`
- [ ] `presentation/SPEAKER_NOTES.md` completed and rehearsed

### Role 5 — QA & Integration Lead (Jesus)
- [x] Repository structure, `.gitignore`, `requirements.txt`, `README.md`
- [x] PR reviews and merge QA for Roles 1–3
- [x] Public access verified (“Everyone with the link”) — repo público
- [x] Final project preview notebook added (`FINAL_PROJECT_PREVIEW.ipynb`)
- [x] 0-baseline and colorblind-safe palette final audit (static check en notebook/dashboard)
- [x] Notebook reproduces from `Kernel → Restart & Run All` (verificado con nbconvert + scipy)
- [x] `.pbix` opens without broken data-source errors (verificado en Power BI Desktop)

---

## QA checklist (Role 5)

- [x] Every bar/column chart starts strictly at **0** (verificado visualmente en Power BI Desktop).
- [x] Sequential palettes for ordered magnitudes; diverging palettes for profit/loss (verificado visualmente).
- [x] Colorblind-safe choices (Viridis, Blue/Orange); no problematic red-green pairing (verificado visualmente).
- [x] No redundant legends, unnecessary gridlines, or top/right spines (verificado visualmente).
- [x] Notebook runs top-to-bottom with no missing files or hard-coded absolute paths (verificado con nbconvert).
- [x] Dashboard loads with the processed CSV and all pages render (verificado en Power BI Desktop).
- [ ] Deck and repository links open in an incognito window (public access).
- [ ] All 5 members speak for ~2 minutes and the total stays at 10 minutes.

---

## Submission links

All submission URLs, access levels, and verification dates live in
[`presentation/LINKS.md`](presentation/LINKS.md).

---

## Academic use

This repository contains coursework for the Database Knowledge Extraction final project.
Dataset credits belong to the original Kaggle publishers.
