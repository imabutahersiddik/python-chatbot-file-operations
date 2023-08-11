import openai
import os
import time
import json
import glob

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_content(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )
    content = response.choices[0].text.strip()
    return content

def create_file(file_name):
    content = generate_content(f"創建名為 {file_name} 的檔案，內容如下：\n")
    try:
        with open(file_name, "w") as file:
            file.write(content)
        print(f"檔案 '{file_name}' 成功創建並保存在當前目錄中！")
    except Exception as e:
        print(f"在當前目錄中創建檔案 '{file_name}' 時發生錯誤。{str(e)}")

def read_files():
    files = glob.glob("*")
    return files

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"讀取檔案 '{file_name}' 時發生錯誤。{str(e)}")
        return ""

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"檔案 '{old_name}' 成功重新命名為 '{new_name}'！")
    except Exception as e:
        print(f"重新命名檔案時發生錯誤。{str(e)}")

cache = {}

def handle_command(command):
    if command.startswith("創建檔案，名為"):
        file_name = command.split("創建檔案，名為")[1]
        create_file(file_name)
        return f"檔案 '{file_name}' 成功在當前目錄中創建！"
    elif command.startswith("讀取檔案列表"):
        files = read_files()
        cache["files"] = files
        return f"當前目錄中的檔案：\n{files}"
    elif command.startswith("讀取檔案，名為"):
        file_name = command.split("讀取檔案，名為")[1]
        if "files" in cache and file_name in cache["files"]:
            return read_file(file_name)
        else:
            return "該檔案未在快取中找到。請使用 '讀取檔案列表' 指令填充快取。"
    elif command.startswith("將"):
        old_name, new_name = command.split("將")[1].split("重新命名為")
        rename_file(old_name, new_name)
        return f"檔案 '{old_name}' 成功重新命名為 '{new_name}'！"
    elif command.startswith("刪除快取"):
        cache.clear()
        return "快取已成功清除！"
    else:
        return "無效的指令。請重試。"

def generate_response(prompt):
    response = generate_content(prompt)
    return response

def chat():
    print("\n嗨！我是 AI。有什麼可以幫助您的？")
    while True:
        user_input = input("> ")
        if user_input.lower() in ["退出", "再見", "結束"]:
            print("再見！")
            break
        else:
            response = generate_response(user_input)
            print(response)

            if "創建檔案，名為" in user_input or "將" in user_input or "讀取檔案列表" in user_input or "刪除快取" in user_input:
                print(handle_command(user_input))

            with open("對話記錄.json", "a") as f:
                data = {"輸入": user_input, "回應": response, "時間戳記": time.time()}
                f.write(json.dumps(data) + "\n")

if __name__ == '__main__':
    chat()