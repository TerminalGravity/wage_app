import streamlit as st

def calculate_earnings(hourly_wage, hours_per_week, tax_rate):
    weekly_earnings = hourly_wage * hours_per_week
    monthly_earnings = weekly_earnings * 4
    yearly_earnings = weekly_earnings * 52
    
    monthly_after_tax = monthly_earnings * (1 - tax_rate / 100)
    yearly_after_tax = yearly_earnings * (1 - tax_rate / 100)
    five_years_after_tax = yearly_after_tax * 5
    
    return monthly_after_tax, yearly_after_tax, five_years_after_tax

st.title('Earnings Calculator')

# Input fields
hourly_wage = st.number_input('Enter your hourly wage:', value=10.0, step=0.1)
hours_per_week = st.number_input('Enter the number of hours you work per week:', value=40, step=1)
tax_rate = st.number_input('Enter the tax rate (as a percentage):', value=10.0, step=0.1)

if st.button('Calculate Earnings'):
    monthly, yearly, five_years = calculate_earnings(hourly_wage, hours_per_week, tax_rate)
    
    # Display results
    st.write(f'Monthly earnings after tax: ${monthly:.2f}')
    st.write(f'Yearly earnings after tax: ${yearly:.2f}')
    st.write(f'Earnings after 5 years (after tax): ${five_years:.2f}')
