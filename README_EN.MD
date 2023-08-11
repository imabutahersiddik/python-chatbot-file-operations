# Python Chatbot

This is a simple Python chatbot that uses the OpenAI API to generate responses based on user input. The chatbot can perform basic file operations such as creating, reading, and renaming files in the current directory.

## Prerequisites

Before running the chatbot, make sure you have the following:

- Python 3.x installed
- OpenAI API key

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command:

   ```
   pip install openai
   ```

3. Set your OpenAI API key as an environment variable. You can obtain your API key from the OpenAI website.

   ```
   export OPENAI_API_KEY=your-api-key
   ```

## Usage

1. Run the chatbot script by executing the following command:

   ```
   python chatbot_en.py
   ```

2. The chatbot will greet you and wait for your input.

3. Enter your message or command. The chatbot will generate a response based on the input.

4. You can use the following commands to interact with the chatbot:

   - `create file named <filename>`: Creates a file with the specified name and generates its content.
   - `read files`: Lists all the files in the current directory.
   - `read file <filename>`: Reads the content of the specified file.
   - `rename <old_filename> to <new_filename>`: Renames a file from the old name to the new name.
   - `delete cache`: Clears the chatbot's cache.

5. To exit the chatbot, type `exit`, `bye`, or `quit`.

## License

This project is licensed under the [MIT License](LICENSE).