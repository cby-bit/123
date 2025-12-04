from flask import Flask, redirect, request, send_file
import datetime
import csv
import os

app = Flask(__name__)
CSV_FILE = "clicks.csv"

# 取得使用者真實 IP
def get_client_ip():
    if "X-Forwarded-For" in request.headers:
        return request.headers["X-Forwarded-For"].split(",")[0].strip()
    else:
        return request.remote_addr

# 跳轉並記錄點擊
@app.route("/")
@app.route("/track")
def track():
    target = "https://reurl.cc/MMOOMk"  # 改成你想跳轉的網址
    click_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_ip = get_client_ip()

    # 寫入 CSV
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["time", "ip", "target"])
        writer.writerow([click_time, user_ip, target])

    print(f"{click_time} - 點擊來自 {user_ip} - 目標：{target}")
    return redirect(target)

# 顯示 CSV 點擊紀錄
@app.route("/logs")
def logs():
    if not os.path.isfile(CSV_FILE):
        return "No logs yet."
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        content = f.read().replace("\n", "<br>")
    return content

# 下載 CSV 檔案
@app.route("/download")
def download():
    if not os.path.isfile(CSV_FILE):
        return "No logs yet."
    return send_file(CSV_FILE, as_attachment=True)
