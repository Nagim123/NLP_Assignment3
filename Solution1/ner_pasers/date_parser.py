from typing import List
from annotation import Annotation, NERtype
from ner_pasers.abstract_parser import AbstractParser
from pullenti.ner.date.DateReferent import DateReferent

class DateParser(AbstractParser):
    """
    Parse Referents related to Date class.
    """

    def parse(self, referent: DateReferent) -> List[Annotation]:
        extracted_ners = []
        
        if (referent.year == 0 and referent.month == 0 and referent.day == 0) and\
            (referent.minute > -1 or referent.second > -1 or referent.hour > -1):
            
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype("TIME")))
        else:
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype("DATE")))
        
        return extracted_ners