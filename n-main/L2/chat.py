import smtplib

mas = ''''From Joy <joy@boy.com>
To: TO Mika <pakin@pakin.com>
MIME-Version: 1.0
Content-Type: text/html
Subject: Test HTML Email

This is an email message sent as HTML.
<b>This is a test HTML Message</b>
<h1>This is headling 1</h1>
'''

try:
    smtp = smtplib.SMTP("192.168.153.131")
    smtp.sendmail('pakin','pakin',mas)
    print('suc')

except Exception as err:
    print(str(err))