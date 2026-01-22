from __future__ import annotations
import json
import xml.etree.ElementTree as ET
from interfaces import Serializer, BookDTO


class JsonSerializer(Serializer):
    def serialize(self, book: BookDTO) -> str:
        # еквівалентно старому serialize("json")
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: BookDTO) -> str:
        # еквівалентно старому serialize("xml")
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
