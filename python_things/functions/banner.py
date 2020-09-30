"""Create a banner across the screen."""


def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Create a banner-style text with centered text.

    :Args
        text (str): Defaults to a space and prints to the screen
            as two asterisks (**) on each side of the banner.  If
            text is supplied the text will be centered in the banner
            block.
        screen_width (int): Defaults to 80.  Determines the width of
            the banner.

    :Raises
        ValueError: Value Error is raised if provdied text is longer
            than scrreen_width parameter.
    """
    if len(text) > screen_width - 4:
        raise ValueError(f"String '{text}' is larger than specified "
                         f"width {screen_width}.")

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{}**".format(centered_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text()
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")
