import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from php_function import php_code_generate
# from pyvirtualdisplay import Display
# display = Display(visible=1, extra_args=['-s', '0'])
# display.start()

#  Refreshing is requried after creating a workspace then only the workspace will list on workflow
def refresh_podio():
    print("\n REFRESHING STARTED -------------------")
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    browser_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
    options.add_argument(f"user-agent={browser_agent}")
    service = Service(executable_path="chromedriver.exe") # for local
    # service = Service(executable_path="/var/www/html/podio_webapp/chromedriver")  # for server
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://workflow-automation.podio.com/")
    # click login
    driver.implicitly_wait(5)
    try:
        loginEle = driver.find_element(By.XPATH, "//a[.='LOGIN']")
        loginEle.click()
    except:
        print("in login exec")
        driver.implicitly_wait(5)
        # driver.get_screenshot_as_file("login-exec.png")
        loginEle = driver.find_element(By.XPATH, "//a[.='LOGIN']")
        loginEle.click()
    # wait for login form to render
    driver.implicitly_wait(5)
    # fill login form
    try:
        elem = driver.find_element(By.NAME, "email")
        elem.send_keys("Silver@investoffmarket.com")
    except:
        print("in email exec")
        driver.implicitly_wait(5)
        elem = driver.find_element(By.NAME, "email")
        elem.send_keys("Silver@investoffmarket.com")

    elem = driver.find_element(By.NAME, "password")
    elem.send_keys("Realestate23B@")
    driver.find_element(By.ID, "loginFormSignInButton").click()
    # wait till account option render
    driver.implicitly_wait(5)
    # click on Admin TCO account
    try:
        driver.find_element(By.XPATH, "//span[.='Admin TCO']").click()
    except:
        print("in tco exec")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//span[.='Admin TCO']").click()
    print("Refreshing Podio --------------- ")
    # to refresh the site
    driver.get("https://workflow-automation.podio.com/buildtree.php")
    time.sleep(15)
    print("REFRESHING ENDED --------------------")
    return driver
    
# function to create the flow to automatically the select values when item is created    
def  flow_creation(driver,app_id,county,flowname,field):   
    if field == "Section":
        key = 3
    elif field == "Cities":
        key = 1
    elif field == "Zip Codes":
        key = 2   
    # to generate php code for the flow    
    county_name = county.lower()
    print(county_name)
    county_name = county_name.replace(",",'')
    county_name = county_name.replace(' ','-')
    field_name = field.lower()
    item_value = county_name+'-'+field_name
    item_value = item_value.replace(" ",'-')
    print(item_value)
    # to generate php code for the flow    
    php_function = php_code_generate(county,key,field,item_value)
    # print(php_function)  
    print ("\n STARTING SELENIUM CREATION -------------------")
    # open add flow page 
    print("app_id=====>",app_id)
    driver.get(f"https://workflow-automation.podio.com/configureflow.php?i={app_id}&t=C")
    # wait till form render
    # wait.until(EC.element_to_be_clickable((By.ID, 'saveButton')))
    driver.implicitly_wait(5)
    # driver.get_screenshot_as_file("workflowpage.png")
    print ("\n WRITING FLOWNANE -------------------")
    # fill data into flowname field
    elem = driver.find_element(By.ID, "flowName")
    elem.send_keys(flowname)
    driver.implicitly_wait(5) 
    elem = driver.find_element(By.XPATH,"//*[@id='actions']/div/div[1]/a").click()
    driver.implicitly_wait(5)
    try:
        print("Inside Try.......")
        custom_calc_options = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='sidebarblock advancedbrick']/small[@class='brickdescription']")))
        # selecting custom variable in action 
        driver.execute_script("arguments[0].click();", custom_calc_options[8])
        driver.implicitly_wait(5)
        variable_name = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Variable Name"]')
        variable_name.send_keys("data")
        time.sleep(5)
        php_code = driver.find_element(By.CSS_SELECTOR,'textarea[class="xgmcalc"]')
        php_code.send_keys(php_function)
        time.sleep(5)
        driver.get_screenshot_as_file("afterphpfunctioncreation.png")
        # selecting update variable in action
        elem = driver.find_element(By.XPATH,"//*[@id='actions']/div/div[1]/a").click()
        update_item_field = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='sidebarblock hasapp']/small[@class='brickdescription']")))
        driver.implicitly_wait(5)
        driver.execute_script("arguments[0].click();", update_item_field[3])
        driver.implicitly_wait(5)
        field_value_1 = driver.find_element(By.XPATH,"//td[@class='stepLeader']//select")
        driver.implicitly_wait(5)
        field_value_1 = Select(field_value_1)
        driver.implicitly_wait(5)
        if field != 'Zip Codes':
            value_field_item =county +' Zip Codes'
        else:
            value_field_item =county +' Cities'
        driver.implicitly_wait(5)
        print(value_field_item)
        field_value_1.select_by_visible_text(value_field_item)
        driver.implicitly_wait(5)
        field_value_2 = driver.find_element(By.XPATH,"//td[@class='stepMiddle']//select")
        field_value_2 = Select(field_value_2)
        field_value_2.select_by_index(2)
        driver.implicitly_wait(5)
        field_value_3 = driver.find_element(By.XPATH,'//*[@id="gmvalue2_1"]')        
        if field != 'Zip Codes':        
            field_value_3.send_keys(f'[*item_value_{county_name}-zip-codes*].&#34;,&#34;.[*item_value_pfprepfield:data*]')        
        else:
            field_value_3.send_keys(f'[*item_value_{county_name}-cities*].&#34;,&#34;.[*item_value_pfprepfield:data*]')                   
        driver.implicitly_wait(3)
    except Exception as e:
        print(e)
    # submit form (click save button)
    driver.find_element(By.XPATH,"//a[.='Save']").click()
    driver.implicitly_wait(3)
    print ("\n END SELENIUM CREATION -------------------")

# function to create the flow to automatically the select values when item is updated    
def flow_updation(driver,app_id,county,flowname,field):
    if field == "Section":
        key = 3
    elif field == "Cities":
        key = 1
    elif field == "Zip Codes":
        key = 2    
    # to generate php code for the flow    
    county_name = county.lower()
    print(county_name)
    county_name = county_name.replace(",",'')
    county_name = county_name.replace(' ','-')
    field_name = field.lower()
    item_value = county_name+'-'+field_name
    item_value = item_value.replace(" ",'-')
    print(item_value)
    # to generate php code for the flow    
    php_function = php_code_generate(county,key,field,item_value)  
    # print(php_function)
    print ("\n STARTING SELENIUM UPDATION -------------------")
    # open add flow page 
    print("app_id=====>",app_id)
    driver.get(f"https://workflow-automation.podio.com/configureflow.php?i={app_id}&t=C")
    # wait till form render
    driver.implicitly_wait(5)
    print ("\n WRITING FLOWNANE -------------------")
    # fill data into flowname field
    elem = driver.find_element(By.ID, "flowName")
    elem.send_keys(flowname)
    driver.implicitly_wait(5)
    trigger_type = driver.find_element(By.XPATH,"//*[@id='triggerType']")
    trigger_type = Select(trigger_type)
    driver.implicitly_wait(5)
    trigger_type.select_by_value("U")
    driver.implicitly_wait(5)
    elem = driver.find_element(By.XPATH,"//*[@id='actions']/div/div[1]/a").click()
    driver.implicitly_wait(5)
    try:
        print("Inside Try.......")
        custom_calc_options = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='sidebarblock advancedbrick']/small[@class='brickdescription']")))
        # selecting custom variable in action 
        driver.execute_script("arguments[0].click();", custom_calc_options[8])
        driver.implicitly_wait(5)
        driver.implicitly_wait(5)
        variable_name = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Variable Name"]')
        variable_name.send_keys("data")
        time.sleep(5)
        php_code = driver.find_element(By.CSS_SELECTOR,'textarea[class="xgmcalc"]')
        php_code.send_keys(php_function)
        time.sleep(5)
        driver.get_screenshot_as_file("afterphpfunctionupdation.png")
        # selecting update variable in action
        elem = driver.find_element(By.XPATH,"//*[@id='actions']/div/div[1]/a").click()
        update_item_field = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='sidebarblock hasapp']/small[@class='brickdescription']")))
        driver.implicitly_wait(5)
        driver.execute_script("arguments[0].click();", update_item_field[3])
        driver.implicitly_wait(5)
        field_value_1 = driver.find_element(By.XPATH,"//td[@class='stepLeader']//select")
        driver.implicitly_wait(5)
        field_value_1 = Select(field_value_1)
        driver.implicitly_wait(5)
        if field != 'Zip Codes':
            value_field_item =county +' Zip Codes'
        else:
            value_field_item =county +' Cities'
        driver.implicitly_wait(5)
        print(value_field_item)
        field_value_1.select_by_visible_text(value_field_item)
        driver.implicitly_wait(5)
        field_value_2 = driver.find_element(By.XPATH,"//td[@class='stepMiddle']//select")
        field_value_2 = Select(field_value_2)
        field_value_2.select_by_index(2)
        driver.implicitly_wait(5)
        field_value_3 = driver.find_element(By.XPATH,'//*[@id="gmvalue2_1"]')        
        if field != 'Zip Codes':        
            field_value_3.send_keys(f'[*item_value_{county_name}-zip-codes*].&#34;,&#34;.[*item_value_pfprepfield:data*]')        
        else:
            field_value_3.send_keys(f'[*item_value_{county_name}-cities*].&#34;,&#34;.[*item_value_pfprepfield:data*]')                   
        driver.implicitly_wait(3)
    except Exception as e:
        print(e)
    # submit form (click save button)
    driver.find_element(By.XPATH,"//a[.='Save']").click()
    driver.implicitly_wait(5)
    print ("\n END SELENIUM UPDATION -------------------")
    
# code for to create automation of seller app
# if flow number is 1 then create flow for to move seller lead to closings
# if flow number is 2 then create the flow to genarate the excel sheet 
def seller_app_flow(driver,app_id,flow_number):
    
    driver.get('https://workflow-automation.podio.com/flows.php?app=28794198')
    time.sleep(1)
    if flow_number == 1:
        driver.find_element(By.XPATH,'//*[@id="appFlows"]/div[3]').click()
        driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/h4/span/ul/li/a').click()
        driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/h4/span/ul/li/ul/li[1]/a').click()
    else:
        driver.find_element(By.XPATH,'//*[@id="appFlows"]/div[4]').click()
        driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/h4/span/ul/li/a').click()
        driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/h4/span/ul/li/ul/li[1]/a').click()        
    time.sleep(2)
    #selecting the seller app of the new workspace
    seller_app_select = driver.find_element(By.ID,'xcopy_to')
    seller_app_select = Select(seller_app_select)
    seller_app_select.select_by_value(f'{app_id}')
    time.sleep(1)
    #click copy button
    driver.find_element(By.XPATH,'//*[@id="simplemodal-data"]/form/input[2]').click()
    if flow_number == 1:
        time.sleep(2)
    else:
        time.sleep(7)
        trigger_type = driver.find_element(By.XPATH,"//*[@id='triggerType']")
        trigger_type = Select(trigger_type)
        trigger_type.select_by_value("C")
    #click on save button
    driver.find_element(By.ID,'saveButton').click()
    time.sleep(1)
    
def closings_app_flow_1(driver,app_id,value):
    driver.get('https://workflow-automation.podio.com/flows.php?app=28794199')
    time.sleep(1)
    if value == 1:
        driver.find_element(By.XPATH,'//*[@id="appFlows"]/div[2]').click()
    else:
        driver.find_element(By.XPATH,'//*[@id="appFlows"]/div[3]').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/h4/span/ul/li/a').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/h4/span/ul/li/ul/li[1]/a').click()
    time.sleep(2)
    #selecting the seller app of the new workspace
    closings_app_select = driver.find_element(By.ID,'xcopy_to')
    closings_app_select = Select(closings_app_select)
    closings_app_select.select_by_value(f'{app_id}')
    time.sleep(1)
    #click copy button
    driver.find_element(By.XPATH,'//*[@id="simplemodal-data"]/form/input[2]').click()
    time.sleep(7)
    #click on save button
    driver.find_element(By.ID,'saveButton').click()
    time.sleep(1)
    
def closings_app_flow_2(driver,app_id):   
    driver.get('https://workflow-automation.podio.com/flows.php?app=28794199')
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="appFlows"]/div[4]').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/h4/span/ul/li').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/h4/span/ul/li/ul/li[1]/a').click()
    time.sleep(1)
    closings_app_select = driver.find_element(By.ID,'xcopy_to')
    closings_app_select = Select(closings_app_select)
    closings_app_select.select_by_value(f'{app_id}')
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="simplemodal-data"]/form/input[2]').click()
    driver.implicitly_wait(7)
    # selecting the another flow
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/form/div[1]/div[2]/div[3]/div/ul/li[3]/div/div[2]/div/table/tbody/tr/td[2]/select').click()
    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(1)
    #click on save button   
    driver.find_element(By.ID,'saveButton').click()
    time.sleep(1)
    
def closing_click_send(driver,app_id,option):
    driver.get('https://workflow-automation.podio.com/flows.php?app=28794199')
    time.sleep(1)  
    driver.find_element(By.XPATH,'//*[@id="appFlows"]/div[3]').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/h4/span/ul/li/a').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/h4/span/ul/li/ul/li[1]/a').click()
    time.sleep(2)
    #selecting the seller app of the new workspace
    closings_app_select = driver.find_element(By.ID,'xcopy_to')
    closings_app_select = Select(closings_app_select)
    closings_app_select.select_by_value(f'{app_id}')
    time.sleep(1)  
    driver.find_element(By.XPATH,'//*[@id="simplemodal-data"]/form/input[2]').click()
    # select click send field
    click_send = driver.find_element(By.NAME,'fields1')
    click_send = Select(click_send)
    click_send.select_by_visible_text('Click Send')
    time.sleep(2)
    # select click send value field
    click_send_value = driver.find_element(By.NAME,'input1')
    click_send_value = Select(click_send_value)
    click_send_value.select_by_value('Push Values  ----> Click Send')
    time.sleep(2)
    # giving api call value
    url = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/form/div[1]/div[2]/div[3]/div/ul/li/div/div[2]/div/table/tbody/tr[2]/td[2]/div[1]/div/textarea')
    url.clear()
    url.send_keys(f'http://191.235.35.183:5043/file/[*item_value_podio_item_id*]/[*item_value_click-send-username*]/[*item_value_click-send-password*]/{option}')
    time.sleep(1)
    #click on save button
    driver.find_element(By.ID,'saveButton').click()
    time.sleep(1)

# Function to download an podio item pdf      
def file_download(file_link):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    browser_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
    options.add_argument(f"user-agent={browser_agent}")
    service = Service(executable_path="chromedriver.exe") # for local
    # service = Service(executable_path="/var/www/html/podio_webapp/chromedriver")  # for server
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://podio.com/login')
    time.sleep(1)
    # username and password 
    email = driver.find_element(By.NAME,'email')
    email.send_keys('Silver@investoffmarket.com')
    password = driver.find_element(By.NAME,'password')
    password.send_keys('Realestate23B@')
    #login button
    driver.find_element(By.ID,'loginFormSignInButton').click()
    time.sleep(2)
    # Trigger the file download
    driver.get(file_link)
    time.sleep(5)  
    print("File Downloaded")
    # Use requests to fetch the content of the downloaded fil
    driver.quit()
    
# Function to create flow for commercial app 
def flow_creation_commercial_app(driver,app_id,option):
    if option == 1:
        print("Stated Commercial App flow 1")
    driver.get("https://workflow-automation.podio.com/flows.php?app=28602483")
    time.sleep(1)
    if option == 1:
        driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/div/div[2]").click()
    else:
        driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div[2]/div[1]/div/div/div[3]").click()  
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/h4/span/ul/li").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div/h4/span/ul/li/ul/li[1]/a").click()
    com_app_select = driver.find_element(By.ID,'xcopy_to')
    com_app_select = Select(com_app_select)
    com_app_select.select_by_value(f'{app_id}')
    driver.find_element(By.XPATH,'//*[@id="simplemodal-data"]/form/input[2]').click()
    time.sleep(5)
    driver.find_element(By.ID,'saveButton').click()
    time.sleep(1)
    