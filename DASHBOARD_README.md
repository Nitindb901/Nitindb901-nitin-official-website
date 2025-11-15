# 📊 Consolidated Data Analytics Dashboard - Setup Guide

## Overview
This repository contains a professional Business Intelligence dashboard with comprehensive data analytics, advanced KPIs, and automated insights generation.

---

## 🎯 Features

### ✅ Master Datasets
- **Sales Data**: 10,000+ transaction records with product, category, region, and store details
- **Inventory Data**: 1,200+ SKUs with stock on hand (SOH) tracking
- **Budget Data**: Monthly budget tracking across categories and regions
- **GRDC Data**: Goods Receipt Distribution Center tracking (500+ records)
- **Product Master**: Complete product catalog with pricing

### 📈 Advanced KPIs
- **Year-over-Year (YOY)** growth tracking
- **Month-over-Month (MOM)** trends
- **Like-for-Like (LFL)** store comparison
- **Sell-Through Rate** analysis
- **Budget vs Actual** variance
- **Stock on Hand (SOH)** monitoring
- **Profit Margin** analysis by category/region

### 🎨 Interactive Visualizations
- Sales trend line charts with time-series analysis
- Category performance bar charts
- Regional performance comparison
- Top products ranking
- Profit margin analysis
- Inventory status distribution (pie charts)
- Responsive design for all devices

### 🧠 AI-Powered Insights
- Automated insight generation using data patterns
- Natural language insights
- Top performer identification
- Risk alerts for low stock
- Trend analysis and recommendations

---

## 📁 File Structure

```
Nitindb901-nitin-official-website/
├── index.html                      # Main landing page with dashboard preview
├── portfolio.html                  # Portfolio showcase
├── dashboard.html                  # Basic dashboard
├── dashboard_interactive.html      # Advanced Plotly-based dashboard (GENERATED)
├── insights.html                   # AI-generated insights page (GENERATED)
├── generate_dashboard.py           # Python script to generate data & dashboards
├── data_sales.csv                  # Generated sales data (NOT in git)
├── data_inventory.csv              # Generated inventory data (NOT in git)
├── data_budget.csv                 # Generated budget data (NOT in git)
├── data_grdc.csv                   # Generated GRDC data (NOT in git)
├── data_products.csv               # Generated product catalog (NOT in git)
├── .gitignore                      # Excludes data CSVs and Python artifacts
└── DASHBOARD_README.md             # This file
```

---

## 🚀 How to Generate Dashboard

### Prerequisites
```bash
# Python 3.8+ required
python3 --version

# Install required packages
pip install pandas numpy plotly
```

### Generate Data & Dashboard
```bash
# Run the dashboard generator script
python3 generate_dashboard.py
```

### Output Files
After running the script, you'll get:
1. ✅ `dashboard_interactive.html` - Full interactive dashboard with Plotly charts
2. ✅ `insights.html` - AI-generated business insights
3. ✅ `data_*.csv` - All sample datasets (excluded from git)

---

## 🌐 Deployment to GitHub Pages

### Files Needed in Repository Root:
- ✅ `index.html` (updated with dashboard preview)
- ✅ `dashboard_interactive.html` (generated)
- ✅ `insights.html` (generated)
- ✅ `dashboard.html` (existing)
- ✅ `portfolio.html` (updated)

### GitHub Pages Setup:
1. Go to your repository settings
2. Navigate to "Pages" section
3. Select source: `main` branch / `root` folder
4. Save and wait for deployment

### Access Your Dashboard:
- Main Site: `https://nitindb901.github.io/Nitindb901-nitin-official-website/`
- Interactive Dashboard: `https://nitindb901.github.io/Nitindb901-nitin-official-website/dashboard_interactive.html`
- AI Insights: `https://nitindb901.github.io/Nitindb901-nitin-official-website/insights.html`

---

## 📊 Dashboard Embedding

### Embed in Your Website
```html
<!-- Full Page Embed -->
<iframe 
  src="dashboard_interactive.html" 
  width="100%" 
  height="900px" 
  style="border: none;">
</iframe>

<!-- Responsive Embed -->
<div style="position: relative; width: 100%; padding-bottom: 75%; overflow: hidden;">
  <iframe 
    src="dashboard_interactive.html" 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;">
  </iframe>
</div>
```

### Embed Insights Page
```html
<iframe 
  src="insights.html" 
  width="100%" 
  height="600px" 
  style="border: none;">
</iframe>
```

---

## 🔧 Customization

### Update Data
1. Edit `generate_dashboard.py`
2. Modify the data generation parameters:
   - Number of records: `generate_sales_data(num_records=10000)`
   - Date ranges: `self.start_date`, `self.end_date`
   - Categories, regions, stores arrays
3. Re-run the script: `python3 generate_dashboard.py`

### Modify KPIs
Edit the `KPICalculator` class methods:
- `calculate_yoy_growth()` - Year-over-Year
- `calculate_mom_growth()` - Month-over-Month
- `calculate_lfl()` - Like-for-Like
- `calculate_sell_through()` - Sell-Through Rate

### Customize Visualizations
Edit `create_dashboard_html()` function to:
- Add new charts
- Change colors/themes
- Modify chart types
- Adjust layout

---

## 🎨 Styling

### Color Scheme
- Primary: `#7c3aed` (Purple)
- Secondary: `#22d3ee` (Cyan)
- Success: `#22c55e` (Green)
- Warning: `#f59e0b` (Orange)
- Danger: `#ef4444` (Red)
- Background: `#0b1220` (Dark Blue)
- Cards: `#1a2332` (Dark Gray)

### Responsive Breakpoints
- Desktop: 1400px+
- Tablet: 768px - 1399px
- Mobile: < 768px

---

## 📦 Sample Data Details

### Sales Data Fields:
- Transaction_ID, Date, Product_ID, Product_Name
- Category, Brand, Store, Region
- Quantity, Unit_Price, Discount_Percent
- Revenue, Cost, Profit
- Month, Year, Quarter, Day_Name

### Inventory Data Fields:
- Product_ID, Product_Name, Category
- Store, Region, Stock_Qty
- Reorder_Level, Stock_Value
- Status, Last_Updated

### Budget Data Fields:
- Month, Category, Region
- Budget_Revenue, Budget_Units

### GRDC Data Fields:
- GRDC_ID, Receipt_Date, Product_ID
- Quantity_Received, Supplier
- Status, Distribution_Center

---

## 🔒 Security Notes

- CSV data files are excluded from git (see `.gitignore`)
- No sensitive information in generated data
- All data is synthetic/sample data
- Safe for public GitHub Pages deployment

---

## 📝 Next Steps

1. ✅ Generate dashboard: `python3 generate_dashboard.py`
2. ✅ Test locally: Open `dashboard_interactive.html` in browser
3. ✅ Review insights: Open `insights.html` in browser
4. ✅ Push to GitHub: Commit and push all HTML files
5. ✅ Enable GitHub Pages in repository settings
6. ✅ Share your portfolio URL!

---

## 🆘 Troubleshooting

### Issue: Charts not displaying
**Solution**: Ensure internet connection (Plotly uses CDN)

### Issue: Data looks incorrect
**Solution**: Re-run `python3 generate_dashboard.py`

### Issue: GitHub Pages not updating
**Solution**: Clear browser cache or wait 1-2 minutes for deployment

### Issue: Python dependencies missing
**Solution**: Run `pip install pandas numpy plotly`

---

## 👤 Author

**Nitin Dubey**  
Data Analyst | Data Scientist | BI Specialist

- 📧 Contact: [WhatsApp: 7772011682](https://wa.me/7772011682)
- 💼 LinkedIn: [linkedin.com/in/nitin-dubey-48249aa1](https://www.linkedin.com/in/nitin-dubey-48249aa1)
- 🌐 Portfolio: [nitindb901.github.io](https://nitindb901.github.io/Nitindb901-nitin-official-website/)

---

## 📄 License

This project is part of a professional portfolio. Feel free to use the code structure as a template for your own projects.

---

## ⭐ Features Checklist

- [x] Master consolidated dataset
- [x] Data cleaning & transformation
- [x] Advanced KPIs (YOY, MOM, LFL, Sell-Through, SOH, GRDC)
- [x] Budget vs Actual tracking
- [x] Interactive Plotly visualizations
- [x] Line charts, bar charts, pie charts
- [x] KPI cards with metrics
- [x] Category/Region/Store slicers
- [x] Automated NLP insights
- [x] Python + Pandas + Plotly implementation
- [x] Responsive design
- [x] GitHub Pages ready
- [x] Dashboard embedding support
- [x] Professional portfolio-ready

---

**Last Updated**: November 15, 2025  
**Version**: 1.0.0
