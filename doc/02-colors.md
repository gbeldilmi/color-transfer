# Premiers pas en couleur

Après avoir traité les images en niveaux de gris, nous allons maintenant nous intéresser à la couleur. Pour cela, nous allons commencer par une approche simple : répéter le processus [précédent](01-grayscale.md) sur chaque canal de couleur.

## Principe et implémentation

Chaque canal de chaque image sera représenté par un tableau de `p1d` servant à accueillir la valeur de pixel ainsi que ses coordonnées dans l'image.

- [cf. `02-colors.py`](../src/02-colors.py)
- [cf. `arr1d.py`](../src/arr1d.py)

## Analyse et résultats

Nous notons dans les résultats que les images obtenues sont bien en couleur, mais que les couleurs ne sont pas fidèles à l'original. En effet, les canaux de couleur ne sont pas liés entre eux, ce qui entraîne une perte d'information et la création de couleurs qui n'existaient pas dans l'image d'origine.
