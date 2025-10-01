from pyreveal import PyReveal, ImageBackground

# 背景圖片路徑
bg_image_path = "assets/blockhole.jpg"

# 初始化簡報
presentation = PyReveal(title="My Presentation", theme="white", transition="slide")
bg_image = ImageBackground(image_url=bg_image_path)

# 自訂全局字型樣式（放到 <head>）
custom_head_style = """
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap" rel="stylesheet">
<style>
body, h1, h2, h3, p, div {
    font-family: 'Noto Sans TC', sans-serif;
}
.fragment {
    opacity: 0;
}
.reveal .slides .fragment.visible {
    opacity: 1;
}
</style>
"""

# 投影片內容
slides_content = [
    # 第一張
    ("""計算機程式概論課程<br>可攜式系統組成內容介紹""",
     """組員：41423201余思葶、41423204 徐雨晴、41423205張詠晴、<br>
     41423224林靖叡、41423230張倬翊、41423248蔡承修"""),

    # 第二張 fragment
    ("Git是什麼",
     """<p class="fragment">「凡走過必留下痕跡」Git就是在做這件事情，任何一舉一動 Git 都記錄了下來，並且同步遠端的資料庫</p>
     <p class="fragment">Repository（儲存庫）：專案的資料夾，裡面有 Git 記錄的歷史。</p>
     <p class="fragment">Commit（提交）：你每次存檔，會有一個版本紀錄（誰改的、改了什麼）。</p>
     <p class="fragment">Branch（分支）：你可以平行開不同的開發線路，不會互相干擾。</p>
     <p class="fragment">Merge（合併）：把分支的改動整合回來。</p>
     <p class="fragment">Remote（遠端）：像 GitHub、GitLab、Bitbucket 這種雲端版本庫，讓大家可以同步合作。</p>"""),

    # 第三張（GitHub是什麼）
    ("GitHub是什麼",
     """GitHub集結了世界各地許多工程師的智慧結晶，舉凡是資料庫、開源程式碼等等都可以在 GitHub 上找到相關的資料庫。<br>
     AI 神經網絡甚至也可以從中找到模組或架構，例如：AI 網路爬蟲、tensorflow 等神經網絡架構，因此只要會寫程式或對某個程式應用有了解，GitHub 上的資料就可以提供幫助。"""),

    # 其他投影片
    ("Gits是什麼",
     "Gits 用來快速分享程式碼片段、筆記或任何文字檔，只要有連結就能快速分享。"),
    ("Cmsimde是什麼",
     "CMSiMDE 是一套以 Python 和 Flask 框架開發的網際內容管理系統，專注於機械設計領域，可管理數位內容，並具有部落格與簡報功能。"),
    ("如何使用這些工具?",
     "1. 建立 GitHub 帳號<br>2. 建立 Git 並連結 GitHub<br>3. 設定 Cms 與 GitHub 溝通<br>4. 將資料庫連結至 Cmsimde<br>5. 推送修改：<br>git add .<br>git commit -m ''<br>git push origin main"),
    ("為什麼要使用這些工具?",
     "建立好可攜系統後，攜帶 USB 或 SSD 就可隨時修改程式，並同步到 GitHub，Git 會記錄修改歷程。"),
    ("資料索引",
     "少量GPT<br>集結組員知識"),
    ("感謝聆聽", "報告完畢")
]

# 加入投影片
for title, content in slides_content:
    html_content = f"""
<h2 style="text-align:center;">{title}</h2>
<div style="text-align:left; font-size:35px;">
{content}
</div>
"""
    presentation.add_slide(html_content, background=bg_image)

# 生成 HTML
presentation.save_to_file("my_presentation.html")

# 讀取 HTML（用二進位模式避免編碼問題）
with open("my_presentation.html", "rb") as f:
    html_bytes = f.read()

html_text = html_bytes.decode("utf-8", errors="ignore")

# 在 <head> 後插入自訂字型樣式
html_text = html_text.replace("<head>", f"<head>\n{custom_head_style}")

# 寫回 HTML，確保使用 UTF-8
with open("my_presentation.html", "wb") as f:
    f.write(html_text.encode("utf-8"))

print("簡報生成完成，繁體中文字型已加入 <head>，可直接在 GitHub Pages 顯示！")
