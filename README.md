# Filtering and Searching a Mineral Catelog
Add features to a web application that catalogs minerals to build a fully-featured web site. Add the ability to search information and filter it to match user preferences.

## Project Requirements
Full-text search and filtering of mineral fields
Unit test the app
Optimize query times to the database

## App Requirements
Django == 1.11.3

django-debug-toolbar == 1.8

### Start Application
After installing django and required files, run django on your local machine terminal to get the interactive minerals site
```python
python manage.py runserver
```
## Features
Once the porject is running, in your browser, you should be able to see and do the following:
1. Homepage - see a list of minerals
2. Click on a list to see more minerals
3. Search field to search minerals by the following multiple fields
e.g. searching for the strunz-classification term "09.Db.45" and this would yield the "Aerinite" mineral
```python
def mineral_search(request):
    term = request.GET.get("q")
    minerals = m.filter(
        Q(name__icontains=term) |
        Q(group__icontains=term) |
        Q(image_caption__icontains=term) |
        Q(category__icontains=term) |
        Q(formula__icontains=term) |
        Q(crystal_system__icontains=term) |
        Q(color__icontains=term) |
        Q(luster__icontains=term) |
        Q(crystal_habit__icontains=term) |
        Q(specific_gravity__icontains=term) |
        Q(streak__icontains=term) |
        Q(strunz_classification__icontains=term)
```
4. Filter minerals by first letter name
5. Filter minerals by group
```python
# Template tag for the index.html template
@register.inclusion_tag('minerals/group_nav.html')
def nav_mineral_groups():
    groups = ["Silicates", "Oxides", "Sulfates", "Sulfides", "Carbonates", "Halides", "Sulfosalts", "Phosphates",
              "Borates", "Organic Minerals", "Arsenates", "Native Elements", "Other"]
    return {'groups': groups}
```
6. Filter minerals by color
