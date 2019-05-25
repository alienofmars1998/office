import pandas as pd
import re
import csv
from tempfile import NamedTemporaryFile
import os
from os import path
import shutil


def marge():
    validatePhn()
    locations = pd.read_csv('Office_Locations.csv')
    services = pd.read_csv('Office_Services.csv')
    offices = pd.read_csv('offices.csv')
    sername = pd.read_csv('services.csv')

    merged1 = pd.merge(services, offices, how='left', on='OfficeID')
    merged2 = pd.merge(merged1, sername, how='left', on='ServiceID')
    merged3 = pd.merge(merged2, locations, how='left', on='OfficeID')

    merged3.to_csv('office_service_locations.csv', index=False)
    validatePhn()
    f = pd.read_csv("office_service_locations.csv")
    keep_col = ['OfficeServiceID', 'OfficeID', 'ServiceName', 'OfficeID', 'Contact Name', 'Suburb', 'Phone Number', 'Email', 'Lat', 'Lon']
    new_f = f[keep_col]
    new_f.to_csv("office_service_locations.csv", index=False)

def validatePhn():
    filename = 'offices.csv'
    tempfile = 'testtest.csv'

    fields = ['OfficeID', 'Contact Name', 'Suburb', 'State', 'Postcode', 'Phone Number', 'Email']
    with open(filename, 'r') as csvfile, open(tempfile,'w', newline='') as tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)

        regex1 = "\(\+\d{2}\) \d{2} \d{8}"
        regex2 = "\d{4} \d{4}"
        regex3 = "^\d{8}$"
        regex4 = "\+\d{2} \d{1} \d{4} \d{4}"
        regex5 = "\d{2} \d{4} \d{4}"
        regex6 = "^\d{11}$"
        regex7 = "\(\d{2}\) \d{1} \d{4} \d{4}"
        regex8 = "^\d{9}$"
        regex9 = "^\d{10}$"
        regex10 = "\d{3} \d{3} \d{4}"
        regex11 = "\(\d{2}\) \d{4} \d{4}"
        regex12 = "\d{4} \d{1} \d{4} \d{4}"

        for row in reader:
            if re.match(regex1, row['Phone Number']):
                print(row['Phone Number'])

            if re.match(regex2, row['Phone Number']):
                tem = row['Phone Number'].split(" ")
                if row['State'] == str("NSW"):
                    row['Phone Number'] = "(+61) " + "02 " + tem[0] + tem[1]
                if row['State'] == str("VIC"):
                    row['Phone Number'] = "(+61) " + "03 " + tem[0] + tem[1]
                if row['State'] == str("QLD"):
                    row['Phone Number'] = "(+61) " + "07 " + tem[0] + tem[1]
                if row['State'] == str("SA"):
                    row['Phone Number'] = "(+61) " + "09 " + tem[0] + tem[1]

            if re.match(regex3, row['Phone Number']):
                if row['State'] == str("NSW"):
                    row['Phone Number'] = "(+61) " + "02 " + row['Phone Number']
                if row['State'] == str("VIC"):
                    row['Phone Number'] = "(+61) " + "03 " + row['Phone Number']
                if row['State'] == str("QLD"):
                    row['Phone Number'] = "(+61) " + "07 " + row['Phone Number']
                if row['State'] == str("SA"):
                    row['Phone Number'] = "(+61) " + "09 " + row['Phone Number']


            if re.match(regex4, row['Phone Number']):
                tem = row['Phone Number'].split(" ")
                if row['State'] == str("NSW"):
                    row['Phone Number'] = "(+61) " + "02 " + tem[2] + tem[3]
                if row['State'] == str("VIC"):
                    row['Phone Number'] = "(+61) " + "03 " + tem[2] + tem[3]
                if row['State'] == str("QLD"):
                    row['Phone Number'] = "(+61) " + "07 " + tem[2] + tem[3]
                if row['State'] == str("SA"):
                    row['Phone Number'] = "(+61) " + "09 " + tem[2] + tem[3]


            if re.match(regex5, row['Phone Number']):
                tem = row['Phone Number'].split(" ")
                if row['State'] == str("NSW"):
                    row['Phone Number'] = "(+61) " + "02 " + tem[1] + tem[2]
                if row['State'] == str("VIC"):
                    row['Phone Number'] = "(+61) " + "03 " + tem[1] + tem[2]
                if row['State'] == str("QLD"):
                    row['Phone Number'] = "(+61) " + "07 " + tem[1] + tem[2]
                if row['State'] == str("SA"):
                    row['Phone Number'] = "(+61) " + "09 " + tem[1] + tem[2]

            if re.match(regex6, row['Phone Number']):
                if row['State'] == str("NSW"):
                    row['Phone Number'] = "(+61) " + "02 " + row['Phone Number'][-8:len(row['Phone Number'])]
                if row['State'] == str("VIC"):
                    row['Phone Number'] = "(+61) " + "03 " + row['Phone Number'][-8:len(row['Phone Number'])]
                if row['State'] == str("QLD"):
                    row['Phone Number'] = "(+61) " + "07 " + row['Phone Number'][-8:len(row['Phone Number'])]
                if row['State'] == str("SA"):
                    row['Phone Number'] = "(+61) " + "09 " + row['Phone Number'][-8:len(row['Phone Number'])]

            if re.match(regex7, row['Phone Number']):
                tem = row['Phone Number'].split(" ")
                if row['State'] == str("NSW"):
                    row['Phone Number'] = "(+61) " + "02 " + tem[2] + tem[3]
                if row['State'] == str("VIC"):
                    row['Phone Number'] = "(+61) " + "03 " + tem[2] + tem[3]
                if row['State'] == str("QLD"):
                    row['Phone Number'] = "(+61) " + "07 " + tem[2] + tem[3]
                if row['State'] == str("SA"):
                    row['Phone Number'] = "(+61) " + "09 " + tem[2] + tem[3]
                

            if re.match(regex8, row['Phone Number']):
                if row['State'] == str("NSW"):
                    row['Phone Number'] = "(+61) " + "02 " + row['Phone Number'][-8:len(row['Phone Number'])]
                if row['State'] == str("VIC"):
                    row['Phone Number'] = "(+61) " + "03 " + row['Phone Number'][-8:len(row['Phone Number'])]
                if row['State'] == str("QLD"):
                    row['Phone Number'] = "(+61) " + "07 " + row['Phone Number'][-8:len(row['Phone Number'])]
                if row['State'] == str("SA"):
                    row['Phone Number'] = "(+61) " + "09 " + row['Phone Number'][-8:len(row['Phone Number'])]

            if re.match(regex9, row['Phone Number']):
                if row['State'] == str("NSW"):
                    row['Phone Number'] = "(+61) " + "02 " + row['Phone Number'][-8:len(row['Phone Number'])]
                if row['State'] == str("VIC"):
                    row['Phone Number'] = "(+61) " + "03 " + row['Phone Number'][-8:len(row['Phone Number'])]
                if row['State'] == str("QLD"):
                    row['Phone Number'] = "(+61) " + "07 " + row['Phone Number'][-8:len(row['Phone Number'])]
                if row['State'] == str("SA"):
                    row['Phone Number'] = "(+61) " + "09 " + row['Phone Number'][-8:len(row['Phone Number'])]

            if re.match(regex10, row['Phone Number']):
                if row['State'] == str("NSW"):
                    row['Phone Number'] = "(+61) " + "02 " + row['Phone Number'].replace(" ", "")[
                                                             -8:len(row['Phone Number'])]
                if row['State'] == str("VIC"):
                    row['Phone Number'] = "(+61) " + "03 " + row['Phone Number'].replace(" ", "")[
                                                             -8:len(row['Phone Number'])]
                if row['State'] == str("QLD"):
                    row['Phone Number'] = "(+61) " + "07 " + row['Phone Number'].replace(" ", "")[
                                                             -8:len(row['Phone Number'])]
                if row['State'] == str("SA"):
                    row['Phone Number'] = "(+61) " + "09 " + row['Phone Number'].replace(" ", "")[
                                                             -8:len(row['Phone Number'])]
                

            if re.match(regex11, row['Phone Number']):
                tem = row['Phone Number'].split(" ")
                if row['State'] == str("NSW"):
                    row['Phone Number'] = "(+61) " + "02 " + tem[1] + tem[2]
                if row['State'] == str("VIC"):
                    row['Phone Number'] = "(+61) " + "03 " + tem[1] + tem[2]
                if row['State'] == str("QLD"):
                    row['Phone Number'] = "(+61) " + "07 " + tem[1] + tem[2]
                if row['State'] == str("SA"):
                    row['Phone Number'] = "(+61) " + "09 " + tem[1] + tem[2]

            if re.match(regex12, row['Phone Number']):
                tem = row['Phone Number'].split(" ")
                if row['State'] == str("NSW"):
                    row['Phone Number'] = "(+61) " + "02 " + tem[2] + tem[3]
                if row['State'] == str("VIC"):
                    row['Phone Number'] = "(+61) " + "03 " + tem[2] + tem[3]
                if row['State'] == str("QLD"):
                    row['Phone Number'] = "(+61) " + "07 " + tem[2] + tem[3]
                if row['State'] == str("SA"):
                    row['Phone Number'] = "(+61) " + "09 " + tem[2] + tem[3]

            if any(row):
                writer.writerow(row)
    if path.exists('testtest.csv'):
        # get the path to the file in the current directory
        src = path.realpath('testtest.csv');
        os.remove('offices.csv')
        # rename the original file
        os.rename("testtest.csv", "offices.csv")

marge()
