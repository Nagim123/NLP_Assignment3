from typing import List
from annotation import Annotation, NERtype
from ner_pasers.abstract_parser import AbstractParser
from pullenti.ner.org.OrganizationReferent import OrganizationReferent

class OrganizationParser(AbstractParser):
    """
    Parse Referents related to Organization class.
    """

    def parse(self, referent: OrganizationReferent) -> List[Annotation]:
        extracted_ners = []

        if referent.get_slot_value("NAME") is None:
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype.ORGANIZATION))
        else:
            org_name = referent.get_slot_value("NAME").lower() 
            for occurence in referent.occurrence:
                if len(occurence.get_text()) < len(org_name):
                    continue
                start_pos = occurence.get_text().lower().find(org_name)
                end_pos = start_pos + len(org_name) - 1
                extracted_ners.append(Annotation(occurence.begin_char + start_pos, occurence.begin_char + end_pos, NERtype.ORGANIZATION))
        return extracted_ners