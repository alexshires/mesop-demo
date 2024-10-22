#  Copyright 2024 Google. This software is provided as-is, without warranty
#   or representation for any use or purpose. Your use of it is subject to your
#    agreement with Google.

import mesop as me

from utils import header_text, header_buttons, footer

# imports
from predict import predict_page
from visualise import visualise_page

@me.page(path="/home",
         security_policy=me.SecurityPolicy(
             dangerously_disable_trusted_types=True
         ))
def main_page():
  """
  create the functionality for the main page
  :return:
  """
  with me.box(
      style=me.Style(
          background="#fff",
          min_height="calc(100% - 48px)",
          padding=me.Padding(bottom=16),
      )
  ):
    with me.box(
        style=me.Style(
            width="min(720px, 100%)",
            margin=me.Margin.symmetric(horizontal="auto"),
            padding=me.Padding.symmetric(
                horizontal=16,
            ),
        )
    ):
      header_text("Python Learning Demo")
      header_buttons()

  footer()