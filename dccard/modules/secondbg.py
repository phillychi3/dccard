from PIL import Image, ImageDraw

def Secondbg(image:Image,draw:ImageDraw):
    # 圓角長方形
    draw.rectangle([(0,0),(50,50)],fill='#ffffff',outline='#ffffff',width=10)
