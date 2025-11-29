import os
import uvicorn

def start():
    uvicorn.run("main:app")

def inngest_ui():
    os.system("npx inngest-cli@latest dev -u http://127.0.0.1:8000")