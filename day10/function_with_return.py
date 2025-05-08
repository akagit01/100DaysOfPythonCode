def format_name(fname,lname):
    """
    This function takes the firstname and lastname
    and uses built in function .title() to convert
    text with initial letter as upper case and rest in lower case
    :param fname:
    :param lname:
    :return:
    """
    name=(fname.title())+ ' '+ (lname.title())   #.title sets first letter in upper case
    return name

name=format_name('aka','naka')
print(name)