import cutility as cu

# test text
f_text = "dummy text data"
cu.write_text(f_text, "./data/example.txt")
f_text = cu.read_text("./data/example.txt")
print(f_text)

# test json
f_json = {"dummy": "dummy json data"}
cu.write_json(f_json, "./data/example.json")
f_json = cu.read_json("./data/example.json")
print(f_json)

# test yaml
f_yaml = {"p1": "dummy", "p2": ["yaml"]}
cu.write_yaml(f_yaml, "./data/example.yml")
f_yaml = cu.read_yaml("./data/example.yml")
print(f_yaml)
