"""
molssi_devops
A package containing useful math functions
"""

# Add imports here
from .molssi_math import mean, canvas
from .util import title_case

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
