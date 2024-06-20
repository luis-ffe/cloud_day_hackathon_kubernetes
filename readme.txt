Megabosses team @42Porto

Users: ruiolive, t-chow, luis-ffe , massoares, jorteixe

Google Cloud Day Hackathon, leveraging AI for the public sector.



--------- Folders ----------

-> Google Cloud App Engine

    This folder contains the code used to setup and deploy the website chatbot in the App Engine
    It is required that you activate de respective apis in google console to use App Engine.
    Language selected was python for this version for AE.

 - requirements.txt
    Dependencis needed to run the app in AE and use Google and external APIs, see google documentation to see other APIs

 - app.yaml
    configuration file for the App Engine environment setup.

    This app can be deployed using Google cloud shell directly but we used Google Cloud SDK and Google Cloud CLI (Comand line interface).

    gcloud init
    gcloud app deploy
    gcloud app run

-> Goofle Kubernetes Engine
