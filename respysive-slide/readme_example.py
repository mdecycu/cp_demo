from respysive import Slide, Presentation

# 建立簡報物件
p = Presentation()

# === 第一張投影片：標題 ===
slide1 = Slide(center=True)
logo_url = "https://upload.wikimedia.org/wikipedia/commons/4/4d/Fractal_canopy.svg"

title_page_content = {
    'title': '計算機程式概論課程',
    'subtitle': '可攜式系統組成內容介紹',
    'authors': '組員：41423201余思葶、41423204徐雨晴、41423205張詠晴、41423224林靖叡、41423230張倬翊、41423248蔡承修',
    'logo': logo_url
}

# 設定標題頁字型大小
styles = [
    {'color': '#e63946', 'class': 'r-fit-text border-top', 'font-size':'60px'},  # title
    {'color': '#457b9d', 'font-size': '36px'},  # subtitle
    {'color': '#457b9d', 'font-size': '30px'},  # authors
    {'filter': 'invert(100%) opacity(30%)'}  # logo
]

slide1.add_title_page(title_page_content, styles)
p.add_slide(slide1)

# === 第二張投影片：Git是什麼 ===
slide2 = Slide()
slide2.add_title('<span style="font-size:50px;">Git是什麼</span>')

content_git = """
<p class="fragment" style="font-size:30px;">「凡走過必留下痕跡」Git就是在做這件事情，任何一舉一動 Git 都記錄了下來，並且同步遠端的資料庫</p>
<p class="fragment" style="font-size:30px;">Repository（儲存庫）：專案的資料夾，裡面有 Git 記錄的歷史。</p>
<p class="fragment" style="font-size:30px;">Commit（提交）：你每次存檔，會有一個版本紀錄（誰改的、改了什麼）。</p>
<p class="fragment" style="font-size:30px;">Branch（分支）：你可以平行開不同的開發線路，不會互相干擾。</p>
<p class="fragment" style="font-size:30px;">Merge（合併）：把分支的改動整合回來。</p>
<p class="fragment" style="font-size:30px;">Remote（遠端）：像 GitHub、GitLab、Bitbucket 這種雲端版本庫，讓大家可以同步合作。</p>
"""
slide2.add_content([content_git])
p.add_slide(slide2)

# === 第三張投影片：GitHub是什麼 ===
slide3 = Slide()
slide3.add_title('<span style="font-size:50px;">GitHub是什麼?</span>')

content_github = """
<p style="font-size:36px;">
GitHub集結了世界各地許多工程師的智慧結晶，舉凡是資料庫、開源程式碼等等這些都可以在 GitHub 上找到相關的資料庫。<br>
AI 神經網絡甚至也可以從中找到模組或者架構，就例如：AI 網路爬蟲、tensorflow 這類的神經網絡架構，因此只要會寫程式或對某個程式應用方面有些許了解，GitHub 上的資料就可以提供強力幫助。
</p>
<br>
<img src="assets/201510294LJJGcc6vv.jpg" style="width:400px; display:block; margin:auto;">
"""
slide3.add_content([content_github])
p.add_slide(slide3)

# === 第四張投影片：Gits是什麼 ===
slide4 = Slide()
slide4.add_title('<span style="font-size:50px;">Gits是什麼?</span>')
content_gits = """
<p style="font-size:36px;">
Gits 用來快速分享程式碼片段、筆記或任何文字檔，並且只要有連結就可以快速地將檔案分享給其他人。<br>
常被用來放程式碼範例、快速筆記、或是分享設定檔。
</p>
"""
slide4.add_content([content_gits])
p.add_slide(slide4)

# === 第五張投影片：Cmsimde ===
slide5 = Slide()
slide5.add_title('<span style="font-size:50px;">Cmsimde是什麼?</span>')
content_cmsimde = """
<p style="font-size:36px;">
CMSiMDE 是一套以 Python 和 Flask 框架開發的網際內容管理系統，專注於機械設計領域，可管理數位內容，並具有部落格與網頁簡報製作等功能。
</p>
"""
slide5.add_content([content_cmsimde])
p.add_slide(slide5)

# === 最後一張投影片：感謝聆聽 ===
slide6 = Slide(center=True)
slide6.add_title('<span style="font-size:50px;">感謝聆聽<br>報告完畢</span>')
p.add_slide(slide6)

# === 生成 HTML 簡報 ===
p.save_html("my_presentation.html")
print("簡報生成完成！請使用瀏覽器打開 my_presentation.html")