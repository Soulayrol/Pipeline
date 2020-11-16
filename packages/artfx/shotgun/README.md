# fileSystem

## Info 

The fileSystem module is composed by a lib and a config folder.

In the lib folder, you have a file_system to manage file system function, file_info a helper to give info link to a file and template to convert path to dict and dict to pacth

In the config folder, you can find the template_conf need to resolve template path / dictionary

## Functions

#### file_system.py
```python
+ get_childs(data) => generator of dict

+ get_directories(path, full_path=True, recursive=False) => generator
+ get_files(path, full_path=True, recursive=False) => generator

+ create_file(data, content, option="w+")
```

#### file_info.py
```python
+ get_size(file) => str size
+ get_create_date(file) => str date formatter
+ convert_size(size_bytes) => str date
```

#### template.py
```python
+ path_to_dict(path) => dict
+ dict_to_path(data) => str
```
