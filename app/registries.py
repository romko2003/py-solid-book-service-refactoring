from __future__ import annotations
from typing import Dict
from interfaces import DisplayStrategy, PrintStrategy, Serializer
from display_strategies import ConsoleDisplay, ReverseDisplay
from print_strategies import ConsolePrinter, ReversePrinter
from serializers import JsonSerializer, XmlSerializer


# Простий DI-реєстр (відповідає Open/Closed: додаємо нові типи без змін клієнтів)
DISPLAY_REGISTRY: Dict[str, DisplayStrategy] = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_REGISTRY: Dict[str, PrintStrategy] = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}

SERIALIZER_REGISTRY: Dict[str, Serializer] = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}
