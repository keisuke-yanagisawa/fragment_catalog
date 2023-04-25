from typing import List, Tuple
from cluster import Cluster
from fragment import Fragment
from scaffold import Scaffold
from compound import Compound


def __load_compounds(ctof_file: str) -> List[Compound]:
    NotImplementedError()


def __load_fragments(ftoc_file: str) -> List[Fragment]:
    NotImplementedError()


def __load_scaffolds(stof_file: str) -> List[Scaffold]:
    NotImplementedError()


def __load_clusters(ctos_file: str) -> List[Cluster]:
    NotImplementedError()


def __set_parent_for_scaffold(scaffolds: List[Scaffold], clusters: List[Cluster]):
    NotImplementedError()


def __set_parent_for_fragment(fragments: List[Fragment], scaffolds: List[Scaffold]):
    NotImplementedError()


def load_database(ctos_file,
                  stof_file,
                  ftoc_file,
                  ctof_file) -> Tuple[List[Cluster], List[Scaffold], List[Fragment], List[Compound]]:
    clusters = __load_clusters(ctos_file)
    scaffolds = __load_scaffolds(stof_file)
    fragments = __load_fragments(ftoc_file)
    compounds = __load_compounds(ctof_file)

    __set_parent_for_scaffold(scaffolds, clusters)
    __set_parent_for_fragment(fragments, scaffolds)

    return clusters, scaffolds, fragments, compounds
