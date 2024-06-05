import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pandas.read_csv("data.csv")


# Mapear las categorías a números
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# Definir características y etiquetas
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

# Entrenar el clasificador de decisión de árbol
dtree = DecisionTreeClassifier()
dtree.fit(X, y)

# Visualizar el árbol de decisión
plt.figure(figsize=(15,10))
tree.plot_tree(dtree, feature_names=features, filled=True)
plt.show()