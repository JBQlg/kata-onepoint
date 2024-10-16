
## Projet de simulation de réservation de vols - KATA Onepoint

Un code permettant de simuler un système de réservation de vol avec attribution des places dans un avion. 

Le code devra permettre : 

* La définition et la gestion de plusieurs types d’avion (taille, disposition des sièges) 
* L’attribution des sièges à un ou plusieurs passagers en tenant compte des sièges déjà attribués 
* La modification du siège d’un ou plusieurs passagers 
* L’impression des détails de la réservation (numéro de vol + siège) d’un ou plusieurs passagers. Bien que cela ne soit pas explicitement pris en compte dans l’évaluation, la possibilité d’exécuter le code en ligne de commande serait un plus. Le candidat devra mettre en œuvre autant que possible les meilleurs pratiques de développement (organisation du code, syntaxe, documentation du code, tests unitaires) 

---

### Fonctionnement du code

Le developement de ce code à partir de ce cahier des charges a été fait avec pour commencer une approche de base fonctionnant avec des menus contextuels.
Ensuite, une approche avec des commandes directes a été ajoutée pour permettre une utilisation plus fluide du code.
Enfin, une persistance des données a été ajoutée pour permettre de sauvegarder les données des vols et des passagers.


#### Approches de développement
* approche de base avec menu contextuel
* approche avec commande directe 

#### persistance des données 
* approche avec JSON

  
---

Les différentes notes de conceptions expliquant les différentes approches de développement et les choix de conception sont disponibles dans le dossier `documentation`.