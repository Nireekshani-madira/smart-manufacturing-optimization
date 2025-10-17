# Power BI Instructions: Smart Manufacturing Project

This guide explains how to visualize the machine failure predictions using Power BI.

---

## 1. Load Data
1. Open Power BI Desktop.
2. Click **Home → Get Data → Text/CSV**.
3. Select `outputs/predictions.csv`.

---

## 2. Create Charts
- **Failure Distribution**:
  - Use a bar chart.
  - Axis: `predicted_failure`
  - Value: Count of `machine_id`

- **Actual vs Predicted**:
  - Use a clustered column chart.
  - Axis: `machine_id`
  - Values: `failure` and `predicted_failure`

- **Feature Analysis** (Optional):
  - Import `data/processed/processed.csv`.
  - Use scatter or line charts for features like `rpm`, `temperature`, `vibration`.

---

## 3. Refresh
- Whenever `predictions.csv` updates, click **Refresh** in Power BI to update visualizations.

---

## 4. Save & Share
- Save your Power BI report as `.pbix`.
- Share the report or publish to Power BI Service for dashboards.
# Power BI instructions
