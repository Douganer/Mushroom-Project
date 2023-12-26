import time

from Mushroom.utils.dm import DM


# 移动点击，需要判断鼠标是否移动到目标位置，再点击【左键】
def move_click(dm: DM, x, y):
    dm.MoveTo(x, y)
    while True:
        suc, cur_pos_x, cur_pos_y = dm.GetCursorPos()
        if cur_pos_x == x and cur_pos_y == y:
            dm.LeftClick()
            return
        else:
            dm.MoveTo(x, y)
            time.sleep(0.01)
