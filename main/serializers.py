class LightSerializer():
    def __init__(self, *args, **kwargs):
        kwargs.pop("read_only", None)
        kwargs.pop("partial", None)
        kwargs.pop("files", None)
        context = kwargs.pop("context", {})
        view = kwargs.pop("view", {})
        super().__init__(*args, **kwargs)
        self.context = context
        self.view = view