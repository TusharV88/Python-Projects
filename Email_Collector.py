# Email Collector by using Regular Expression.

import re

string = 'Emails : gen.e.rat.o.r+mildhede@gmail.com,gen.e.ra.tor+hoankan@gmail.com,gen.e.ra.to.r+cembali@gmail.com,gen.e.ra.t.or+anticrack@gmail.com,ge.ne.rat.or+beginjaren@gmail.com'

# Extract emails from strings
ec = re.findall(r"[a-zA-Z0-9._+%]+@[a-zA-Z0-9._+%]+[.][a-zA-Z0-9]+",string) 

c = 1 # Count no.of emails

print('\n   Email/Emails/Gmail/Gmailsl')

for i in ec:
    print(f'\n{c}.',i)
    c += 1
    
    
    
