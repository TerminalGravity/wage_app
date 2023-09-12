import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def calculate_earnings(hourly_wage, hours_per_week, tax_rate):
    weekly_earnings = hourly_wage * hours_per_week
    monthly_earnings = weekly_earnings * 4
    yearly_earnings = weekly_earnings * 52
    
    monthly_after_tax = monthly_earnings * (1 - tax_rate / 100)
    yearly_after_tax = yearly_earnings * (1 - tax_rate / 100)
    five_years_after_tax = yearly_after_tax * 5
    
    return monthly_earnings, yearly_earnings, five_years_after_tax, monthly_after_tax, yearly_after_tax, five_years_after_tax

def format_large_number(num):
    if num >= 1_000_000:
        return f"${num / 1_000_000:.2f}m"
    elif num >= 1_000:
        return f"${num / 1_000}k"
    else:
        return f"${num}"

def enhanced_bar_chart(pre_tax_values, post_tax_values, labels):
    x = range(len(labels))
    
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#6A0572')
    ax.set_facecolor('purple')
    ax.set_facecolor((0, 0, 0, 0))
    ax.axhspan(0, max(pre_tax_values), facecolor='#4B0082', alpha=0.5)
    ax.axhspan(0, 0, facecolor='#800080', alpha=0.5)
    
    ax.bar(x, pre_tax_values, width=0.4, label='Pre-Tax', align='center', color='#FF5733')
    ax.bar(x, post_tax_values, width=0.4, label='Post-Tax', align='edge', color='#33FF57')
    
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12, fontweight='bold', color='#FF7518', style='italic')
    ax.set_ylabel('Earnings', fontsize=12, fontweight='bold', color='#FF7518', style='italic')
    ax.set_title('💼 Pre-Tax vs. 🌱 Post-Tax Earnings', fontsize=14, fontweight='bold', color='#FF7518', style='italic')
    
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: format_large_number(x)))
    ax.tick_params(axis='both', colors='#FF7518')
    ax.grid(axis='y', linestyle='--', linewidth=0.5, color='#FF7518', alpha=0.6)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#FF7518')
    ax.spines['bottom'].set_color('#FF7518')
    
    ax.legend()
    
    return fig

st.title('💹 Earnings Calculator 🧮')

with st.sidebar:
    st.header('🔧 Settings')
    hourly_wage = st.number_input('💰 Enter your hourly wage:', value=10.0, step=0.1)
    hours_per_week = st.number_input('⏰ Hours you work per week:', value=40, step=1)
    tax_rate = st.number_input('📊 Tax rate (in %):', value=10.0, step=0.1)
    calculate_button = st.button('🚀 Calculate Earnings')

if calculate_button:
    monthly, yearly, five_years, monthly_taxed, yearly_taxed, five_years_taxed = calculate_earnings(hourly_wage, hours_per_week, tax_rate)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        # 📢 Earnings Summary:
        - **Monthly:** 💸 <span style="color:#FF5733; font-size:24px; font-style:italic">{format_large_number(monthly_taxed)}</span>
        - **Yearly:** 🎉 <span style="color:#FF5733; font-size:24px; font-style:italic">{format_large_number(yearly_taxed)}</span>
        - **5 Years:** 🚀 <span style="color:#FF5733; font-size:24px; font-style:italic">{format_large_number(five_years_taxed)}</span>
        """, unsafe_allow_html=True)
    
    labels = ['📅 Monthly', '🗓 Yearly', '📆 5 Years']
    pre_tax_values = [monthly, yearly, five_years]
    post_tax_values = [monthly_taxed, yearly_taxed, five_years_taxed]
    fig = enhanced_bar_chart(pre_tax_values, post_tax_values, labels)
    st.pyplot(fig)
