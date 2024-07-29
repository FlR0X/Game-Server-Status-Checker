import requests

def check_server_status(server_url):
    try:
        # Send a request to the server's status endpoint
        response = requests.get(server_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'online':
                print(f"Server is online. Current player count: {data['player_count']}")
            else:
                print("Server is offline.")
        else:
            print(f"Failed to get status. HTTP Status Code: {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace this URL with the actual status endpoint of your game server
    server_url = 'https://example.com/api/server/status'
    check_server_status(server_url)
