import csv, smtplib, ssl

message = """Subject: Tsunami Alert

Hi {name}, {grade} """
from_address = "saviout97@gmail.com"
password = "Sandeep1997san"
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("sanemail1.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name,grade=grade),
            )