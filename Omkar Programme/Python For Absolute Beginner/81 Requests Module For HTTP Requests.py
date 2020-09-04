import requests

r = requests.get("https://www.google.com/search?q=river+images&rlz=1C1CHBF_enIN878IN889&oq=river+ima&aqs=chrome.1.69i57j0l7.27602j1j7&sourceid=chrome&ie=UTF-8")
print(r.text)        # To get http information in text form
print(r.status_code)      # check other status codes on google


url = "www.something1.com"
data = {
    "p1":4,
    "p2":8
}
r2 = requests.post(url=url, data=data)



url = "http://www.facebook.com?"
data = {
    "username":"omkarsutar",
    "password":12345678
}
r3 = requests.post(url=url, data=data)
print(r3.text)
print(r3.status_code)