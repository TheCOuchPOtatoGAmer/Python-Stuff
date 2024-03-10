import requests

def get_ip_info(ip_address, api_key):
    base_url = "https://api.ipgeolocation.io/ipgeo"
    params = {
        'apiKey': api_key,
        'ip': ip_address
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print("IP Information:")
            print(f"IP Address: {data['ip']}")
            print(f"Country: {data['country_name']}")
            print(f"City: {data['city']}")
            print(f"Latitude: {data['latitude']}")
            print(f"Longitude: {data['longitude']}")
            print(f"ISP: {data['isp']}")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    target_ip = input("Enter the IP address you want to look up: ")
    api_key = input("Enter your API Key: ")

    get_ip_info(target_ip, api_key)
