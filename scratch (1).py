import os.path
import pikepdf as pkdf
import datetime
from exif import Image
import socket
import re, uuid

mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


def file_Logs(user_file_type, user_file_name, device_mac, device_ip, new_final_file_name):
    if os.path.exists('File Logs.txt'):
        with open('File Logs.txt', 'a') as file_logs:
            file_logs.write(f'\nTime: {str(datetime.datetime.now())}\n')
            file_logs.write(f'File Type: {user_file_type}\n')
            file_logs.write(f'User File Name: {user_file_name}\n')
            file_logs.write(f'Device MAC: {device_mac}\n')
            file_logs.write(f'Device IP: {device_ip}\n')
            file_logs.write(f'New File Name: {new_final_file_name}\n')

    else:
        with open('File Logs.txt', 'w') as file_logs:

            file_logs.write(f'\nTime: {str(datetime.datetime.now())}\n')
            file_logs.write(f'File Type: {user_file_type}\n')
            file_logs.write(f'User File Name: {user_file_name}\n')
            file_logs.write(f'Device MAC: {device_mac}\n')
            file_logs.write(f'Device IP: {device_ip}\n')
            file_logs.write(f'New File Name: {new_final_file_name}\n')


def img_File(img_file_name):
    global mac , hostname , ip

    img = Image(img_file_name)
    img.model = hostname+", "+mac+", "+ip

    with open('cam2.jpg', 'wb') as new_img_file:
        new_img_file.write(img.get_file())

    return img.model ,ip,'cam2.jpg'

# Pike PDF

def pdf_File(pdf_file_name):
    global mac , hostname , ip
    open_pdf = pkdf.open(pdf_file_name)
    get_metadata = open_pdf.open_metadata()
    host_mac= hostname+", "+mac

    with open_pdf.open_metadata() as edit_metadata:
        edit_metadata['dc:device_ID'] = ip
        edit_metadata['dc:mac_hostname']= host_mac

    new_pdf_file_name = f'output({pdf_file_name}).pdf'
    open_pdf.save(new_pdf_file_name)

    return host_mac, ip, new_pdf_file_name


while True:
    user_choice = int(input("Enter your choice for the filetype:  \n" 
                            "1. Image "
                            "2. PDF "
                            "3. Exit: "))

    # For image file
    if user_choice == 1:

        file_name_input = input("Enter image file name: ")
        device_mac,ip, new_file_name = img_File(file_name_input)
        file_Logs(user_choice, file_name_input, device_mac,ip,new_file_name)
        # img_File(image_file_name)
    
    # For pdf file
    elif user_choice == 2:

        file_name_input = input("Enter pdf file name: ")
        device_mac, ip, new_file_name = pdf_File(file_name_input)
        print(f'PDF Metadata below: {pdf_File(file_name_input)}')

        file_Logs(user_choice, file_name_input,device_mac,ip , new_file_name)

    else:
        break
