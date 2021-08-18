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
## Run the `godaddy_dns_modifier` script with appropriate values

`python godaddy_dns_modifier.py --domain veniqa.com --name _acme-challenge.admin-server --type TXT --data secretkey`
