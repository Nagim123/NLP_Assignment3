from typing import List
from annotation import Annotation, NERtype
from ner_pasers.abstract_parser import AbstractParser
from pullenti.ner.money.MoneyReferent import MoneyReferent

class MoneyParser(AbstractParser):
    """
    Parse Referents related to Money class.
    """

    def parse(self, referent: MoneyReferent) -> List[Annotation]:
        extracted_ners = []
        for occurence in referent.occurrence:
            extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype.MONEY))
        return extracted_ners