import json

with open('ingredient_db.json') as f:
    db = json.load(f)

def convert_to_grams(parsed_data):
    results = []
    for item in parsed_data:
        ingredient = item['ingredient']
        unit = item['unit']
        qty = item['quantity']

        if ingredient in db and unit in db[ingredient]:
            grams = qty * db[ingredient][unit]
            results.append({
                "ingredient": ingredient,
                "grams": round(grams, 2)
            })
    return results
 
