#!/bin/bash
# Activate python virtual env
source venv/bin/activate

# splits CERTBOT_DOMAIN on . and loads the results into an array 
domain_split=(${CERTBOT_DOMAIN//./ })

subdomain_name=${domain_split[0]}
domain="${domain_split[1]}.${domain_split[2]}"

echo "CERTBOT_VALIDATION: ${CERTBOT_VALIDATION}"
echo "CERTBOT_DOMAIN: ${CERTBOT_DOMAIN}"
echo "subdomain_name: ${subdomain_name}"
echo "domain: ${domain}"

python godaddy_dns_modifier.py --domain $domain --name _acme-challenge.$subdomain_name --type TXT --data $CERTBOT_VALIDATION

# Forcing to wait so we allow enough time for changes to propagate in godaddy servers before next step
sleep 20
