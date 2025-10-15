import requests

def get_ip_info(ip):
    # Free API (no API key needed)
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        print("🌍 IP Location Details")
        print(f"IP Address : {data['query']}")
        print(f"City       : {data['city']}")
        print(f"Region     : {data['regionName']}")
        print(f"Country    : {data['country']}")
        print(f"ISP        : {data['isp']}")
        print(f"Timezone   : {data['timezone']}")
    else:
        print("❌ Invalid IP address or lookup failed.")

# Ask user for input
ip = input("Enter an IP address: ")
get_ip_info(ip)
