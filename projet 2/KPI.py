

# Importer les librairies
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px

# Configuration de la page
def set_page_config():
    st.set_page_config(
        page_title="Tableau de bord",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )


# charger et convertir les dates directement en datetime
#@st.cache_data
#def load_data() -> pd.DataFrame:
    #data = pd.read_csv('data/sales_data_sample.csv', encoding='latin1')
    #data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'])
    #return data


#def filter_data(data: pd.DataFrame, column: str, values: List[str]) -> pd.DataFrame:
    #return data[data[column].isin(values)] if values else data


#@st.cache_data
#def calculate_kpis(data: pd.DataFrame) -> List[float]:
    #total_sales = data['SALES'].sum()
    #sales_in_m = f"{total_sales / 1000000:.2f}M"
    #total_orders = data['ORDERNUMBER'].nunique()
    #average_sales_per_order = f"{total_sales / total_orders / 1000:.2f}K"
    #unique_customers = data['CUSTOMERNAME'].nunique()
    #return [sales_in_m, total_orders, average_sales_per_order, unique_customers]

st.title('Quête Streamlit')
st.write('Analyse')
# Charger les données
df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')
st.sidebar.header('Please Filter Here:')
country = st.sidebar.multiselect(
    'Select Country:',
    options=df['continent'].unique(),
    default=df['continent'].unique()
)
