import easyocr

# 初始化 EasyOCR 对象，指定使用的语言模型
reader = easyocr.Reader(['ch_sim', 'en'])
def main():
    # 读取图像并进行文字识别
    image_path = 'C:\\Users\\Administrator\\Desktop\\7.2336\\1.png'
    result = reader.readtext(image_path)

    # 输出识别结果
    for detection in result:
        text = detection[1]
        print(f'Text: {text}')

    # 可选：可视化识别结果
   # reader.visualize(image_path, result)


if __name__ == "__main__":
    main()
