class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False
    def sent(self):
        self.is_sent = True
    def get_info(self):
        return (f"{self.sender} says to {self.receiver}: {self.content}."
                f" Sent: {self.is_sent}"
                )


emails = []
while True:
    email = input()
    if email == "Stop":
        break
    email = email.split(" ", maxsplit=2)
    sender = email[0]
    receiver = email[1]
    content = email[2]

    mail = Email(sender, receiver, content)
    emails.append(mail)
send_emails = input().split(", ")

for x in send_emails:
    emails[int(x)].sent()
for mails in emails:
    print(mails.get_info())


