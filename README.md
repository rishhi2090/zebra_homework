# zebra_homework
A Cloud Function to process a file uploaded to a bucket. The file will contain a list of products by departments and the function should process the file and save it to two different buckets: one for valid and one for invalid products. Your output files should keep the original structure of the input file.

# Deployment Instructions
Create three buckets, one to upload the JSON to parse, one to upload the output of the valid JSON to and one to upload the output of the invalid JSON to.

Clone project using:
git clone https://github.com/rishhi2090/zebra_homework.git

Change directory to the code:
cd zebra_homework

Open the code and change lines 5 and 6 to the bucket names you have created for valid and invalid;


valid_bucket_name = 'valid-bucket'

invalid_bucket_name = 'invalid-bucket'

place your trigger bucket name into TRIGGER_BUCKET_NAME, then run the command:

gcloud functions deploy validator --runtime python37 --trigger-resource TRIGGER_BUCKET_NAME --trigger-event google.storage.object.finalize

# Testing the function
for testing the function i used the following Triggering event

{
   "bucket":"validator-zebra-bucket",
   "contentType":"application/json",
   "crc32c":"Onfqjg==",
   "etag":"CL3WoqrOjecCEAE=",
   "generation":"1579366400699197",
   "id":"validator-zebra-bucket/products.json/1579366400699197",
   "kind":"storage#object",
   "md5Hash":"fGW3/F0D2DLiGaFyaP0irA==",
   "mediaLink":"https://www.googleapis.com/download/storage/v1/b/validator-zebra-bucket/o/products.json?generation=1579366400699197&alt=media",
   "metageneration":"1",
   "name":"products.json",
   "selfLink":"https://www.googleapis.com/storage/v1/b/validator-zebra-bucket/o/products.json",
   "size":"2589",
   "storageClass":"STANDARD",
   "timeCreated":"2020-01-18T16:53:20.699Z",
   "timeStorageClassUpdated":"2020-01-18T16:53:20.699Z",
   "updated":"2020-01-18T16:53:20.699Z"
}
