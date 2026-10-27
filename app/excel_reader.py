import pandas as pd
from pathlib import Path


def clean(value):
    """Turn 2280, 2280.0, ' 2280 ' all into '2280'."""
    s = str(value).strip()
    if s.endswith(".0"):
        s = s[:-2]
    return s


def find_part_in_excel(part_number, data_dir="data"):
    part_number = clean(part_number)
    results = []

    for file in Path(data_dir).glob("*.xls*"):
        if file.name.startswith("~$"):
            continue
        sheets = pd.read_excel(file, sheet_name=None, dtype=str)
        for sheet_name, df in sheets.items():
            for idx, row in df.iterrows():
                if any(clean(cell) == part_number for cell in row.values):
                    facts = {col: str(val) for col, val in row.items()
                             if pd.notna(val) and str(val).strip() != ""}
                    results.append({
                        "source": f"Excel file '{file.name}', sheet '{sheet_name}', row {idx + 2}",
                        "facts": facts,
                    })
    return results
