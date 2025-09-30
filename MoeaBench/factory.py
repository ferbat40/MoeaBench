from .MoeaBench import MoeaBench

class _MoeaBenchWrapper:
    def __getattr__(self, name):
        inst = MoeaBench()
        return getattr(inst, name)

    def __call__(self, *args, **kwargs):
        return MoeaBench(*args, **kwargs)

moeabench = _MoeaBenchWrapper()