from typing import List
from annotation import Annotation, NERtype
from ner_pasers.abstract_parser import AbstractParser
from pullenti.ner.measure.MeasureReferent import MeasureReferent
from pullenti.ner.measure.MeasureKind import MeasureKind

class MeasureParser(AbstractParser):
    """
    Parse Referents related to Measure class.
    """

    def parse(self, referent: MeasureReferent) -> List[Annotation]:
        extracted_ners = []
        
        if referent.kind == MeasureKind.TIME:
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype.AGE))
        elif referent.kind == MeasureKind.COUNT:
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype.NUMBER))
        elif referent.kind == MeasureKind.PERCENT:
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype.PERCENT))

        return extracted_ners