# SolidWorks MCP Server

Professional SolidWorks MCP (Model Context Protocol) server for local AI assistants. Works with LM Studio, Ollama, and other MCP-compatible applications.

## Features

### Part Design
- **Sketching**: Lines, Arcs, Splines, Circles, Rectangles, Relations, Dimensions
- **3D Features**: Extrude, Revolve, Sweep, Loft, Hole Wizard, Shell, Rib, Dome, Wrap
- **Editing**: Fillet, Chamfer, Draft, Mirror, Scale, Move Face

### Assembly Design
- Component Insertion, Move, Rotate
- Mates (Standard, Advanced, Mechanical)
- Smart Fasteners, Interference Detection

### Drawing Creation
- Standard Views, Projected Views
- Section Views, Detail Views, Break Views
- Dimensions, Geometric Tolerances, Surface Finish
- Weld Symbols, Notes

### Simulation
- Static, Thermal, Frequency Analysis
- Fixtures, Loads, Mesh Control
- Results: Stress, Strain, Displacement

### Additional Tools
- Sheet Metal (Flanges, Bends, Flat Pattern)
- Weldments (Structural Members, Gussets)
- Surfacing, Mold Tools, Routing
- Motion Analysis

## Installation

### Prerequisites
- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager

### Quick Install (uvx)

```bash
# Run directly with uvx from local directory
cd solidworks-mcp
uvx --from . solidworks-mcp
```

### Install as Package

```bash
# Clone repository
git clone https://github.com/cosanostratr/solidworks-mcp.git
cd solidworks-mcp

# Install dependencies
uv sync

# Run
uv run solidworks-mcp

# Or install globally
uv pip install -e .
solidworks-mcp
```

## LM Studio Configuration

### Method 1: Direct Command
In LM Studio, add MCP server with:

```
Command: uvx
Arguments: solidworks-mcp
```

### Method 2: Custom Path
```bash
# Clone and install
git clone https://github.com/cosanostratr/solidworks-mcp.git
cd solidworks-mcp
uv sync

# In LM Studio, point to:
Command: /full/path/to/solidworks-mcp/.venv/bin/python
Arguments: -m solidworks_mcp
```

## Available Tools

| Category | Tools |
|----------|-------|
| Sketch | line, arc, spline, circle, rectangle, dimension, relation, trim, offset |
| 3D Features | extrude, revolve, sweep, loft, hole_wizard, shell, rib, dome, wrap |
| Editing | fillet, chamfer, draft, mirror_feature, scale, move_face |
| Assembly | insert_component, move_component, rotate_component, mate, smart_mate |
| Drawing | create_drawing, add_standard_view, add_section_view, add_dimension |
| Simulation | create_study, assign_material, add_fixture, add_load, run_analysis |
| Sheet Metal | base_flange, edge_flange, fold, unfold, punch, flat_pattern |
| Weldments | structural_member, gusset, end_cap, weld_bead |
| Surfacing | boundary_surface, fill_surface, knit_surface, thicken |
| Mold Tools | parting_line, core_cavity, shut_off |
| Routing | auto_route, manual_route, add_fitting |
| Motion | add_motor, add_spring, add_contact |

## Keyboard Shortcuts (SolidWorks)

| Shortcut | Function |
|----------|----------|
| Ctrl+N | New File |
| Ctrl+S | Save |
| Ctrl+Z | Undo |
| Ctrl+1 | Front View |
| Ctrl+2 | Top View |
| Ctrl+3 | Right View |
| Ctrl+4 | Isometric View |
| Space | View Orientation |
| Ctrl+Q | Quick Edit |
| Ctrl+R | Rebuild |

## Certification Paths

- **CSWA**: Certified SolidWorks Associate
- **CSWP**: Certified SolidWorks Professional
- **CSWE**: Certified SolidWorks Expert

## License

MIT License

## Notes

This MCP server provides tool definitions and documentation. For actual SolidWorks interaction, you need SolidWorks installed on your system. The server acts as an interface between AI assistants and SolidWorks.
