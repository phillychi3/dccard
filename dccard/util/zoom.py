from PIL import Image, ImageDraw

def zoom_magnification(image,prrp):
    return image.resize((int(image.width*prrp),int(image.height*prrp)))

def zoom_extent(image,where,extent):
    if extent<=0:
        raise ValueError("extent must be greater than 0")
    
    if where == "lenght": 
        return (extent,int(extent*image.width/image.height))
        
    elif where == "width":
        return (int(extent*image.height/image.width),extent)
        
