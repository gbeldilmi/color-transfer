# Adaptation de la spécification d'histogramme à des images en couleurs

Nous avons vu en cours comment adapter une image en niveaux de gris à une autre en utilisant la spécification d'histogramme. Nous allons ici essayer de transposer cette méthode à des images en couleurs.

Cependant, la spécification d'histogramme telle que nous l'avons vue en cours ne peut pas être directement appliquée à des images en couleurs. En effet, la spécification d'histogramme consiste à modifier les valeurs des pixels d'une image, qui sont des valeurs correspondant à une seule dimension. Or, dans une image en couleurs, chaque pixel est représenté par trois valeurs, correspondant aux trois composantes de couleur (ici, nous travaillons dans l'espace RGB).

Cette partie consistera à trouver un moyen de transposer la spécification d'histogramme à des images en couleurs.

## Principe et implémentation

Une première interprétation de la spécification d'histogramme pour des images en couleurs pourrait être de reprendre la [méthode utilisée pour les images en niveaux de gris](01-grayscale.md) et de l'appliquer à chaque pixel de l'image (en gardant le lien entre les trois composantes de ces derniers pour ne pas reproduire les résultats de la [deuxième méthode](02-colors.md)).

De cette façon, nous pourrions choisir  de trier les pixels de chaque image selon leur intensité dans chaque composante de couleur (selon un ordre de priorité entre les composantes afin de trier les couleurs plus proches), puis de les associer aux pixels de l'image à traiter en fonction de leur position dans le classement. En appliquant cette méthode à chaque pixel, nous pourrions espérer obtenir une image dont l'histogramme des couleurs serait similaire à celui de l'image de référence.

- [cf. `05-specification.py`](../src/05-specification.py)
- [cf. `arr3d.py`](../src/arr3d.py)

## Analyse et résultats

Les résultats obtenus avec cette méthode sont les plus proches de ce que nous pourrions attendre d'une spécification d'histogramme pour des images en couleurs. Cependant, le résultat diffère selon l'ordre des composantes utilisé pour le tri des pixels, une même combinaison d'images peut donner six résultats différents. Ainsi le choix du meilleur ordre de tri dépendra des images à traiter ainsi que de l'effet recherché, induisant une part de subjectivité de la part de l'utilisateur.
