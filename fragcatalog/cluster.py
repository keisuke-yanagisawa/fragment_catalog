from dataclasses import dataclass
from hierarchical_group import HierarchicalGroup
from fragment import Fragment


@dataclass
class Cluster(HierarchicalGroup):
    rep_frag: Fragment
