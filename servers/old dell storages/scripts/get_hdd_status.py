import re
import sys
import json
import subprocess

cmd = "omreport storage pdisk controller=0"

output = subprocess.check_output(cmd)
output = output.decode("utf-8")
output = output.replace('\r', '')

def getCount(output):
    pattern = r"(^ID.*$)\n"
    match = re.findall(pattern, output, re.MULTILINE)
    return len(match)

def getMatchID():
    pattern = r"(^ID.*$)\n"
    match = re.findall(pattern, output, re.MULTILINE)
    return match

def getMatchStatus():
    pattern = r"(^Status.*$)\n"
    match = re.findall(pattern, output, re.MULTILINE)
    return match

def getMatchName():
    pattern = r"(^Name.*$)\n"
    match = re.findall(pattern, output, re.MULTILINE)
    return match

def getMatchState():
    pattern = r"(^State.*$)\n"
    match = re.findall(pattern, output, re.MULTILINE)
    return match

def getMatchPowerStatus():
    pattern = r"(^Power Status.*$)\n"
    match = re.findall(pattern, output, re.MULTILINE)
    return match

js = {'data':[]}

el = getCount(output)
for i in range(el):
    jsd = {}
    jsd['ID'] = getMatchID()[i].split(":", 1)[1].lstrip()
    jsd['Status'] = getMatchStatus()[i].split(":", 1)[1].lstrip()
    jsd['Name'] = getMatchName()[i].split(":", 1)[1].lstrip()
    jsd['State'] = getMatchState()[i].split(":", 1)[1].lstrip()
    jsd['Power Status'] = getMatchPowerStatus()[i].split(":", 1)[1].lstrip()
    js['data'].append(jsd)

if len(sys.argv) == 1:
    print(json.dumps(js))

if len(sys.argv) == 3:
    id_hdd = sys.argv[1]
    data_hdd = sys.argv[2]
    for yy in range(el):
        if id_hdd in js['data'][yy]['ID']:
            if data_hdd == 'Status':
                print(js['data'][yy]['Status'])
            if data_hdd == 'State':
                print(js['data'][yy]['State'])
            if data_hdd == 'Power Status':
                print(js['data'][yy]['Power Status'])
