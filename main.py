import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText

current_day = dt.datetime.now().weekday()
quote_message = ""
with open("quotes.txt", "r") as quotes:
    data = quotes.read()
    data_into_list = data.split("\n")
    random_number = random.randint(0, len(data_into_list))
    quote_message = data_into_list[random_number]

sendEmail = ""
recvEmail = ""
password = ""

smtpName = "smtp.naver.com"  # smtp 서버 주소
smtpPort = 587  # smtp 포트 번호

text = quote_message

msg = MIMEText(text)  # MIMEText(text , _charset = "utf8")
msg['Subject'] = "quote_message"
msg['From'] = sendEmail
msg['To'] = recvEmail

with smtplib.SMTP(smtpName, smtpPort) as connection:
    connection.starttls()  # TLS 보안 처리
    connection.login(sendEmail, password)  # 로그인
    connection.sendmail(sendEmail, recvEmail, msg.as_string())  # 메일 전송, 문자열로 변환하여 보냅니다.
    connection.close()  # smtp 서버 연결을 종료합니다.
