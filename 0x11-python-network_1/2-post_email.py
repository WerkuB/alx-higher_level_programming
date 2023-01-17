#!/usr/bin/python3
''' A Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
.The email must be sent in the email variable
.You must use the packages urllib and sys
.You are not allowed to import packages other than urllib and sys
.do not need to check arguments passed to the script (number or type)
.You must use the with statement'''

if __name__ == '__main__':
    import sys
    from urllib import request, parse

    data = parse.urlencode({'email': sys.argv[2]}).encode()
    req = request.Request(sys.argv[1], data=data)
    with request.urlopen(req) as res:
        print(res.read().decode('UTF-8'))
