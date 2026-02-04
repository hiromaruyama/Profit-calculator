# Pricing & Profit Calculator

An interactive **business pricing simulator** built with **Python + Streamlit** that helps users understand how costs, profit targets, and sales volume affect product pricing and margins.

This tool is designed for entrepreneurs, students, and business analysts who want a simple way to model **revenue, costs, and profitability** visually.

**Link to try:** https://profitcalculator-econ.streamlit.app/ 
---

## What This App Does

The calculator allows you to:

- Input product unit price and units sold  
- Input Cost of Goods Sold (COGS)  
- Input SG&A (Selling, General & Administrative) costs   

After clicking, "Calculate", the app automatically calculates:

- **Total Revenue**
- **Total Costs**
- **Profit** (outputs)
- **Net Margin (%)** (outputs)

There is also a **Waterfall Chart** showing Profit after subtracting costs from revenue.

---

## Why This Project Matters

Pricing is one of the most important business decisions. This tool helps users understand:

- How costs impact pricing  
- How margins change with different sales volumes  
- How much profit is realistic  
- The relationship between revenue, expenses, and profit  

It turns abstract business concepts into something **visual and interactive**.

I built this because in school, we had shark tank project. 
I wanted to have a platform where it can calculates whether our product is profitable or not.

---

## 🛠️ Built With

- Python  
- Streamlit (interactive web app)  
- Matplotlib (charts)  
- NumPy / Pandas (calculations & structure)  

---

## 📷 Features

### 1️⃣ Input Panel
Users can adjust:
- Unit Price  
- Units Sold  
- COGS  
- SG&A  
- Target Profit  

### 2️⃣ Real-Time Financial Output

```
Revenue = Price × Units Sold
Profit = Revenue − COGS − SG&A
Net Margin = Profit / Revenue
```

### 3️⃣ Waterfall Visualization

A business-style chart that shows:

**Revenue → COGS → SG&A → Profit**

So users can clearly see how each cost reduces earnings.

---

## 💡 Who This Is For

- Students learning business & finance  
- Entrepreneurs setting product prices  
- Anyone learning Python + data visualization  
- People preparing for business interviews or case studies  

---

## 📈 Example Use Case

If:

- Price = $50  
- Units Sold = 1,000  
- COGS = $15,000  
- SG&A = $10,000  

The app will show:

- Revenue = $50,000  
- Profit = $25,000  
- Margin = 50%  

And visualize how each cost contributes.

