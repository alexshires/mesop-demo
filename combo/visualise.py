#  Copyright 2024 Google. This software is provided as-is, without warranty
#   or representation for any use or purpose. Your use of it is subject to your
#    agreement with Google.

import mesop as me

from utils import header_text, footer, header_buttons, State

def click_send_visual():
  pass


def select_visualise_func():
  pass

def output_visualise_func():
  pass


def visualisation_func():
  """
  TODO implement your own example here
  :return:
  """
  pass



@me.page(path="/predict",
        security_policy=me.SecurityPolicy(
            dangerously_disable_trusted_types=True
        )
        )
def visualise_page():
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
      header_text("Predict a shape")
      header_buttons()
      # visualise shape - numpy plot
      select_visualise_func()
      # get prediction
      me.button("Get Prediction", on_click=click_send_visual)
      output_visualise_func()


  footer()
