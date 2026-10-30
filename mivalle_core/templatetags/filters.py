from django import template

register = template.Library()

@register.filter
def pluralize_rol(value):
    # Si value es none:
    if not value:
        return ''
    
    val = value.lower()

    # Excepciones invariables
    if val in ['mecenas']:
        return value 
    
    # Reglas generales de pluralización
    if val.endswith('or'):
        return value[:-1] + 'res'
    if val.endswith('ro'):
        return value + 's'
    elif val.endswith('ista'):
        return value + 's'
    elif val.endswith("ar"): 
        return value + "es"
    elif val.endswith('e'):
        return value + 's'
    else:
        return value + 'es'

@register.filter   
def join_roles(roles_queryset, sep=', '):    
    return sep.join([str(r) for r in roles_queryset]) if roles_queryset else ''