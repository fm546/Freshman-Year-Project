import pyttsx3

# 初始化
test = pyttsx3.init()

# 设置要说的话
test.say("这是一条测试语句")

# 保存为音频文件
test.save_to_file("这是一条测试语句", "./study/test.mp3")

# 运行并等待完成
test.runAndWait()