import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import json
from pandas import json_normalize
import matplotlib.dates as mdates


def last_30(moedas):
    result_df = pd.DataFrame()
    ax = None
    for moeda in moedas:
        request = requests.get(f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/30")
        data = json.loads(request.text)
        df = json_normalize(data)
        result_df[f"{moeda} - Valor"] = df['bid'].astype(float)
        result_df[f"{moeda} - Data"] = df['timestamp'].astype(int).apply(lambda x: datetime.fromtimestamp(x).strftime('%d-%m-%Y'))
        result_df[f"{moeda} - Data"] = pd.to_datetime(result_df[f"{moeda} - Data"], infer_datetime_format=True)
        ax = result_df.plot(figsize=(15, 5), x=f"{moeda} - Data", y=f"{moeda} - Valor", xlabel="Data", ylabel="Valor em real",
                       legend="teste", ax=ax)

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))

    plt.gcf().autofmt_xdate()

    plt.show()


def last_15(moedas):
    result_df = pd.DataFrame()
    ax = None
    for moeda in moedas:
        request = requests.get(f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/15")
        data = json.loads(request.text)
        df = json_normalize(data)
        result_df[f"{moeda} - Valor"] = df['bid'].astype(float)
        result_df[f"{moeda} - Data"] = df['timestamp'].astype(int).apply(
            lambda x: datetime.fromtimestamp(x).strftime('%d-%m-%Y'))
        result_df[f"{moeda} - Data"] = pd.to_datetime(result_df[f"{moeda} - Data"], infer_datetime_format=True)
        ax = result_df.plot(figsize=(15, 5), x=f"{moeda} - Data", y=f"{moeda} - Valor", xlabel="Data", ylabel="Valor",
                            legend="teste", ax=ax)

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))

    plt.gcf().autofmt_xdate()

    plt.show()


def date_range(moedas, start_date, end_date):

    result_df = pd.DataFrame()
    ax = None
    for moeda in moedas:
        request = requests.get(f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={start_date}&end_date={end_date}")
        data = json.loads(request.text)
        df = json_normalize(data)
        result_df[f"{moeda} - Valor"] = df['bid'].astype(float)
        result_df[f"{moeda} - Data"] = df['timestamp'].astype(int).apply(
            lambda x: datetime.fromtimestamp(x).strftime('%d-%m-%Y'))
        result_df[f"{moeda} - Data"] = pd.to_datetime(result_df[f"{moeda} - Data"], infer_datetime_format=True)
        ax = result_df.plot(figsize=(15, 5), x=f"{moeda} - Data", y=f"{moeda} - Valor", xlabel="Data", ylabel="Valor",
                            legend="teste", ax=ax)

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))

    plt.gcf().autofmt_xdate()

    plt.show()








