from typing import Any, List, Tuple


def get_choices(constants_class: Any) -> List[Tuple[str, str]]:
    """ enum을 choice field에 넣기 위해 formatting """
    return [
        (member.value, member.name)
        for member in constants_class
    ]
