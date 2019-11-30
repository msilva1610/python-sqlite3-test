import requests
import sqlite3
import json


def insertjson():


    countries_api_res = requests.get('http://api.worldbank.org/countries?format=json&per_page=100')
    countries = countries_api_res.json()[1]

    # print(countries)

    conn = sqlite3.connect('testjson.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS countries (id varchar(3), data json)")

    for country in countries:
        c.execute("insert into countries values (?, ?)", [country['id'], json.dumps(country)])
        conn.commit()
    conn.close()

def selectjson():
    conn = sqlite3.connect('testjson.db')
    c = conn.cursor()
    c.execute("select json_extract(data, '$.region.id'), json_extract(data, '$.name') from countries where json_extract(data, '$.name') = 'Fiji';")
    data = c.fetchall()
    # print(data)
    # for d in data:
    #     print(d)
    for item in data:
        print('Region id: {} - Nome: {}'.format(item[0],item[1]))
        # print(json.loads(item[0]))


selectjson()




