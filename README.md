
# Projet de simulation de réservation de vols - KATA Onepoint

Un code permettant de simuler un système de réservation de vol avec attribution des places dans un avion. 

Le code devra permettre : 

* La définition et la gestion de plusieurs types d’avion (taille, disposition des sièges) 
* L’attribution des sièges à un ou plusieurs passagers en tenant compte des sièges déjà attribués 
* La modification du siège d’un ou plusieurs passagers 
* L’impression des détails de la réservation (numéro de vol + siège) d’un ou plusieurs passagers. Bien que cela ne soit pas explicitement pris en compte dans l’évaluation, la possibilité d’exécuter le code en ligne de commande serait un plus. Le candidat devra mettre en œuvre autant que possible les meilleurs pratiques de développement (organisation du code, syntaxe, documentation du code, tests unitaires) 

---

### Fonctionnement du code

Le developement de ce code à partir de ce cahier des charges a été fait avec une première approche fonctionnant avec des menus contextuels.
Ensuite, une approche avec des commandes directes a été ajoutée pour permettre une utilisation plus fluide du code.
Enfin, une persistance des données a été programmée pour permettre de sauvegarder les données des vols et des passagers.


#### Approches de fonctionnement
* Approche de base avec menu contextuel
  
  Dans cette approche, le code fonctionne avec des menus contextuels permettant de naviguer dans les différentes fonctionnalités du code. Selon le choix fait les différentes actions sont réalisées avec des demandes d'informations complémentaires si nécessaire.

  ![Menu principal](/documentation/diagram/screen_main_menu.png)

* Approche avec commande directe 
  
  La seconde approche vient en réalité se greffer aux méthodes de la première. Elle a pour objectif de permettre une utilisation plus fluide du code en permettant de réaliser des actions concrètes sans passer par les menus contextuels.
  Elle permet donc un gain de temps pour la plupart des actions (exceptées celles de création d'une réservation nécessitant une plus grande quantité d'informations et l'affichage entre étapes intermédiaire du plan de l'appareil). Cela permet également de faciliter des implémentations avec d'autres systèmes de gestion ultérieur.

    * Exemple d'ajout d'un vol : 

  ![Exemple ajouter un vol ](/documentation/diagram/direct_cmd_add_flight_ex.png)

    * Détail des commandes disponibles :
  
    ![Détail des commandes](/documentation/diagram/direct_cmd_help.png)

#### Persistence des données 
* Persistence des données via JSON
  
  Bien qu'une fonction ai été ajoutée pour simuler des exemples d'éléments de ce simulateur (avions, vols, réservations, ...), les données saisies sont sauvegardées automatiquement dans un fichier JSON.

  ![Exemple de données sauvegardées](/documentation/diagram/json_data_example.png)

  (Une persistence des données en base de données pourrait être envisagée pour une utilisation plus poussée de ce code, l'architecture actuelle permettant de facilement ajouter cette fonctionnalité)
---
Dans la section  `documentation` vous trouverez les premiers diagrammes UML de conceptions permettant d'imaginer l'évolution de ce programme pendant ce kata (tous n'y sont pas forcément (notament les derniers mais si intéressé, je peux les fournir).
