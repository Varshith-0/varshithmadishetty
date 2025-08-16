class _Varshith:
    def __call__(self, *args, **kwargs):
        return "Fuck you"

# Expose a callable instance at the module level
import sys
sys.modules[__name__] = _Varshith()
