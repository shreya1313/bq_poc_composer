# bq_poc_composer

**Creation of Service Account and giving the access:**

  To see what APIs are enabled:
  `gcloud services list`
    
  If BQ API is not enabled:
  `gcloud services enable bigquery.googleapis.com`
    
  `export PROJECT_ID=$(gcloud config get-value core/project)`

  Create BQ Service account:
    `gcloud iam service-accounts create my-bigquery-sa --display-name "my bigquery service account"`

  Create credentials & save it in JSON:
    `gcloud iam service-accounts keys create ~/key.json --iam-account my-bigquery-sa@${PROJECT_ID}.iam.gserviceaccount.com`

  Set the GOOGLE_APPLICATION_CREDENTIALS environment variable, which is used by the BigQuery Python client library:
    `export GOOGLE_APPLICATION_CREDENTIALS=~/key.json`

  Set access for the SA you created:
    `gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member "serviceAccount:my-bigquery-sa@${PROJECT_ID}.iam.gserviceaccount.com" \
    --role "roles/bigquery.user"`

  Verify that the SA has user role:
	`gcloud projects get-iam-policy $PROJECT_ID`
	
  **Install Client library:**
  `pip3 install --user --upgrade google-cloud-bigquery`
    
  **Then write the code using shell editor and the corresponding Dockerfile having dependencies in requirements.txt file.**
  
  **Give permissions for GCR & Storage Buckets.**   
   
  **Build and push the image to GCR**
  
  **Create Cluster and namespaces**  
  
  **Create a dag file (here it's called `poc_airflow_cmp.py`)**
  
  **Create Composer env and upload the DAG file and voila, ALL SET!**
