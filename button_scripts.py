import requests
from podio_api import get_field_id

def button_update_seller_app(token, workspace_name, app_id, org_name):
    workspace_name = workspace_name.lower()
    workspace_name = workspace_name.replace(" ", "-")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    unique_id = get_field_id(token, app_id, "unique-id")

    # button 1
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Direct+to Seller+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Property +Information&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Lead +Status&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link4 = "![alt](http://dabuttonfactory.com/button.png?t=Qualifying+Questions&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link5 = "![alt](http://dabuttonfactory.com/button.png?t=Overcoming+Objections&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link6 = "![alt](http://dabuttonfactory.com/button.png?t=Lead+ Evaluation&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link7 = "![alt](http://dabuttonfactory.com/button.png?t=Appointment&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link8 = "![alt](http://dabuttonfactory.com/button.png?t=Offer+& +Contract&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link9 = "![alt](http://dabuttonfactory.com/button.png?t=Cash+Buyer+List&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/seller-leads/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-13") + " " +\nlink2.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-19") + " " + \nlink3.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-37") + " " +\nlink4.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-16") + " " +\nlink5.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-25") + " " +\nlink6.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-36") + " " +\nlink7.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-17") + " " +\nlink8.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-28") + " " +\nlink9.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-23")'
    field_id = get_field_id(token, app_id, "ctn")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 9,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }

    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 1 seller app script  updated====>")
    else:
        print(response.text)

    # buttton 2
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Acquisition+Relation+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Direct+to+Seller+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Property+Information&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link4 = "![alt](http://dabuttonfactory.com/button.png?t=Lead+Status&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link5 = "![alt](http://dabuttonfactory.com/button.png?t=Qualifying+Questions&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link6 = "![alt](http://dabuttonfactory.com/button.png?t=Overcoming+Objections&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link7 = "![alt](http://dabuttonfactory.com/button.png?t=Appointment&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link8 = "![alt](http://dabuttonfactory.com/button.png?t=Offer+& +Contract&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link9 = "![alt](http://dabuttonfactory.com/button.png?t=Cash+Buyer+List&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/seller-leads/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-39") + " " +\nlink2.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-13") + " " + \nlink3.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-19") + " " +\nlink4.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-37") + " " +\nlink5.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-16") + " " +\nlink6.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-25") + " " +\nlink7.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-17") + " " +\nlink8.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-28") + " " +\nlink9.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-23")'
    field_id = get_field_id(token, app_id, "ctn-2")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 28,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 2 seller app script  updated====>")

    # button 3
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Acquisition+Relation+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Property +Information&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Lead +Status&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link4 = "![alt](http://dabuttonfactory.com/button.png?t=Qualifying+Questions&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link5 = "![alt](http://dabuttonfactory.com/button.png?t=Overcoming+Objections&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link6 = "![alt](http://dabuttonfactory.com/button.png?t=Lead+ Evaluation&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link7 = "![alt](http://dabuttonfactory.com/button.png?t=Appointment&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link8 = "![alt](http://dabuttonfactory.com/button.png?t=Offer+& +Contract&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link9 = "![alt](http://dabuttonfactory.com/button.png?t=Cash+Buyer+List&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/seller-leads/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-39") + " " +\nlink2.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-19") + " " + \nlink3.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-37") + " " +\nlink4.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-16") + " " +\nlink5.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-25") + " " +\nlink6.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-36") + " " +\nlink7.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-17") + " " +\nlink8.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-28") + " " +\nlink9.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-23")'
    field_id = get_field_id(token, app_id, "ctn-3")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 33,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 3 seller app script  updated====>")

    # button 4
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Acquisition+Relation+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Direct+to+Seller+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Property+Information&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link4 = "![alt](http://dabuttonfactory.com/button.png?t=Qualifying+Questions&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link5 = "![alt](http://dabuttonfactory.com/button.png?t=Overcoming+Objections&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link6 = "![alt](http://dabuttonfactory.com/button.png?t=Lead+ Evaluation&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link7 = "![alt](http://dabuttonfactory.com/button.png?t=Appointment&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link8 = "![alt](http://dabuttonfactory.com/button.png?t=Offer+& +Contract&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link9 = "![alt](http://dabuttonfactory.com/button.png?t=Cash+Buyer+List&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/seller-leads/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-39") + " " +\nlink2.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-13") + " " + \nlink3.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-19") + " " +\nlink4.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-16") + " " +\nlink5.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-25") + " " +\nlink6.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-36") + " " +\nlink7.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-17") + " " +\nlink8.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-28") + " " +\nlink9.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-23")'
    field_id = get_field_id(token, app_id, "ctn-4")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 38,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 4 seller app script  updated====>")

    # button 5
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Acquisition+Relation+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Direct+to+Seller+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Property+Information&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link4 = "![alt](http://dabuttonfactory.com/button.png?t=Lead+Status&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link5 = "![alt](http://dabuttonfactory.com/button.png?t=Overcoming+Objections&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link6 = "![alt](http://dabuttonfactory.com/button.png?t=Lead+ Evaluation&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link7 = "![alt](http://dabuttonfactory.com/button.png?t=Appointment&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link8 = "![alt](http://dabuttonfactory.com/button.png?t=Offer+& +Contract&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link9 = "![alt](http://dabuttonfactory.com/button.png?t=Cash+Buyer+List&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/seller-leads/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-39") + " " +\nlink2.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-13") + " " + \nlink3.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-19") + " " +\nlink4.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-37") + " " +\nlink5.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-25") + " " +\nlink6.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-36") + " " +\nlink7.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-17") + " " +\nlink8.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-28") + " " +\nlink9.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-23")'
    field_id = get_field_id(token, app_id, "ctn-5")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 46,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 5 seller app script  updated====>")

    # button 6
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Acquisition+Relation+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Direct+to+Seller+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Property+Information&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link4 = "![alt](http://dabuttonfactory.com/button.png?t=Lead+Status&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link5 = "![alt](http://dabuttonfactory.com/button.png?t=Qualifying+Questions&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link6 = "![alt](http://dabuttonfactory.com/button.png?t=Lead+ Evaluation&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link7 = "![alt](http://dabuttonfactory.com/button.png?t=Appointment&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link8 = "![alt](http://dabuttonfactory.com/button.png?t=Offer+& +Contract&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link9 = "![alt](http://dabuttonfactory.com/button.png?t=Cash+Buyer+List&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/seller-leads/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-39") + " " +\nlink2.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-13") + " " + \nlink3.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-19") + " " +\nlink4.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-37") + " " +\nlink5.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-16") + " " +\nlink6.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-36") + " " +\nlink7.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-17") + " " +\nlink8.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-28") + " " +\nlink9.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-23")'
    field_id = get_field_id(token, app_id, "ctn-6")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 58,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 6 seller app script  updated====>")
    # button 7
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Acquisition+Relation+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Direct+to+Seller+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Property+Information&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link4 = "![alt](http://dabuttonfactory.com/button.png?t=Lead+Status&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link5 = "![alt](http://dabuttonfactory.com/button.png?t=Qualifying+Questions&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link6 = "![alt](http://dabuttonfactory.com/button.png?t=Lead+ Evaluation&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link7 = "![alt](http://dabuttonfactory.com/button.png?t=Appointment&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link8 = "![alt](http://dabuttonfactory.com/button.png?t=Offer+& +Contract&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link9 = "![alt](http://dabuttonfactory.com/button.png?t=Cash+Buyer+List&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/seller-leads/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-39") + " " +\nlink2.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-13") + " " + \nlink3.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-19") + " " +\nlink4.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-37") + " " +\nlink5.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-16") + " " +\nlink6.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-36") + " " +\nlink7.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-17") + " " +\nlink8.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-28") + " " +\nlink9.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-23")'
    field_id = get_field_id(token, app_id, "ctn-7")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 69,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 7 seller app script  updated====>")

    # button 8
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Acquisition+Relation+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Direct+to+Seller+Lead&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Property+Information&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link4 = "![alt](http://dabuttonfactory.com/button.png?t=Lead+Status&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link5 = "![alt](http://dabuttonfactory.com/button.png?t=Qualifying+Questions&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link6 = "![alt](http://dabuttonfactory.com/button.png?t=Overcoming+Objections&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link7 = "![alt](http://dabuttonfactory.com/button.png?t=Evaluation&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link8 = "![alt](http://dabuttonfactory.com/button.png?t=Offer+& +Contract&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link9 = "![alt](http://dabuttonfactory.com/button.png?t=Cash+Buyer+List&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/seller-leads/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-39") + " " +\nlink2.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-13") + " " + \nlink3.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-19") + " " +\nlink4.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-37") + " " +\nlink5.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-16") + " " +\nlink6.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-25") + " " +\nlink7.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-36") + " " +\nlink8.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-28") + " " +\nlink9.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-23")'
    field_id = get_field_id(token, app_id, "ctn-8")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 82,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 8 seller app script  updated====>")

    # button 9
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Back+To+Top&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/seller-leads/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#seller-name")'
    field_id = get_field_id(token, app_id, "ctn-9")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 102,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 9 seller app script  updated====>")
def button_update_closings_app(token, workspace_name, app_id, org_name):
    workspace_name = workspace_name.lower()
    workspace_name = workspace_name.replace(" ", "-")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    unique_id = get_field_id(token, app_id, "unique-id")

    # button 1
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Exist+Strategy+:+Wholesale&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Deal+Profit&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Cash+Buyer+List&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/closings/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-5") + " " +\nlink2.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-6") + " " +\nlink3.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-7")'
    field_id = get_field_id(token, app_id, "ctn")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 6,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 1 closings app script  updated====>")

    # buttton 2
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Closing&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Deal+Profit&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Cash+Buyer+List&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/closings/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-4") + " " +\nlink2.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-6") + " " +\nlink3.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-7")'
    field_id = get_field_id(token, app_id, "ctn-2")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 13,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 2 closings app script  updated====>")

    # button 3
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Closing&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Exist+Strategy+:+Wholesale&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Cash+Buyer+List&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/closings/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-4") + " " +\nlink2.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-5") + " " +\nlink3.link(podioUrl + @[Unique ID](field_{unique_id}) + "#field-7")'
    field_id = get_field_id(token, app_id, "ctn-3")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 41,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 3 closings app script  updated====>")

    # button 4
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Back+To+Top&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/closings/items/"\n     \nlink1.link(podioUrl + @[Unique ID](field_{unique_id}) + "#location")'
    field_id = get_field_id(token, app_id, "ctn-4")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 51,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 4 closings app script  updated====>")

def button_update_relationship_app(token, workspace_name, app_id, org_name):
    workspace_name = workspace_name.lower()
    workspace_name = workspace_name.replace(" ", "-")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    unique_id = get_field_id(token, app_id, "unique-id")

    # button 1
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Reference+Property&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Market+Automations&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Skip+Tracing&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link4 = "![alt](http://dabuttonfactory.com/button.png?t=Elephant+Data&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\n\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/relationships/items/"\n     \nlink1.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-2") + " " +\nlink2.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-3") + " " +\nlink3.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-4") + " " +\nlink4.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-5")'
    field_id = get_field_id(token, app_id, "ctn")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 1,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 1 relationship app script  updated====>")

    # buttton 2
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Contact+Info&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Market+Automations&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Skip+Tracing&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)"\nvar link4 = "![alt](http://dabuttonfactory.com/button.png?t=Elephant+Data&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)"\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/relationships/items/"\n     \nlink1.link(podioUrl + @[Unique ID](item_app_item_id) + "#field") + " " +\nlink2.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-3") + " " +\nlink3.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-4") + " " +\nlink4.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-5")'
    field_id = get_field_id(token, app_id, "ctn-2")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 20,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 2 relationship app script  updated====>")

    # button 3
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Contact+Info&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Reference+Property&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Skip+Tracing&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link4 = "![alt](http://dabuttonfactory.com/button.png?t=Elephant+Data&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/relationships/items/"\n     \nlink1.link(podioUrl + @[Unique ID](item_app_item_id) + "#field") + " " +\nlink2.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-2") + " " +\nlink3.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-4") + " " +\nlink4.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-5")'
    field_id = get_field_id(token, app_id, "ctn-3")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 47,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 3 relationship app script  updated====>")

    # button 4
    script_value = f'var link1 = "![alt](http://dabuttonfactory.com/button.png?t=Contact+Info&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link2 = "![alt](http://dabuttonfactory.com/button.png?t=Reference+Property&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link3 = "![alt](http://dabuttonfactory.com/button.png?t=Market+Automation&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar link4 = "![alt](http://dabuttonfactory.com/button.png?t=Elephant+Data&f=Open+Sans-Bold=9&tc=fff&tshs=1&tshc=000&hp=20&vp=8&c=5&bgt=unicolored&bgc=3d85c6&ebgc 073763)";\nvar podioUrl = "https://podio.com/{org_name}/{workspace_name}/apps/relationships/items/"\n     \nlink1.link(podioUrl + @[Unique ID](item_app_item_id) + "#field") + " " +\nlink2.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-2") + " " +\nlink3.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-3") + " " +\nlink4.link(podioUrl + @[Unique ID](item_app_item_id) + "#field-5")\n'
    field_id = get_field_id(token, app_id, "ctn-4")
    url = f"https://api.podio.com/app/{app_id}/field/{field_id}"
    payload = {
        "delta": 56,
        "label": "CTN",
        "settings": {
            "script": script_value,
        },
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Button 4 relationship app script  updated====>")
