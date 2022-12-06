# BOXIT [![Downloads](https://static.pepy.tech/personalized-badge/boxit?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/boxit)

### Command line utility to make you text stand out

![boxit-banner](https://raw.githubusercontent.com/ShivamPandya/files/main/boxit/banner.gif)

How to install:
```
pip3 install boxit
```

### Arguments currecntly available to use:

| Arguments | Usage |
| :--- | :--- |
| Title object | Anything you want to 'box'. Passing this is mandatory. |
| Pattern | The kind of box you want (Solid, hollow, hollow open(hopen), simple, dbstyle). |
| Color | Color of the entire box including text. |
| Text color | Use this if you want text color to be different from box color. |
| Spacing | How far should your title be from each side inside the box. |
| Shift | How far your box should be from your cli wall. |

Contribute:
- Please do not raise any spam PR.
- You can add documentation as long as it adds some value and makes it easier for the users.
- If you can create a good cover image, I will be very thankful.
- Adding coding snippets for the documentation is required.

## Simple usage:

### Code:
```shell
from boxit.boxit import boxit
name = "Jon Doe"
boxed = boxit(name, pattern='solid')
print(boxed)
```

### Output:
```
┏━━━━━━━┓
┃Jon Doe┃
┗━━━━━━━┛
```

