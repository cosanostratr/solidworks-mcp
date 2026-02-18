"""
SolidWorks MCP Server - Main Entry Point
Run with: uvx solidworks-mcp
"""

import asyncio
from solidworks_mcp import main

if __name__ == "__main__":
    asyncio.run(main())
