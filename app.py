from flask import Flask, redirect, request
import datetime

app = Flask(__name__)

@app.route("/track")
def track():
    target = "https://www.youtube.com/"  # ← 這裡改成你想跳轉的網址
    click_time = datetime.datetime.now()
    user_ip = request.remote_addr
    print(f"{click_time} - 點擊來自 {user_ip} - 目標：{target}")
    return redirect(target)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
