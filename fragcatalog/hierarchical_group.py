from dataclasses import dataclass
from typing import List


@dataclass
class HierarchicalGroup:
    id: int
    children: List["HierarchicalGroup"]
    parent: "HierarchicalGroup"
