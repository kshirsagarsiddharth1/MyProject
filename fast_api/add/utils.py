import multiprocessing
from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add_lists(lists: List[List[int]]) -> List[int]:
    with multiprocessing.Pool() as pool:
        results = pool.map(sum, lists)
    return results
