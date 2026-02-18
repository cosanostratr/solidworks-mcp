"""
Run with: python -m solidworks_mcp
"""

import asyncio
import sys
from solidworks_mcp import main

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
