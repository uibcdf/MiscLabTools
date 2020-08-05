from .rgb2hex import hex2rgb as _hex2rgb

class Palette():

    def __init__(self, dict_colors=None):

        if dict_colors is None:

            self.color={
                'dark_red' : None,
                'red' : None,
                'light_red' : None,
                'dark_green' : None,
                'green' : None,
                'light_green' : None,
                'dark_blue' : None,
                'blue' : None,
                'light_blue' : None,
                'dark_yellow' : None,
                'yellow' : None,
                'light_yellow' : None,
                'dark_orange' : None,
                'orange' : None,
                'light_orange' : None,
                'dark_purple' : None,
                'purple' : None,
                'light_purple' : None,
                'dark_brown' : None,
                'brown' : None,
                'light_brown' : None,
                'dark_gray' : None,
                'gray' : None,
                'light_gray' : None,
                'white' : None
                    }

        else:

            self.color=dict_colors

    def rgb(self, color):

        return _hex2rgb(self.color[color])

    def hex(self, color):

        return self.color[color]


class Palette_1(Palette):

    def __init__(self):

        self.color = {
            'dark_red' : '#9B1C1C',
            'red' : '#D62828',
            'light_red' : '#E98686',
            'dark_green' : '#384733',
            'green' : '#77966D',
            'light_green' : '#9CB295',
            'dark_blue' : '#00283D',
            'blue' : '#006AA3',
            'light_blue' : '#85D4FF',
            'dark_yellow' : '#C88304',
            'yellow' : '#FBAF23',
            'light_yellow' : '#FCCC73',
            'dark_orange' : '#C92E03',
            'orange' : '#F13704',
            'light_orange' : '#FC7753',
            'dark_purple' : '#341E24',
            'purple' : '#8E5263',
            'light_purple' : '#D9BDC5',
            'dark_brown' : '#261702',
            'brown' : '#4C2E05',
            'light_brown' : '#865209',
            'dark_gray' : '#3E3C3D',
            'gray' : '#828783',
            'light_gray' : '#B6B9B7',
            'white' : '#FBFFFE'
                }

