from enum import Enum
from typing import Any, Optional

import flet as ft

@ft.control("FletTts")
class FletTts(ft.LayoutControl):
    """
    FletTts Control description.
    """

    value: str
