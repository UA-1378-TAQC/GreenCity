def print_response(response):
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        print("Response Data:", response.json())
    else:
        print("Error:", response.text)
