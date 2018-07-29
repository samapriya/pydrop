import requests
import json
import csv
import os

def dropletread(tag=None):
    if tag is not None:
        params = (
            ('tag_name', 'awesome'),
        )
        try:
            key=os.path.join(os.path.expanduser('~'), 'dokey.csv')
            f=open(key)
            for row in csv.reader(f):
                keyval=str(row).strip("[']")
        except Exception:
            os.system('pydrop dokey')
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+str(keyval)
        }
        params = (
            ('tag_name', tag),
        )
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers,params=params)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            print('Droplet name: '+str(items['name']))
            print('Droplet ID: '+str(items['id']))
            print('Status: '+str(items['status']))
            print('Created at: '+str(items['created_at']))
            print('IPv4 address: '+str(items['networks']['v4'][0]['ip_address']))
            print('No of CPUs: '+str(items['vcpus']))
            print('Memory: '+str(items['memory']))
            print('Disk Size GB: '+str(items['disk']))
            print('Image Used: '+str(items['image']['slug']))
            print('')
        print('Price Summary')
        price_monthly=0
        price_hourly=0
        for items in json_data['droplets']:
            price_monthly=price_monthly+float(items['size']['price_monthly'])
            price_hourly=price_hourly+float(items['size']['price_hourly'])
        print('Total Price Monthly: $'+str(price_monthly))
        print('Total Price Hourly: $'+str(price_hourly))
    elif tag is None:
        key=os.path.join(os.path.expanduser('~'), 'dokey.csv')
        f=open(key)
        for row in csv.reader(f):
            keyval=str(row).strip("[']")
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+str(keyval)
        }
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            print('Droplet name: '+str(items['name']))
            print('Droplet ID: '+str(items['id']))
            print('Status: '+str(items['status']))
            print('Created at: '+str(items['created_at']))
            print('IPv4 address: '+str(items['networks']['v4'][0]['ip_address']))
            print('No of CPUs: '+str(items['vcpus']))
            print('Memory: '+str(items['memory']))
            print('Disk Size GB: '+str(items['disk']))
            print('Image Used: '+str(items['image']['slug']))
            print('')
        print('Price Summary')
        price_monthly=0
        price_hourly=0
        for items in json_data['droplets']:
            price_monthly=price_monthly+float(items['size']['price_monthly'])
            price_hourly=price_hourly+float(items['size']['price_hourly'])
        print('Total Price Monthly: $'+str(price_monthly))
        print('Total Price Hourly: $'+str(price_hourly))
#dropletread()
#dropletread(tag="dev")
