import json

with open("sample-data.json", "r") as file:
    data = json.load(file)
print("Interface Status")
print("=================================================================================")
print("DN                                             Description      Speed    MTU")
print("---------------------------------------------------------------------------------")

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")

    print("{:<42} {:<20} {:<8} {:<8}".format(dn, descr, speed, mtu))