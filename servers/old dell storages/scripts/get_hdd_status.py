import re
import sys
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

print(json.dumps(js))
