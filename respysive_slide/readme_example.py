from respysive import Slide, Presentation

# 建立簡報物件
p = Presentation()

# 軍綠色背景
bg_color = "#4B5320"
# 文字顏色
text_color = "#f0f0f0"
# 字型
font_family = "Arial, Helvetica, sans-serif"

# === 第一張投影片：標題 ===
slide1 = Slide(center=True, background_color=bg_color)
logo_url = "https://upload.wikimedia.org/wikipedia/commons/4/4d/Fractal_canopy.svg"
title_page_content = {
    'title': '計算機程式概論課程',
    'subtitle': '可攜式系統組成內容介紹',
    'authors': '組員：41423201余思葶、41423204徐雨晴、41423205張詠晴、41423224林靖叡、41423230張倬翊、41423248蔡承修',
    'logo': logo_url
}
styles = [
    {'color': '#e63946', 'class': 'r-fit-text border-top', 'font-size':'60px', 'font-family': font_family},  # title
    {'color': text_color, 'font-size': '36px', 'font-family': font_family},  # subtitle
    {'color': text_color, 'font-size': '30px', 'font-family': font_family},  # authors
    {'filter': 'invert(100%) opacity(30%)'}  # logo
]
slide1.add_title_page(title_page_content, styles)
p.add_slide(slide1)

# === 第二張投影片：Git是什麼 ===
slide2 = Slide(background_color=bg_color)
slide2.add_title(f'<span style="font-size:50px; color:{text_color}; font-family:{font_family};">Git是什麼</span>')
content_git = f"""
<p class="fragment" style="font-size:30px; color:{text_color}; font-family:{font_family};">
「凡走過必留下痕跡」Git就是在做這件事情，任何一舉一動 Git 都記錄下來，並同步遠端資料庫。
</p>
<p class="fragment" style="font-size:30px; color:{text_color}; font-family:{font_family};">
Repository（儲存庫）：專案資料夾，裡面有 Git 記錄的歷史。
</p>
<p class="fragment" style="font-size:30px; color:{text_color}; font-family:{font_family};">
Commit（提交）：每次存檔都會有版本紀錄。
</p>
"""
slide2.add_content([content_git])
p.add_slide(slide2)

# === 第三張投影片：GitHub是什麼 ===
slide3 = Slide(background_color=bg_color)
slide3.add_title(f'<span style="font-size:50px; color:{text_color}; font-family:{font_family};">GitHub是什麼?</span>')
content_github = f"""
<p style="font-size:30px; color:{text_color}; font-family:{font_family};">
GitHub 集結世界各地工程師的智慧結晶，資料庫、開源程式碼等都能找到相關資料。
</p>
<img src="assets/201510294LJJGcc6vv.jpg" style="width:400px; display:block; margin:auto;">
"""
slide3.add_content([content_github])
p.add_slide(slide3)

# === 第四張投影片：Gits是什麼 ===
slide4 = Slide(background_color=bg_color)
slide4.add_title(f'<span style="font-size:50px; color:{text_color}; font-family:{font_family};">Gits是什麼?</span>')
content_gits = f"""
<p style="font-size:30px; color:{text_color}; font-family:{font_family};">
Gits 用來快速分享程式碼片段、筆記或文字檔，並且只要有連結就可分享。
</p>
"""
slide4.add_content([content_gits])
p.add_slide(slide4)

# === 第五張投影片：Cmsimde ===
slide5 = Slide(background_color=bg_color)
slide5.add_title(f'<span style="font-size:50px; color:{text_color}; font-family:{font_family};">Cmsimde是什麼?</span>')
content_cmsimde = f"""
<p style="font-size:30px; color:{text_color}; font-family:{font_family};">
CMSiMDE 是一套以 Python 和 Flask 框架開發的網際內容管理系統，可管理數位內容。
</p>
"""
slide5.add_content([content_cmsimde])
p.add_slide(slide5)

# === 最後一張投影片：感謝聆聽 ===
slide6 = Slide(center=True, background_color=bg_color)
slide6.add_title(f'<span style="font-size:50px; color:{text_color}; font-family:{font_family};">感謝聆聽<br>報告完畢</span>')
p.add_slide(slide6)

# 生成 HTML 簡報
p.save_html("my_presentation.html")
print("簡報生成完成！請使用瀏覽器打開 my_presentation.html")
