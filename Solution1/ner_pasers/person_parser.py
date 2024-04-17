from typing import List
from annotation import Annotation, NERtype
from ner_pasers.abstract_parser import AbstractParser
from pullenti.ner.person.PersonReferent import PersonReferent

class PersonParser(AbstractParser):
    """
    Parse Referents related to Person class.
    """

    def parse(self, referent: PersonReferent) -> List[Annotation]:
        extracted_ners = []
        check_names = []
        for check_name in ["FIRSTNAME", "MIDDLENAME", "LASTNAME"]:
            attr_name = referent.get_slot_value(check_name)
            if attr_name is not None:
                check_names.append(attr_name[:-2 if len(attr_name) > 3 else -1].lower())
        
        for occurence in referent.occurrence:
            begin_ind, end_ind = len(occurence.get_text()), 0
            for segment in occurence.get_text().split(" "):
                for check_name in check_names:
                    s_s = occurence.get_text().find(segment)
                    s_e = s_s + len(segment)
                    if check_name in segment.lower():
                        begin_ind = min(begin_ind, s_s)
                        end_ind  = max(end_ind, s_e)
            if end_ind - 1 < begin_ind:
                continue
    
            extracted_ners.append(Annotation(occurence.begin_char + begin_ind, occurence.begin_char + end_ind - 1, NERtype.PERSON))
        
        return extracted_ners