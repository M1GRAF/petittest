import streamlit as st
st.title("Bienvenue sur mon application moi Malika tchêpo")
st.write("Je suis Malika tchêpo")
age = st.slider("Quel est votre âge ?", 0, 100, 25)
nom = st.text_input("Quel est votre nom ?")
if st.button("Valider"):
    st.write(f"Coucou {nom} !")

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.header("Visualisation de données avec Seaborn")
st.subheader("Voici quelques visualisations de données avec Seaborn")
df = sns.load_dataset("planets")
st.dataframe(df)

fig, ax = plt.subplots()
sns.histplot(df["mass"], kde=True, ax=ax)
st.pyplot(fig)

st.write("Voici le code à taper pour avoir le même graphique :")
st.markdown("""
```python
fig, ax = plt.subplots()
sns.scatterplot(x="distance", y="mass", data=df, ax=ax)
st.pyplot(fig)
```
        """)
fig, ax = plt.subplots()
sns.scatterplot(x="distance", y="mass", data=df, ax=ax)
st.pyplot(fig)


st.markdown("""

- age : 25
- nom : Malika tchêpo     

```python
print("Je suis tchêpo")
```       

            """)