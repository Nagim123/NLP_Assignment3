from typing import List
from annotation import Annotation, NERtype
from ner_pasers.abstract_parser import AbstractParser
from pullenti.ner.person.PersonPropertyReferent import PersonPropertyReferent
from pullenti.ner.person.PersonPropertyKind import PersonPropertyKind

class PersonPropertyParser(AbstractParser):
    """
    Parse Referents related to Person Property class.
    """

    def parse(self, referent: PersonPropertyReferent) -> List[Annotation]:
        extracted_ners = []
        profession_kinds = [
            PersonPropertyKind.BOSS,
            PersonPropertyKind.KING,
            PersonPropertyKind.MILITARYRANK,
            PersonPropertyKind.UNDEFINED
        ]

        if referent.kind in profession_kinds:
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype.PROFESSION))
        elif referent.kind == PersonPropertyKind.NATIONALITY:
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype.NATIONALITY))
        
        return extracted_ners