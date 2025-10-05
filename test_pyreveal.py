from pyreveal import PyReveal, ImageBackground

# 相對路徑或絕對路徑都可以
bg_image_path = "assets/blockhole.jpg"

presentation = PyReveal(title="My Presentation", theme="white", transition="slide")
bg_image = ImageBackground(image_url=bg_image_path)
presentation = PyReveal()
# 加入幻燈片
presentation.add_slide("Introduction to Computer Programming\n\
Introduction to the components of the portable system", background=bg_image)
presentation.add_slide(
    content="計算機程式概論課程<br>可攜式系統組成內容介紹",
    background=bg_image
)
presentation.add_slide(
    content="組員：<br>41423201 余思葶、<br>41423204 徐雨晴 、<br>41423205 張詠晴 、<br>41423224 林靖叡 、<br>41423230 張倬翊 、<br>41423248 蔡承修。",
    background=bg_image
)
presentation.add_slide(
    content="git是什麼?<br>凡走過必留下痕跡，git就是在做這件事情，任何一舉一動都git記錄下來了，並且同步遠端的資料庫",
    background=bg_image
)
# 生成 HTML 簡報
presentation.save_to_file("my_presentation.html")
print("簡報生成完成！")
 
