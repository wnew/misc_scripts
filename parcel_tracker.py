import os, urllib

packages = ["RS915893595CH",
            "RC872541047HK",
            "RC740667074CN",
            "RB595183543CN",
            "RF207929317SG",
            "RB596971431CN",
            "RC464416917CN",
            "RC266409604CN",
            "RF207687615SG",
            "RC463879428CN",
            "RB596903697CN",
            "RC266408484CN",
            "RB596903079CN"]

url = 'http://sms.postoffice.co.za/TrackingParcels/Parcel.aspx?id='

for package in packages:
   f = open(urllib.urlretrieve(url+package)[0],'r')
   html = f.read()
   if "could not be found in our database" in html:
      print package + " could not be found"
   else:
      print package + " " + html.split("local Item number: </b>")[1].split("\n")[0].replace("<b>","").replace("</b>","").replace("</font>","").replace("</td>","")[:-1] + " at " + html.split("Location last scanned: ")[1].split("\n")[0].replace("<b>","").replace("</b>","").replace("</font>","").replace("</td>","")
   f.close()

