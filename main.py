from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from function import *

app = FastAPI()

# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=[  # for production
        "http://192.168.1.150:3000", 
    ],
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1)(:\d+)?",  # for local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/smtp/{sender}/{receiver}/{title}/{content}",summary='메일 송신 api',description='예시: /smtp/[gmail/naver]/[gmail/naver]/title/content')
async def smtp(sender: str, receiver: str, title: str, content: str):
    return(send_simple_mail(
    sender=sender,  # 또는 'gmail'
    receiver=receiver, 
    title=title,
    content=content,
))

@app.get("/imap/{receiver}", summary='메일 수신 api',description='예시: /imap/[gmail/naver]')
async def imap(receiver: str):
    return(recv_simple_mail(
    receiver=receiver,
))