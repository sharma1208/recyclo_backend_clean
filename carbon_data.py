carbon_data = {
    "glass": {
        "material": "glass",
        "recyclable": True,
        "type": "none",
        "recycling_rate_percent": 33.2,
        "recycled_mtco2e_per_short_ton": -0.28,
        "unrecycled_mtco2e_per_short_ton": 0.60,
        "recycled_carbon_score": -0.309,  # kg CO2e/kg
        "unrecycled_carbon_score": 0.662,  # kg CO2e/kg
        "carbon_impact_rating_recycled": "low",
        "carbon_impact_rating_unrecycled": "high",
        "notes": [
            "Carbon scores converted from EPA WARM values (MTCO2e/short ton) to kg CO2e/kg using the formula:",
            "kg CO2e per kg = MTCO2e per short ton × (1000 / 907.185) ≈ MTCO2e per short ton × 1.103",
            "Recycling rate based on EPA 2018 data; update as new data becomes available.",
            "Recycling carbon score reflects net emissions reduction (negative value means avoided emissions).",
            "Unrecycled carbon score reflects emissions from virgin production."
        ],
        "source_url": "https://www.epa.gov/system/files/documents/2023-12/warm_containers_packaging_and_non-durable_goods_materials_v16_dec.pdf"
    },
    "metal": {
        "material": "metal",
        "recyclable": True,
        "types": {
            "aluminum cans" : {
                "type": "aluminum cans", 
                "recycling_rate_percent": 50.4, 
                "recycled_mtco2e_per_short_ton": -9.13,
                "unrecycled_mtco2e_per_short_ton": 10.98,
                "recycled_carbon_score": round(-9.13 * 1.103, 3),
                "unrecycled_carbon_score": round(10.98 * 1.103, 3),
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                        "High GHG savings from recycling aluminum due to energy-intensive virgin production.",
                        "Data from WARM Exhibit 2-17 and 2-23. Total virgin emissions ≈ 7.17 + 0.09 + 3.72 = 10.98 MTCO2e/short ton.",
                        "Carbon scores converted using 1 MTCO2e/short ton ≈ 1.103 kg CO2e/kg."
                    ]
            }, 
            "aluminum ingot": {
                "type": "aluminum ingot",
                "recycling_rate_percent": 50.4,
                "recycled_mtco2e_per_short_ton": -7.20,
                "unrecycled_mtco2e_per_short_ton": 7.48,
                "recycled_carbon_score": round(-7.20 * 1.103, 3),     # ≈ -7.946 kg CO2e/kg
                "unrecycled_carbon_score": round(7.48 * 1.103, 3),    # ≈ 8.254 kg CO2e/kg
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Ingot emissions slightly lower than cans due to differences in processing.",
                    "Virgin emissions from Exhibit 2-23: 4.23 + 0.07 + 3.18 = 7.48 MTCO2e/short ton.",
                    "Carbon score uses same MTCO2e to kg CO2e/kg formula."
                ]
            },
            "steel cans": {
                "type": "steel cans",
                "recycling_rate_percent": 70.9,
                "recycled_mtco2e_per_short_ton": -1.83,
                "unrecycled_mtco2e_per_short_ton": 3.64,
                "recycled_carbon_score": round(-1.83 * 1.103, 3),     # ≈ -2.019 kg CO2e/kg
                "unrecycled_carbon_score": round(3.64 * 1.103, 3),    # ≈ 4.017 kg CO2e/kg
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Steel cans have substantial GHG savings from recycling due to reduced need for virgin iron/ore processing.",
                    "Virgin emissions = 2.40 + 0.37 + 0.87 = 3.64 MTCO2e/short ton.",
                    "Recycled includes negative emissions due to avoided extraction."
                ]
            },
            "copper wire": {
                "type": "copper wire",
                "recycling_rate_percent": 34.1,
                "recycled_mtco2e_per_short_ton": -4.49,
                "unrecycled_mtco2e_per_short_ton": 6.78,
                "recycled_carbon_score": round(-4.49 * 1.103, 3),     # ≈ -4.954 kg CO2e/kg
                "unrecycled_carbon_score": round(6.78 * 1.103, 3),    # ≈ 7.483 kg CO2e/kg
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Copper wire has high emissions due to energy-intensive mining and smelting.",
                    "Virgin emissions = 6.72 + 0.06 = 6.78 (no process non-energy emissions).",
                    "Recycling reduces emissions significantly, though some transport/process remains."
                ]
            }
            
            
        },
        "source_url": "https://www.epa.gov/system/files/documents/2023-12/warm_containers_packaging_and_non-durable_goods_materials_v16_dec.pdf"
    },
    "cardboard": {
        "material": "cardboard",
        "type": "None",
        "recyclable": True,
        "recycling_rate_percent": 96.5,
        "recycled_mtco2e_per_short_ton": -3.14,
        "unrecycled_mtco2e_per_short_ton": 0.83,
        "recycled_carbon_score": round(-3.14 * 1.103, 3), # kg CO2e/kg
        "unrecycled_carbon_score": 0.916,  # kg CO2e/kg
        "carbon_impact_rating_recycled": "low",
        "carbon_impact_rating_unrecycled": "high",
        "notes": [
            "Recycled carbon score reflects post-consumer emissions from Exhibit 3-17.",
            "Unrecycled emissions computed from process energy + transportation + process non-energy (Exhibit 3-21).",
            "MTCO2e/short ton values converted to kg CO2e/kg using MTCO2e × 1.103.",
            "Corrugated containers represent cardboard in WARM modeling due to lack of separate category.",
            "High recycling rate (96.5%) contributes to low overall impact when recycled."
        ],
        "source_url": "https://www.epa.gov/system/files/documents/2023-12/warm_containers_packaging_and_non-durable_goods_materials_v16_dec.pdf"
            
    },
    "paper": {
        "material": "paper",
        "recyclable": True,
        "types": {
            "magazines_third_class_mail": {
                "type": "magazines/third-class mail",
                "recycling_rate_percent": 65.0,
                "recycled_mtco2e_per_short_ton": -3.07,
                "unrecycled_mtco2e_per_short_ton": 1.60,
                "recycled_carbon_score": round(-3.07 * 1.103, 3),  
                "unrecycled_carbon_score": round(1.60 * 1.103, 3), 
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Virgin: 1.58 + 0.02 + 0.00 = 1.60 MTCO₂e/short ton - based on EPA WARM v16, Exhibit 3-21",
                    "Recycled: Exhibit 3-17"
                ]
            },
            "newspaper": {
                "type": "newspaper",
                "recycling_rate_percent": 65.0,
                "recycled_mtco2e_per_short_ton": -2.71,
                "unrecycled_mtco2e_per_short_ton": 1.91,
                "recycled_carbon_score": round(-2.71 * 1.103, 3),   
                "unrecycled_carbon_score": round(1.91 * 1.103, 3), 
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Virgin: 1.85 + 0.06 + 0.00 = 1.91 MTCO₂e/short ton - based on EPA WARM v16, Exhibit 3-21",
                    "Recycled: Exhibit 3-17"
                ]
            },
            "office paper": {
                "type": "office paper",
                "recycling_rate_percent": 65.0,
                "recycled_mtco2e_per_short_ton": -2.86,
                "unrecycled_mtco2e_per_short_ton": 1.98,
                "recycled_carbon_score": round(-2.86 * 1.103, 3), 
                "unrecycled_carbon_score": round(0.98 * 1.103, 3),
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Virgin: 0.93 + 0.02 + 0.03 = 0.98 MTCO₂e/short ton - based on EPA WARM v16, Exhibit 3-21",
                    "Recycled: Exhibit 3-17"
                ]
            },
            "phone books": {
                "type": "phone books",
                "recycling_rate_percent": 65.0,
                "recycled_mtco2e_per_short_ton": -2.62 ,
                "unrecycled_mtco2e_per_short_ton": 2.33,
                "recycled_carbon_score": round(-2.62 * 1.103, 3) , 
                "unrecycled_carbon_score": round(2.33 * 1.103, 3),
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Virgin: 2.29 + 0.04 + 0.00 = 2.33 MTCO₂e/short ton -based on EPA WARM v16, Exhibit 3-21",
                    "Recycled: Exhibit 3-17"
                ]
            },
            "textbooks": {
                "type": "textbooks",
                "recycling_rate_percent": 65.0,
                "recycled_mtco2e_per_short_ton": -3.1,
                "unrecycled_mtco2e_per_short_ton": 2.06,
                "recycled_carbon_score": round(-3.1 * 1.103, 3),   # ~2.194
                "unrecycled_carbon_score": round(2.06 * 1.103, 3),
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Virgin: 2.02 + 0.04 + 0.00 = 2.06 MTCO₂e/short ton - based on EPA WARM v16, Exhibit 3-21",
                    "Recycled: Exhibit 3-17"
                ]
            },  
            "mixed paper general": {
                "type": "mixed paper (general)",
                "recycling_rate_percent": 65.0,
                "recycled_mtco2e_per_short_ton": -3.55,
                "unrecycled_mtco2e_per_short_ton": 1.18,
                "recycled_carbon_score": round(-3.55 * 1.103, 3),  
                "unrecycled_carbon_score": round(1.18 * 1.103, 3), # ~1.302
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Virgin: 1.08 + 0.09 + 0.01 = 1.18", 
                    "Recycled: Exhibit 3-17"
                ]
            },
            "mixed paper residential": {
                "type": "mixed paper (primarily residential)",
                "recycling_rate_percent": 65.0,
                "recycled_mtco2e_per_short_ton": -3.55,
                "unrecycled_mtco2e_per_short_ton": 1.18,
                "recycled_carbon_score": round(-3.55 * 1.103, 3), 
                "unrecycled_carbon_score": round(1.18 * 1.103, 3), # ~1.302
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Virgin: 1.07 + 0.10 + 0.01 = 1.18", 
                    "Recycled: Exhibit 3-17"
                ]
            },
            "mixed paper office": {
                "type": "mixed paper (primarily from offices)",
                "recycling_rate_percent": 65.0,
                "recycled_mtco2e_per_short_ton": -3.58,
                "unrecycled_mtco2e_per_short_ton": 1.38,
                "recycled_carbon_score": round(-3.58 * 1.103, 3),  
                "unrecycled_carbon_score": round(1.38 * 1.103, 3), # ~1.523
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Recycled: 1.32 + 0.03 + 0.00 = 1.35",
                    "Virgin: 1.34 + 0.03 + 0.01 = 1.38"
                ]
            }
        },
        "source_url": "https://www.epa.gov/system/files/documents/2023-12/warm_containers_packaging_and_non‑durable_goods_materials_v16_dec.pdf"
        
    },
    "plastic": {
        "material": "plastic",
        "recyclable": True,
        "types": {
            "HDPE": {
                "type": "HDPE",
                "recycling_rate_percent": 8.7,  # EPA 2018
                "recycled_mtco2e_per_short_ton": -0.76,
                "unrecycled_mtco2e_per_short_ton": 1.52,
                "recycled_carbon_score": round(-0.76 * 1.103, 3),      # kg CO2e/kg
                "unrecycled_carbon_score": round(1.52 * 1.103, 3),     # kg CO2e/kg
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Used for bottles, containers, drums, and chemical packaging.",
                    "Recycled score based on EPA WARM v16, Exhibit 5-11.",
                    "Unrecycled score based on virgin production values (process + transport), Exhibit 5-14."
                ]
            },
            "PET": {
                "type": "PET",
                "recycling_rate_percent": 8.7,  # EPA 2018
                "recycled_mtco2e_per_short_ton": -1.04,
                "unrecycled_mtco2e_per_short_ton": 2.22,
                "recycled_carbon_score": round(-1.04 * 1.103, 3),
                "unrecycled_carbon_score": round(2.22 * 1.103, 3),
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Used in beverage bottles and synthetic fibers.",
                    "Only HDPE, PET, and PP have recycling data available in WARM.",
                    "Carbon scores converted using ×1.103 factor (short ton to kg CO2e/kg)."
                ]
            },
            "PP": {
                "type": "PP",
                "recycling_rate_percent": 8.7,  # EPA 2018
                "recycled_mtco2e_per_short_ton": -0.79,
                "unrecycled_mtco2e_per_short_ton": 1.53,
                "recycled_carbon_score": round(-0.79 * 1.103, 3),
                "unrecycled_carbon_score": round(1.53 * 1.103, 3),
                "carbon_impact_rating": "high",
                "carbon_impact_rating_recycled": "low",
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Used in packaging, fibers, automotive parts.",
                    "High impact strength and heat resistance; limited low-temp performance.",
                    "Recycling data available for PP in WARM v16."
                ]
            },
            "LDPE": {
                "type": "LDPE",
                "recycling_rate_percent": 8.7,  # EPA 2018
                "recycled_mtco2e_per_short_ton": None,
                "unrecycled_mtco2e_per_short_ton": 1.76,
                "recycled_carbon_score": None,
                "unrecycled_carbon_score": round(1.76 * 1.103,3),
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Unrecycled value from WARM Exhibit 5-8, 5‑9, & 5-10 /v16; recycling not modeled in WARM."
                ]
            },
            "LLDPE": {
                "type": "LLDPE", 
                "recycling_rate_percent": 8.7,  # EPA 2018
                "recycled_mtco2e_per_short_ton": None,
                "unrecycled_mtco2e_per_short_ton": 1.54,
                "recycled_carbon_score": None,
                "unrecycled_carbon_score": round(1.54 * 1.103,3),
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Unrecycled value from WARM Exhibit 5‑8, 5-9, & 5-10/v16; recycling not modeled in WARM."
                ]
            },
            "PS": {
                "type": "PS", 
                "recycling_rate_percent": 8.7,  # EPA 2018
                "recycled_mtco2e_per_short_ton": None,
                "unrecycled_mtco2e_per_short_ton": 2.46,
                "recycled_carbon_score": None,
                "unrecycled_carbon_score": round(2. * 1.103,3),
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Unrecycled value from WARM Exhibit 5‑8, 5-9, & 5-10/v16; recycling not modeled in WARM."
                ]
            },
            "PVC": {
                "type": "PVC", 
                "recycling_rate_percent": 8.7,  # EPA 2018
                "recycled_mtco2e_per_short_ton": None,
                "unrecycled_mtco2e_per_short_ton": 1.89,
                "recycled_carbon_score": None,
                "unrecycled_carbon_score": round(1.89 * 1.103,3),
                "carbon_impact_rating_unrecycled": "high",
                "notes": [
                    "Unrecycled value from WARM Exhibit 5‑8, 5-9, & 5-10/v16; recycling not modeled in WARM."
                ]
            },
            
        },
        "notes": [
            "Only HDPE, PET, and PP have full recycled carbon data in WARM v16.",
            "All CO2 scores converted to kg CO2e/kg using ×1.103 factor from MTCO2e/short ton.",
            "Recycling rate from EPA 2018 data (most plastics still poorly recycled)."
        ],
        "source_url": "https://www.epa.gov/system/files/documents/2023-12/warm_containers_packaging_and_non-durable_goods_materials_v16_dec.pdf"
        },
    "trash": {
        "material": "trash",
        "recyclable": False,
        "type": "fallback",
        "recycling_rate_percent": 0.0,
        "recycled_mtco2e_per_short_ton": None,
        "unrecycled_mtco2e_per_short_ton": 0.25,  # conservative estimate from mixed MSW landfill
        "recycled_carbon_score": None,
        "unrecycled_carbon_score": round(0.25 * 1.103, 3),  # ≈ 0.276 kg CO₂e/kg
        "carbon_impact_rating_unrecycled": "medium",
        "carbon_impact_rating_recycled": "medium",
        "notes": [
            "**This is a fallback category** for items that could not be confidently classified into a known recyclable material type.",
            "Emission factor based on EPA WARM landfill estimates for mixed municipal solid waste (MSW): ~0.2–0.3 MTCO₂e/short ton.",
            "Converted using: 0.25 × 1.103 = ~0.276 kg CO₂e/kg.",
            "Actual impact may vary depending on material mix, landfill gas capture efficiency, and disposal method.",
            "Update this value if more specific post-classification handling data becomes available."
        ],
        "source_url": "https://www.epa.gov/warm"
    }
}
