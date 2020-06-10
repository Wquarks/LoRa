import re
lat=" "
lon=" "
snr=" "

fin = open("data.txt", "r")
fout = open("SNREnGPX.gpx", "w")

fout.write("<?xml version='1.0' ?>")
fout.write("\n<gpx xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' version='1.0' creator='William WS'>")
fout.write("\n  <trk>") 
fout.write("\n    <trkseg>")
    
for line in fin:
    lat = re.search(r"\(\([0-9]{1,2}[.][0-9]{,7}", line)
    if  lat :
        lat=lat.group().replace("((", "")
    else:
        lat=0
        
    lon = re.search(r"[ ][0-9]{1,2}[.][0-9]{,7}", line)
    if  lon :
        lon=lon.group()
    else:
        lon=0
    
    snr = re.search(r"snr=[-]?[0-9]{1,2}[.][0-9]{,7}", line)
    if  snr :
        snr=snr.group().replace("snr=", "")
    else:
        snr=0
        
    var="\n      <trkpt lat='"+str(lat)+"' lon='"+str(lon)+"'>"
    fout.write(str(var))
    var="\n        <ele>"+str(snr)+"</ele>"
    fout.write(str(var))
    fout.write("\n      </trkpt>")

    
fout.write("\n    </trkseg>")
fout.write("\n  </trk>")
fout.write("\n</gpx>")

fin.close()
fout.close()

print("OK")

  
