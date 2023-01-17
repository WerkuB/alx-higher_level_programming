#!/usr/bin/python3
'''a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as
a parameter, and finally displays the body of the response.
The email must be sent in the variable email
You must use the packages requests and sys
are not allowed to import packages other than requests and sys
don not need to error check arguments passed to the script
(number or type)'''

if __name__ == '__main__':
    import requests
    import sys

    params = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=params)
    print(res.text)
