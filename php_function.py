import openpyxl
sheet = "sheets/Zips for Podio V3.xlsx"

def php_code_generate(county,key,field,item_value):
    
    value1 = f"""foo();
function foo(){{

$zip = explode(",",[*item_value_{item_value}*] );

$area = array (\n """

    value3 = """ );

foreach($zip as $value)
{
$data=$area[$value];
foreach($data as $value1){$finaldata.=",".$value1;}
}

$county= array_unique(explode(",",trim($finaldata,",")));
$finaldata="";
foreach($county as $value2){$finaldata.=",".$value2;}
return trim($finaldata,",");
}\n"""
    def value_extraction(list):
        string = ""
        for i in range(len(list)):
            list_value = str(list[i])
            if "'" in list_value:
                list_value = list[i].replace("'"," ")
            value = f"{i} => '{list_value}',\n"
            string = string + value 
        string = string + '),\n'
        return string
        
    def key_value_extraction(section):
        print("Inside Key Value Extraction")
        value2 = ""
        for k,v in section.items():
            k = str(k)
            if "'" in k:
                k = k.replace("'"," ")
            value_k = f"""'{k}' => 
    array (\n"""
            value_v = value_extraction(v)
            value2 = value2 + value_k + value_v
        value2 = value2 + "\n"
        php_function = value1 + value2 + value3
        return php_function

    def sheet_data_extraction(county):
        dataframe = openpyxl.load_workbook(sheet)
        worksheet = dataframe.active
        dict = {}
        for row in worksheet.iter_rows(min_row=2, values_only=True):
            if county in row[4]:
                name = row[key]
                if key == 2:
                    zip_code = row[1]
                else:
                    zip_code = row[2]
                if name not in dict:
                    dict[name] = [zip_code]
                else:
                    dict[name].append(zip_code)
        print("PHP code creation started")
        data= key_value_extraction(dict)
        return data
    data = sheet_data_extraction(county)
    return data
    
       
       
       