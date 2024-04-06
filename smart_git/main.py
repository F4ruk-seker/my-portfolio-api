from database import get_session, Dependency

param = """
asgiref==3.8.0
beautifulsoup4==4.12.2
cachetools==5.3.2
certifi==2023.11.17
cffi==1.16.0
charset-normalizer==3.3.2
cloudinary==1.37.0
cryptography==41.0.7
discord-webhook==1.3.0
Django==4.2.11
django-autoslug==1.9.9
django-cors-headers==4.3.1
django-dbbackup==4.1.0
django-debug-toolbar==4.2.0
django-environ==0.11.2
django-gdrive-backup==0.0.10
django-rest-knox==4.2.0
django-storages==1.14.2
djangorestframework==3.15.0
djangorestframework-simplejwt==5.3.1
encrypted-credentials==0.0.4
fake-useragent==1.4.0
git-filter-repo==2.38.0
google-api-core==2.16.2
google-api-python-client==2.116.0
google-auth==2.27.0
google-auth-httplib2==0.2.0
google-client-helper==0.0.3
google-cloud-core==2.4.1
google-cloud-storage==2.14.0
google-crc32c==1.5.0
google-resumable-media==2.7.0
googleapis-common-protos==1.62.0
gunicorn==21.2.0
httplib2==0.22.0
idna==3.6
markdown-to-json==2.1.0
packaging==23.2
Pillow==10.1.0
protobuf==4.25.2
psycopg2==2.9.9
pyasn1==0.5.1
pyasn1-modules==0.3.0
pycparser==2.21
PyJWT==2.8.0
pyotp==2.9.0
pyparsing==3.1.1
python-dateutil==2.8.2
pytz==2024.1
PyYAML==6.0.1
requests==2.31.0
rsa==4.9
six==1.16.0
soupsieve==2.5
sqlparse==0.4.4
tzdata==2024.1
uritemplate==4.1.1
urllib3==2.1.0
whitenoise==6.6.0
"""

for dependency, version in [_.split('==') for _ in param.split('\n') if len(_.split('==')) == 2]:
    print(dependency, version)

