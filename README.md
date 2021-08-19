# ssl-cert-renewal-suite

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
API_KEY = VALUE
API_SECRET = VALUE
```

---

## Make shell scripts executables

```
> chmod +x kickoff.sh
> chmod +x dns_challenge_hook.sh
> chmod +x cert_processor.sh
```
## Kickoff the certificate renewal process

`./kickoff.sh`

## Run Cert Processor

Once the renewed certificates have been generated,
* Update the paths and passwords in the `cert_processor.sh` to point to the folder of your choice
* Run `./cert_processor.sh`
