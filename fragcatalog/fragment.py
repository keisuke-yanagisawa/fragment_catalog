from dataclasses import dataclass
from hierarchical_group import HierarchicalGroup


@dataclass
class Fragment(HierarchicalGroup):
    smiles: str
