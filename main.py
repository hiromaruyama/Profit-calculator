import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Profit Calculator", layout="wide")
# Title and description
st.markdown("<h1 style ='text-align: center;'>Profit Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color:gray'>Adjust costs and target profit to see required price + margins</h4>", unsafe_allow_html=True)
#Create layout
spacer,left, spacer, right, spacer = st.columns([0.2,1,0.2,2,0.2])
with left:
    st.header("Input Parameters")
    unit_price = st.number_input("Unit Price ($): ", min_value=0.0, value=0.0, step=1.0, key="unit_price")
    amount_sold = st.number_input("Units Sold (per month): ", min_value=0.0, value=0.0, step=1.0, key="amount_sold")
    revenue = unit_price * amount_sold
    st.write("Total Revenue: $", f'{revenue:,.2f}')
    st.markdown("<hr style='margin: 1px 0px;'>", unsafe_allow_html=True)

    unit_cogs_price = st.number_input("Unit Cost of Goods Sold (COGS): ", min_value=0.0, value=0.0, step=1.0, key="cogs")
    # Calculate actual COGS
    net_cogs = unit_cogs_price * amount_sold
    st.write("COGS cost: $", f'{net_cogs:,.2f}')
    st.markdown("<hr style='margin: 1px 0px;'>", unsafe_allow_html=True)

    sga = st.number_input("Selling, General & Administrative Expenses (SG&A)", min_value=0.0, value=0.0, step=1.0, key="sga")
    # Calculate actual SG&A
    st.write("SG&A cost: $", f'{sga:,.2f}')
    st.markdown("<hr style='margin: 1px 0px;'>", unsafe_allow_html=True)


    Start=st.button("Calculate Required Price")

    st.markdown("View source code: [GitHub Repository](https://github.com/hiromaruyama/Profit-calculator.git)")


# Calculations 
with right: 
    if Start:
        st.header("Results")
        profit = unit_price * amount_sold - net_cogs - sga
        net_margin = (profit / (unit_price * amount_sold) * 100) if revenue != 0 else 0.0

        st.markdown(f"<div style='font-size:22px;'>Net Profit ($ per month): ${profit:,.2f}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:22px;'>Net Margin (%): {net_margin:,.2f}%</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        wf_labels = ['Revenue', 'COGS', 'SG&A', 'Profit']
        wf_values = [revenue, -net_cogs, -sga, profit]
        bottoms = [0,revenue, revenue - net_cogs, 0]

        # Create waterfall chart with 9 inch width and 4 inch height
        fig, ax = plt.subplots(figsize=(9, 4))

        colors = ["#244FC6", "#E15759","#3EE307", "#EBE407"]

        for i in range(len(wf_values)):
            ax.bar(wf_labels[i], wf_values[i], bottom=bottoms[i], color=colors[i])
        
        ax.set_title("Waterfall Chart: Revenue & Profit")
        ax.axhline(0, color='black', linewidth=0.8)
        ax.set_xlabel("Revenue Breakdown")
        ax.set_ylabel("Amount ($)")
        
        ax.grid(axis='y', alpha = 0.2)
        
        def format_currency(x):
            return f'${x:,.0f}'

        # Revenue
        ax.text(0, wf_values[0]/2,format_currency(revenue), ha='center', va='bottom', fontsize=10)
        #COGS
        ax.text(1, bottoms[1]+wf_values[1]/2, f"-{format_currency(net_cogs)}", ha='center', va='center', fontsize=10)
        #SG&A
        ax.text(2, wf_values[2]/2+bottoms[2], f"-{format_currency(sga)}", ha='center', va='center', fontsize=10)
        
        profit_offset = 0.02*max(abs(profit), 1)
        ax.text(3, wf_values[3]/2+bottoms[3], f"{format_currency(profit)}", ha='center', va='center', fontsize=10)

        st.pyplot(fig)

        
