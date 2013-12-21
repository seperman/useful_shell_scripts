"""
grabs a file and converts lines into comma seperated stuff
"""
with open("temp.txt.csv") as f:
   data = f.read()
   data = data.replace("\n",",")
   print data