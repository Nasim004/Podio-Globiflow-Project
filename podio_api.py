import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.podio.com/"
USERNAME = os.environ["string_1"]
PASSWORD = os.environ["string_2"]
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def get_access_token(username,password):
    url = BASE_URL + "oauth/token"
    response = requests.post(
        url,
        data={
            "grant_type": "password",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "username": username,
            "password": password,
        },
    )

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        return None

def create_workspace(token, org_id, workspace_name):
    url = BASE_URL + "space/"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"org_id": org_id, "name": workspace_name}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["space_id"]
    else:
        print(response.text)
        return None

def install_apps(token, app_id, space_id):
    url = BASE_URL + f"app/{app_id}/install"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"space_id": space_id}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["app_id"]
    else:
        print(response.text)
        return None

def get_field_id(token, app_id, external_id):
    url = BASE_URL + f"app/{app_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for id in data["fields"]:
            if id["external_id"] == external_id:
                field_id = id["field_id"]
                return field_id

def delete_field(token, app_id,index):
    external_ids =['philadelphia-section','philadelphia-area','philadelphia-zip-code','delaware-section','delware-neighborhood','delaware-zip-codes']
    # to delete the atlanta section
    field_id = get_field_id(token, app_id, external_ids[index])
    url_1 = BASE_URL + f"app/{app_id}/field/{field_id}"
    # to delete the atlanta cities
    field_id = get_field_id(token, app_id, external_ids[index+1])
    url_2 = BASE_URL + f"app/{app_id}/field/{field_id}"
    # to delete the atlanta zipcodes
    field_id = get_field_id(token, app_id, external_ids[index+2])
    url_3 = BASE_URL + f"app/{app_id}/field/{field_id}"

    headers = {"Authorization": f"Bearer {token}"}
    response_1 = requests.delete(url_1, headers=headers)
    response_2 = requests.delete(url_2, headers=headers)
    response_3 = requests.delete(url_3, headers=headers)
    
def update_market(token, app_id, county):
    external_id = "statet"
    colours = ["D1F3EC","E1D8ED","FFD5C2","DCEBD8","F7D1D0","D1F3EC"]
    field_id = get_field_id(token, app_id, external_id)
    url = BASE_URL + f"app/{app_id}/field/{field_id}"
    headers = {"Authorization": f"Bearer {token}"}
    
    new_options = []
    for i in range(len(county)):
        if county[i] != 'None':    
            option = {
                "id":i+1,
                "text":f"{county[i]}",
                "status":"active",
                "color":colours[i],
            }
            new_options.append(option)
        
    data = {"label": "Markets","delta":49, "settings": {"options": new_options, "multiple": True}}

    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Succesfully updated market")
        return response.json()
    else:
        print(response.text)
        return None

def add_script(field_name,id):
    line_to_write = f'+(@[{field_name}](field_{id})?@[{field_name}](field_{id}).join(\",\"):\"\")+\",\"'
    with open('script.txt','a') as file:
        file.write(line_to_write)
    file.close()
    return ("Updated the script txt file")

def app_field_create(token,app_id,data_list,colour_code,field_name):
    url = BASE_URL + f"app/{app_id}/field"
    headers = {"Authorization": f"Bearer {token}"}
    #values of new field
    colours = ["D1F3EC","E1D8ED","FFD5C2","DCEBD8","F7D1D0","D1F3EC"]
    new_option = []
    for i in range(len(data_list)):
        if data_list[i] is not None:
            option = {
                "id":i+1,
                "text":f"{data_list[i]}",
                "status":"active",
                "color":colours[colour_code],
            }
            new_option.append(option)
    field_type = "category"
    field_settings ={
        "options":new_option,
        "multiple": True,
        "display":"inline"
    }
    field_delta = 55
    field_label = field_name
    field_config = {"label":field_label,"delta":field_delta,"settings":field_settings}
    new_field = {"type":field_type,"config":field_config}
    response = requests.post(url,headers=headers,json=new_field)
    if response.status_code == 200:
        print(f"{field_name} Created")
        if 'Zip Codes' in field_label:
            id = response.json()['field_id']
            add_script(field_name,id)
        return response.json()
    else:
        print(response.text)
        return None

def interested_zip_code_update(token,app_id):
    external_id = 'intrested-area-zip-internal'
    id = get_field_id(token,app_id,external_id)
    print(id)
    url = BASE_URL + f"app/{app_id}/field/{id}"
    print(url)
    headers = {"Authorization": f"Bearer {token}"}
    with open('script.txt','r') as file:
        script_value = file.read()
        print(script_value)
    file.close()
    
    data = {    
    "label" : "Intrested Area Zip (Internal)",
    "hidden":True,
    "settings":{
        "script": script_value
            }
    }
    response = requests.put(url,headers=headers,json=data)
    if response.status_code == 200:
        print("Interested Zip Code updated")
        return response
    else:
        print(response.text)
        return None
        

def get_organisations():
    url = 'https://api.podio.com/org'
    token = get_access_token(USERNAME,PASSWORD)
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        response = response.json()
        response_dict = {}
        for i in range(0,len(response)):
            name = response[i]['name']
            org_id = response[i]['org_id']
            response_dict[name] = org_id
        return response_dict
    
def clicksend_field(token,app_id):
    url = BASE_URL + f"app/{app_id}/field"
    headers = {"Authorization": f"Bearer {token}"}
    # field for click send username
    username_field={
            "config": {
                "delta": 3,
                "hidden": False,
                "label": "Click Send Username",    
                "hidden_create_view_edit": False,
                "settings": {
                    "size": "small",
                    "format": "plain"
                },
                "unique": False,
                "visible": True
            },
            "label": "Click Send Username",
            "type": "text"
        }
    response = requests.post(url,headers=headers,json=username_field)
    if response.status_code == 200:
        print("username field created")
    else:
        print(response.text)
    # field for click send password
    password_field={
            "config": {
                "delta": 3,
                "hidden": False,
                "label": "Click Send Password",    
                "hidden_create_view_edit": False,
                "settings": {
                    "size": "small",
                    "format": "plain"
                },
                "unique": False,
                "visible": True
            },
            "label": "Click Send Password",
            "type": "text"
        }
    response = requests.post(url,headers=headers,json=password_field)
    if response.status_code == 200:
        print("password field created")
    else:
        print(response.text)
    # field for click send list id 
    # list_field={
    #         "config": {
    #             "delta": 3,
    #             "hidden": False,
    #             "label": "Click Send List ID",    
                
    #             "hidden_create_view_edit": False,
    #             "settings": {
    #                 "size": "small",
    #                 "format": "plain"
    #             },
    #             "unique": False,
    #             "visible": True
    #         },
    #         "label": "Click Send List ID",
    #         "type": "text"
    #     }
    # response = requests.post(url,headers=headers,json=list_field)
    # if response.status_code == 200:
    #     print("id field created")
    # else:
    #     print(response.text)
    # for click send option
    clicksend_option = {
            "config": {
                "delta": 4,
                "label": "Click Send",
                "settings": {
                    "options": [
                        {
                            "id": 1,
                            "status": "active",
                            "text": "Push Values  ----> Click Send",
                            "color": "DCEBD8"
                        }
                    ],
                    "multiple": False,
                    "display": "dropdown"
                },
                "unique": False,
                "visible": True
            },
            "label": "Click Send",
            "status": "active",
            "type": "category"
        }
    response = requests.post(url,headers=headers,json=clicksend_option)
    if response.status_code == 200:
        print("click send option field created")
    else:
        print(response.text)

def get_organisations_url_label(token,org_id):
    url = f'https://api.podio.com/org/{org_id}'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        response = response.json()
        return(response['url_label'])
        
