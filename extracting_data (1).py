import pikepdf as pkdf
import socket
import re, uuid
from exif import Image

# fetching device macaddress and ipaddress
# mac=':'.join(re.findall('..', '%012x' % uuid.getnode()))
# hostname = socket.gethostname()

def extract_image_meta_data(img_file_name):
    img = Image(img_file_name)

    if img.get('model') is not None:
        get_ip_val = img.get('model')

        return f'The extracted details from the given image file are {get_ip_val}'

    else:
        return 'No mac address found'

def extract_pdf_meta_data(pdf_file_name):
    open_pdf = pkdf.open(pdf_file_name)

    get_meta_data = open_pdf.open_metadata()

    if get_meta_data['dc:device_ID'] is not None:
        get_ip_val = get_meta_data['dc:device_ID']
        if get_meta_data['dc:mac_hostname'] is not None:
            get_mac_val = get_meta_data['dc:mac_hostname']

            return f'The extracted IP is {get_ip_val} and Host Name & Mac address is {get_mac_val}'

        else:
            return f'The extracted IP is {get_ip_val}'

    else:
        return 'No IP found!'


while True:
    user_choice = int(input("Enter the number for the filetype:  \n" 
                            "1. IMG "
                            "2. PDF "
                            "3. Exit: "))

    # For image file
    if user_choice == 1:
        user_input_file = input("Enter file name: ")
        print(extract_image_meta_data(user_input_file))

    elif user_choice == 2:
        user_input_file = input("Enter file name: ")
        print(extract_pdf_meta_data(user_input_file))

    else:
        break

