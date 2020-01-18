import json
from google.cloud import storage

#bucket names, change to your bucket names
valid_bucket_name = 'valid-bucket'
invalid_bucket_name = 'invalid-bucket'

#file name to save files to bucket
valid_file_name = 'valid.json'
invalid_file_name = 'invalid.json'

def upload_blob(bucket_name, file_name, json_object):
    """Uploads the validated file to the appropriate bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    with open('/tmp/'+file_name, 'w',encoding="utf8") as fp:
        json.dump(json_object, fp)
    blob = bucket.blob(file_name)
    with open('/tmp/'+file_name, 'rb') as json_file:
        blob.upload_from_file(json_file)

def download_blob(bucket_name,file_name):
    """Downloads the json to parse from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    json_blob = blob.download_as_string()
    json_data = json.loads(json_blob)
    return json_data

def validator(data, context):
    """Function to parse a JSON file and to put all the valid products in a JSON and upload it to a bucket.
    The invalid products go into a separate JSON and uploaded to a different bucket

    A product is valid if:

        * it has a description

        * The price is a number

        * UPC is a 12 digit number

    """
    total_valid_products={}
    total_invalid_products={}
    json_data = download_blob(data['bucket'],data['name'])
    for section,products in json_data.items():
        valid_products = []
        invalid_products = []
        for product in products:
            if('description' in product and 'price' in product and 'upc' in product):
                if(len(product['upc'])==12 and isinstance(product['price'], float)):
                    valid_products.append(product)
                else:
                    invalid_products.append(product)
            else:
                invalid_products.append(product)
        total_valid_products[section] = valid_products
        total_invalid_products[section] = invalid_products
    upload_blob(valid_bucket_name,valid_file_name,total_valid_products)
    upload_blob(invalid_bucket_name,invalid_file_name ,total_invalid_products)