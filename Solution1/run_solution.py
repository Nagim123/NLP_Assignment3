import json
import argparse
from typing import List, Tuple
from solution import PullentiSolution
from annotation import Annotation

def read_inference_dataset(filepath: str) -> Tuple[List[str], List[int]]:
    """
    Read inference dataset and returns sentences along with their identificators.

    Parameters:
        filepath (str): Path to inference file.
    Return:
        (Tuple[List[str], List[str]]): List of sentence and list of corresponding sentences ids.
    """
    sentences = []
    sentence_ids = []
    
    with open(filepath) as dataset_file:
        lines = dataset_file.readlines()
    
    for line in lines:
        content = json.loads(line)
        sentences.append(content["senences"])
        sentence_ids.append(content["id"])

    return (sentences, sentence_ids)

def write_results_to_file(filepath: str, annotations: List[List[Annotation]], sentence_ids: List[int]) -> None:
    """
    Write results to a file supported by CodaLab submit format.

    Parameters:
        filepath (str): Path where to save the file.
        annotations (List[List[Annotation]]): List of annotations for each sentence.
        sentence_ids (List[int]): Identificators of sentence.
    """
    with open(filepath, "w") as result_file:
        for annotation, sentence_id in zip(annotations, sentence_ids):
            content = dict()
            ners = []
            for ner in annotation:
                ners.append([ner.begin_index, ner.end_index, ner.ner_type.value])
            content["ners"] = ners
            content["id"] = sentence_id
            line = json.dumps(content)
            result_file.write(line + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--test_file_path', type=str, help="Path to file to read test samples from and do inference", required=True)
    args = parser.parse_args()

    # Read test file
    test_file_path = args.test_file_path
    sentences, sentence_ids = read_inference_dataset(test_file_path)

    # Find NERs
    solution = PullentiSolution()
    annotated_sentences = solution.annotate_ner(sentences)

    # Create submit file
    write_results_to_file("data/test.jsonl", annotated_sentences, sentence_ids)