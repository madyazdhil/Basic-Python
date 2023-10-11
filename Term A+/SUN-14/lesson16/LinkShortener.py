import requests

def shorten_link(link, name):
    API_KEY = '50ff34b9497a8111838783f91b8fb254130e3'
    BASE_URL = 'https://cutt.ly/api/api.php'

    #variable to store the parameters
    payload = {'key': API_KEY,'short':link, 'name': name }
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    try:
        #create a vara to store the title of the website
        title = data['url']['title']
        #create a var to shortening the links
        short_link = data['url']['shortLink']
        #create a var to tell us the status
        status = data['url']['status']
        print()
        print(f"Title of the website is      : {title}")
        print(f"The shortened link is        : {short_link}")
        print(f"Status of shortening the link: {status}")
    except:
        status=data['url']['status']
        print(f"status error is {status}")

link = input("Masukkan link yang ingin dipendekin :")
name = input("Masukkan nama link yang anda mau    :")
shorten_link(link,name)