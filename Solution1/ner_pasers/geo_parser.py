from typing import List
from annotation import Annotation, NERtype
from ner_pasers.abstract_parser import AbstractParser
from pullenti.ner.geo.GeoReferent import GeoReferent

class GeoParser(AbstractParser):
    """
    Parse Referents related to GEO class.
    """

    def parse(self, referent: GeoReferent) -> List[Annotation]:
        extracted_ners = []
        
        if referent.is_city or referent.is_big_city:
            for occurence in referent.occurrence:
                city_name = occurence.get_text().split()[-1]
                cut_start = occurence.get_text().find(city_name)
                cut_end = cut_start + len(city_name) - 1
                extracted_ners.append(Annotation(occurence.begin_char + cut_start,occurence.begin_char + cut_end, NERtype.CITY))
        elif referent.is_state:
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype.COUNTRY))
        elif referent.is_region:
            for occurence in referent.occurrence:
                extracted_ners.append(Annotation(occurence.begin_char, occurence.end_char, NERtype.STATE_OR_PROVINCE))

        return extracted_ners