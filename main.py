
import smtplib
from email.mime.text import MIMEText

sendEmail = "email_address"
recvEmail = "email_address"
password = "password"

smtpName = "smtp.naver.com" #smtp 서버 주소
smtpPort = 587 #smtp 포트 번호

text = "test"

msg = MIMEText(text) #MIMEText(text , _charset = "utf8")
msg['Subject'] ="Hello worlddd"
msg['From'] = sendEmail
msg['To'] = recvEmail

with smtplib.SMTP( smtpName , smtpPort ) as connection:
    connection.starttls() #TLS 보안 처리
    connection.login( sendEmail , password ) #로그인
    connection.sendmail( sendEmail, recvEmail, msg.as_string() ) #메일 전송, 문자열로 변환하여 보냅니다.
    connection.close() #smtp 서버 연결을 종료합니다.