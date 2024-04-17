from typing import List, Dict
from pullenti.Sdk import Sdk
from pullenti.ner.ProcessorService import ProcessorService
from pullenti.ner.Processor import Processor
from pullenti.ner.SourceOfAnalysis import SourceOfAnalysis
from pullenti.ner.AnalysisResult import AnalysisResult
from pullenti.ner.Referent import Referent
from pullenti.ner.measure.MeasureAnalyzer import MeasureAnalyzer
from pullenti.ner.Token import Token
from pullenti.ner.NumberToken import NumberToken
from pullenti.ner.NumberSpellingType import NumberSpellingType
from annotation import Annotation, NERtype

from ner_pasers.abstract_parser import AbstractParser
from ner_pasers.person_parser import PersonParser
from ner_pasers.personproperty_parser import PersonPropertyParser
from ner_pasers.date_parser import DateParser
from ner_pasers.decree_parser import DecreeParser
from ner_pasers.measure_parser import MeasureParser
from ner_pasers.money_parser import MoneyParser
from ner_pasers.organziation_parser import OrganizationParser
from ner_pasers.geo_parser import GeoParser
from ner_pasers.named_entity_parser import NamedEntityParser


class PullentiSolution():
    """
    Solution that utilize rule-based Russian library Pullenti
    """
    def __init__(self) -> None:
        super().__init__()
        Sdk.initialize_all()
        self.processor: Processor = ProcessorService.create_processor()
        self.processor.add_analyzer(MeasureAnalyzer())
        self.parsers : Dict[str, AbstractParser] = {
            "PERSON": PersonParser(),
            "PERSONPROPERTY": PersonPropertyParser(),
            "GEO": GeoParser(),
            "ORGANIZATION": OrganizationParser(),
            "MEASURE": MeasureParser(),
            "DATE": DateParser(),
            "MONEY": MoneyParser(),
            "DECREE": DecreeParser(),
            "NAMEDENTITY": NamedEntityParser()
        }
    
    def __anotate_numbers(self, begin_token: Token) -> List[Annotation]:
        """
        Annotate NERs related to number class using token analysis.

        Parameters:
            begin_token (Token): First token of sentence.
        Return:
            (List[Annotation]): Annotations of NUMBER NER.
        """
        extracted_ners = []
        token: Token = begin_token
        while token is not None:
            # Check if token is a number spelled by words.
            if isinstance(token, NumberToken) and token.typ == NumberSpellingType.WORDS:
                extracted_ners.append(Annotation(token.begin_char, token.end_char, NERtype.NUMBER))
            token = token.next0_
        return extracted_ners
    
    def __remove_nested_dates(self, date_ners: List[Annotation]) -> List[Annotation]:
        """
        Removes dates that are nested.

        Parameters:
            date_ners (List[Annotation]): All date NERs.
        
        Return:
            (List[Annotation]): Cleared list of NERs without any nested NERs.
        """
        
        if len(date_ners) == 0:    
            return []
        date_ners.sort(key=lambda x: x.begin_index - x.end_index)
        parent_dates = [date_ners[0]] # Only dates that are not children are allowed
        for date_ner in date_ners:
            flag = False
            for span in parent_dates:
                if (date_ner.begin_index >= span.begin_index and date_ner.end_index <= span.end_index):
                    flag = True
            if not flag:
                parent_dates.append(date_ner)

        return parent_dates

    def annotate_ner(self, sentences: List[str]) -> List[List[Annotation]]:
        """
        Find and annotate NERs in arbitary sentences.

        Parameters:
            sentence (List[str]): Sentences to process.
        Return:
            (List[List[Annotation]]): Annotation for each sentence.
        """
        annotations = []
        for sentence in sentences:
            ners = []
            date_ners = []
            
            # Find number NER by token analysis
            analysis_result: AnalysisResult = self.processor.process(SourceOfAnalysis(sentence))
            ners.extend(self.__anotate_numbers(analysis_result.first_token))
            
            # Find other types of NERs using Pullenti and custom written parsers.
            entity: Referent
            for entity in analysis_result.entities:
                if entity.type_name not in self.parsers: # If we met something we can not handle, skip it.
                    continue

                parsed_ners = self.parsers[entity.type_name].parse(entity)
                for ner in parsed_ners:
                    if ner.ner_type == NERtype.DATE:
                        # Collect DATE NERs into a seperate list.
                        date_ners.append(ner)
                    else:
                        ners.append(ner)
            #Remove nested DATE NERs since there is no such NERs in our dataset.
            ners.extend(self.__remove_nested_dates(date_ners))

            annotations.append(ners)
        return annotations