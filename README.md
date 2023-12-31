# Python 聊天機器人

這是一個簡單的 Python 聊天機器人，使用 OpenAI API 根據使用者輸入生成回應。該聊天機器人可以執行基本的檔案操作，例如在當前目錄中創建、讀取和重新命名檔案。

## 前置需求

在運行聊天機器人之前，請確保擁有以下內容：

- 安裝 Python 3.x
- OpenAI API 金鑰

## 安裝

1. 克隆存儲庫或下載源代碼。
2. 通過運行以下命令安裝所需的依賴項：

   ```
   pip install openai
   ```

3. 將 OpenAI API 金鑰設置為環境變量。您可以從 OpenAI 網站獲取 API 金鑰。

   ```
   export OPENAI_API_KEY=您的 API 金鑰
   ```

## 使用方法

1. 通過執行以下命令運行聊天機器人腳本：

   ```
   python chatbot.py
   ```

2. 聊天機器人將向您問候並等待您的輸入。

3. 輸入您的訊息或指令。聊天機器人將根據輸入生成回應。

4. 您可以使用以下指令與聊天機器人互動：

   - `創建檔案，名為<檔案名>`：創建具有指定名稱的檔案並生成其內容。
   - `讀取檔案列表`：列出當前目錄中的所有檔案。
   - `讀取檔案，名為<檔案名>`：讀取指定檔案的內容。
   - `將<舊檔案名>重新命名為<新檔案名>`：將檔案從舊名稱重新命名為新名稱。
   - `刪除快取`：清除聊天機器人的快取。

5. 要退出聊天機器人，輸入 `exit`、`bye` 或 `quit`。

## 授權

本項目採用 [MIT 授權](LICENSE)。