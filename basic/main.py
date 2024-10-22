#  Copyright 2024 Google. This software is provided as-is, without warranty
#   or representation for any use or purpose. Your use of it is subject to your
#    agreement with Google.


import mesop as me


@me.stateclass
class State:
    input: str
    output: str
    count: int = 0


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


def on_click_nav0(e: me.ClickEvent):
    state = me.state(State)
    state.count += 1
    me.navigate("/demo")


def header_buttons():
    me.button("Home", on_click=on_click_nav0)


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
