#  Copyright 2024 Google. This software is provided as-is, without warranty
#   or representation for any use or purpose. Your use of it is subject to your
#    agreement with Google.

import mesop as me
import json
# - Navigation buttons

from utils import header_text, footer, header_buttons, State





def call_api_predict(input):
  state = me.state(State)
  yield "\n\nPrediction process..."
  #time.sleep(1)
  hostname = "http://localhost:8001/api/quote/predict"
  #
  try:
    data = json.loads(state.selected_data)
    yield f"\n\nPrediction data... {data}"
    # print(data)
    res = {'result' : 0.0}
    yield f"\n\nPrediction result...{res}"
    print(res)
    res = res['result']
    # np.random.randint(0, 5000)
    #
  except Exception as e:
    print(e)
    res = -1
  yield f"\n\nCost per part: {res}"


def click_send_predict(e: me.ClickEvent):
  state = me.state(State)
  # if not state.input:
  #    return
  state.in_progress = True
  input = state.input
  state.input = ""
  yield

  for chunk in call_api_predict(input):
    state.output += chunk
    yield
  state.in_progress = False
  yield

def select_prediction_func():
  """
  TODO implement your own example here
  :return:
  """
  pass

def output_prediction_func():
  """
  TODO implement your own example here
  :return:
  """
  state = me.state(State)
  if state.output or state.in_progress:
    with me.box(
      style=me.Style(
          background="#F0F4F9",
          padding=me.Padding.all(16),
          border_radius=16,
          margin=me.Margin(top=36),
      )
    ):
      if state.output:
        me.markdown(state.output)
      if state.in_progress:
        with me.box(style=me.Style(margin=me.Margin(top=16))):
          me.progress_spinner()


me.page(path="/predict",
        security_policy=me.SecurityPolicy(
            dangerously_disable_trusted_types=True
        )
        )
def predict_page():
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
      select_prediction_func()
      # get prediction
      me.button("Get Prediction", on_click=click_send_predict)
      output_prediction_func()


  footer()






