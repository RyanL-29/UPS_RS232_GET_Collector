import json
from pydantic import BaseModel, ConfigDict
from typing import Type, TypeVar, Any, Callable, Union
from pathlib import Path
import os
from pydantic.alias_generators import to_camel, to_snake
import re

T = TypeVar("T", bound="CamelBase")

class CamelBase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )
    
    @staticmethod
    def _convert_keys(data: Any, converter: Callable[[str], str]) -> Any:
        if isinstance(data, dict):
            return {converter(k): CamelBase._convert_keys(v, converter) for k, v in data.items()}
        if isinstance(data, list):
            return [CamelBase._convert_keys(i, converter) for i in data]
        return data
    
    def to_json_file(self, path: Union[str, Path]):
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        data_snake = self.model_dump(mode='json')
        data_camel = self._convert_keys(data_snake, to_camel)
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.model_dump_json(by_alias=True, indent=4))
            
    @staticmethod
    def uuid_safe_to_snake(key: str) -> str:
        uuid_pattern = r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
        numberCharKey_pattern = r'[a-zA-Z]\d'
        if re.match(uuid_pattern, key):
            return key
        if re.match(numberCharKey_pattern, key):
            return key
        return to_snake(key)
    
    @classmethod    
    def from_json_file(cls: Type[T], path: Union[str, Path]) -> T:
        if not os.path.exists(path):
            raise FileNotFoundError(f"JSON file not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            data_camel = json.load(f)
        
        data_snake = cls._convert_keys(data_camel, cls.uuid_safe_to_snake)    
        return cls.model_validate(data_snake)