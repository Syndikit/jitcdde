from . import _helpers
from ._jitcdde import jitcdde, provide_advanced_symbols, UnsuccessfulIntegration, _find_max_delay

try:
    from . import version
except ImportError:
    from warnings import warn
    warn('Failed to find (autogenerated) version.py. Do not worry about this unless you really need to know the version.')