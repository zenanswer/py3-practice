#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from hgijson import JsonPropertyMapping, MappingJSONEncoderClassBuilder, MappingJSONDecoderClassBuilder

class JsonMetaClass(type):
    def __init__(cls, classname, superclasses, attributedict):
        JSONEncoder = MappingJSONEncoderClassBuilder(cls, cls.mapping_schema).build()

        def to_json(self):
            return json.dumps(self, cls=JSONEncoder)
        cls.to_json = to_json

        JSONDecoder = MappingJSONDecoderClassBuilder(cls, cls.mapping_schema).build()

        @classmethod
        def to_obj(cls, str):
            return json.loads(str, cls=JSONDecoder)
        cls.to_obj = to_obj


class Person(metaclass=JsonMetaClass):
    mapping_schema = [
        # to json str
        JsonPropertyMapping("full_name", "name"),
        JsonPropertyMapping("first_name", object_property_getter=lambda person: person.get_first_name()),
        JsonPropertyMapping("family_name", object_property_getter=lambda person: person.get_family_name()),

        # to object
        JsonPropertyMapping("full_name", object_property_setter=lambda person, name: person.set_name(name))
    ]

    def __init__(self):
        self.age = 99
        self.name = "Bob Smith"

    def set_name(self, name: str):
        self._name = name

    def get_first_name(self) -> str:
        return self.name.split(" ")[0]

    def get_family_name(self) -> str:
        return self.name.split(" ")[1]


str = '''
{"full_name": "Full Name", "first_name": "Bob", "family_name": "Smith"}
'''
person = Person.to_obj(str)
print(person)
print(person.to_json())
