import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"

LOGIN = 'login@gmail.com'
PASSWORD = 'qwerty'
SUBJECT = 'Subject'
RECIPIENTS = ['vasya@email.com', 'petya@email.com']
MESSAGE = 'Message'
HEADER = None


class MailAgent:
    def __init__(self):
        self.login = LOGIN
        self.password = PASSWORD

    def sending_message(self):
        # send message
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(RECIPIENTS)
        msg['Subject'] = SUBJECT
        msg.attach(MIMEText(MESSAGE))

        ms = smtplib.SMTP(GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login,
                    ms, msg.as_string())
        ms.quit()
        # send end

    def recieving_message(self):
        # recieve
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % HEADER if HEADER else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        # end recieve


if __name__ == '__main__':
    gmail = MailAgent()
    gmail.sending_message()
    gmail.recieving_message()
