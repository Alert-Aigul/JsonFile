# Installing
```
pip install easy_json_file
```

# Example
```py
from easy_json_file import JsonFile

with JsonFile("info.json") as info:
    config["hello"] = "world"
```