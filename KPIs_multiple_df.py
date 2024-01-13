
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px

# Fonction pour afficher la page KPI
def afficher_kpi():
    st.title("Catégorie KPI")
    
    # Boutons pour les sous-catégories KPI
    selected_kpi_category = st.radio("Sélectionnez une sous-catégorie KPI", ["Vue globale sur le monde cinématographique","Acteurs", "Directeurs"])

    # Affichage des informations en fonction de la sous-catégorie sélectionnée
    if selected_kpi_category == "Acteurs":
        afficher_kpi_acteurs()
    elif selected_kpi_category == "Directeurs":
        afficher_kpi_directeurs()
    elif selected_kpi_category == "Vue globale sur le monde cinématographique":
        afficher_kpi_global_films()

# Fonction pour afficher la page KPI global
def afficher_kpi_global_films():
    st.title("Vue globale sur le monde cinématographique")
    
    # Ajoutez le code pour afficher les informations spécifiques à la catégorie KPI global
    # ajouter uniquement les commandes qui permettent d'arriver à notre résultat
    df = pd.read_csv("C:/PROJET2/Working/Databases clean/imdb_clean_pays_KPI.tsv")
    df['production_companies_country1'] = df['production_companies_country1'].replace("URSS", "Fédération De Russie")
    
    # quand on arrive au graphique de notre KPI conformément à notre script ipynb, il faut utiliser la méthodo streamlit et plus matplotlib
    fig = px.bar(df['production_companies_country1'].value_counts().reset_index().head(15),
                 title='Répartition du nombre de films produits par pays',
                 text='production_companies_country1', color_continuous_scale='Blues')

    fig.update_layout(title_x=0.5)

    
    # façon 1 d'afficher :
    
    st.plotly_chart(fig)
    
# Fonction pour afficher la page KPI Acteurs
def afficher_kpi_acteurs():
    st.title("Acteurs")
    # Ajoutez le code pour afficher les informations spécifiques à la catégorie KPI Acteurs ici


# Fonction pour afficher la page KPI Directeurs
def afficher_kpi_directeurs():
    st.title("Directeurs")
    # Ajoutez le code pour afficher les informations spécifiques à la catégorie KPI Directeurs ici
    
# Fonction pour afficher la page Homepage
def afficher_homepage():
    st.title("Bienvenue")
    st.write("Ceci est un outil vous permet de vous renseigner sur les tendances du monde cinématographique.")
    st.write("Il vous propose également des recommandations de films suivant vos précédents visionnages.")
# Fonction pour afficher la page Bibliothèque
def afficher_bibliotheque():
    st.title("Recommandations films")
    st.write("Algorithme ici")

# Créer une barre de navigation pour les onglets
tabs = ["Homepage", "KPI", "Bibliothèque"]
selected_tab = st.sidebar.selectbox("Sélectionnez une page", tabs)

# Contenu de la page en fonction de l'onglet sélectionné
if selected_tab == "Homepage":
    afficher_homepage()
elif selected_tab == "KPI":
    afficher_kpi()
elif selected_tab == "Bibliothèque":
    afficher_bibliotheque()
