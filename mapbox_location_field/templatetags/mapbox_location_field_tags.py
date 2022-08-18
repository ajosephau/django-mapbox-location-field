from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def location_field_includes():
    html = "<meta name='viewport' content='initial-scale=1,maximum-scale=1,user-scalable=no'/><script src='https://static.bikeparty.com.au/static/libraries/mapbox_gl/mapbox-gl.js'></script><link href='https://static.bikeparty.com.au/static/libraries/mapbox_gl/mapbox-gl.css' rel='stylesheet'/><script src='https://static.bikeparty.com.au/static/libraries/mapbox_gl_geocoder/mapbox-gl-geocoder.min.js'></script><link rel='stylesheet' href='https://static.bikeparty.com.au/static/libraries/mapbox_gl_geocoder/mapbox-gl-geocoder.css' type='text/css'/>"
    return mark_safe(html)


@register.simple_tag
def include_jquery():
    return mark_safe("")


@register.filter
@register.simple_tag
def tuple_to_array(coordinates_tuple):
    return list(coordinates_tuple)


