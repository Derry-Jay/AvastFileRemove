import re
import os
import datetime as dt

fp = open("C:/ProgramData/AVAST Software/Avast/report/aswBoot.txt", "r")
fp1 = open("C:/Users/shaky/Documents/boot_scan_report_" + dt.datetime.now().strftime("%d-%m-%Y %H_%M_%S") + ".txt", "w")
chars = re.split("\n", fp.read())
cfps = []
d = 0
cd = 0
ad = 0
df = []
adf = []
cdf = []
for i in chars:
    if re.search("File", i) is not None:
        add_path = re.split("\|>", re.search("File", i).string[5:])[0]
        add_p = add_path if re.search(
            " is ", add_path) is None else re.split(" is ", add_path)[0]
        adp = add_p if re.search(
            " Error ", add_p) is None else re.split(" Error ", add_p)[0]
        ap = adp if re.search(":W", adp) is None else re.split(":W", adp)[0]
        if ap not in cfps:
            cfps.append(ap)
for j in cfps:
    if os.path.exists(j):
        try:
            os.remove(j)
            df.append(j)
            d += 1
        except Exception as e:
            cdf.append(j)
            cd += 1
            print(e)
    else:
        adf.append(j)
        ad += 1
fp1.write("Deleted Files: \n")
if df is not None and df != []:
    for i in df:
        fp1.write("    -> " + i + "\n")
fp1.write("Files that cannot be Deleted: \n")
if cdf is not None and cdf != []:
    for i in cdf:
        fp1.write("    -> " + i + "\n")
fp1.write("Files that are already Deleted: \n")
if adf is not None and adf != []:
    for i in adf:
        fp1.write("    -> " + i + "\n")
print("Cannot Delete:%d" % cd)
print("Already Deleted:%d" % ad)
print("Deleted:%d" % d)
