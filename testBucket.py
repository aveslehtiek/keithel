import boto3

# constants
BUCKET_NAME = 'keithelseva'
S3_FILE = 'sample.png'
LOCAL_NAME = 'sample.png'

s3 = boto3.resource('s3')

# test listing
bucket = s3.Bucket(BUCKET_NAME)
for f in bucket.objects.all():
    print(f.key)

# test downloading
bucket.download_file(S3_FILE, LOCAL_NAME)

# test uploading
data = open('sample_draft.jpg', 'rb')
bucket.put_object(Key='SampleDraft', Body=data)

