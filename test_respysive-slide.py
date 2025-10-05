from respysive import Slide, Presentation

# 建立簡報
p = Presentation()

# === 第一張投影片：標題頁 ===
slide1 = Slide(center=True)
title_page_content = {
    'title': '計算機程式概論課程',
    'subtitle': '可攜式系統組成內容介紹',
    'authors': '41423201余思葶、41423204 徐雨晴、41423205張詠晴、41423224林靖叡、41423230張倬翊、41423248蔡承修',
    'logo': 'https://upload.wikimedia.org/wikipedia/commons/4/4d/Fractal_canopy.svg'
}
styles = [
    {'color': '#e63946', 'class': 'r-fit-text border-top'},  # 標題
    {},  # 副標題
    {},  # 作者
    {'filter': 'invert(100%) opacity(30%)'},  # logo
]
slide1.add_title_page(title_page_content, styles)
p.add_slide(slide1)

# === 第二張投影片：Git是什麼 (逐段顯示) ===
slide2 = Slide()
slide2.add_text("""
<h2 style="font-family:'Noto Sans TC', sans-serif;">Git是什麼</h2>
<p class="fragment" style="font-size:24px; font-family:'Noto Sans TC', sans-serif;">「凡走過必留下痕跡」Git就是在做這件事情，任何一舉一動 Git 都記錄下來，並且同步遠端資料庫。</p>
<p class="fragment" style="font-size:24px; font-family:'Noto Sans TC', sans-serif;">Repository（儲存庫）：專案資料夾，裡面有 Git 的歷史紀錄。</p>
<p class="fragment" style="font-size:24px; font-family:'Noto Sans TC', sans-serif;">Commit（提交）：你每次存檔，會有一個版本紀錄（誰改的、改了什麼）。</p>
<p class="fragment" style="font-size:24px; font-family:'Noto Sans TC', sans-serif;">Branch（分支）：你可以平行開不同的開發線路，不會互相干擾。</p>
<p class="fragment" style="font-size:24px; font-family:'Noto Sans TC', sans-serif;">Merge（合併）：把分支的改動整合回來。</p>
<p class="fragment" style="font-size:24px; font-family:'Noto Sans TC', sans-serif;">Remote（遠端）：像 GitHub、GitLab、Bitbucket 這種雲端版本庫，讓大家可以同步合作。</p>
""")
p.add_slide(slide2)

# === 第三張投影片：GitHub是什麼 + 圖片 ===
slide3 = Slide()
slide3.add_text("""
<h2 style="font-family:'Noto Sans TC', sans-serif;">GitHub是什麼?</h2>
<p style="font-size:24px; font-family:'Noto Sans TC', sans-serif;">
GitHub集結了世界各地許多工程師的智慧結晶，舉凡是資料庫、開源程式碼等等這些都可以在 GitHub 上找到相關的資料庫。
AI 神經網絡甚至也可以從中找到模組或者架構，例如：AI 網路爬蟲、TensorFlow 等神經網絡架構。
</p>
<img src="assets/201510294LJJGcc6vv.jpg" style="width:400px; display:block; margin:auto;">
""")
p.add_slide(slide3)

# === 第四張投影片：Gits是什麼 ===
slide4 = Slide()
slide4.add_text("""
<h2 style="font-family:'Noto Sans TC', sans-serif;">Gits是什麼?</h2>
<p style="font-size:24px; font-family:'Noto Sans TC', sans-serif;">
Gits 用來快速分享程式碼片段、筆記或任何文字檔，並且只要有連結就可以快速地將檔案分享給其他人。
常被用來放程式碼範例、快速筆記、或分享設定檔。
</p>
""")
p.add_slide(slide4)

# === 第五張投影片：Cmsimde ===
slide5 = Slide()
slide5.add_text("""
<h2 style="font-family:'Noto Sans TC', sans-serif;">Cmsimde是什麼?</h2>
<p style="font-size:24px; font-family:'Noto Sans TC', sans-serif;">
CMSiMDE 是一套以 Python 和 Flask 框架開發的網際內容管理系統，專注於機械設計領域，可管理數位內容，並具有部落格與網頁簡報製作等功能。
</p>
""")
p.add_slide(slide5)

# === 第六張投影片：如何使用這些工具 ===
slide6 = Slide()
slide6.add_text("""
<h2 style="font-family:'Noto Sans TC', sans-serif;">如何使用這些工具?</h2>
<p style="font-size:24px; font-family:'Noto Sans TC', sans-serif;">
1. 建立 GitHub 帳號<br>
2. 在本地建立 Git 並連結 GitHub<br>
3. 透過 Cms 設定 Git 和 GitHub 溝通<br>
4. 將 GitHub 資料庫網址連結至 Cmsimde<br>
5. 推送修改到遠端：<br>
&nbsp;&nbsp;git add .<br>
&nbsp;&nbsp;git commit -m '描述修改'<br>
&nbsp;&nbsp;git push origin main
</p>
""")
p.add_slide(slide6)

# === 第七張投影片：為什麼要使用這些工具 ===
slide7 = Slide()
slide7.add_text("""
<h2 style="font-family:'Noto Sans TC', sans-serif;">為什麼要使用這些工具?</h2>
<p style="font-size:24px; font-family:'Noto Sans TC', sans-serif;">
建立本地和遠端系統後，只要攜帶 USB 或 SSD 就能隨時修改程式，並將程式連結 GitHub。
Git 會記錄每一次修改，Cmsimde 也會記錄修改歷程。
</p>
""")
p.add_slide(slide7)

# === 第八張投影片：資料索引 ===
slide8 = Slide()
slide8.add_text("""
<h2 style="font-family:'Noto Sans TC', sans-serif;">資料索引</h2>
<p style="font-size:24px; font-family:'Noto Sans TC', sans-serif;">
少量 GPT<br>
集結組員知識
</p>
""")
p.add_slide(slide8)

# === 最後一張投影片：感謝聆聽 ===
slide9 = Slide(center=True)
slide9.add_text("""
<h1 style="font-family:'Noto Sans TC', sans-serif;">感謝聆聽<br>報告完畢</h1>
""")
p.add_slide(slide9)

# === 儲存簡報 ===
p.save("my_presentation.html")
print("簡報生成完成！請使用瀏覽器打開 my_presentation.html")
