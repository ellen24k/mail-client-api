import email
import smtplib
from email.mime.text import MIMEText
import imaplib
import os

from email.header import decode_header, make_header

def parse(raw_readable):
    email_message = email.message_from_string(raw_readable)

    # 보낸 사람
    fr = make_header(decode_header(email_message.get('From')))
    print(fr)

    # 메일 제목
    title = make_header(decode_header(email_message.get('Subject')))
    print(title)

    # 날짜
    date = make_header(decode_header(email_message.get('Date')))
    print(date)

    # 본문 내용 파싱
    body = None

    def get_decoded_payload(part):
        charset = part.get_content_charset()
        payload = part.get_payload(decode=True)
        if payload:
            try:
                return payload.decode(charset or 'utf-8', errors='replace')
            except (LookupError, UnicodeDecodeError):
                return payload.decode('utf-8', errors='replace')
        return None

    if email_message.is_multipart():
        for part in email_message.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get('Content-Disposition'))

            if content_type in ['text/plain', 'text/html'] and 'attachment' not in content_disposition:
                decoded = get_decoded_payload(part)
                if decoded:
                    body = decoded
                    break
    else:
        body = get_decoded_payload(email_message)

    if not body:
        body = '본문 없음'

    return {
        'from': str(fr),
        'title': str(title),
        'date': str(date),
        'content': body
    }


def send_simple_mail(
    sender: str,
    receiver: str,
    title: str,
    content: str,
    charset: str = 'utf-8'
):
    sender = sender.lower()
    receiver = receiver.lower()
    
    smtp_port = 587
    if sender == 'gmail':
        smtp_server = 'smtp.gmail.com'
        sender_email = os.getenv("GMAIL_EMAIL")
        sender_password = os.getenv("GMAIL_PASSWORD")
    elif sender == 'naver':
        sender_email = os.getenv("NAVER_EMAIL")
        sender_password = os.getenv("NAVER_PASSWORD")
        smtp_server = 'smtp.naver.com'
    else:
        print("지원하지 않는 서비스입니다. 'gmail' 또는 'naver'를 사용하세요.")
        return


    if receiver == 'gmail':
        to_email = os.getenv("GMAIL_EMAIL")
    elif receiver == 'naver':
        to_email = os.getenv("NAVER_EMAIL")
    else:
        print("지원하지 않는 서비스입니다. 'gmail' 또는 'naver'를 사용하세요.")
        return

    try:
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(sender_email, sender_password)
        
        msg = MIMEText(content, _charset=charset)
        msg['Subject'] = title
        msg['From'] = sender_email
        msg['To'] = to_email

        smtp.sendmail(sender_email, to_email, msg.as_string())
        print(f"{sender.upper()} 메일 전송 성공!")

    except smtplib.SMTPAuthenticationError:
        print("로그인 실패: 이메일 또는 비밀번호가 잘못됐거나 보안 설정이 차단 중입니다.")
    except Exception as e:
        print(f"메일 전송 실패: {e}")
    finally:
        smtp.quit()

def recv_simple_mail(
    receiver: str,
):
    receiver = receiver.lower()
    if receiver == 'gmail':
        imap_server = 'imap.gmail.com'
        receiver_email = os.getenv("GMAIL_EMAIL")
        password = os.getenv("GMAIL_PASSWORD")
    elif receiver == 'naver':
        imap_server = 'imap.naver.com'
        receiver_email = os.getenv("NAVER_EMAIL")
        password = os.getenv("NAVER_PASSWORD")
    else:
        print("지원하지 않는 서비스입니다. 'gmail' 또는 'naver'를 사용하세요.")
        return
    
    imap = imaplib.IMAP4_SSL(imap_server)

    imap.login(receiver_email, password)

    imap.select('inbox')
    status, data = imap.uid('search', None, 'ALL')

    messages = data[0].split() 
    fetch_count = min(5, len(messages))  # 최근 5개 메일 가져오기
    decoded_emails = []

    for i in range(1, fetch_count + 1): # todo
        res, msg_data = imap.uid('fetch', messages[-i], '(RFC822)')
        raw_email = msg_data[0][1]
        raw_readable = raw_email.decode('utf-8')
        decoded_emails.append(parse(raw_readable))

    return(decoded_emails)