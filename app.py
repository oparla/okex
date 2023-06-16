import streamlit as st
import websocket
import json
import pandas as pd
import plotly.graph_objects as go

# Fungsi untuk mengirim pesan ke WebSocket
def send_message(ws, message):
    ws.send(json.dumps(message))

# Fungsi untuk memproses pesan yang diterima dari WebSocket
def process_message(ws, message):
    data = json.loads(message)
    pair = data['market']
    price = data['last']

    if pair == 'batidr':
        global bat_prices
        bat_prices.append(price)
    elif pair == 'bcdidr':
        global bcd_prices
        bcd_prices.append(price)

# Callback function saat WebSocket terhubung
def on_open(ws):
    # Subscribe ke pasangan BAT-IDR dan BCD-IDR
    send_message(ws, {'action': 'subscribe', 'channel': 'trades', 'pair': 'batidr'})
    send_message(ws, {'action': 'subscribe', 'channel': 'trades', 'pair': 'bcdidr'})

# Callback function saat pesan diterima dari WebSocket
def on_message(ws, message):
    process_message(ws, message)

# Membuat WebSocket connection ke Indodax
ws = websocket.WebSocketApp('wss://kline.indodax.com/ws/',
                            on_open=on_open,
                            on_message=on_message)

# List untuk menyimpan harga
bat_prices = []
bcd_prices = []

# Membuat layout Streamlit
st.title('Harga Cryptocurrency di Indodax')
st.subheader('BAT (Basic Attention Token) - IDR')
st.subheader('BCD (Bitcoin Diamond) - IDR')

# Membuka WebSocket connection
ws.run_forever()

# Menampilkan grafik harga menggunakan Streamlit
if bat_prices:
    df_bat = pd.DataFrame({'Price': bat_prices})
    df_bat['Time'] = pd.to_datetime('now')

    fig_bat = go.Figure(data=go.Scatter(x=df_bat['Time'], y=df_bat['Price']))
    fig_bat.update_layout(title='Grafik Harga BAT (Basic Attention Token)', xaxis_title='Time', yaxis_title='Price (IDR)')
    st.plotly_chart(fig_bat, use_container_width=True)

if bcd_prices:
    df_bcd = pd.DataFrame({'Price': bcd_prices})
    df_bcd['Time'] = pd.to_datetime('now')

    fig_bcd = go.Figure(data=go.Scatter(x=df_bcd['Time'], y=df_bcd['Price']))
    fig_bcd.update_layout(title='Grafik Harga BCD (Bitcoin Diamond)', xaxis_title='Time', yaxis_title='Price (IDR)')
    st.plotly_chart(fig_bcd, use_container_width=True)
