# zebra_homework
A Cloud Function to process a file uploaded to a bucket. The file will contain a list of products by departments and the function should process the file and save it to two different buckets: one for valid and one for invalid products. Your output files should keep the original structure of the input file.

# Deployment Instructions
Create three buckets, one to upload the file to, one to upload the valid JSON to and one to upload the invalid JSON to.

Clone project using:
git clone https://github.com/rishhi2090/zebra_homework.git

Change directory to the code:
cd zebra_homework

Open the code and change lines 5 and 6 to the bucket names you have created for valid and invalid;

#bucket names, change to your bucket names
valid_bucket_name = 'valid-bucket'
invalid_bucket_name = 'invalid-bucket'

place your trigger bucket name into TRIGGER_BUCKET_NAME, then run the command:

gcloud functions deploy validator --runtime python37 --trigger-resource TRIGGER_BUCKET_NAME --trigger-event google.storage.object.finalize
