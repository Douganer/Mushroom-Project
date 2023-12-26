import ctypes
import os
from pathlib import Path

# Global variable to store the loaded DLL instance
ocr = None
model = None


# 加载ocr的dll,并初始化
def load_ocr():
    global ocr, model
    try:
        path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'resources'))
        ocr = ctypes.windll.LoadLibrary(path + "./ocr/RapidOCR.dll")
        #    检测模型det,方向模型cl,识别模型rec,字典模型
        det_path = Path(path + "/ocr/检测模型/中文_OCRv4.onnx")
        cl_path = Path(path + "/ocr/方向模型/原始分类器模型.onnx")
        rec_path = Path(path + "/ocr/识别模型/中文简体_OCRv4.onnx")
        keys_path = Path(path + "/ocr/识别字典/中文简体_OCRv4_高精度.txt")
        model = ocr.model(det_path.read_bytes(), det_path.stat().st_size,
                          cl_path.read_bytes(), cl_path.stat().st_size,
                          rec_path.read_bytes(), rec_path.stat().st_size,
                          keys_path.read_bytes(), 2)
    except Exception as e:
        print("系统异常", e)


def findStr(str):
    if ocr is None:
        raise RuntimeError("DLL not loaded. Call load_dll first.")
    ocr.findtext(model, '', '', '', 60, 1024, 0.3, 0.3, 1.5)


if __name__ == "__main__":
    load_ocr()
    # findStr(str)
