import requests
from bs4 import BeautifulSoup
from tqdm import tqdm



##### constants
item_url = 'https://www.dmv.virginia.gov/dmvnet/common/router.asp'
validation_url = 'https://www.dmv.virginia.gov/dmvnet/plate_purchase/select_plate.asp'
available = 'Congratulations.  The message you requested is available.'
not_available = 'If you have reserved this message or it is on a vehicle you own, click Purchase Plate Now; if not, try a new message.'
censored = 'Personalized message requested is not available. Please try another message.'


# Input your desired license plate name, and this function
# makes a request to the dmv's website to check the plate availability
# returns a string whether your plate is available or nah

def Request_DMV(name):
    if(len(name) > 9 or len(name) < 0):
        return "Your license plate name needs to be 8 or less characters"

    letters = [None] * 8

    i=0
    while i < len(name): # loop through the name
        if (name[i] != ' '): # if we have a space in the name, keep the None in our letter array
            letters[i] = name[i]
        i += 1
    
    item_request_body = {
    'TransType': 'INQ',
    'TransID': 'RESINQ',
    'ReturnPage': '/dmvnet/plate_purchase/s2end.asp',
    'HelpPage': None, 
    'Choice': 'A',
    'PltNo': name,  
    'HoldISA': 'N',
    'HoldSavePltNo': None,
    'HoldCallHost': None,
    'NumCharsInt': '8',
    'CurrentTrans': 'plate_purchase_reserve',
    'PltType': 'SNAUT',
    'PltNoAvail': None,
    'PersonalMsg': 'Y',
    'Let1': letters[0],
    'Let2': letters[1],
    'Let3': letters[2],
    'Let4': letters[3],
    'Let5': letters[4],
    'Let6': letters[5],
    'Let7':  letters[6],
    'Let8':  letters[7],
    }

    session = requests.Session()
    form_response = session.get(validation_url) # get the form page
    response = session.post(url=item_url, data=item_request_body,
                            headers={'Referer': form_response.url})
    soup = BeautifulSoup(response.content, features="html.parser")
    if(not soup.body):
        return "Error with the connection or invalid characters supplied in the plate name."

    r = soup.body.findAll(text=available)
    if(len(r) > 0):
        return "Available"
    else:
        r = soup.body.findAll(text=not_available)
        if(len(r) > 0):
            return "Plate Taken."
        else:
            r = soup.body.findAll(text=censored)
            if(len(r) > 0):
                return "Plate censored."
            else: 
                "Request failed."



def Go_Through_Textfile(file_name):
    num_lines = sum(1 for line in open(file_name,'r'))
    with open(file_name) as f:
        for line in tqdm(f, total=num_lines):
            checked = Request_DMV(line)
            with open("output.txt", "a") as myfile:
                my_plate = line.rstrip() + " - " + checked + "\n"
                myfile.write(my_plate)




my_file = '/Users/awad/Coding/Personal_Projects/licenseplate/input.txt'
Go_Through_Textfile(my_file)



