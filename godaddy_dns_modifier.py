# Example command: python godaddy_dns_modifier.py --domain veniqa.com --name _acme-challenge.admin-server --type TXT --data secretkey

from godaddypy import Client, Account
import configparser
import argparse

# Reading in the arguments
parser = argparse.ArgumentParser(description='Details for the DNS record to modify')
parser.add_argument('--domain', type=str, required=True,
                    help='the domain that the DNS record belongs to')
parser.add_argument('--name', type=str, required=True,
                    help='the name part of the DNS record')
parser.add_argument('--type', type=str, required=True,
                    help='the type part of the DNS record')
parser.add_argument('--data', type=str, required=True,
                    help='the data part of the DNS record')
parser.add_argument('--ttl', type=int, required=False, default=3600,
                    help='the ttl of the DNS record')                    
                    
args = parser.parse_args()

# Reading in the config file
config = configparser.ConfigParser()
config.read('.env')

# Authenticating with Godaddy
account = Account(api_key=config['GODADDY']['API_KEY'], api_secret=config['GODADDY']['API_SECRET'])
client = Client(account)

# print(client.get_domains())
# Updating the record
response = client.update_record(domain=args.domain, record={'type': args.type, 'name': args.name, 'data': args.data, 'ttl': args.ttl})

# Notifying of status
if response:
    print(f'Updating {args.name} {args.type} record was SUCCESSFUL...')
    latest_records = client.get_records(args.domain, record_type=args.type)
    match = [item for item in latest_records if item.get('name') == args.name]
    print(match)
else:
    print(f'Updating {args.name} {args.type} record was NOT SUCCESSFUL...')