from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 用來存儲聊天記錄的檔案路徑
chat_log_path = "chat_log.txt"

def load_chat_log():
    try:
        with open(chat_log_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def save_chat_log(messages):
    with open(chat_log_path, "w", encoding="utf-8") as file:
        file.writelines(messages)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form.get('message')
    messages = load_chat_log()
    messages.append(message + "\n")
    save_chat_log(messages)
    return jsonify({'success': True})

@app.route('/get_messages', methods=['GET'])
def get_messages():
    messages = load_chat_log()
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
