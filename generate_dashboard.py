#!/usr/bin/env python3
"""
Consolidated Data Analytics Dashboard Generator
Creates professional BI-style dashboard with sample data
Author: Nitin Dubey - Data Analyst & BI Specialist
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

class DashboardDataGenerator:
    """Generate realistic sample datasets for retail analytics"""
    
    def __init__(self):
        self.start_date = datetime(2023, 1, 1)
        self.end_date = datetime(2024, 12, 31)
        self.categories = ['Electronics', 'Clothing', 'Food & Beverage', 'Furniture', 'Home & Kitchen']
        self.regions = ['North', 'South', 'East', 'West', 'Central']
        self.stores = [f'Store_{i:03d}' for i in range(1, 51)]
        self.products = self._generate_products()
        
    def _generate_products(self):
        """Generate product master data"""
        products = []
        product_names = {
            'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch', 'Camera', 'Monitor', 'Keyboard'],
            'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Dress', 'Shoes', 'Sweater', 'Shorts', 'Socks'],
            'Food & Beverage': ['Coffee', 'Tea', 'Snacks', 'Juice', 'Cookies', 'Cereal', 'Pasta', 'Rice'],
            'Furniture': ['Chair', 'Table', 'Sofa', 'Bed', 'Desk', 'Cabinet', 'Shelf', 'Wardrobe'],
            'Home & Kitchen': ['Cookware', 'Utensils', 'Storage', 'Decor', 'Bedding', 'Curtains', 'Towels', 'Appliances']
        }
        
        product_id = 1
        for category, items in product_names.items():
            for item in items:
                products.append({
                    'Product_ID': f'P{product_id:05d}',
                    'Product_Name': f'{item} - {random.choice(["Pro", "Plus", "Elite", "Premium", "Standard"])}',
                    'Category': category,
                    'Brand': random.choice(['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE']),
                    'Unit_Price': round(random.uniform(10, 1000), 2),
                    'Cost_Price': None  # Will be calculated
                })
                product_id += 1
        
        df = pd.DataFrame(products)
        df['Cost_Price'] = (df['Unit_Price'] * random.uniform(0.6, 0.8)).round(2)
        return df
    
    def generate_sales_data(self, num_records=10000):
        """Generate sales transaction data"""
        dates = pd.date_range(start=self.start_date, end=self.end_date, freq='D')
        
        sales_data = []
        for _ in range(num_records):
            date = random.choice(dates)
            product = self.products.sample(1).iloc[0]
            quantity = random.randint(1, 20)
            discount = random.choice([0, 0.05, 0.10, 0.15, 0.20])
            
            sales_data.append({
                'Transaction_ID': f'TXN{len(sales_data)+1:08d}',
                'Date': date,
                'Product_ID': product['Product_ID'],
                'Product_Name': product['Product_Name'],
                'Category': product['Category'],
                'Brand': product['Brand'],
                'Store': random.choice(self.stores),
                'Region': random.choice(self.regions),
                'Quantity': quantity,
                'Unit_Price': product['Unit_Price'],
                'Discount_Percent': discount,
                'Revenue': round(quantity * product['Unit_Price'] * (1 - discount), 2),
                'Cost': round(quantity * product['Cost_Price'], 2)
            })
        
        df = pd.DataFrame(sales_data)
        df['Profit'] = df['Revenue'] - df['Cost']
        df['Month'] = df['Date'].dt.to_period('M')
        df['Year'] = df['Date'].dt.year
        df['Quarter'] = df['Date'].dt.quarter
        df['Day_Name'] = df['Date'].dt.day_name()
        
        return df
    
    def generate_inventory_data(self):
        """Generate Stock on Hand (SOH) data"""
        inventory = []
        for _, product in self.products.iterrows():
            for store in random.sample(self.stores, random.randint(20, 40)):
                stock_qty = random.randint(0, 500)
                reorder_level = random.randint(20, 100)
                
                inventory.append({
                    'Product_ID': product['Product_ID'],
                    'Product_Name': product['Product_Name'],
                    'Category': product['Category'],
                    'Store': store,
                    'Region': random.choice(self.regions),
                    'Stock_Qty': stock_qty,
                    'Reorder_Level': reorder_level,
                    'Stock_Value': round(stock_qty * product['Unit_Price'], 2),
                    'Status': 'Out of Stock' if stock_qty == 0 else ('Low Stock' if stock_qty < reorder_level else 'In Stock'),
                    'Last_Updated': datetime.now()
                })
        
        return pd.DataFrame(inventory)
    
    def generate_budget_data(self):
        """Generate Budget vs Actual data"""
        months = pd.period_range(start='2024-01', end='2024-12', freq='M')
        budget_data = []
        
        for month in months:
            for category in self.categories:
                budget = random.uniform(50000, 200000)
                budget_data.append({
                    'Month': month,
                    'Category': category,
                    'Region': random.choice(self.regions),
                    'Budget_Revenue': round(budget, 2),
                    'Budget_Units': int(budget / random.uniform(50, 150))
                })
        
        return pd.DataFrame(budget_data)
    
    def generate_grdc_data(self):
        """Generate GRDC (Goods Receipt Distribution Center) tracking data"""
        grdc_data = []
        for i in range(500):
            receipt_date = self.start_date + timedelta(days=random.randint(0, 700))
            product = self.products.sample(1).iloc[0]
            quantity = random.randint(100, 1000)
            
            grdc_data.append({
                'GRDC_ID': f'GRDC{i+1:06d}',
                'Receipt_Date': receipt_date,
                'Product_ID': product['Product_ID'],
                'Product_Name': product['Product_Name'],
                'Category': product['Category'],
                'Quantity_Received': quantity,
                'Supplier': random.choice(['Supplier_A', 'Supplier_B', 'Supplier_C', 'Supplier_D']),
                'Status': random.choice(['Received', 'In Transit', 'Pending', 'Delivered']),
                'Distribution_Center': random.choice(['DC_North', 'DC_South', 'DC_East', 'DC_West'])
            })
        
        return pd.DataFrame(grdc_data)

class KPICalculator:
    """Calculate advanced KPIs and metrics"""
    
    @staticmethod
    def calculate_yoy_growth(df, metric_col, date_col='Date'):
        """Calculate Year-over-Year growth"""
        df_copy = df.copy()
        df_copy['Year'] = pd.to_datetime(df_copy[date_col]).dt.year
        yearly = df_copy.groupby('Year')[metric_col].sum()
        yoy = ((yearly.pct_change() * 100).round(2))
        return yoy
    
    @staticmethod
    def calculate_mom_growth(df, metric_col, date_col='Date'):
        """Calculate Month-over-Month growth"""
        df_copy = df.copy()
        df_copy['Month'] = pd.to_datetime(df_copy[date_col]).dt.to_period('M')
        monthly = df_copy.groupby('Month')[metric_col].sum()
        mom = ((monthly.pct_change() * 100).round(2))
        return mom
    
    @staticmethod
    def calculate_lfl(current_df, previous_df, store_col='Store', metric_col='Revenue'):
        """Calculate Like-for-Like (LFL) growth"""
        current_stores = set(current_df[store_col].unique())
        previous_stores = set(previous_df[store_col].unique())
        common_stores = current_stores.intersection(previous_stores)
        
        current_lfl = current_df[current_df[store_col].isin(common_stores)][metric_col].sum()
        previous_lfl = previous_df[previous_df[store_col].isin(common_stores)][metric_col].sum()
        
        lfl_growth = ((current_lfl - previous_lfl) / previous_lfl * 100) if previous_lfl > 0 else 0
        return round(lfl_growth, 2)
    
    @staticmethod
    def calculate_sell_through(sales_df, inventory_df):
        """Calculate Sell-Through Rate"""
        sold = sales_df.groupby('Product_ID')['Quantity'].sum()
        stock = inventory_df.groupby('Product_ID')['Stock_Qty'].sum()
        
        combined = pd.DataFrame({'Sold': sold, 'Stock': stock}).fillna(0)
        combined['Sell_Through_Rate'] = (combined['Sold'] / (combined['Sold'] + combined['Stock']) * 100).round(2)
        return combined

class InsightGenerator:
    """Generate automated insights from data"""
    
    @staticmethod
    def generate_insights(sales_df, inventory_df, budget_df):
        """Generate NLP-style insights"""
        insights = []
        
        # Revenue insights
        total_revenue = sales_df['Revenue'].sum()
        avg_transaction = sales_df['Revenue'].mean()
        insights.append(f"💰 Total revenue generated: ${total_revenue:,.2f} with average transaction value of ${avg_transaction:,.2f}")
        
        # Top performing category
        category_sales = sales_df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
        top_category = category_sales.index[0]
        top_category_revenue = category_sales.iloc[0]
        insights.append(f"🏆 Top performing category: {top_category} with ${top_category_revenue:,.2f} in revenue ({(top_category_revenue/total_revenue*100):.1f}% of total)")
        
        # Regional performance
        region_sales = sales_df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
        top_region = region_sales.index[0]
        insights.append(f"🌍 Best performing region: {top_region} region contributing ${region_sales.iloc[0]:,.2f}")
        
        # Inventory insights
        low_stock_count = len(inventory_df[inventory_df['Status'] == 'Low Stock'])
        out_of_stock_count = len(inventory_df[inventory_df['Status'] == 'Out of Stock'])
        insights.append(f"⚠️ Inventory Alert: {low_stock_count} products with low stock, {out_of_stock_count} products out of stock")
        
        # Profit margin
        total_profit = sales_df['Profit'].sum()
        profit_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0
        insights.append(f"📊 Overall profit margin: {profit_margin:.2f}% with total profit of ${total_profit:,.2f}")
        
        # Month-over-month trend
        monthly_revenue = sales_df.groupby('Month')['Revenue'].sum()
        if len(monthly_revenue) >= 2:
            latest_growth = ((monthly_revenue.iloc[-1] - monthly_revenue.iloc[-2]) / monthly_revenue.iloc[-2] * 100)
            trend = "increasing" if latest_growth > 0 else "decreasing"
            insights.append(f"📈 Sales trend: Revenue is {trend} by {abs(latest_growth):.1f}% compared to previous month")
        
        # Brand performance
        brand_sales = sales_df.groupby('Brand')['Revenue'].sum().sort_values(ascending=False)
        top_brand = brand_sales.index[0]
        insights.append(f"🏅 Leading brand: {top_brand} with ${brand_sales.iloc[0]:,.2f} in sales")
        
        # Days of week analysis
        dow_sales = sales_df.groupby('Day_Name')['Revenue'].mean().sort_values(ascending=False)
        best_day = dow_sales.index[0]
        insights.append(f"📅 Peak sales day: {best_day} with average revenue of ${dow_sales.iloc[0]:,.2f}")
        
        return insights

def create_dashboard_html(sales_df, inventory_df, budget_df, grdc_df, insights):
    """Create enhanced interactive dashboard with Plotly"""
    
    # Calculate KPIs
    total_revenue = sales_df['Revenue'].sum()
    total_profit = sales_df['Profit'].sum()
    total_orders = len(sales_df)
    stock_value = inventory_df['Stock_Value'].sum()
    low_stock_items = len(inventory_df[inventory_df['Status'] == 'Low Stock'])
    
    # Create subplots
    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=('Sales Trend Over Time', 'Sales by Category', 
                       'Top 10 Products by Revenue', 'Regional Performance',
                       'Profit Margin by Category', 'Inventory Status Distribution'),
        specs=[[{'type': 'scatter'}, {'type': 'bar'}],
               [{'type': 'bar'}, {'type': 'bar'}],
               [{'type': 'bar'}, {'type': 'pie'}]],
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )
    
    # 1. Sales Trend
    daily_sales = sales_df.groupby('Date')['Revenue'].sum().reset_index()
    fig.add_trace(
        go.Scatter(x=daily_sales['Date'], y=daily_sales['Revenue'], 
                  mode='lines', name='Daily Revenue', 
                  line=dict(color='#22d3ee', width=2),
                  fill='tozeroy', fillcolor='rgba(34, 211, 238, 0.1)'),
        row=1, col=1
    )
    
    # 2. Sales by Category
    category_sales = sales_df.groupby('Category')['Revenue'].sum().sort_values(ascending=True)
    fig.add_trace(
        go.Bar(x=category_sales.values, y=category_sales.index, 
              orientation='h', name='Category Sales',
              marker=dict(color='#7c3aed')),
        row=1, col=2
    )
    
    # 3. Top Products
    product_sales = sales_df.groupby('Product_Name')['Revenue'].sum().sort_values(ascending=False).head(10)
    fig.add_trace(
        go.Bar(x=product_sales.values, y=product_sales.index,
              orientation='h', name='Top Products',
              marker=dict(color='#22c55e')),
        row=2, col=1
    )
    
    # 4. Regional Performance
    region_sales = sales_df.groupby('Region')['Revenue'].sum().sort_values()
    fig.add_trace(
        go.Bar(x=region_sales.values, y=region_sales.index,
              orientation='h', name='Regional Sales',
              marker=dict(color='#f59e0b')),
        row=2, col=2
    )
    
    # 5. Profit Margin by Category
    category_metrics = sales_df.groupby('Category').agg({'Revenue': 'sum', 'Profit': 'sum'}).reset_index()
    category_metrics['Profit_Margin'] = (category_metrics['Profit'] / category_metrics['Revenue'] * 100)
    fig.add_trace(
        go.Bar(x=category_metrics['Profit_Margin'], y=category_metrics['Category'],
              orientation='h', name='Profit Margin %',
              marker=dict(color='#06b6d4')),
        row=3, col=1
    )
    
    # 6. Inventory Status
    status_counts = inventory_df['Status'].value_counts()
    fig.add_trace(
        go.Pie(labels=status_counts.index, values=status_counts.values,
              marker=dict(colors=['#22c55e', '#f59e0b', '#ef4444'])),
        row=3, col=2
    )
    
    # Update layout
    fig.update_layout(
        title_text="<b>Comprehensive Business Intelligence Dashboard</b>",
        title_font_size=24,
        title_x=0.5,
        showlegend=False,
        height=1400,
        template='plotly_dark',
        paper_bgcolor='#0b1220',
        plot_bgcolor='#1a2332',
        font=dict(color='#e6edf3')
    )
    
    # Update axes
    fig.update_xaxes(showgrid=True, gridcolor='#2b3b56')
    fig.update_yaxes(showgrid=True, gridcolor='#2b3b56')
    
    return fig

def create_insights_html(insights):
    """Create insights HTML page"""
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Business Insights | Nitin Dubey</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body, html {{ 
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
      background: #0b1220; 
      color: #e6edf3;
      min-height: 100vh;
    }}
    .nav {{ 
      position: sticky; 
      top: 0; 
      background: rgba(0,0,0,0.8); 
      backdrop-filter: blur(10px);
      padding: 12px 0; 
      z-index: 100; 
      border-bottom: 1px solid #1f2a40;
    }}
    .nav-inner {{ 
      display: flex; 
      justify-content: space-between; 
      align-items: center; 
      max-width: 1400px; 
      margin: 0 auto; 
      padding: 0 20px;
    }}
    .brand {{ 
      font-weight: bold; 
      background: linear-gradient(135deg, #7c3aed, #3b82f6); 
      padding: 10px 16px; 
      border-radius: 8px; 
      color: white; 
      text-decoration: none;
      font-size: 18px;
    }}
    .links a {{ 
      color: #9da7b3; 
      margin-left: 20px; 
      text-decoration: none;
      transition: color 0.2s;
    }}
    .links a:hover, .links a.active {{ color: white; }}
    
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 40px 20px;
    }}
    
    h1 {{
      font-size: 36px;
      background: linear-gradient(90deg, #a78bfa, #22d3ee);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      margin-bottom: 30px;
      text-align: center;
    }}
    
    .insight-card {{
      background: linear-gradient(135deg, #1a2332 0%, #0e1626 100%);
      border: 1px solid #2b3b56;
      border-radius: 12px;
      padding: 25px;
      margin-bottom: 20px;
      position: relative;
      overflow: hidden;
      transition: transform 0.2s;
    }}
    
    .insight-card:hover {{
      transform: translateY(-5px);
    }}
    
    .insight-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: linear-gradient(180deg, #7c3aed, #06b6d4);
    }}
    
    .insight-text {{
      font-size: 18px;
      line-height: 1.6;
      padding-left: 15px;
    }}
    
    .timestamp {{
      text-align: center;
      color: #9da7b3;
      margin-top: 40px;
      font-size: 14px;
    }}
    
    footer {{
      background: #111;
      padding: 20px;
      text-align: center;
      color: #9da7b3;
      margin-top: 50px;
    }}
    
    @media (max-width: 768px) {{
      h1 {{ font-size: 28px; }}
      .insight-text {{ font-size: 16px; }}
    }}
  </style>
</head>
<body>
  <header class="nav">
    <div class="nav-inner">
      <a class="brand" href="./">ND</a>
      <nav class="links">
        <a href="./">Home</a>
        <a href="portfolio.html">Portfolio</a>
        <a href="dashboard.html">Dashboard</a>
        <a class="active" href="insights.html">Insights</a>
        <a href="resume.pdf" download>Resume</a>
      </nav>
    </div>
  </header>

  <div class="container">
    <h1>🧠 Automated Business Insights</h1>
    <p style="text-align: center; color: #9da7b3; margin-bottom: 40px;">
      AI-powered analysis of your business data
    </p>
    
"""
    
    for i, insight in enumerate(insights, 1):
        html += f"""    <div class="insight-card">
      <div class="insight-text">{insight}</div>
    </div>
"""
    
    html += f"""    
    <div class="timestamp">
      Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}
    </div>
  </div>

  <footer>
    <p>© 2025 Nitin Dubey | Automated Business Intelligence</p>
  </footer>
</body>
</html>
"""
    return html

def main():
    """Main function to generate all data and create dashboard"""
    print("🚀 Starting Consolidated Dashboard Generation...")
    print("=" * 60)
    
    # Initialize data generator
    generator = DashboardDataGenerator()
    
    # Generate datasets
    print("\n📊 Generating Sample Datasets...")
    sales_df = generator.generate_sales_data(num_records=10000)
    inventory_df = generator.generate_inventory_data()
    budget_df = generator.generate_budget_data()
    grdc_df = generator.generate_grdc_data()
    
    print(f"✅ Sales Data: {len(sales_df)} records")
    print(f"✅ Inventory Data: {len(inventory_df)} records")
    print(f"✅ Budget Data: {len(budget_df)} records")
    print(f"✅ GRDC Data: {len(grdc_df)} records")
    
    # Save datasets to CSV
    print("\n💾 Saving Datasets...")
    sales_df.to_csv('data_sales.csv', index=False)
    inventory_df.to_csv('data_inventory.csv', index=False)
    budget_df.to_csv('data_budget.csv', index=False)
    grdc_df.to_csv('data_grdc.csv', index=False)
    generator.products.to_csv('data_products.csv', index=False)
    print("✅ All datasets saved as CSV files")
    
    # Calculate KPIs
    print("\n📈 Calculating Advanced KPIs...")
    kpi_calc = KPICalculator()
    
    # YOY Growth
    yoy_revenue = kpi_calc.calculate_yoy_growth(sales_df, 'Revenue')
    print(f"✅ YoY Revenue Growth: {yoy_revenue.iloc[-1]:.2f}%")
    
    # MOM Growth
    mom_revenue = kpi_calc.calculate_mom_growth(sales_df, 'Revenue')
    print(f"✅ MoM Revenue Growth: {mom_revenue.iloc[-1]:.2f}%")
    
    # Sell-Through Rate
    sell_through = kpi_calc.calculate_sell_through(sales_df, inventory_df)
    avg_sell_through = sell_through['Sell_Through_Rate'].mean()
    print(f"✅ Average Sell-Through Rate: {avg_sell_through:.2f}%")
    
    # Generate insights
    print("\n🧠 Generating Automated Insights...")
    insight_gen = InsightGenerator()
    insights = insight_gen.generate_insights(sales_df, inventory_df, budget_df)
    print(f"✅ Generated {len(insights)} insights")
    
    # Create dashboard visualizations
    print("\n🎨 Creating Interactive Dashboard...")
    dashboard_fig = create_dashboard_html(sales_df, inventory_df, budget_df, grdc_df, insights)
    
    # Save dashboard as HTML
    dashboard_fig.write_html(
        'dashboard_interactive.html',
        config={'displayModeBar': True, 'responsive': True}
    )
    print("✅ Interactive dashboard saved as 'dashboard_interactive.html'")
    
    # Create insights page
    print("\n📝 Creating Insights Page...")
    insights_html = create_insights_html(insights)
    with open('insights.html', 'w', encoding='utf-8') as f:
        f.write(insights_html)
    print("✅ Insights page saved as 'insights.html'")
    
    # Print summary
    print("\n" + "=" * 60)
    print("✨ Dashboard Generation Complete!")
    print("=" * 60)
    print("\n📁 Generated Files:")
    print("  • data_sales.csv")
    print("  • data_inventory.csv")
    print("  • data_budget.csv")
    print("  • data_grdc.csv")
    print("  • data_products.csv")
    print("  • dashboard_interactive.html")
    print("  • insights.html")
    print("\n🌐 Next Steps:")
    print("  1. Open dashboard_interactive.html in your browser")
    print("  2. Open insights.html to view automated insights")
    print("  3. All files are ready for GitHub Pages deployment")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
