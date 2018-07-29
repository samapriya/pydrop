import requests
import json
import os
import csv

def dropreset(idn=None,name=None):
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
    if idn==None and name==None:
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            print('Droplet Name '+str(items['name'])+' has ID '+str(items['id']))
    elif idn==None and name is not None:
        l=[]
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            if name==str(items['name']):
                print('Droplet name matched to ID '+str(items['id']))
                print('Now Deleting '+str(items['name']))
                data = '{"type":"password_reset"}'
                response = requests.post('https://api.digitalocean.com/v2/droplets/'+str(items['id']), headers=headers,data=data)
                if response.status_code==201:
                    print('Password reset started')
                    print('')
                else:
                    print('Password Reset failed with Status Code',str(response.status_code))
                    print('')
            else:
                l.append(str(items['name']))
        print('Unmatched Droplets '+str(len(l)))
    elif name==None and idn is not None:
        l=[]
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            if idn==str(items['id']):
                print('Droplet ID matched to '+str(items['name']))
                print('Now resetting password for '+str(items['id']))
                data = '{"type":"password_reset"}'
                response = requests.post('https://api.digitalocean.com/v2/droplets/'+str(items['id']), headers=headers,data=data)
                if response.status_code==201:
                    print('Password reset started')
                    print('')
                else:
                    print('Password Reset failed with Status Code',str(response.status_code))
                    print('')
            else:
                l.append(str(items['id']))
        print('Unmatched Droplets '+str(len(l)))