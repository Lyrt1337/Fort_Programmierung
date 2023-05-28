"""
-------------------------
Aufgabenblatt_5 Fort.Prog
Aufgabe 22
Autor: Christian Gilomen
Datum: 17.05.2023
-------------------------
"""
import pandas as pd
import plotly.express as px


def histogram(data='Keywords.txt'):
    # die daten aus dem Keywords.txt file lesen
    df = pd.read_csv(data, sep=':', names=['Keyword', 'Count'], nrows=100)
    figure1 = px.histogram(df, x='Keyword', y='Count', labels={'x': 'Keywords', 'y': 'Counts'}, histfunc='max',
                           color='Count')
    figure1.show()

    # in eine histogramm figur einlesen
    # die figur plotten

    return figure1


histogram()

