from . import types
import json

def from_str(s: str) -> types.Document:
    myjson = json.loads(s)
    return types.Document.schema().load(myjson, many=True)



