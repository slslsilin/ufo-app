import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("ufo_sighting_data.csv", parse_dates=["Date_time", "date_documented"])
    return df.dropna(subset=["latitude", "longitude"])

df = load_data()

st.title("🛸 UFO目击分析")
st.sidebar.header("筛选条件")

# 国家筛选
country_list = ["全部"] + sorted(df["country"].dropna().unique().tolist())
selected_country = st.sidebar.selectbox("选择国家", country_list)

# 形状筛选
shape_list = ["全部"] + sorted(df["UFO_shape"].dropna().unique().tolist())
selected_shape = st.sidebar.selectbox("选择形状", shape_list)

# 应用筛选
filtered_df = df.copy()
if selected_country != "全部":
    filtered_df = filtered_df[filtered_df["country"] == selected_country]
if selected_shape != "全部":
    filtered_df = filtered_df[filtered_df["UFO_shape"] == selected_shape]

# 显示地图
st.subheader("目击地点")
st.map(filtered_df[["latitude", "longitude"]].rename(columns={"latitude":"lat", "longitude":"lon"}))
