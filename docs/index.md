# Introduction

FletTts for Flet.

## Examples

```
import flet as ft

from flet_tts import FletTts


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.Alignment.CENTER, bgcolor=ft.Colors.PURPLE_200, content=FletTts(
                    tooltip="My new FletTts Control tooltip",
                    value = "My new FletTts Flet Control",
                ),),

    )


ft.run(main)
```

## Classes

[FletTts](FletTts.md)
