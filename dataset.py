import re
import ast
import pandas as pd
from rapidfuzz import fuzz, process
from constants import DATASET_FILE

class IngredientDataset:
    def __init__(self):
        self.df = pd.read_csv(DATASET_FILE, index_col='id')
        self.search_index = _create_index(self.df)

    def search(self, query: str):
        query = _normalize(query)
        if not query: return None

        if query in self.search_index:
            index = self.search_index[query]
            row = self.df.loc[index].to_dict()
            row = {'id': index, **row}
            return row

        matches = process.extract(
            query=query,
            choices=self.search_index.keys(),
            scorer=fuzz.token_set_ratio,
            limit=1
        )

        if not matches: return None
        match, score, _ = matches[0]
        if score < 80: return None

        index = self.search_index[match]
        row = self.df.loc[index].to_dict()
        row ['id'] = index
        row['variations'] = [
            query,
            row['name'],
            *_to_list(row['variations'])
        ]
        row['name'] = query.capitalize()
        return row

    def filter(self, queries: set[str]) -> dict[str]:
        results = {}
        for query in queries:
            row = self.search(query)
            if row: results[query] = row
        return results

def _clean(s: str) -> str:
    return s.lower().strip()

def _normalize(s: str) -> str:
    if not s: return None
    sn = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    sn = _clean(sn)
    return sn if sn else None

def _create_index(df: pd.DataFrame):
    index = {
        _normalize(var): index
        for index, row in df.iterrows()
            for var in {
                index,
                row['name'],
                *_to_list(row['variations'])
            }
    }
    if None in index: del index[None]
    if '' in index: del index['']
    return index

def _to_list(x) -> list:
    if not x: return []
    if isinstance(x, list): return x
    if isinstance(x, set): return list(x)
    return ast.literal_eval(x.strip("'").strip('"'))
