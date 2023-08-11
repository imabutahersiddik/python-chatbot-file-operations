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
    content = generate_content(f"Create a file named {file_name} with the following content:\n")
    try:
        with open(file_name, "w") as file:
            file.write(content)
        print(f"File '{file_name}' created and saved successfully in the current directory!")
    except Exception as e:
        print(f"Error creating the file '{file_name}' in the current directory. {str(e)}")

def read_files():
    files = glob.glob("*")
    return files

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error reading the file '{file_name}'. {str(e)}")
        return ""

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}' successfully!")
    except Exception as e:
        print(f"Error renaming the file. {str(e)}")

cache = {}

def handle_command(command):
    if command.startswith("create file named"):
        file_name = command.split("create file named ")[1]
        create_file(file_name)
        return f"File '{file_name}' created successfully in the current directory!"
    elif command.startswith("read files"):
        files = read_files()
        cache["files"] = files
        return f"Files in the current directory:\n{files}"
    elif command.startswith("read file"):
        file_name = command.split("read file ")[1]
        if "files" in cache and file_name in cache["files"]:
            return read_file(file_name)
        else:
            return "The file is not found in the cache. Please use the 'read files' command to populate the cache."
    elif command.startswith("rename"):
        old_name, new_name = command.split("rename ")[1].split(" to ")
        rename_file(old_name, new_name)
        return f"File '{old_name}' renamed to '{new_name}' successfully!"
    elif command.startswith("delete cache"):
        cache.clear()
        return "Cache cleared successfully!"
    else:
        return "Invalid command. Please try again."

def generate_response(prompt):
    response = generate_content(prompt)
    return response

def chat():
    print("\nHi! My name is AI. How can I assist you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() in ["exit", "bye", "quit"]:
            print("Goodbye!")
            break
        else:
            response = generate_response(user_input)
            print(response)

            if "create file named" in user_input or "rename" in user_input or "read files" in user_input or "delete cache" in user_input:
                print(handle_command(user_input))

            with open("conversation_logs.json", "a") as f:
                data = {"input": user_input, "response": response, "timestamp": time.time()}
                f.write(json.dumps(data) + "\n")

if __name__ == '__main__':
    chat()
