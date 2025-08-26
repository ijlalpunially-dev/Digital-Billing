import streamlit as st

# Page config
st.set_page_config(page_title="Digital Billing App", page_icon="💡", layout="centered")

st.title("💡 Digital Billing App")

# Cost per unit (you can change this value)
COST_PER_UNIT = 10  # Example: 10 Rs per unit

# Inputs
meter_reading = st.number_input("Enter Meter Reading (Units Consumed):", min_value=0, step=1)
fine = st.number_input("Enter Fine Amount (if any):", min_value=0, step=1)

# Calculate bill
total_cost = (meter_reading * COST_PER_UNIT) + fine

# Show results
st.subheader("📑 Billing Details")
st.write(f"Cost per Unit: **{COST_PER_UNIT} Rs**")
st.write(f"Units Consumed: **{meter_reading}**")
st.write(f"Fine: **{fine} Rs**")
st.success(f"💰 Total Bill: **{total_cost} Rs**")
