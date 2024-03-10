from dataclasses import dataclass
from dataclasses_json import Undefined, dataclass_json
from typing import Optional

# https://github.com/nix-community/noogle/blob/main/pesto/src/main.rs

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass()
class Meta:
    title: str
    signature: Optional[str]

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass()
class ContentSource:
    content: Optional[str]

@dataclass_json
@dataclass()
class Document:
    meta: Meta
    content: Optional[ContentSource]
