import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def plot_battery_usage(log_data):
    df = pd.DataFrame(log_data)  # Simulated or parsed log data
    st.line_chart(df.set_index("timestamp")["battery_level"])
