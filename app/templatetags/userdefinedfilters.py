from django import template

register=template.Library()

@register.filter(name='low')
def lower(value):
    return value.lower()

@register.filter(name='rep')
def replace_char(value,arg):
    return value.replace(arg,'b')

@register.filter()
def remove_char(value,arg):
    return value.replace(arg,'')

def count_char(value,arg):
    cot=0
    for i in range(len(value)):
        if arg==value[i:i+len(arg)]:
            cot+=1
    return cot

register.filter('char',count_char)


#register.filter('low',lower)
#register.filter('rep',replace_char)
#register.filter('rem',remove_char)