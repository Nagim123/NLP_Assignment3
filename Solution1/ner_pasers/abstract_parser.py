from typing import List
from annotation import Annotation
from pullenti.ner.Referent import Referent

class AbstractParser():
    """
    Basic abstract class for parsing useful NERs from Pullenti Referent.
    """
    
    def parse(self, referent: Referent) -> List[Annotation]:
        """
        Extract NERs that are required for comptetion.
        
        Parameters:
            referent (Referent): Pullenti Referent object containing NERs.
        Return:
            (List[Annotation]): List of NER annotations with character span for each.
        """
        pass
