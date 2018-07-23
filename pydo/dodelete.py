import requests
import json
import os
import csv

def dropdelete(idn=None,name=None):
    key=os.path.join(os.path.expanduser('~'), 'dokey.csv')
    f=open(key)
    for row in csv.reader(f):
        keyval=str(row).strip("[']")
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
                response = requests.delete('https://api.digitalocean.com/v2/droplets/'+str(items['id']), headers=headers)
                if response.status_code==204:
                    print('Delete Succeeded ')
                    print('')
                else:
                    print('Delete failed with Status Code',str(response.status_code))
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
                print('Now Deleting '+str(items['id']))
                response = requests.delete('https://api.digitalocean.com/v2/droplets/'+str(items['id']), headers=headers)
                if response.status_code==204:
                    print('Delete Succeeded ')
                    print('')
                else:
                    print('Delete failed with Status Code',str(response.status_code))
                    print('')
            else:
                l.append(str(items['id']))
        print('Unmatched Droplets '+str(len(l)))
#dropdelete(name="devops")

#response = requests.delete('https://api.digitalocean.com/v2/droplets/3164494', headers=headers)
#, params=params
