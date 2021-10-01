from django import template

register = template.Library()

@register.filter
def get_region(value, arg):
    return value[int(arg)].region.region_name_ru

@register.filter
def get_city_name_ru(value, arg):
    return value[int(arg)].city_name_ru

@register.filter
def get_slug(value, arg):
    return value[int(arg)].slug

@register.filter()
def half_list_range(value, is_first):
    list_len = len(value)
    if list_len % 2 != 0:
        if is_first:
            return range(list_len // 2 + 1)
        else:
            return range(list_len // 2 + 1, list_len)
    else:
        if is_first:
            return range(list_len // 2)
        else:
            return range(list_len // 2, list_len)

@register.filter()
def has_places(value, arg):
    if value[int(arg)].places.all():
        return "link-info"
    else:
        return "link-secondary"
