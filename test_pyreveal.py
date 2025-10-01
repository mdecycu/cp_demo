from pyreveal import PyReveal, ImageBackground

# 相對路徑或絕對路徑都可以
bg_image_path = "assets/blockhole.jpg"

presentation = PyReveal(title="My Presentation", theme="white", transition="slide")
bg_image = ImageBackground(image_url=bg_image_path)

# 加入幻燈片
presentation.add_slide("計算機程式概論\n\
可攜式系統組成內容介紹", background=bg_image)
presentation.add_slide("Another slide", background=bg_image)

# 生成 HTML 簡報
presentation.save_to_file("my_presentation.html")
print("簡報生成完成！")
 
