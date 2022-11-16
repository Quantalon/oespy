from pathlib import Path
from ctypes import Structure, Union


LIB_PATH = str(Path(__file__).resolve().parent.parent.joinpath('liboes_api.so'))


class BaseStructure(Structure):
    def __str__(self):
        fields_str = ', '.join([f'{name}={str(getattr(self, name))}' for name, _ in self._fields_])
        return f'<{self.__class__.__name__} ({fields_str})>'

    def to_dict(self):
        d = {}
        for name, _ in self._fields_:
            val = getattr(self, name)
            if isinstance(val, bytes):
                val = val.decode('utf-8')
            d[name] = val
        return d


class BaseUnion(Union):
    def __str__(self):
        fields_str = ', '.join([f'{name}={str(getattr(self, name))}' for name, _ in self._fields_])
        return f'<{self.__class__.__name__} ({fields_str})>'

    def to_dict(self):
        d = {}
        for name, _ in self._fields_:
            val = getattr(self, name)
            if isinstance(val, bytes):
                val = val.decode('utf-8')
            d[name] = val
        return d





