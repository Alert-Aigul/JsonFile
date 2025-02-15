__title__ = 'JsonFile'
__author__ = 'Alert Aigul'
__license__ = 'MIT'
__copyright__ = 'Copyright 2025-2026 Alert'
__version__ = '1.0.0'

import asyncio
import json
import os

import aiofiles


class JsonFile(dict):
    def __init__(self, path: str, encoding = "utf8"):
        self.path = path
        self.encoding = encoding
        self.lock = asyncio.Lock()
        super().__init__()
        
    async def __aenter__(self) -> "JsonFile":
        await self.load()
        return self

    async def __aexit__(self, *args) -> None:
        await self.dump()
    
    def __enter__(self) -> "JsonFile":
        self.load_sync()
        return self

    def __exit__(self, *args) -> None:
        self.dump_sync()
        
    async def load(self) -> "JsonFile":
        if not os.path.exists(self.path):
            self.update({})
            return self
        
        async with aiofiles.open(self.path, "r", encoding=self.encoding) as fp:
            self.update(json.loads(await fp.read()))
            
        return self
    
    async def dump(self, ensure_ascii = False, indent = 4) -> "JsonFile":
        async with aiofiles.open(self.path, "w", encoding=self.encoding) as fp:
            await fp.write(json.dumps(self.copy(), ensure_ascii=ensure_ascii, indent=indent))
        
        return self

    def load_sync(self) -> "JsonFile":
        if not os.path.exists(self.path):
            self.update({})
            return self
        
        with open(self.path, "r", encoding = self.encoding) as fp:
            self.update(json.load(fp))
        return self
    
    def dump_sync(self, ensure_ascii=False, indent=4) -> "JsonFile":
        with open(self.path, "w", encoding=self.encoding) as fp:
            json.dump(self.copy(), fp, ensure_ascii=ensure_ascii, indent=indent)
        
        return self
    
    def __getitem__(self, __key):
        return super().__getitem__(str(__key))
    
    def __setitem__(self, __key, __value):
        super().__setitem__(str(__key), __value)
    
    def __contains__(self, __key):
        return super().__contains__(str(__key))
