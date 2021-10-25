import requests

re = requests.get("https://spys.me/proxy.txt")

count =0

file = open("tmp.txt","r+")
file.write(re.text)

file = open("tmp.txt","r")
count =0
proxlist = open("proxies.txt","a")
for line in file:
	if count>=9 and "Free" not in line:
		proxlist.write(line.split(" ")[0])
		proxlist.write("\n")
	count+=1