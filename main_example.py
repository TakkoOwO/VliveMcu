import ScreenTool
import SdTools
import os
import time
import gc

def main():
     # 查看空闲内存字节数
    free_memory = gc.mem_free()
    print("空闲内存:", free_memory)
    
    SdTools.Init()
    print(os.listdir("/sd"))

    ScreenTool.Show("海内存知己天涯若比邻")
    
    ScreenTool.Show("English。，、；：？！“”‘’（）【】《》—…-—— ·")
    
    

    # 查看空闲内存字节数
    free_memory = gc.mem_free()
    print("空闲内存:", free_memory)


if __name__ == '__main__':
    main()


#     import lvgl as lv
#     import fs_driver #字体相关
#     
#     ScreenTool._InitScreen()
#     SdTools.Init()
#     fs_drv = lv.fs_drv_t()
#     fs_driver.fs_register(fs_drv, 'S')
#     fontStream = lv.tiny_ttf_create_file("S:/sd/TTF.ttf",16)
#     print(fontStream)
    





    


    

