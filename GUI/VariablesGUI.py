from dataclasses import dataclass
from tkinter import *


@dataclass
class DropdownVariable:
    typeName: StringVar
    argumentValue: DoubleVar


@dataclass
class CheckboxVariable:
    boolean: BooleanVar
    argumentValue: DoubleVar
