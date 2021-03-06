from django import template
from minerals.models import Mineral

register = template.Library()


@register.inclusion_tag('minerals/mineral_group_nav.html')
def nav_group_list():
    """Returns dictionary of minerals groups to display as a navigation pane"""
    groups = []
    minerals = Mineral.objects.all()
    for mineral in minerals:
        if mineral.group not in groups:
            groups.append(mineral.group)
    groups_count = len(groups)
    return {'groups_count': groups_count}


@register.inclusion_tag('minerals/group_nav.html')
def nav_mineral_groups():
    groups = ["Silicates", "Oxides", "Sulfates", "Sulfides", "Carbonates", "Halides", "Sulfosalts", "Phosphates",
              "Borates", "Organic Minerals", "Arsenates", "Native Elements", "Other"]
    return {'groups': groups}


@register.inclusion_tag('minerals/color_nav.html')
def nav_mineral_colors():
    colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Pink', 'Brown', 'White', 'Gray', 'Black']
    return {'colors': colors}

