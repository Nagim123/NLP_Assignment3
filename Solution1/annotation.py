from enum import Enum

class NERtype(Enum):
    """
    All supported by competion NER types.
    """

    AGE = "AGE"
    AWARD = "AWARD"
    CITY = "CITY"
    COUNTRY = "COUNTRY"
    CRIME = "CRIME"
    DATE = "DATE"
    DISEASE = "DISEASE"
    DISTRICT = "DISTRICT"
    EVENT = "EVENT"
    FACILITY = "FACILITY"
    FAMILY = "FAMILY"
    IDEOLOGY = "IDEOLOGY"
    LANGUAGE = "LANGUAGE"
    LAW = "LAW"
    LOCATION = "LOCATION"
    MONEY = "MONEY"
    NATIONALITY = "NATIONALITY"
    NUMBER = "NUMBER"
    ORDINAL = "ORDINAL"
    ORGANIZATION = "ORGANIZATION"
    PENALTY = "PENALTY"
    PERCENT = "PERCENT"
    PERSON = "PERSON"
    PRODUCT = "PRODUCT"
    PROFESSION = "PROFESSION"
    RELIGION = "RELIGION"
    STATE_OR_PROVINCE = "STATE_OR_PROVINCE"
    TIME = "TIME"
    WORK_OF_ART = "WORK_OF_ART"

class Annotation:
    """
    Class to store annotating data.
    """
    def __init__(self, begin_index: int, end_index: int, ner_type: NERtype) -> None:
        """
        Create annotation by specifying start and end indexes of annotation's characters span and the type of NER.

        Parameters:
            begin_index (int): Character from which span is started (included).
            end_index (int): End character of the span (included).
            ner_type (NERtype): The type of NER.
        """
        
        self.begin_index = begin_index
        self.end_index = end_index
        self.ner_type = ner_type
    
    def __str__(self) -> str:
        return f"[{self.begin_index}, {self.end_index}, {self.ner_type.value}]"
    
    def __repr__(self) -> str:
        return str(self)