from typing import Optional, Union, Any

def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonim"

print(get_name("Alma"))

def process_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number:{value}"
    if isinstance(value, float):
        return ValueError("No floats allowed")
    return f"STR:{value}"

try:
    print(process_value(2.5))
except ValueError as e:
    print(e)


def process_anything(value: Any)-> str:
    return f"Process {value}"

print(process_anything(2.5))