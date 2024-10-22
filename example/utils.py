#  Copyright 2024 Google. This software is provided as-is, without warranty
#   or representation for any use or purpose. Your use of it is subject to your
#    agreement with Google.

import mesop as me

@me.stateclass
class State:
  input: str
  output: str
  in_progress: bool


def header_text(header: str = "Mesop Starter Kit"):
  with me.box(
      style=me.Style(
          padding=me.Padding(
              top=64,
              bottom=36,
          ),
      )
  ):
    me.text(
        header,
        style=me.Style(
            font_size=36,
            font_weight=700,
            background="linear-gradient(90deg, #4285F4, #AA5CDB, #DB4437) text",
            color="transparent",
        ),
    )

def footer():
  with me.box(
      style=me.Style(
          position="sticky",
          bottom=0,
          padding=me.Padding.symmetric(vertical=16, horizontal=16),
          width="100%",
          background="#F0F4F9",
          font_size=14,
      )
  ):
    me.html(
        "Made with <a href='https://google.github.io/mesop/'>Mesop</a>",
    )