from azure.identity import DefaultAzureCredential
from azure.keyvault.certificates import CertificateClient
import configparser
import os

# Reading in the config file
config = configparser.ConfigParser()
config.read('.env')

# Initialize the cert client
os.environ['AZURE_CLIENT_ID'] = config['AZURE']['CLIENT_ID']
os.environ['AZURE_CLIENT_SECRET'] = config['AZURE']['SECRET']
os.environ['AZURE_TENANT_ID'] = config['AZURE']['TENANT_ID']

credential = DefaultAzureCredential()
client = CertificateClient(config['AZURE']['CERT_VAULT_URL'], credential)

# Uploading certificates one by one
for config_section in config['CERTS']['SECTIONS'].split(','):
    with open(config[config_section]['LOCAL_PFX_PATH'], 'rb') as f:
        data = f.read()

    client.import_certificate(config[config_section]['NAME'], data, password=config[config_section]['PASSWORD'])