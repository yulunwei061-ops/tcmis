from flask import Flask, render_template, request
from datetime import datetime
import math

app = Flask(__name__)

# 首頁 (導覽頁面)
@app.route("/")
def index():
    # 使用你指定的標題與連結樣式
    link = "<h1>歡迎進入魏郁倫的網站</h1>"
    link += "<a href='/mis'>課程</a><hr>"
    link += "<a href='/today'>現在日期時間</a><hr>"
    link += "<a href='/me'>關於我</a><hr>"
    link += "<a href='/welcome?nick=郁倫'>測試 Welcome (GET 傳值)</a><hr>"
    link += "<a href='/account'>網頁表單傳值 (Post 傳值)</a><hr>"
    link += "<a href='/math'>數學計算機 (次方與根號)</a><hr>"
    return link

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1><a href='/'>回首頁</a>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime=str(now))

@app.route("/me")
def me():
    return render_template("about.html")

# Get 傳值練習
@app.route("/welcome", methods=["GET"])
def welcome():
    user = request.values.get("nick")
    if not user:
        user = "訪客"
    return render_template("welcome.html", name=user)

# Post 表單傳值 (密碼功能)
@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "；密碼為：" + pwd
        return f"<h2>{result}</h2><a href='/account'>返回表單</a> | <a href='/'>回首頁</a>"
    return render_template("account.html")

# 數學計算機
@app.route("/math", methods=["GET", "POST"])
def math_calc():
    if request.method == "POST":
        x = float(request.form["x"])
        y = float(request.form["y"])
        opt = request.form["opt"]
        if opt == "pow":
            res = math.pow(x, y)
            msg = f"{x} 的 {y} 次方為：{res}"
        else:
            res = math.pow(x, 1/y)
            msg = f"{x} 的 {y} 次方根為：{res}"
        return f"<h1>計算結果</h1><p>{msg}</p><a href='/math'>回計算機</a>"
    return render_template("math.html")

if __name__ == "__main__":
    app.run(debug=True)