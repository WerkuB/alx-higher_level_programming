#!/usr/bin/python3
'''a Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
 display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys'''

if __name__ == '__main__':
    import requests
    import sys

    data = {'q': sys.argv[1] if len(sys.argv) >= 2 else ""}
    res = requests.post('http://0.0.0.0:5000/search_user', data=data)
    text = res.text

    try:
        json = res.json()
        if json.get('id', None) is None:
            print('No result')
        else:
            print('[{}] {}'.format(json['id'], json['name']))
    except Exception:
        print('Not a valid JSON')
