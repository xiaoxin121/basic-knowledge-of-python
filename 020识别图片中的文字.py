import pytesseract
from PIL import Image

"""
pytesseract 只是一个“遥控器”，你需要安装“电视机”（Tesseract 引擎）才能工作。
下载安装包：
    由于 Tesseract 官方没有提供 Windows 安装包，通常使用第三方编译版本。
    你可以从 GitHub 下载最新的安装包（例如 tesseract-ocr-w64-setup-5.x.x.exe）。
    推荐下载地址：https://github.com/UB-Mannheim/tesseract/wiki
安装（关键步骤）：
    运行安装程序时，务必勾选 Additional language data 下方的 chi_sim (简体中文)，否则你后续无法识别中文。
    同时，确保安装路径是默认的（通常是 C:\\Program Files\\Tesseract-OCR）。
配置环境变量 (PATH)
    按 Win + S，搜索“编辑系统环境变量”并打开。
    点击右下角的“环境变量”。
    在“系统变量”（下方的框）中找到 Path，选中后点击“编辑”。
    点击“新建”，输入 Tesseract 的安装路径：
验证安装
    重启你的命令行窗口（CMD 或 PowerShell）或 IDE（PyCharm/VS Code）。
    输入以下命令：cmd
    tesseract -v
    如果显示了版本号（如 tesseract 5.x.x），说明环境配置成功。
    
//如果语言包加载失败，可以手动下载 
下载后，将 chi_sim.traineddata 文件放入你的 Tesseract 安装目录下的 tessdata 文件夹中。
语言包下载地址：https://gitee.com/zealzheng/tessdata_fast
"""


pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

image=Image.open('1.jpeg')

text=pytesseract.image_to_string(image, lang='chi_sim')
print(text)