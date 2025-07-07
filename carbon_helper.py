from carbon_data import carbon_data

def format_material_for_frontend(material_key): 
    
    #all possible carbon data under specific material category
    material_data = carbon_data[material_key]
    
    #JSON details that we will later send back to frontend
    response = {
        "material": material_data.get("material", material_key),
        "recyclable": material_data.get("recyclable", False),
        "recycled_carbon_score": material_data.get("recycled_carbon_score"),
        "unrecycled_carbon_score": material_data.get("unrecycled_carbon_score"),
        "carbon_impact_rating_recycled": material_data.get("carbon_impact_rating_recycled"),
        "carbon_impact_rating_unrecycled": material_data.get("carbon_impact_rating_unrecycled"),
        "recycling_rate_percent": material_data.get("recycling_rate_percent"),
        "notes": material_data.get("notes", []),
        "has_subtypes": "types" in material_data,
        "subtypes": list(material_data["types"].keys()) if "types" in material_data else []
    }
    
    return response

#For if there is a subtype for a category (eg. plastic has HDPE, LDPE etc. that a user can specify
# in drop down frontend)
def format_subtype_for_frontend(material_key, subtype_key):
    #all possible carbon data under specific material category
    material_data = carbon_data[material_key]

    # for categories like cardboard, metal, etc with only type and not types
    if "types" not in material_data:
        raise ValueError(f"{material_key} does not have subtype options")

    if subtype_key not in material_data["types"]:
        raise ValueError(f"Invalid subtype '{subtype_key}' for material '{material_key}'")

    subtype_data = material_data["types"][subtype_key]

    # return updated data for specific subtype (formatted same as original json)
    return {
        "material": material_key,
        "type": subtype_key,
        "recyclable": material_data.get("recyclable", False),
        "recycled_carbon_score": subtype_data.get("recycled_carbon_score"),
        "unrecycled_carbon_score": subtype_data.get("unrecycled_carbon_score"),
        "carbon_impact_rating_recycled": subtype_data.get("carbon_impact_rating_recycled"),
        "carbon_impact_rating_unrecycled": subtype_data.get("carbon_impact_rating_unrecycled"),
        "recycling_rate_percent": subtype_data.get("recycling_rate_percent"),
        "notes": subtype_data.get("notes", []),
    }

def list_all_materials():
    return list(carbon_data.keys())