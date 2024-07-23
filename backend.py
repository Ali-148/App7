import requests

API_KEY = "sbfjksbfkjsdgkjsgjksdgjks"
def get_data(place, forecast_days, kind=None):
    url = f"asfsdddddddhghfgjfghdfhdfhdfhddfdfh={place}& appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))


# API AUTHENTICATION FAILED