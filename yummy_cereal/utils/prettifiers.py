from typing import Dict


def prettify_dict(dct: Dict) -> str:
    return "/n".join(f"{k}: {v}" for k, v in dct.items())
