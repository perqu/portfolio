#!/usr/bin/python
import os

requirements = os.system('cmd /c "pip freeze > requirements.txt"')

template = ["django", "python-dotenv", "black", "pylint", "pymysql"]
output = []

"""
with open("reqs-template.txt", "r", encoding="utf-8") as file:
    for line in file:
        template.append(line.strip().lower())
"""
with open("requirements.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line[: line.find("=")].strip().lower() in template:
            output.append(line)

with open("requirements.txt", "w") as file:
    for line in output:
        file.write(line)
