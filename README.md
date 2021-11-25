# Cours cloud 

### Groupe TD3 : 
* TRICHET Laura
* YE Sylvie

### Sujet :
Créer un projet à déposer sur le cloud (GCP, Azure ou AWS) Ce projet doit permettre d'afficher des informations sur le réveil Lametric.
Nous avons choisi de faire un projet qui affiche le nombre de jours en couple / célibataire, ainsi que le nombre de rapport sexuel / matchs

1. app.py      
Un fichier permettant d'exposer les APIs :   

    a. GET '/'    
Affiche Hello World   

    b. GET '/iam?relationshipDate=2021-11-10&relationshipType=single'   
Affiche les infos   
Prend en entrée un json : le type de relation (couple ou célibataire) && la date du début de cette relation (yyyy-mm-dd)
Ce ws retourne un json de frames à afficher pour le réveil Lametric :
```
{
    "frames": [
        {
            "index": 0,
            "text": "15 days",
            "icon": "i6946"
        },
        {
            "index": 1,
            "text": "23 matchs",
            "icon": "i7756"
        }
    ]
}
```

Pour les tester exécutez les commandes suivantes :   
```cd lovelife```   
```export FLASK_APP=app.py```   
```flask run```   
Ensuite pour les méthodes *GET* vous pouvez les exécuter directement via un moteur de recherche, ou sur un logiciel comme *Postman*. Et pour les *PUT* et *POST*, via *Postman* uniquement.


### Site déployé sur Azure : 
https://lovelifeiim.azurewebsites.net

### Pour le déploiement : 
https://docs.microsoft.com/en-us/azure/developer/python/tutorial-deploy-app-service-on-linux-04
https://medium.datadriveninvestor.com/deploying-flask-web-app-on-microsoft-azure-89cea17e9114

