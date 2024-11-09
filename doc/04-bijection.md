# Bijection entre deux nuages de points

A partir d'ici, nous sortons du projet initial donné en cours et nous nous lançons dans une idée qui m'était venue naturellement durant la découverte du sujet.

Mon idée était de trouver une bijection entre deux nuages de points. C'est à dire que pour chaque point du premier nuage, on lui associe un point du second nuage et réciproquement. Pour cela, j'ai décidé d'associer les points ayant la distance la plus courte entre eux, afin de minimiser la somme des distances des points dans l'espace des couleurs.

## Principe et implémentation

Afin de réaliser cette bijection, j'ai décidé d'utiliser une matrice de distance. Cette matrice est une matrice carrée de taille `n x m` où `n` est le nombre de points du premier nuage et `m` est le nombre de points du second nuage. Chaque élément de la matrice est la distance entre les deux points associés.

Pour associer deux points entre eux, il suffit de trouver le minimum de la matrice et d'associer le `i`-ème point du premier nuage avec le `j`-ème point du second nuage. Ensuite, on rempli la ligne `i` et la colonne `j` de la matrice avec des valeurs infinies pour ne pas les reprendre en compte. Enfin, on réitère l'opération jusqu'à ce que tous les points aient été associés.

- [cf. `04-bijection.py`](../src/04-bijection.py)
- [cf. `arr3d.py`](../src/arr3d.py)

## Analyse et résultats

Les resultats par cette méthode sont satisfaisants sur de petites images mais le temps de calcul devient très long et nécessite une grande quantité de mémoire pour pouvoir traiter des images de taille moyenne. 
