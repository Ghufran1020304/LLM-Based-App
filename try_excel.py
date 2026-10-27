from app.excel_reader import find_part_in_excel

hits = find_part_in_excel("2280")
if not hits:
    print("Not found")
for h in hits:
    print(h["source"])
    for k, v in h["facts"].items():
        print(f"  {k}: {v}")
