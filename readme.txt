Megabosses team @42Porto

Users: ruiolive, t-chow, luis-ffe , massoares, jorteixe

Google Cloud Day Hackathon, leveraging AI for the public sector.


fullscreen_chat - same app as the one in the app engine but deployed in GKE
microsvc_popup - just the chatbot messager microservice runing in GKE
microsvc_popup_tester - a website with the pop up message app microservice added runing in GKE both the site and the microservice

--------- Folders ------------------------------------------------------------------

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

   This is runing the app and ready just for google app engine.
   To use this same code but run this as a image/ container do the following.
   -.dockerignore
      ignoring the .yaml files that were needed fpor the app engine
   -dockerfile
      seting up the same environment as the one used for the app in the app engine environment defined by .yaml
   - You can now build the image.
      the image needs to be created using OS specific commands.
      if you are using a m1 chip macos you need to account for that and use the docker comands to build the imgages acordingly
      also the GKE uses a specific OS that you should account for.

      Tag the image to you gcr.io   artifact  / container registry repository using the docker tag command with the apropriate project id
      Docker push then then
   EXAMPLE:


   KUBERNETES DEPLOYMENT: GKE

   First you need to create the deployment.yaml file and the services.yaml file.

   Apply these changes:

   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml


   kubectl get deployments
   kubectl get services
   kubectl get pods
   kubectl get hpa
   kubectl get pods -n kube-system | grep metrics-server




   This authentications should be made befor atempting to push or aply changes.
      gcloud auth configure-docker
      gcloud auth login

-> Goofle Kubernetes Engine ----------------------------------------------------------------
      
      gcloud auth login
      gcloud auth configure-docker

   Enable the API:
      gcloud services enable container.googleapis.com

   Create the cluster:

      gcloud container clusters create my-cluster --zone us-central1-a --num-nodes=3
      
      The nodes is the number of instances runing. You can set a minimum a maximum etc... and enable autoscaler
      
      gcloud container clusters create my-cluster --zone us-central1-a --enable-autoscaling --min-nodes=1 --max-nodes=5 --num-nodes=3

   This command enables HPA Horizontal Pod Autoscaler and installs metrics server :
      kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

      kubectl autoscale deployment name-of-cluster --cpu-percent=50 --min=1 --max=10

      This last comand just tells the cluster that when a cpu reaches 50% use a new one will be activated (pod).
      see .yaml files also to see if you are using Loadbalancer or nodeport.


   Get credentials makes kubectl command use this cluster
      gcloud container clusters get-credentials my-cluster --zone us-central1-a

      to create the Artifact registry repository:
         gcloud artifacts repositories create gcr.io --repository-format=docker --location=us --description="Docker repository name"


Others:

Update SDK TO ALLOW authentication

   gcloud components update
   gcloud components install gke-gcloud-auth-plugin
   export USE_GKE_GCLOUD_AUTH_PLUGIN=True

The deployment and configuration of the microservice is prety much the same thing just with adjustments to the html code
 and docker image as it needs almost nothing in it and can be added to other websites using just a tiny portion of code.


GKE uses contanerd (cos_containerd ) container optimized OS

to properly build the docker image in a Macos M1 you need to do this:

      # Create and use a new builder instance
      docker buildx create --name mybuilder --use

      # Inspect the builder instance
      docker buildx inspect --bootstrap

      # Build and push the multi-architecture image
      docker buildx build --platform linux/amd64,linux/arm64 -t gcr.io/projectid/thename --push .
