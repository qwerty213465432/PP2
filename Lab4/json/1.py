import json

# Load JSON data from the file
with open('sample_data.json') as f:
    data = json.load(f)

# Print header for the interface status
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Iterate over each interface and print its details
for interface in data:
    dn = interface.get('dn', '')
    description = interface.get('description', '')
    speed = interface.get('speed', 'inherit')
    mtu = interface.get('mtu', '')

    print("{:<50} {:<20} {:<8} {:<}".format(dn, description, speed, mtu))
