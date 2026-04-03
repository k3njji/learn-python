# # bsyq rpxe taiw ogxc
# # smtplib.SMTP("smtp.gmail.com", port=587)

# import smtplib

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     my_email = "harsantokenzie@gmail.com"
#     connection.starttls()

#     connection.login(my_email, password = 'bsyq rpxe taiw ogxc')
#     connection.sendmail(from_addr=my_email, to_addrs='kenzieharsanto123@gmail.com', msg='hello bro')

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
dow = now.weekday

print(now)