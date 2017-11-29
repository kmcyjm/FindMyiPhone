import boto3
import os
from base64 import b64decode
from pyicloud import PyiCloudService

personA_password_encrypted = os.environ['MY_PASSWORD']
personB_password_encrypted = os.environ['personB_PASSWORD']
personA_email_encrypted = os.environ['MY_EMAIL']
personB_email_encrypted = os.environ['personB_EMAIL']
iot_button_encrypted = os.environ['IOT_BUTTON_SERIAL_NUM']

# Decrypt code should run once and variables stored outside of the function
# handler so that these are decrypted once per container

kms = boto3.client('kms')

personA_email_decrypted = kms.decrypt(CiphertextBlob=b64decode(personA_email_encrypted))['Plaintext']
personA_password_decrypted = kms.decrypt(CiphertextBlob=b64decode(personA_password_encrypted))['Plaintext']
personB_email_decrypted = kms.decrypt(CiphertextBlob=b64decode(personB_email_encrypted))['Plaintext']
personB_password_decrypted = kms.decrypt(CiphertextBlob=b64decode(personB_password_encrypted))['Plaintext']
iot_button_decrypted = kms.decrypt(CiphertextBlob=b64decode(iot_button_encrypted))['Plaintext']


def find_personA_iphone(event, context):

    print(event)

    if event['serialNumber'] == iot_button_decrypted.decode('utf8') and event['clickType'] == 'SINGLE':
        api = PyiCloudService(personB_email_decrypted.decode('utf8'), personB_password_decrypted.decode('utf8'))
        api.devices[1].play_sound()

    elif event['serialNumber'] == iot_button_decrypted.decode('utf8') and event['clickType'] == 'DOUBLE':

        api = PyiCloudService(personA_email_decrypted.decode('utf8'), personA_password_decrypted.decode('utf8'))
        api.devices[1].play_sound()
