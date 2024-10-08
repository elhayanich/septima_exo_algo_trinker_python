import json
from termcolor import colored
import plotly.express as px
import pandas as pd

id_de_la_personne_quon_cherche = 558 #Rui

df = pd.read_json("people.json")
df_geo = df.filter(["id", "first_name", "latitude", "longitude"]).copy()
df_geo["highlight"] = 10
df_geo.loc[df_geo["id"] == id_de_la_personne_quon_cherche, "highlight"] = 100
print(df_geo)


fig = px.scatter_geo(df_geo,
                    lat=df_geo.latitude,
                    lon=df_geo.longitude,
                    hover_name="first_name",
                    color=df_geo.highlight,
                    size=df_geo.highlight)
fig.show()
