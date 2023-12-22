

import clicksend_client
from clicksend_client.rest import ApiException




def click_send():
    configuration = clicksend_client.Configuration()
    configuration.username = 'admin@dealflyte.io'
    configuration.password = '78C7FBDC-F601-2A52-C03C-6959E13F0716'
    # create an instance of the API class
    api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
    contact = clicksend_client.Contact(
                phone_number='2121231234',
                first_name='test ',
                custom_1='none',
            )
    try:
        api_response = api_instance.lists_contacts_by_list_id_post(contact, 2338468)
        print(api_response)
    except ApiException as e:
        print("Exception when calling ContactListApi->lists_post: %s\n" % e)
        
        
click_send()