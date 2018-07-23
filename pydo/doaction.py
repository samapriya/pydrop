import requests
import json
import os
import csv
import sys

def doaction(action=None,rname=None,name=None,idn=None):
    key=os.path.join(os.path.expanduser('~'), 'dokey.csv')
    f=open(key)
    for row in csv.reader(f):
        keyval=str(row).strip("[']")
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+str(keyval)
    }
    if action is None:
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            print('Droplet Name '+str(items['name'])+' has ID '+str(items['id']))
    elif action is not None and idn is not None:
        data = {"type":""}
        data["type"]=action
        if action==shutdown:
            url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
        if action==power_off:
            url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
        if action==power_on:
            url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
        if action==rename and rname is not None:
            url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
            data = {"type":"","name":""}
            data["type"]=action
            data["name"]=rname
        response = requests.post(url, headers=headers, data=json.dumps(data))
        #print(response.status_code)
        if response.status_code==201:
            json_data = json.loads(response.text)
            print('Action ID '+str(json_data['action']['id']))
            print('Status '+str(json_data['action']['status']))
            print('Action Type '+str(json_data['action']['type']))
        else:
            print('Failed with error code '+str(response.status_code))
    elif action is not None and name is not None:
        response = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)
        json_data = json.loads(response.text)
        for items in json_data['droplets']:
            if name==str(items['name']):
                idn=str(items['id'])
                data = {"type":""}
                data["type"]=str(action)
                if action=="shutdown":
                    url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
                elif action=="power_off":
                    url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
                elif action=="power_on":
                    url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
                elif action=="rename" and rname is not None:
                    url='https://api.digitalocean.com/v2/droplets/'+str(idn)+'/actions'
                    data = {"type":"","name":""}
                    data["type"]=str(action)
                    data["name"]=rname
                else:
                    print('Unkown action type '+str(action))
                    sys.exit()
                response = requests.post(url, headers=headers, data=json.dumps(data))
                #print(response.status_code)
                if response.status_code==201:
                    json_data = json.loads(response.text)
                    print('Action ID '+str(json_data['action']['id']))
                    print('Status '+str(json_data['action']['status']))
                    print('Action Type '+str(json_data['action']['type']))
                else:
                    print('Failed with error code '+str(response.status_code))
#doaction(action="rename",name="ubuntu-devtest",rname="devops")
        #response = requests.post(url, headers=headers, data=data)


#shutdown="graceful shutdown"
#power_off="hard shutdown"
#power_on="power on"
#rename,name=rename, new name
