from typing import List
from annotation import Annotation, NERtype
from ner_pasers.abstract_parser import AbstractParser
from pullenti.ner.named.NamedEntityReferent import NamedEntityReferent
from pullenti.ner.named.NamedEntityKind import NamedEntityKind

class NamedEntityParser(AbstractParser):
    """
    Parse Referents related to NamedEntity class.
    """

    def parse(self, referent: NamedEntityReferent) -> List[Annotation]:
        extracted_ners = []
        
        if referent.kind == NamedEntityKind.ART or referent.kind == NamedEntityKind.MONUMENT:
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype.WORK_OF_ART))
        elif referent.kind == NamedEntityKind.BUILDING:
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype.FACILITY))
        elif referent.kind == NamedEntityKind.LOCATION:
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype.LOCATION))


        return extracted_ners