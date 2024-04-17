from typing import List
from annotation import Annotation, NERtype
from ner_pasers.abstract_parser import AbstractParser
from pullenti.ner.decree.DecreeReferent import DecreeReferent

class DecreeParser(AbstractParser):
    """
    Parse Referents related to Decree class.
    """

    def parse(self, referent: DecreeReferent) -> List[Annotation]:
        extracted_ners = []
        
        if referent.get_slot_value("NAME") is None:
            return []
        
        law_name = referent.get_slot_value("NAME").lower()
        for occurence in referent.occurrence:
            cut_start = occurence.get_text().lower().find(law_name)
            cut_end = cut_start + len(law_name) - 1
            extracted_ners.append(Annotation(occurence.begin_char + cut_start,occurence.begin_char + cut_end, NERtype.LAW))
        
        return extracted_ners