
import json

with open("sample.json") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<5}")
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "9150")
    print(f"{dn:<50} {'':<20} {speed:<7} {mtu:<5}")