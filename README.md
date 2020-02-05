# Stéréovision

## Hierarchie

![](https://i.imgur.com/MX9LiSn.png)

* `generated/`: n'existe pas initialement et est créé lors de la première calibration.
* `public/`: contient les points d'entré du programme ainsi qu'un fichier de configuration.
* `sources/`: contient les sources du projet.
* `sources/backend`: contient la logique fonctionnelle.
* `sources/camera_system`: contient la logique métier.
* `sources/gui`: contient le code lié à l'interface utilisateur graphique.

## Dépendances

* Python3.7

## Installation

Le logiciel n'a pas été testé sous MacOS. Sous Windows, n'ont été testé que la procédure d'installation et le lancement de l'interface CLI. Linux est vivement conseillé pour utiliser ce programme.


De plus, il est vivement conseillé de faire usage d'un environement virtuel de type [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) ou [pyenv](https://github.com/pyenv/pyenv) pour ségréguer les dépendances du projet des dépendances de l'installation système de Python.

1. Téléchargez ou clonez les sources du projet sur [github](https://github.com/RoscaS/stereovision-he-arc.git).
2. Après décompression de l'archive, ouvrez un terminal à la racine du projet.
3. (optionel) Crééz un nouvel environement virtuel et activez le.
4. Installation des dépendances avec `$ pip install -e .`

## Configuration
Le fichier `public/settings.py` contient les configurations du logiciel. La majorité des valeurs par défaut sont valables mais il est nécessaire d'en adapter certaines:
* `DEVICE`: Les valeurs des champs `left` et `right` correspond à l'id usb qu'occupent vos caméras.
* `CHESSBOARD`:
  * `rows` correspond au nombre de lignes -1 <Note value="en réalité OpenCV compte les intersections et non pas les lignes ou colonnes">nombre de lignes -1</Note>
  * `columns` correspond au nombre de colonnes - 1.
  * `square_size` représente la taille d'un carré en $cm$.


## Utilisation

### CLI

Pour lancer le CLI, À la racine du projet:

```shell
$ python public/stereovision.py
```

![](https://i.imgur.com/Vp8uED1.png)

Les 4 actions possibles sont affichés. Les autres modes ne sont pas visibles car l'application ne détecte pas les fichiers contenant les données de calibration. Avant de lancer la procédure de calibration, il est utile de faire un pré-réglage manuellement des caméras. En pressant la touche "l" (L minuscule) du clavier, des lignes apparaissent:

![](https://i.imgur.com/0pWnNbM.png)


Ces lignes servent à régler grossièrement la position verticale des caméras. Sur la figure précédente, la caméra de gauche devrait être pivotée vers le bas, manuellement.


La figure suivante montre le résultat, après une correction grossière:

![](https://i.imgur.com/60aPOLx.png)

Le système est maintenant prêt à être calibré. Pour ce faire, il est nécessaire de changer de mode pour le mode 2, qui est dédié à la calibration, en pressant sur la touche "2" du clavier:

![](https://i.imgur.com/x1y18hI.png)

Le mode calibration est un mode en deux procédures:
1. Le logiciel va capturer un certain nombre de paires d'images.
2. Le logiciel utilise les images pour déterminer un certain nombre de paramètres, notament les paramètres intrinsèques, les données de distorsion, les matrices fondamentale et essentielle.

Pour effectuer les captures, il est nécessaire de se munir de la mire de calibration et de se balader avec, devant les caméras. Les captures se font automatiquement lors de la détection de la mire dans les deux images. Après une capture, le logiciel laisse 2 secondes à l'utilisateur pour changer de position, avant de recommencer à chercher la mire.


La barre de progression permet de connaitre l'état d'avancement de la procédure:

![](https://i.imgur.com/0xYeZd4.png)

La transition vers la seconde procédure se fait automatiquement lorsque la barre de progression est complète. La seconde procédure ne demande aucune action de l'utilisateur et prend un certain temps pour faire ses calculs:

![](https://i.imgur.com/CTVUHSd.png)

Si la première procédure échoue pour une raison ou pour une autre ou si l'utilisateur souhaite faire une nouvelle calibration, il lui suffit de relancer ce mode.


Une fois les calculs effectués, l'application change automatiquement de mode pour aller dans le numéro 3, c'est à dire le mode distorsion:

![](https://i.imgur.com/oC6TW4x.png)

Dans ce mode il est possible d'afficher les lignes d'aide (touche "l") qui permettent de visualiser la qualité de la rectification ainsi que de la suppression de la distorsion. Pour alterner entre images normales et images réctifiées, il est possible de presser la touche "d".

La touche "4" active le mode depth:

![](https://i.imgur.com/lbfwVRV.png)

Dans ce mode, plus la couleur tend vers le rouge, plus l'objet est proche. Et dans la précédente capture (qui correspond à la scène de la **figure 21**), il est facile de voir que l'objet au premier plan est rouge vif, celui au second jaune et celui dans le 3e bleu clair.


Ce mode offre de nombreuses options qui seront détaillées dans le prochain sous-chapitre:

![](https://i.imgur.com/XsoRzbe.png)

Les dernières lignes de la figure précédente laissent sous entendre qu'il est possible d'obtenir la distance en double cliquant sur un point de l'image. Cette fonctionnalité est expérimentale et est décrite dans le chapitre suivant.


### GUI

Lancer le programme en mode GUI donne accès à une interface graphique. Pour lancer ce mode, à la racine du projet:

```shell
$ python public/stereovision_gui.py
```
![](https://i.imgur.com/G4uvQgR.png)

Dans la GUI, on retrouve les modes de l'application sous forme d'onglets, en haut à gauche. Il y en a un de moins qu'en mode CLI car il n'est pas possible pour le moment de calibrer dans ce mode. Dans chaque onglet, en haut à droite se trouve un bouton pour lancer / stopper la capture. Si une capture est en cours et que l'onglet est changé, la capture cesse automatiquement et doit être relancée dans le nouveau mode. Et finalement, en bas à gauche des images, il y a les différentes options du mode courant, qui sont les mêmes que celles du CLI. Sur la précédente figure, on peut voir un bouton pour activer l'affichage des lignes horizontales d'aide.


Dans l'onglet "Depth", on retrouve l'image résultante du traitement sur les deux caméras qui affiche une carte de profondeur. Par défaut c'est le mode WLS qui est activé et qui propose un filtre particulier qui permet de replaquer le résultat de la carte de profondeur sur une image filtrée:

![](https://i.imgur.com/fAI9GOf.png)

Si on le retire en cliquant sur la radio "Colored", l'image résultante n'est plus traitée avec le filtre WLS et affiche juste une carte de profondeur colorée:

![](https://i.imgur.com/Y4S3brl.png)



Et si on retire la couleur, en cliquant sur la radio "Disparity", il ne reste que la carte de disparité sans aucun traitement autre qu'une normalisation ramenant la disparité maximum à 0.

![](https://i.imgur.com/lYvbRwO.png)

Sur la figure précédente, le mode du blockmatcher a également été changé. Il existe deux modes:

* **SBM** (StereoBlockMatcher): Un mode qui crée des cartes moins riches mais permet d'avoir une image fluide.
* **SGBM**: Un mode qui crée des cartes disparité riches mais très couteux en puissance de calcul. Entraine une réduction conséquente du nombre d'images par secondes.

Il est possible de changer les paramètres du blockmatcher dans le module `public/settings.py` dans la partie `DEPTH_MAP_DEFAULTS`.



![](https://i.imgur.com/nYNP438.png)

La capture précédente montre une carte de profondeur colorée (plus c'est rouge, plus c'est proche) mais avec le blockmatcher **SBM**. Dans ce mode, pour une résolution de capture HD (1280 x 920), le nombre d'images par seconde est proche de 60 alors qu'avec le mode **SGBM** et le filtre WLS il oscille entre 2 et 3 images par secondes.

