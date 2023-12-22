import os
import secrets
import concurrent.futures
from flask_socketio import SocketIO
from click_send import click_send_function
from bigquery import bigquery_data, file_upload
from data_extraction import get_county, sheet_data_extraction
from flask import Flask, render_template, redirect, request
from button_scripts import (
    button_update_seller_app,
    button_update_closings_app,
    button_update_relationship_app,
)
from selenium_function import (
    flow_creation,
    flow_updation,
    refresh_podio,
    seller_app_flow,
    closings_app_flow_1,
    closings_app_flow_2,
    closing_click_send,
    flow_creation_commercial_app,
)
from podio_api import (
    get_access_token,
    create_workspace,
    install_apps,
    delete_field,
    update_market,
    app_field_create,
    get_organisations,
    interested_zip_code_update,
    clicksend_field,
    get_organisations_url_label,
)

secret_key = secrets.token_hex(16)
app = Flask(__name__)
app.secret_key = secret_key
socketio =SocketIO(app)

@app.route("/", methods=["GET"])
def index():
    message = request.args.get("message")
    county = get_county()
    organisations = get_organisations()
    return render_template("index.html", message=message, counties=county, organisations=organisations)
@app.route("/commercial_app", methods=["GET"])
def index2():
    organisations = get_organisations()
    message = request.args.get("message")
    return render_template("index2.html",organisations=organisations,message=message)
@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        workspace_name = request.form.get("workspace_name")
        org_id = request.form.get("organisation")
        counties =set()
        counties.add(request.form.get("county1"))
        counties.add(request.form.get("county2"))
        counties.add(request.form.get("county3"))
        counties.add(request.form.get("county4"))
        counties.add(request.form.get("county5"))
        counties.add(request.form.get("county6"))
        counties_list = list(counties)
        click_send = request.form.get('clicksend')
        print(org_id)
        print(counties_list)
        socketio.emit("update progress",10)
        if org_id is None:
            message = "Select Organisation"
            return render_template("index.html",message=message)
        if len(counties_list) == 1:
            message = "Select 1 county atleast"
            return render_template("index.html",message=message)
        # getting access token from podio
        access_token = get_access_token(username,password)
        print("access_token: ", access_token)
        if access_token:
            # api calling to create workspace under a organisation
            org_id = int(org_id)
            workspace = create_workspace(access_token, org_id, workspace_name)
            print('workspace : ',workspace)
            if workspace:
                # the 3 apps app_id list Seller Lead, Closings, Relationship
                app_id = [28794198, 28794199, 28797718]
                new_app_id = []
                # installing the 3 apps in to workspace
                for id in app_id:
                    apps = install_apps(access_token, id, workspace)
                    # the new app_id are now added to the list
                    new_app_id.append(apps)                   
                # getting Relationship app
                seller_app_id = new_app_id[0]
                closings_app_id = new_app_id[1]
                relationship_app = new_app_id[2]
                print("Apps installed")
                color_code_index = 0
                org_url_label = get_organisations_url_label(access_token,org_id)
                # updating button scripts
                button_update_seller_app(access_token,workspace_name,seller_app_id,org_url_label)
                button_update_closings_app(access_token,workspace_name,closings_app_id,org_url_label)
                button_update_relationship_app(access_token,workspace_name,relationship_app,org_url_label)             
                # getting the google sheet data
                socketio.emit("update progress",25)
                for county in counties_list:
                    if county != 'None':
                        try:
                            data = sheet_data_extraction(county)
                            print(data)
                            cities = data[0]
                            zip_code = data[1]
                            section = data[2]         
                            # add county section to app field
                            app_field_create(access_token,relationship_app,section,color_code_index,f"{county} Section")
                            # add county cities to app field
                            app_field_create(access_token,relationship_app,cities,color_code_index,f"{county} Cities")
                            # add county zipcode to app field
                            app_field_create(access_token,relationship_app,zip_code,color_code_index,f"{county} Zip Codes")
                            color_code_index += 1            
                        except:
                            continue    
                # deleting atlanta and essex details from app
                delete_field(access_token, relationship_app,0)
                print('essex deleted')
                delete_field(access_token, relationship_app,3)
                print('atlantic deleted')
                # update app market value with county name
                update_market(access_token, relationship_app, counties_list)
                interested_zip_code_update(access_token,relationship_app)
                with open('script.txt','w') as file:
                    file.write('" "')
                file.close()
                if click_send == 'clicksend':
                    clicksend_field(access_token,closings_app_id)
                socketio.emit("update progress",50)
                driver = refresh_podio()
                for county in counties_list:
                    if county != 'None':
                        print("section flow started ======>")
                        flow_creation(driver,relationship_app,county,f"{county} section create",'Section')
                        flow_updation(driver,relationship_app,county,f"{county} section update",'Section')
                        socketio.emit("update progress",60)
                        print("section flow ended ======>")
                        print("city flow started ======>")
                        flow_creation(driver,relationship_app,county,f"{county} city create",'Cities')
                        flow_updation(driver,relationship_app,county,f"{county} city update",'Cities')
                        print("city flow ended ======>")
                        socketio.emit("update progress",70)
                        print("zipcode flow started ======>")
                        flow_creation(driver,relationship_app,county,f"{county} zipcode create",'Zip Codes')
                        flow_updation(driver,relationship_app,county,f"{county} zipcode update",'Zip Codes')
                        socketio.emit("update progress",80)
                print("Seller app flow started =======>")
                seller_app_flow(driver,seller_app_id,1)
                seller_app_flow(driver,seller_app_id,2)
                socketio.emit("update progress",90)
                print("Seller app flow ended ========>")
                print("Closings app flow started ====>")
                closings_app_flow_1(driver,closings_app_id,1)
                if click_send == 'clicksend':
                    closing_click_send(driver,closings_app_id,1)
                closings_app_flow_2(driver,closings_app_id)
                print("Closings app flow ended ========>")
                driver.quit()
                socketio.emit("update progress",100)
                return redirect("/?message=Success")
            else:
                return redirect("/?message=User don't have right to add workspace ")
        else:
            return redirect(f"/?message=Username or Password not valid")
@app.route("/submit2", methods=["POST"])
def submit2():
    if request.method == "POST":
        # getting username
        username = request.form.get("username")
        # getting password
        password = request.form.get("password")
        # getting organisation
        organisation = request.form.get("organisation")
        # getting  workspace name
        workspace_name = request.form.get("workspace_name")
        # checking click send check box
        click_send = request.form.get('clicksend')
        socketio.emit("update progress",10)
        # getting access token of podio
        token = get_access_token(username,password)
        if token:
            org_id = int(organisation)
            workspace = create_workspace(token, org_id, workspace_name)
            print("workspace",workspace)
            if workspace:
                app_id = 28602483
                new_app = install_apps(token, app_id, workspace)
                print('new com app id ',new_app)
                if click_send == 'clicksend':
                    clicksend_field(token,new_app)
                socketio.emit("update progress",40)
                driver = refresh_podio()
                socketio.emit("update progress",50)
                flow_creation_commercial_app(driver,new_app,1)
                socketio.emit("update progress",75)
                flow_creation_commercial_app(driver,new_app,2)
                socketio.emit("update progress",90)
                if click_send == 'clicksend':
                    closing_click_send(driver,new_app,2)
                socketio.emit("update progress",100)
                return redirect("/commercial_app?message=Success")
            return redirect("/commercial_app?message=Not Success")
@app.route("/file/<item_id>/<username>/<password>/<option>")
def click_send_api(item_id,username,password,option): 
    print(item_id,username,password,option)
    # calling click send function
    click_send_function(item_id,username,password,option)
    # removing the intrestedinvestors file from project directory
    os.remove("interestedinvestor.xlsx")
    return 'Added'
@app.route("/reiaethos/<item_id>/<address>/<asset_type>")
def bigquery_function(item_id,address,asset_type):
    print(item_id,address,asset_type)
    asset_types = tuple(asset_type.split(","))
    bigquery_data(address,asset_types)
    id = int(item_id)
    file_upload(id)
    return 'File Uploaded'
    
if __name__ == "__main__":
    socketio.run(app=app,host='0.0.0.0', port='5043',debug=True) # for local
    # socketio.run(app=app,host='0.0.0.0', port='5043',debug=False) # for server
    
