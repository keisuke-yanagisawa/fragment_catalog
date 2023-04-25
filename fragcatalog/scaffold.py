from dataclasses import dataclass
from hierarchical_group import HierarchicalGroup


@dataclass
class Scaffold(HierarchicalGroup):
    smiles: str
