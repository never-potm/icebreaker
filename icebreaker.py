import os

from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    print("Hello langchain.")
    print(os.environ["DUMMY_API_KEY"])
