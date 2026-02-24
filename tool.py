#
# Tool for get problem url, generate md file, update README.md to track progress
#

import requests
import re
import os
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://projecteuler.net"
SCRAPE_URL = "https://math.berkeley.edu/~elafandi/euler"  # Only first 58 problems now
READ_ME_FILE_PATH = "./README.md"

def normalize_content(content):
    # Remove \( and \) delimiters completely
    content = re.sub(r"\\\(|\\\)", "", content)
    # Remove \[ and \] delimiters completely
    content = re.sub(r"\\\[|\\\]", "", content)
    return content


def make_folder(folder_name):
    folder_path = f"./{folder_name}"
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder created at: {folder_path}")
    return str(folder_path)

def make_file(folder_path, file_name, file_content, file_extension):
    file_path = os.path.join(folder_path, f"{file_name}.{file_extension}")

    with open(file_path, "w", encoding="utf-8") as f:
        if file_content:
          f.write(file_content)
        else:
          pass
    print(f"File created at: {file_path}")

def update_ongoing_readme(problem_title):
    now = datetime.now()
    today = now.strftime("%d/%m/%y")
    content = f"""## 🏃 Ongoing
- [] **{problem_title}** — *{today}*
    """
    
    with open(READ_ME_FILE_PATH, "a", encoding="utf-8") as f:   # “a” = append mode
      f.write(f"\n{content}\n")

def init_problem(problem_title, number, problem_number, problem_name, problem_content):
    folder_path = make_folder(problem_number)
    make_file(folder_path, problem_name, problem_content, "md")
    make_file(folder_path, f"p{number}", "", "py")
    update_ongoing_readme(problem_title)

def get_problem():
    number = int(input("Enter the problem number: "))
    problem_url = f"{URL}/problem={number}"

    if number <= 58:
        content_url = f"{SCRAPE_URL}/p{number}"
        response = requests.get(content_url)
        soup = BeautifulSoup(response.text, "html.parser")
        problem_title = soup.find("h1").get_text()

        problem_content = soup.find(class_="problem_content").get_text()

        problem_number = problem_title.split(":")[0].strip()
        problem_name = problem_title.split(":")[1].strip()

        normalized_content = normalize_content(problem_content)

        problem_file_content = f"""[{problem_name}]({problem_url})
{normalized_content}
        """

        init_problem(problem_title, number, problem_number, problem_name, problem_file_content)

    return str(f"(̿▀̿‿ ̿▀̿ ̿) Here your link Sir: {problem_url}")


if __name__ == "__main__":
    print("Welcome to Project Euler CLI tool (っ´ω`c)♡.")
    while True:
        print(
            """
Enter 1: Create Problem 'x' folder contains a problem content markdown file and a python file, return web link to the problem to submit answer.
Enter 2: Write the answer of a problem when submit successfully.
Enter q: Terminate this program.
"""
        )
        user_input = input().strip()
        match user_input:
            case "1":
                print(get_problem())
            case "2":
                continue
            case "q":
                print("Goodbye! See you soon (ʘ‿ʘ)╯")
                break
            case _:
                print("Please try again (ง •̀_•́)ง")
        print("---------------------------")
