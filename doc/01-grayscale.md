# Un premier pas : les niveaux de gris

Afin de tester la faisabilité de notre projet, nous avons commencé par créer une application permettant de tester notre concept dans un dommaine simplifié, les niveaux de gris.

En prenant, ici, une seule valeur par pixel, on simplifie l'espace RGB en un espace à une seule dimension. On peut alors appliquer naïvement nos traitements sur ces valeurs afin d'obtenir un résultat pouvant ou non valider notre concept avant de passer à des images en couleurs.

## Principe et implémentation

Chaque pixel de chaque image sera représenté par un objet `p1d` servant uniquement à acceuillir une valeur de pixel ainsi que ses coordonnées dans l'image.

Ensuite, nous allons crééer, pour chaque image, un tableau de `p1d` contenant tous les pixels de l'image. Chaque tableau sera ensuite trié par ordre croissant de valeur de pixel. Nous pourrons alors associer chaque pixel d'une image à un unique pixel de la seconde en fonction de leur position dans le tableau trié : le premier pixel de l'image 1 sera associé au premier pixel de l'image 2, le second au second, etc.

- [cf. `01-grayscale.py`](../src/01-grayscale.py)
- [cf. `arr1d.py`](../src/arr1d.py)

## Analyse et résultats

Globalement, le résultat est satisfaisant. Les images obtenues conservent bien la répartition des niveaux de gris de l'image source tout en adoptant la répartition des niveaux de gris de l'image cible. Cependant, cette méthode n'est applicable qu'à des images en niveaux de gris. Il nous faudra trouver un moyen de transposer ce concept à des images en couleurs.
