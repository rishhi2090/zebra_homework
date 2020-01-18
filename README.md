# zebra_homework
A Cloud Function to process a file uploaded to a bucket. The file will contain a list of products by departments and the function should process the file and save it to two different buckets: one for valid and one for invalid products. Your output files should keep the original structure of the input file.

# Deployment Instructions
Create three buckets, one to upload the file to, one to upload the valid JSON to and one to upload the invalid JSON to.


place your bucket name into TRIGGER_BUCKET_NAME
gcloud functions deploy validator --runtime python37 --trigger-resource TRIGGER_BUCKET_NAME --trigger-event google.storage.object.finalize
