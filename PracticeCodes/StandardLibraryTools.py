from datetime import date
import re
from urllib.request import urlopen
import smtplib


# Date Time Calculation
now = date.today()
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
birthday = date(1990, 4, 21)
age = now - birthday
print("You have lived for {} days.".format(age.days))


# String Manipulation using regular expression re module
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')


# Internet Access using urllib.request
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8') # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line: # look for Eastern Time
            print(line)

# Email sending using smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                """To: jcaesar@example.org
                From: soothsayer@example.org
                
                Beware the Ides of March.
                """)
server.quit()
