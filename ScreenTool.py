import lvgl as lv
from ili9XXX import ili9488
from espidf import VSPI_HOST
from machine import Pin
import fs_driver #字体相关
import time

# 屏幕启动
def Init():
    # 点亮LED
    p16 = Pin(16, Pin.OUT)
    p16.value(1)
    
    disp = ili9488(miso=13, mosi=11, clk=12, cs=10, dc=17, rst=18,
                    spihost=VSPI_HOST, mhz=20,power=-1,backlight=-1,
                    factor=16, hybrid=True, width=320, height=480,rot=0x40,
                    invert=False, double_buffer=True, half_duplex=False,initialize=True)
    


# 弹幕区域
_dmArea = None #弹幕区域
def _GetDMArea():
    global _dmArea
    if _dmArea is None:
        _dmArea = lv.obj(lv.scr_act)
        _dmArea.set_size(320, 480)
        _dmArea.center()
        _dmArea.set_flex_flow(lv.FLEX_FLOW.COLUMN_REVERSE)
    return _dmArea

# 加载字体
_font = None
def InitFont():
    Show("LoadingFont...")
    global _font
    fs_drv = lv.fs_drv_t()
    fs_driver.fs_register(fs_drv, 'S')
    font_path = "S:./Ali.bin"
    
    time1 = time.time()
    _font = lv.font_load(font_path)
    time1 = time.time() - time1
    font_load_info = (font_path+"的字体载入完毕,共用时" +str(time1)+"S")
    print(font_load_info)
    Show(font_load_info)
                                    
# 显示信息
def Show(msg):
    global _font
    print("[Show]: "+msg)
    dmArea = _GetDMArea()
    lable = lv.label(dmArea)
    if _font is not None:
        lable.set_style_text_font(_font, 0)  # 设置字体
    lable.set_text(msg)
    lv.scr_load(dmArea)




    