## Megabosses Team @ 42Porto

**Users:** ruiolive, t-chow, luis-ffe, massoares, jorteixe

---

## Google Cloud Day Hackathon: Leveraging AI for the Public Sector

### Projects Deployed on Google Cloud:

1. **fullscreen_chat** - Same app as the one in App Engine but deployed in GKE.
2. **microsvc_popup** - Chatbot messenger microservice running in GKE.
3. **microsvc_popup_tester** - Website with the popup message app microservice running in GKE (both site and microservice).

---

## Folders and Files Overview

### Google Cloud App Engine

- **Purpose:** Contains code for setting up and deploying the website chatbot on App Engine.
- **Language:** Python.
  
### Contents:

- **requirements.txt:** Dependencies needed to run the app on App Engine and utilize Google and external APIs.
- **app.yaml:** Configuration file for App Engine environment setup.

### Deployment Steps:

1. **Google Cloud SDK Setup:**
   - Initialize (`gcloud init`), deploy (`gcloud app deploy`), and run (`gcloud app run`) the app using Google Cloud SDK and CLI.

2. **Docker Configuration:**
   - **.dockerignore:** Ignore unnecessary files, such as `.yaml` files used for App Engine.
   - **Dockerfile:** Setup Docker environment similar to App Engine using Python.

3. **Image Build and Push:**
   - Build the Docker image using OS-specific commands, especially if using macOS M1.
   - Tag the image (`docker tag gcr.io/projectid/image_name`) with the appropriate project ID.
   - Push the image (`docker push gcr.io/projectid/image_name`) to Google Cloud Registry (`gcr.io`).

### Kubernetes Deployment (GKE)

- **Steps:**
  - Create `deployment.yaml` and `service.yaml` files.
  - Apply changes using `kubectl apply -f deployment.yaml` and `kubectl apply -f service.yaml`.
  - Verify deployment with commands like `kubectl get deployments`, `kubectl get services`, `kubectl get pods`, `kubectl get hpa`, and `kubectl get pods -n kube-system | grep metrics-server`.

### Authentication and Setup:

- **Authentication:**
  - Configure Docker (`gcloud auth configure-docker`) and login (`gcloud auth login`) for Google Cloud.
  - Get credentials to use Kubernetes cluster (`gcloud container clusters get-credentials my-cluster --zone us-central1-a`).

- **Enable APIs and Cluster Creation:**
  - Enable necessary APIs (`gcloud services enable container.googleapis.com`).
  - Create a Kubernetes cluster (`gcloud container clusters create my-cluster --zone us-central1-a --num-nodes=3`).
  - Optionally, enable autoscaling (`--enable-autoscaling --min-nodes=1 --max-nodes=5 --num-nodes=3`) and configure HPA.

- **Artifact Registry Setup:**
  - Create Artifact Registry repository (`gcloud artifacts repositories create gcr.io --repository-format=docker --location=us --description="Docker repository name"`).

### Additional Configurations and Notes:

- **Update SDK and Tools:**
  - Update Google Cloud components (`gcloud components update`).
  - Install GKE-specific plugins (`gcloud components install gke-gcloud-auth-plugin`).
  - Export environment variable to use GKE plugin (`export USE_GKE_GCLOUD_AUTH_PLUGIN=True`).

- **Docker Image Building on macOS M1:**
  - Use Docker Buildx to build multi-architecture images:
    ```sh
    # Create and use a new builder instance
    docker buildx create --name mybuilder --use

    # Inspect the builder instance
    docker buildx inspect --bootstrap

    # Build and push the multi-architecture image
    docker buildx build --platform linux/amd64,linux/arm64 -t gcr.io/projectid/thename --push .
    ```

---
