
def get_cmap(name, palette, tone=None):

    if name=='red_white_blue':

        return _red_white_blue(palette, tone=tone)

    if name=='red_gray_blue':

        return _red_gray_blue(palette, tone=tone)

    else:
        raise NotImplementedError


def make_cmap_linear(name, palette, values):

    from matplotlib.colors import LinearSegmentedColormap

    for ii in range(len(values)):

        values[ii][1] = palette.rgb(values[ii][1])

    cmap = LinearSegmentedColormap.from_list(name, values)

    return cmap


cmap_names = ['red_white_blue', 'red_gray_blue']


def _red_white_blue(palette, tone=None):

    from matplotlib.colors import LinearSegmentedColormap

    if tone is None:
        prefix = ''
    else:
        prefix = tone+'_'

    c1 = palette.rgb(prefix+'red')
    c2 = palette.rgb('white')
    c3 = palette.rgb(prefix+'blue')

    values = [[0.0, c1], [0.5, c2], [1.0, c3]]
    cmap = LinearSegmentedColormap.from_list('red_white_blue', values)

    return cmap


def _red_gray_blue(palette, tone=None):

    from matplotlib.colors import LinearSegmentedColormap

    if tone is None:
        prefix = ''
    else:
        prefix = tone+'_'

    c1 = palette.rgb(prefix+'red')
    c2 = palette.rgb(prefix+'gray')
    c3 = palette.rgb(prefix+'blue')

    values = [[0.0, c1], [0.5, c2], [1.0, c3]]
    cmap = LinearSegmentedColormap.from_list('red_white_blue', values)

    return cmap


