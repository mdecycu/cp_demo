from pyreveal import PyReveal, ImageBackground

# 背景圖片路徑
bg_image_path = "assets/blockhole.jpg"

presentation = PyReveal(title="My Presentation", theme="white", transition="slide")
bg_image = ImageBackground(image_url=bg_image_path)

# 第一張投影片
presentation.add_slide(
    """<h2 style="text-align:center;">計算機程式概論課程<br>可攜式系統組成內容介紹</h2><br><br>
<div style="text-align:left; font-size:35px;">
組員：41423201余思葶、41423204 徐雨晴、41423205張詠晴、<br>
41423224林靖叡、41423230張倬翊、41423248蔡承修
</div>""",
    background=bg_image
)

# 第二張投影片（fragment，逐段顯示）
presentation.add_slide(
    """<h2 style="text-align:center;">Git是什麼</h2>
<div style="text-align:left; font-size:35px;">
<p class="fragment">「凡走過必留下痕跡」Git就是在做這件事情，任何一舉一動 Git 都記錄了下來，並且同步遠端的資料庫</p>
<p class="fragment">Repository（儲存庫）：專案的資料夾，裡面有 Git 記錄的歷史。</p>
<p class="fragment">Commit（提交）：你每次存檔，會有一個版本紀錄（誰改的、改了什麼）。</p>
<p class="fragment">Branch（分支）：你可以平行開不同的開發線路，不會互相干擾。</p>
<p class="fragment">Merge（合併）：把分支的改動整合回來。</p>
<p class="fragment">Remote（遠端）：像 GitHub、GitLab、Bitbucket 這種雲端版本庫，讓大家可以同步合作。</p>
</div>""",
    background=bg_image
)


# 第三張投影片（GitHub是什麼）
presentation.add_slide(
    """<h2 style="text-align:center;">GitHub是什麼?</h2>
<div style="text-align:left; font-size:35px;">
GitHub集結了世界各地許多工程師的智慧結晶，舉凡是資料庫、開源程式碼等等這些都可以在 GitHub 上找到相關的資料庫。<br>
AI 神經網絡甚至也可以從中找到模組或者架構，就例如：AI 網路爬蟲、tensorflow 這類的神經網絡架構，因此只要會寫程式或對某個程式應用方面有些許了解，GitHub 上的資料就可以提供強力幫助。
</div>""",
    background=bg_image
)

# 其餘投影片
presentation.add_slide(
    """<h2 style="text-align:center;">Gits是什麼?</h2>
<div style="text-align:left; font-size:35px;">
Gits 用來快速分享程式碼片段、筆記或任何文字檔，並且只要有連結就可以快速地將檔案分享給其他人。<br>
常被用來放程式碼範例、快速筆記、或是分享設定檔。
</div>""",
    background=bg_image
)

presentation.add_slide(
    """<h2 style="text-align:center;">Cmsimde是什麼?</h2>
<div style="text-align:left; font-size:35px;">
CMSiMDE 是一套以 Python 和 Flask 框架開發的網際內容管理系統，專注於機械設計領域，可管理數位內容，並具有部落格與網頁簡報製作等功能。
</div>""",
    background=bg_image
)

presentation.add_slide(
    """<h2 style="text-align:center;">如何使用這些工具?</h2>
<div style="text-align:left; font-size:35px;">
  1. 建立 GitHub 帳號以方便使用 Gits<br>
  2. 在近端建立 Git 並連結 GitHub<br>
  3. 透過 Cms 設定 Git 和 GitHub 間的溝通管道<br>
  4. 接著將 GitHub 資料庫網址存下並連結至 Cmsimde<br>
  5. 日後只要用 Cms 查詢網路，推送到遠端：<br>
　git push origin main <br>
　暫存修改：git add .<br>
　提交修改：git commit -m ''<br>
　檢查工作目錄狀態：git status<br>
基本上就完成了。
</div>""",
    background=bg_image
)

presentation.add_slide(
    """<h2 style="text-align:center;">為什麼要使用這些工具?</h2>
<div style="text-align:left; font-size:35px;">
在製作近端及遠端的過程中，我們清楚明白地理解到，一旦建立好近端可攜系統後，日後只要攜帶個 USB 或 SSD 固態硬碟就可以隨時隨地立即修改程式，再將程式連結 GitHub 就可以輕鬆更改程式，在這過程中甚至還有 Git 紀錄修改的過程，就連 Cmsimde 在修改的過程也會錄下來。
</div>""",
    background=bg_image
)

presentation.add_slide(
    """<h2 style="text-align:center;">資料索引</h2>
<div style="text-align:left; font-size:35px;">
少量GPT<br>
集結組員知識
</div>""",
    background=bg_image
)

presentation.add_slide("感謝聆聽<br>報告完畢", background=bg_image)

# 生成 HTML 簡報
presentation.save_to_file("my_presentation.html")
print("簡報生成完成！")
