from wallet_connect import wallet_connect
import streamlit as st
from about import about
from blocks import blocks
from marketplace import marketplace
from collections_ import collections_
from nfts import nfts
from subs import subs


st.set_page_config(
    page_title="DCR Setup Assistant",
    page_icon="❄️️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "This app generates scripts for data clean rooms!"
    }
)


st.sidebar.image("bear_snowflake_hello.png")
action = st.sidebar.radio("What action would you like to take?", ("About", "Blockchains", "Marketplaces", "Collections", "Nfts", "Subcriptions"))

def wallet_con():
    with st.sidebar:
        st.markdown('##')
        wallet = wallet_connect(label="wallet", key='wallet')
        return wallet
    


if action == 'Blockchains':
    blocks()
elif action == 'Marketplaces':
    marketplace()
elif action == 'Collections':
    collections_()
elif action == 'Nfts':
    nfts()
elif action == 'About':
    about()
elif action == 'Subcriptions':
    subs()




wallet = wallet_con()