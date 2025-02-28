import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

# Load data
with open("data/foodreportdata.txt", "r") as file:
    data = json.load(file)

def process_data(data):
    records = []
    for entry in data:
        query = entry["query"]
        output = entry["query_output"]
        records.append({
            "Food Item": query["fooditem"],
            "Food Wasted Area": int(query["area_of_food_wasted"]),
            "Total Plate Area": int(query["area_of_plate_total_area"]),
            "Wastage Percentage": float(query["percentage_of_food_wasted"].strip('%')),
            "Meal Time": query["time_of_meal"],
            "Age": int(query["age_of_person"]),
            "Place": query["place_where_food_was_eaten"],
            "Consumer Solution": output["consumer_solution"],
            "Management Solution": output["management_solution"]
        })
    return pd.DataFrame(records)

df = process_data(data)

# Streamlit UI
st.title("Food Wastage Analysis Dashboard")

# Filters
food_item = st.selectbox("Select Food Item", ["All"] + sorted(df["Food Item"].unique().tolist()))
meal_time = st.selectbox("Select Meal Time", ["All"] + sorted(df["Meal Time"].unique().tolist()))
place = st.selectbox("Select Place", ["All"] + sorted(df["Place"].unique().tolist()))

filtered_df = df.copy()
if food_item != "All":
    filtered_df = filtered_df[filtered_df["Food Item"] == food_item]
if meal_time != "All":
    filtered_df = filtered_df[filtered_df["Meal Time"] == meal_time]
if place != "All":
    filtered_df = filtered_df[filtered_df["Place"] == place]

st.write("### Food Waste Data")
st.dataframe(filtered_df)

# Visualization
st.write("### Wastage Percentage Distribution")
fig, ax = plt.subplots()
ax.hist(filtered_df["Wastage Percentage"], bins=10, color='skyblue', edgecolor='black')
ax.set_xlabel("Wastage Percentage")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Solutions
st.write("### Suggested Solutions")
for _, row in filtered_df.iterrows():
    st.subheader(row["Food Item"])
    st.write("**Consumer Solution:**", row["Consumer Solution"])
    st.write("**Management Solution:**", row["Management Solution"])
