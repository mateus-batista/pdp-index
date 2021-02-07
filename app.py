import requests
from flask import Flask

app = Flask(__name__)
session = requests.Session()


@app.route('/surveys')
def hello_world():
    url = "https://www.my.pdpworks.com/api/sessions"
    json = {
        "emailAddress": "judd@ae.studio",
        "password": "Katiepdppassword42",
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "65",
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "www.my.pdpworks.com",
        "Origin": "https://www.my.pdpworks.com",
        "Referer": "https://www.my.pdpworks.com/app/login",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent":
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    }

    session.post(url, json=json, headers=headers)

    query_params = {
        "folderId": "0",
        "textSearch": "",
        "notes": "",
        "reportTypeId": "0",
        "fromDate": "",
        "toDate": "",
        "isArchived": "false",
        "sorts": "survey.last - name / asc",
        "sorts": "survey.first - name / asc",
        "sorts": "app.date / desc",
        "sorts": "app.survey - type / desc",
        "level": "report",
        "limit": "100",
        "offset": ""
    }

    result = session.get("https://www.my.pdpworks.com/api/individuals")

    return result.text


if __name__ == '__main__':
    app.run()
