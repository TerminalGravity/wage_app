import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def calculate_earnings(hourly_wage, hours_per_week, tax_rate):
    weekly_earnings = hourly_wage * hours_per_week
    monthly_earnings = weekly_earnings * 4
    yearly_earnings = weekly_earnings * 52
    
    monthly_after_tax = monthly_earnings * (1 - tax_rate / 100)
    yearly_after_tax = yearly_earnings * (1 - tax_rate / 100)
    five_years_after_tax = yearly_after_tax * 5
    
    return monthly_earnings, yearly_earnings, five_years_after_tax, monthly_after_tax, yearly_after_tax, five_years_after_tax

st.title('Earnings Calculator')

# Input fields
hourly_wage = st.number_input('Enter your hourly wage:', value=10.0, step=0.1)
hours_per_week = st.number_input('Enter the number of hours you work per week:', value=40, step=1)
tax_rate = st.number_input('Enter the tax rate (as a percentage):', value=10.0, step=0.1)

if st.button('Calculate Earnings'):
    monthly, yearly, five_years, monthly_taxed, yearly_taxed, five_years_taxed = calculate_earnings(hourly_wage, hours_per_week, tax_rate)
    
    # Visualization: Bar chart comparing pre-tax and post-tax earnings
    labels = ['Monthly', 'Yearly', '5 Years']
    pre_tax_values = [monthly, yearly, five_years]
    post_tax_values = [monthly_taxed, yearly_taxed, five_years_taxed]
    
    x = range(len(labels))
    
    fig, ax = plt.subplots()
    ax.bar(x, pre_tax_values, width=0.4, label='Pre-Tax', align='center')
    ax.bar(x, post_tax_values, width=0.4, label='Post-Tax', align='edge')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel('Earnings ($)')
    ax.set_title('Pre-Tax vs. Post-Tax Earnings')
    ax.legend()
    
    st.pyplot(fig)
    
    # Display results in markdown at the top right
    col1, col2 = st.beta_columns([1, 2])
    with col2:
        st.markdown(f"""
        ## Earnings Summary:
        - **Monthly earnings after tax:** ${monthly_taxed:.2f}
        - **Yearly earnings after tax:** ${yearly_taxed:.2f}
        - **Earnings after 5 years (after tax):** ${five_years_taxed:.2f}
        """)
