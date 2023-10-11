import requests

def shortenLink(link, name):
    API_KEY = 'c258a81323e9cbf4d4dd950cc3e057d4306aa'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short':link, 'name': name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    print('')
    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']
        print(f"Title = {title}")
        print(f"link = {short_link}")
    except:
        status = data['url']['status']
        print(f" You have an error. Status of error is {status}")

masuklink = input("Masukkan link panjang = ")
nama = input("Mau disingkat jadi apa= ")

shortenLink(masuklink,nama)