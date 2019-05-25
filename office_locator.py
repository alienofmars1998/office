#!flask/bin/python
from flask import Flask, jsonify, render_template
from flask import abort
from flask import request
import csv
import json
app = Flask(__name__)

def read_csv(file, format, Sid):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            if row['OfficeServiceID'] == str(Sid):
                csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
                return write_json(csv_rows,'dd', format)

#Convert csv data into json and write it
def write_json(data, json_file, format):
    with open(json_file, "w") as f:
        if format == "pretty":
            return json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '))
        else:
            return json.dumps(data)

def read_services(file, format):
    # Read From CSV File
    tempstr=''
    with open('services.csv', 'r') as csvfile:
        next(csvfile)
        csvfilereader = csv.reader(csvfile, delimiter=',', quotechar='|')
        # Print each Row
        for row in csvfilereader:
            if any(row):
                tempstr=tempstr+'['+'"'+row[0]+'"'+','+'"'+row[1]+'"],'
    return  '['+tempstr+']'

@app.route('/getoffices', methods=['GET'])
def get_offices():
    serviceid = request.args.get('serviceid')
    tasks = read_csv("office_service_locations.csv", "pretty", str(serviceid))
    return tasks

@app.route('/getservices', methods=['GET'])
def get_services():
    getservices = request.args.get('getservices')
    tasks = read_services("services.csv", "pretty")
    return tasks


@app.route('/', methods=['GET'])
def get_servicesDropDown():
    getservices = request.args.get('getservices')
    tasks = read_services("services.csv", "pretty")

    tasks = tasks.replace("[", "")
    tasks = tasks.replace("]", "")
    temp = tasks.split(",")
    count = 0
    tempastr = ''
    for ele in temp:
        if count == 0:
            count = +1
        else:
            tempastr = tempastr + '<option value=' + ele.replace("\"", "") + '>' + ele.replace("\"", "") + '</option>'
            count = 0
    tempastr='<form class="teamSelection" method="POST" action="/submitted"> ' \
             '<select id="teamDropdownSelector" type="text" name="teamDropdown">'+tempastr+'</select>' \
                                                                                           '<input class="btn" type="submit" value="Locate Office">' \
                                                                                           '</form>'

    return tempastr

@app.route("/submitted", methods=['POST'])
def hello():
   myvariable = request.form.get("teamDropdown")
   tasks = read_csvMapread("office_service_locations.csv", "pretty", str(myvariable))
   return render_template('office_map.html', test=tasks)


def read_csvMapread(file, format, Sid):
    csv_rows = []

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            temp=[]
            if str(Sid) in  row['ServiceName']:
                temp.append('<b>'+row['Contact Name']+'</b> '+row['Suburb']+' <br />Phon No. '+row['Phone Number']+' <br /><a href="mailto:'+row['Email']+'" target="_top">'+row['Email']+'</a>')
                temp.append(row['Lat'])
                temp.append(row['Lon'])
            if any(temp):
                csv_rows.append(temp)
        return csv_rows


if __name__ == '__main__':
    app.run(debug=True)