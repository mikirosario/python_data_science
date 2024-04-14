def ft_print_type(allowed_types: set[type], object: any) -> str:
    obj_type: type = type(object)
    if (obj_type not in allowed_types):
        return 'Type not found'
    prefix: str
    if (obj_type == str):
        prefix = f'{object} is in the kitchen'
    else:
        prefix = f'{obj_type.__name__.capitalize()}'
    return f'{prefix} : {obj_type}'

def all_thing_is_obj(object: any) -> int:
    allowed_types: set[type] = {list, tuple, set, dict, str}
    print(f'{ft_print_type(allowed_types, object)}')
    return 42