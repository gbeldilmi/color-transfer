# Transfert optimal par tranches

Une autre méthode abordé dans le projet est le transfert optimal par tranches. Cette méthode consiste à s'approcher petit à petit des couleurs de l'image source en déplaçant les pixels de l'image cible. 

## Principe et implémentation

Pour cela, on commence par générer un axe aléatoire dans l'espace RGB, puis on projette les pixels des deux images sur cet axe afin de pouvoir en faire deux listes ordonnées. Ensuite, on calcule pour chaque pixel la distance entre le i-ème pixel de l'image 1 et le i-ème pixel de l'image 2 à l'aide du produit scalaire. Enfin, on déplace chaque pixel de l'image cible en fonction de la distance calculée. On répète ce processus jusqu'à ce que notre condition d'arrêt soit atteinte. Dans notre cas, nous avons trois conditions d'arrêt possibles :

- La distance moyenne entre les pixels des deux images est inférieure à un certain seuil
- Le nombre d'itérations est supérieur à un certain seuil
- Nous sommes arrivés à la fin d'une liste de vecteurs prédéfinis (qui permettent de générer des axes non-aléatoires dans l'espace RGB)

Notons qu'en cas de sortie de l'espace des couleurs, nous ramenons le pixel à l'intérieur de l'espace RGB en le projetant sur le bord de l'espace.

- [cf. `03-transfer.py`](../src/03-transfer.py)
- [cf. `arr3d.py`](../src/arr3d.py)

## Analyse et résultats

Les resultats obtenus avec les deux premières conditions d'arrêt sont assez mitigés, parfois donnant de bons résultats puis d'autres fois des résultats avec des couleurs absentes de l'image source, certains resultats apparaissent aussi avec des couleurs très saturées. Cependant, la troisième condition d'arrêt donne des résultats plus satisfaisants, avec un nombre d'itérations raisonnable (7 vecteurs prédéfinis).

