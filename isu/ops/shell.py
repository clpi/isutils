
from PIL import Image
import os, glob

def shell_assets( 
                direct: str,
                bg_path: str, # PATH OF LOWEST Z-INDEX BG IMG. If bg img dims > demo asset dims, demo res set to bg img res 
                shell_path: str, # if provided, path of img to be placed on top of bg_img but below asset (must be smaller than asset) 
                ):
    res = (1125, 2436)
    asset_new_coord = (736, 48)
    asset_new_size = (449, 972)
    shell_new_coord = (0, 0)
    shell_new_size = (1920, 1080)

    bg_img = Image.open(bg_path)
    bg_dims = bg_img.size

    if 1125 < bg_dims[0] or 2436 < bg_dims[1]:
        res = bg_dims
        fit_res_to_bg = True

    bound = lambda size, loc: tuple(map(sum, zip(size, loc)))
    exceeds_res = lambda bound: bound[0]>1125 or bound[1]>2436

    shell_img = Image.open(shell_path)
    # shell_img_resize = shell_img.resize(shell_new_size, Image.ANTIALIAS)
    # bg_img.paste(shell_img_resize, shell_new_coord, shell_img_resize.convert('RGBA'))

        
    print(bg_dims)
    rx = float(asset_new_size[0] / bg_dims[0])
    ry = float(asset_new_size[1] / bg_dims[1])
    offset_x = asset_new_coord[0]
    offset_y = asset_new_coord[1]
    #rx, ry = tuple(map(lambda z: float(z[0]/z[1]), zip(asset_new_size, bg_dims)))
    #self.insert_img(to_sect, bg_img, "", asset_new_size, asset_new_coord)
    filelist=os.listdir(direct)
    os.chdir(direct)
    for img in glob.glob("*.png"):
        print(img)
        curr_img = bg_img.copy()
        asset = Image.open(str(img))
        asset_resize = asset.resize(asset_new_size, Image.ANTIALIAS)
        curr_img.paste(asset_resize, asset_new_coord, asset_resize.convert('RGBA'))
        curr_img.paste(shell_img.copy(), (0,0), shell_img.convert('RGBA'))
        curr_img.save(str(img))

if __name__ == "__main__":
    shell_assets(
        'C:/Users/Jess/Desktop/screens/AOS-workload 3 screens/',
        r'C:\Users\Jess\Desktop\screens\bgaos.png',
        r'C:\Users\Jess\Desktop\screens\fgaos.png'
    )