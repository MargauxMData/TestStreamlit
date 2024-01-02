import streamlit as st
import pandas as pd
import seaborn as sns


st.title('Hello Wilders, welcome to my application!')
st.write("I enjoy to discover streamlit possibilities")

#link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
#df_weather = pd.read_csv(link)

# façon 1 d'afficher :
#st.write(df_weather)

# façon 2 d'afficher : Here we use "magic commands":
#df_weather

# ajouter un graphique avec la bibli de streamlit
#st.line_chart(df_weather['MAX_TEMPERATURE_C'])

#ajouter un graphique avec nos biblis habituelles : matplot, seaborn..
# on ne peut pas utiliser plt.show mais st.pyplot(nom_variable, figure) si c'est avec matplotlib
# pour plotly , la syntaxe est la suivante :  st.plotly_chart()
#viz_correlation = sns.heatmap(df_weather.corr(), 
#center=0,
#cmap = sns.color_palette("vlag", as_cmap=True)
#)

#st.pyplot(viz_correlation.figure)

# on peut aussi faire des calculs depuis un input
name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")
