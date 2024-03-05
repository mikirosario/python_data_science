def NULL_not_found(object: any) -> int:
    allowed_types: dict[type, tuple[str, callable[[any], bool]]] = {
        type(None): ("Nothing", lambda val : type(val) is type(None)),
        float: ("Cheese", lambda val : val != val),
        int: ("Zero", lambda val : not bool(val)),
        str: ("Empty", lambda val : not bool(val)),
        bool: ("Fake", lambda val : not val)
        }
    obj_type: type = type(object)
    dicVal: tuple[str, callable[[any], bool]] = allowed_types.get(obj_type)
    nullName: str = dicVal[0]
    pred: callable[[any], bool] = dicVal[1]
    if (nullName is None or not pred(object)):
        print('Type not found')
        return 1
    else:
        print(f'{nullName}:', f'{object} {obj_type}' if obj_type is not str else f'{obj_type}')
        return 0
