import ocr
from dataset import IngredientDataset
from constants import IMAGE_FILE

ings = ocr.extract_ingredients(IMAGE_FILE)
print(ings)

dataset = IngredientDataset()
rows = dataset.filter(ings)

for row in rows.values():
    print(row['name'], ':', row['ruling'])
