from storages.backends.s3boto3 import S3Boto3Storage

class photo_storage(S3Boto3Storage):
    location = 'photos'
    file_overwrite = False
    default_acl = 'public-read'


class roadmap_storage(S3Boto3Storage):
    file_overwrite = True
    default_acl = 'public-read'