import streamlit as st
from src.MontyHall import MontyHall

st.title("Monty Hall Simulation")

main_column = st.columns(1)[0]
col1, col2, col3 = st.columns(3)

main_column.image("monty-hall.png", width=400, )
num_simulations = main_column.slider(":blue[Number of simulations]", min_value=1, max_value=10000, value=1000)
keep = col2.radio(":blue[keep]", ["Yes", "NO"], horizontal=True)
keep = True if keep == "Yes" else False

if col2.button("Run Simulation"):
    chart = st.line_chart(x=None, y=None, height=300, width=1000)
    win_count = 0
    for iter_count, s in enumerate(MontyHall(num_simulations, keep=keep)) :
        win_count += int(s)

        if iter_count%100 == 0 : # it's too heavy to update the chart each time, so we do it every 100 times
            chart.add_rows([win_count / (iter_count+1)])
