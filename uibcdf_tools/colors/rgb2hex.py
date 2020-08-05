
def rgb2hex(rgb):

    from matplotlib.colors import to_hex

    return to_hex(rgb, keep_alpha=False)

def hex2rgb(hex):


    from matplotlib.colors import to_rgb

    return to_rgb(hex)

