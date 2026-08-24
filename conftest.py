"""Pytest configuration for ForestAI.

This ensures the project root is in sys.path so that 'src' package
can be imported when running pytest from the project root.
"""

import sys
from pathlib import Path

# Add project root to sys.path so 'src' package is importable
project_root = Path(__file__).parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))