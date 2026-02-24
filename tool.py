#
# Tool for get problem url, problem content, generate md file, update README.md to track progress
#

import requests
import re
import os
from bs4 import BeautifulSoup
from datetime import datetime
from answer import ANSWERS

URL = "https://projecteuler.net"
SCRAPE_URL = "https://math.berkeley.edu/~elafandi/euler"  # Only first 58 problems now
READ_ME_FILE_PATH = "./README.md"
ANSWER_FILE_PATH = "./answer.txt"

PYTHON_SOLUTION_TEMPLATE = """def compute():
  ans = 0
  return str(ans)

if __name__ == "__main__":
	print(compute())
"""

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


def get_today():
    now = datetime.now()
    today = now.strftime("%d/%m/%y")
    return today


def update_ongoing_readme(problem_title):
    today = get_today()
    content = f"""## 🏃 Ongoing
- [ ] **{problem_title}** — *{today}*
    """

    with open(READ_ME_FILE_PATH, "a", encoding="utf-8") as f:  # “a” = append mode
        f.write(f"{content}\n")


def update_completed_readme(problem_title):
    today = get_today()
    content = f"- [x] **{problem_title}** — *{today}*"
    with open(READ_ME_FILE_PATH, "a", encoding="utf-8") as f:  # “a” = append mode
        f.write(f"{content}\n")


def remove_ongoing_section():
    with open(READ_ME_FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    skip = False
    for line in lines:
        if line.strip().startswith("## 🏃 Ongoing"):
            skip = True
            continue
        if skip:
            # stop skipping when we hit the next section header
            if line.startswith("## "):
                skip = False
                new_lines.append(line)
            else:
                continue
        else:
            new_lines.append(line)

    with open(READ_ME_FILE_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def update_answer_file(number, problem_title, user_answer):
    content = f"{number}. {problem_title}: {user_answer}"
    with open(ANSWER_FILE_PATH, "a", encoding="utf-8") as f:  # “a” = append mode
        f.write(f"\n{content}\n")


def answer_problem(user_answer, problem_title, number):
    remove_ongoing_section()
    update_completed_readme(problem_title)
    update_answer_file(number, problem_title, user_answer)

    print(
        f"Congratulations! You are correct for answering {user_answer} for {problem_title}"
    )


def init_problem(problem_title, number, problem_number, problem_name, problem_content):
    folder_path = make_folder(problem_number)
    make_file(folder_path, problem_name, problem_content, "md")
    make_file(folder_path, f"p{number}", PYTHON_SOLUTION_TEMPLATE, "py")
    update_ongoing_readme(problem_title)

def get_problem_detail(number):
  content_url = f"{SCRAPE_URL}/p{number}"

  response = requests.get(content_url)
  soup = BeautifulSoup(response.text, "html.parser")
  problem_title = soup.find("h1").get_text()

  problem_content = soup.find(class_="problem_content").get_text()

  problem_number = problem_title.split(":")[0].strip()
  problem_name = problem_title.split(":")[1].strip()

  return {problem_title, problem_content, problem_number, problem_name}

def get_problem():
    number = int(input("Enter the problem number: "))
    problem_url = f"{URL}/problem={number}"

    if number <= 58:
        problem_title, problem_content, problem_number, problem_name = get_problem_detail(number)

        normalized_content = normalize_content(problem_content)

        problem_file_content = f"""[{problem_name}]({problem_url})
{normalized_content}
        """

        init_problem(
            problem_title, number, problem_number, problem_name, problem_file_content
        )

    return str(f"(̿▀̿‿ ̿▀̿ ̿) Here your link Sir: {problem_url}")


def answer():
    number = int(input("Enter the problem number you want to submit: "))

    problem_title, problem_content, problem_number, problem_name = get_problem_detail(number)

    user_answer = input(f"Enter your answer of {problem_title} ✌(-‿-)✌: ")
    actual_answer = ANSWERS[number]

    if user_answer == actual_answer:
        answer_problem(user_answer, problem_title, number)
    else:
        print("You are wrong, please try again ┌(◉ ͜ʖ◉)つ!")


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
                answer()
            case "q":
                print("Goodbye! See you soon (ʘ‿ʘ)╯")
                break
            case _:
                print("Please try again (ง •̀_•́)ง")
        print("---------------------------")
