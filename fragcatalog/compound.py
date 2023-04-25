from dataclasses import dataclass
from typing import List
from fragment import Fragment


@dataclass
class Compound:
    id: int
    smiles: str
    parents: List[Fragment]
