import re

def parse_ingredients(text):
    pattern = r'(\d+(?:\.\d+)?|\w+)\s*(cups?|tablespoons?)\s+of\s+(\w+)'
    matches = re.findall(pattern, text.lower())
    
    result = []
    word_to_number = { 'one': 1, 'two': 2, 'three': 3, 'half': 0.5 }

    for qty, unit, item in matches:
        qty_num = float(word_to_number.get(qty, qty))
        result.append({
            "ingredient": item,
            "unit": unit,
            "quantity": float(qty_num)
        })

    return result
 
