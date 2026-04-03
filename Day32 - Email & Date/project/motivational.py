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
print(now)
day = now.weekday()

if(day == 4):
    import smtplib
    import random
    quotes = []
    try:
        with open('Day32 - Email & Date/quotes.txt') as data:
            for line in data:
                line = line.strip()
                quote, author = line.rsplit(" - ", 1)
                quote = quote.strip('"')
                quotes.append([quote, author])
    except FileNotFoundError:
        raise('no file was found')


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

        my_email = "harsantokenzie@gmail.com"
        connection.starttls()
        quote = random.choice(quotes)

        connection.login(my_email, password = 'bsyq rpxe taiw ogxc')

        connection.sendmail(
            from_addr=my_email,
            to_addrs='kenzieharsanto123@gmail.com',
            msg=f"Subject:Quote of the Day\n\nHere is your quote of the day:\n\n{quote[0]}\nBy {quote[1]}"
        )

print(day)