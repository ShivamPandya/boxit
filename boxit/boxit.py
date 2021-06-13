def boxit(title, color:str='', pattern:str= None,
        textcolor:str='', spacing:int=0, shift:int = 0)->str:

    title = str(title)

    colors = {
        'black':30, 'red':31, 'green':32, 'brown':33,
        'blue':34, 'purple':35, 'cyan':36, 'grey':37,
        'orange': 91,'lightgreen': 92,'yellow': 93, 'lightblue': 94,
        'lightpurple': 95,'lightcyan': 96,'white': 97, '':'' }

    patterns = {"hollow" : {"ulc": "╔", "llc": "╚",
                            "urc": "╗", "lrc": "╝",
                            "hoz": "═", "bar": "║"},
                "solid"  : {"ulc": "┏", "llc": "┗",
                            "urc": "┓", "lrc": "┛",
                            "hoz": "━", "bar": "┃"},
                "simple" : {"ulc": "+", "llc": "+",
                            "urc": "+", "lrc": "+",
                            "hoz": "-", "bar": "|"},
                "curved" : {"ulc": "╭", "llc": "╰",
                            "urc": "╮", "lrc": "╯",
                            "hoz": "-", "bar": "|"},
                "hopen"  : {"ulc": "╬", "llc": "╬",
                            "urc": "╬", "lrc": "╬",
                            "hoz": "═", "bar": "║"},
                "dbstyle":  {"ulc": "+", "llc": "+",
                            "urc": "+", "lrc": "+",
                            "hoz": "-", "bar": "¦"}   
                            }
    
    '''This block is to handle custome exception.
    It is mainly for data validation. It validates for color and spacing
    Incase the color is not availabale or the user enters something wrong in that field,
    and/or incase the spacing & shifting is not integer value(s),
    the following block(s) will raise exception'''
    if color not in colors or textcolor not in colors:
        err1 = "\u001b[31mColor not available! List of available colors:\n"
        err2 = "red, blue*, green*, cyan*, purple*, orange, brown, yellow, white, grey, black\n"
        err3 = "*These colors have lighter shades too. Prepend 'light' to activate it, example: lightgreen\u001b[0m"
        ColorError = err1+err2+err3
        raise Exception(ColorError)

    if type(spacing) != int or type(shift) != int:
        TypeError = "\u001b[31mInvalid data type, 'spacing' and/or 'shift' must be an integer\u001b[0m"
        raise Exception(TypeError)

    '''Custome excpetion ends'''

    if color:
        color = f"\u001b[{colors[color]}m"
    if textcolor:
        textcolor = f"\u001b[{colors[textcolor]}m"

    if pattern == None:
        result = f'{color}{title}\033[0m'
        return result
    
    pattern = pattern.lower()
    title = " "*spacing + title + " "*spacing
    length = len(title) 

    row1 = f"{color}{' '*shift}{patterns[pattern]['ulc']}{patterns[pattern]['hoz']*length}{patterns[pattern]['urc']}\033[0m\n"
    row2 = f"{color}{' '*shift}{patterns[pattern]['bar']}{textcolor}{title}{color}{patterns[pattern]['bar']}\033[0m\n"
    row3 = f"{color}{' '*shift}{patterns[pattern]['llc']}{patterns[pattern]['hoz']*length}{patterns[pattern]['lrc']}\033[0m"
    
    result = f"{row1}{row2}{row3}"

    return result