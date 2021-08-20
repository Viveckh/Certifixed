<p align="center">
  <a href="https://github.com/Viveckh">
    <img src="https://www.veniqa.com/img/certifixed/certifixed-logo.png" width="300px" alt="Certifixed: SSL Certification Renewal Suite. " />
  </a>
</p>
<p align="center">
<strong>CERTIFIXED</strong><i> - SSL Certification Renewal Suite.</i>
<br>
<br>Automated bot that finishes domain verification challenges with Godaddy, renews SSL certificates with letsencrypt, converts certificates to pfx, and replaces the expired version in Azure Vault.
<br>
<br> &#8680; <strong>Technologies: </strong> Python, Shell Scripting, Godaddy API, Azure API
<br> &#8680; <strong>Author: </strong> (EJ) Vivek Pandey
</p>

<p align="center">
  <a href="https://viveckh.com" target="_blank">Author's Website</a> |
  <a href="https://github.com/Viveckh" target="_blank">Author's Github</a> |
</p>

---

<i>Coded it one weekend to simplify my own life, 

Definitely feel free to drop in issues or PR if interested in pushing this project further.</i>

---

# Quickstart
## Setup virtual env & depedencies

```
> virtualenv -p python3 venv
> source venv/bin/activate
> pip3 install -r requirements.txt
```
---
## Credentials file
Create an `.env` file in the project folder with the following structure and input values.

```
[GODADDY]
API_KEY=xxxxxxx
API_SECRET=xxxxxxx

[AZURE]
CERT_VAULT_URL=https://xxxxxxx.vault.azure.net/
CLIENT_ID=xxxxxxx
TENANT_ID=xxxxxxx
SECRET=xxxxxxx

[CERTS]
SECTIONS=ADMIN_SERVER_CERT,SHOP_SERVER_CERT

[ADMIN_SERVER_CERT]
NAME=xxxxxxx
LOCAL_PFX_PATH=/xxxxxxx/admin-server.veniqa.com/certificate.pfx
PASSWORD=xxxxxxx

[SHOP_SERVER_CERT]
NAME=xxxxxxx
LOCAL_PFX_PATH=/xxxxxxx/shop-server.veniqa.com/certificate.pfx
PASSWORD=xxxxxxx
```

**Note**
* Anything from the `CERTS` section and below can be entered later before running the cert processor.
* `[ADMIN_SERVER_CERT]` is an example of a section that is needed per certificate you want renewed.
You can name such a section anything as long as you fulfill the following conditions:
    * It has all the key-value pairs as shown in the example
    * The custom section's name is included in the `[CERTS]` section's `SECTIONS` entry
---

## Make shell scripts executables

```
> chmod +x kickoff.sh
> chmod +x dns_challenge_hook.sh
> chmod +x cert_processor.sh
```
---

## Kickoff the certificate renewal process
Command: `./kickoff.sh`


## Run Cert Processor

Once the renewed certificates have been generated,
* Update the paths and passwords in the `cert_processor.sh` to point to the folder of your choice
* Run `./cert_processor.sh`
---
## Point your app to use the cert in Azure vault
The automated process ends with renewing the certificate and updating in the Azure Vault

You will then have to log in and point your app to use the updated certificate stored in your Azure vault. 
I couldn't find an API to facilitate this part. If you find a way, feel free to drop an issue with the resource.
