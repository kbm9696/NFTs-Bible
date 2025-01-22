from io import StringIO
import requests
import streamlit as st
import pandas as pd
import datetime
import altair as alt
import time
import os
from g4f.client import AsyncClient
import asyncio
import sys
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import aiohttp
import asyncio


# if sys.platform.startswith('win'):
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def get_response(url):
    headers = {
    'Content-type': 'application/json', 
    'x-api-key': '2rOpRIb5TEcRLcexOw3Am4cR7SI7r9S2lf7Ahi1r',
}  

    url = f"{url}"
    try:
        response = requests.get(url,auth=None, headers=headers)
        if response.status_code == 200:
            json_response = response.json()
            if json_response:
                return json_response
            else:
                return "Error in API response"
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"




async def chat_bot(prompt):

    client = AsyncClient()
    response = await client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    )
    # response = g4f.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     #model=g4f.models.default,
    #     messages=[{"role": "user", "content": prompt}],
    #     stream=True,
    # )

    return response.choices[0].message.content

@st.cache_resource
def generate_summary(df):
    csv_data_str = df.to_string(index=False)
    prompt = f"Here  blockchain data\n{csv_data_str}\ngive some short summary insights about the data in 6 sentences and major few insights in points. Resposnse should be in english"
    st.write(chat_bot(prompt))

@st.cache_resource
def generate_summary_p(df):
    csv_data_str = df.to_string(index=False)
    prompt = f"Here aptos blockchain data\n{csv_data_str}\ngive some short summary insights about the data in 6 sentences and in points"
    st.write(chat_bot(prompt))



@st.cache_data
def fetch_analytics_data(blockchain, time_range):
    """
    Fetch analytics data from the API with caching.
    """
    url = f'https://api.unleashnfts.com/api/v2/nft/marketplace/analytics?blockchain={blockchain}&time_range={time_range}&sort_by=name&sort_order=desc&offset=0&limit=30'
    response = get_response(url)
    return response["data"]

def marketplace():

   

    # Function to predict future points
    def prepare_dataframe(data_item, trend_column):
        block_dates = data_item["block_dates"]
        trend_data = data_item[trend_column]
        df = pd.DataFrame({"DATE": block_dates, trend_column: trend_data})
        df["DATE"] = pd.to_datetime(df["DATE"])
        return df

    # Function to predict future points
    def predict_trend(df, trend_column, num_points=2):
        df["TIME_NUM"] = df["DATE"].map(pd.Timestamp.timestamp)  # Convert datetime to numerical
        X = df["TIME_NUM"].values.reshape(-1, 1)
        y = df[trend_column].values

        # Fit the Random Forest model
        rf_model = RandomForestRegressor(n_estimators=700, random_state=42)
        rf_model.fit(X, y)

        # Calculate the average interval between data points
        df = df.sort_values("DATE")  # Ensure the data is sorted by date
        intervals = df["TIME_NUM"].diff().dropna()
        avg_interval = intervals.mean()

        # Generate future timestamps
        last_timestamp = df["TIME_NUM"].iloc[-1]
        future_timestamps = [last_timestamp + (i + 1) * avg_interval for i in range(num_points)]
        future_dates = pd.to_datetime(future_timestamps, unit='s')

        # Predict the trend values for future timestamps
        future_predictions = rf_model.predict(np.array(future_timestamps).reshape(-1, 1))

        # Combine the actual and predicted data
        future_df = pd.DataFrame({
            "DATE": future_dates,
            trend_column: future_predictions,
            "TYPE": "Predicted"
        })
        df["TYPE"] = "Actual"
        return pd.concat([df, future_df], ignore_index=True)

    # User input for blockchain
    option = st.selectbox(
        "Select a blockchain:",
        ("ethereum", "polygon", "avalanche", "solana", "binance", "linea", "bitcoin"),
    )

    st.write("You selected:", option)

    st.markdown("##")

    # Fetch data from API
    analytics_15m = fetch_analytics_data(option, "15m")
    analytics_30m = fetch_analytics_data(option, "30m")
    analytics_24h = fetch_analytics_data(option, "24h")

    
    st.markdown("##")

    st.subheader("15 Minute")

    st.dataframe(pd.DataFrame(analytics_15m))

    #generate_summary(pd.DataFrame(analytics_15m))

    st.markdown("##")

    st.subheader("30 Minute")
    st.write(pd.DataFrame(analytics_30m))

    #generate_summary(pd.DataFrame(analytics_30m))

    st.markdown("##")

    st.subheader("24 Hour")
    st.write(pd.DataFrame(analytics_24h))

    #generate_summary(pd.DataFrame(analytics_24h))