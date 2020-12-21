sklearn-flask-docker
Un exemple de déploiement d'un modèle sklearn à l'aide de Flask à l'aide d'un conteneur Docker.

Ce didacticiel nécessite des connaissances de base sur Docker.

Pas:
1. Former le modèle
Pour cet exemple, nous entraînons un modèle de jouet à l'aide du jeu de données d'entraînement Iris. Pour entraîner un nouveau modèle, exécutez ceci:

python train.py

Cela génère un modèle pickle dans un fichier nommé model.pkl.

2. Créez une image Docker contenant Flask et le modèle
Construisez une image ( docker build) appelée chrisalbon / sklearn-flask-docker ( --tag chrisalbon/sklearn-flask-docker) à partir du Dockerfile ( .).

La construction de cette image est définie par Dockerfile.

docker build --tag chrisalbon/sklearn-flask-docker .

3. Créer un conteneur à partir de l'image Docker
Créez et démarrez ( docker run) un -dconteneur Docker détaché ( ) appelé sklearn-flask-docker ( --name sklearn-flask-docker) à partir de l'image chrisalbon/sklearn-flask-docker:latestoù le port de la machine hôte est connecté au port 3333 du conteneur Docker ( -p 3000:3333).

docker run -p 3000:3333 -d --name sklearn-flask-docker chrisalbon/sklearn-flask-docker:latest

4. Interrogez l'API Prediction avec un exemple d'observation
Puisque notre modèle est entraîné sur l'ensemble de données du jouet Iris, nous pouvons tester l'API en l'interrogeant pour la classe prédite pour cet exemple d'observation:
#  ['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip'] 
# 11.,  33.,   7., 136.,   5.,   5.,   0
tenure = 11.0
age = 33.0
address = 7.0
income = 136.0
ed=5.0
employ=5.0
equip=0
Dans votre navigateur
Collez cette URL dans la barre de votre navigateur:

http://0.0.0.0:3000/api/v1.0/predict?sl=4.5&sw=2.3&pl=1.3&pw=0.3

Dans votre navigateur, vous devriez voir quelque chose comme ceci:

{"features":[4.5,2.3,1.3,0.3],"predicted_class":0}
"predicted_class":0 signifie que la classe prédite est "Iris setosa"

Utiliser Curl
Collez cette URL dans votre terminal:

curl -i "0.0.0.0:3000/api/v1.0/predict?tenure=11.0&age=33.0&address=7.0&income=136.0&ed=5.0&employ=5.0&equip=0"

Vous devriez voir quelque chose comme ceci:

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 51
Server: Werkzeug/1.0.1 Python/3.6.12
Date: Tue, 25 Aug 2020 20:29:41 GMT

{"features":[11.,  33.,   7., 136.,   5.,   5.,   0],"predicted_class":1}
Opérations de base de Docker
Vous devrez utiliser sudo pour ces commandes, mais la meilleure pratique consiste à ajouter votre utilisateur au dockergroupe lors de la production.

Démarrer le conteneur
sudo docker start sklearn-flask-docker

Arrêtez le conteneur
sudo docker stop sklearn-flask-docker

Supprimer le conteneur
sudo docker rm sklearn-flask-docker
