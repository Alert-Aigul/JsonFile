# Installing
```
pip install json_file
```

# Example
```py
from json_file import JsonFile

with JsonFile("info.json") as info:
    config["hello"] = "world"
```