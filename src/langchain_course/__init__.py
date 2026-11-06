from dotenv import load_dotenv
import os

load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")
    print(os.environ.get("TEST_KEY"))


if __name__ == "__main__":
    main()
