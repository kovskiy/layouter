def logger_window(sender, **kwargs):
    w = kwargs["window_class"]
    print("current window: ", w)
def logger_layout(sender, **kwargs):
    l = kwargs["layout_name"]
    k = kwargs["keyboard_name"]
    print(f"current layout: {k} + {l}")