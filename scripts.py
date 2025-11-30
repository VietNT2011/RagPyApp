import os
import uvicorn
import sys

def start():
    uvicorn.run("main:app", reload=True)

def inngest_ui():
    os.system("npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest")

# Only run when executed directly on command line
if __name__ == "__main__":
    command = sys.argv[1]
    if command == "start":
        start()
    elif command == "inngest_ui":
        inngest_ui()
    else:
        print(f"Not found: {command}")