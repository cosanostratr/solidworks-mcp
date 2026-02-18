"""
SolidWorks MCP Server
Professional SolidWorks CAD tools for local AI assistants (LM Studio, etc.)
"""

from typing import Any
import json
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from pydantic import AnyUrl
import mcp.server.stdio

# SolidWorks tools and their descriptions
SOLIDWORKS_TOOLS = {
    # Part Design - Sketching
    "sketch_line": "Create lines in sketch (Line, Centerline)",
    "sketch_arc": "Create arcs (Tangent Arc, 3-Point Arc)",
    "sketch_spline": "Create spline curves",
    "sketch_circle": "Create circles and ellipses",
    "sketch_rectangle": "Create rectangles (Corner Rectangle, Center Rectangle)",
    "sketch_polygon": "Create polygons (3-12 sides)",
    "sketch_point": "Create points",
    "sketch_dimension": "Add dimensions to sketch",
    "sketch_relation": "Add geometric relations (Coincident, Parallel, etc.)",
    "sketch_trim": "Trim sketch entities",
    "sketch_offset": "Offset entities",
    "sketch_mirror": "Mirror entities",
    "sketch_convert": "Convert entities from edges",
    
    # Part Design - 3D Features
    "extrude": "Extruded Boss/Base - Single/Double direction, Thin feature",
    "revolve": "Revolved Boss/Base - Axis selection, Thin feature",
    "sweep": "Swept Boss/Base - Profile, Path, Guide curves",
    "loft": "Lofted Boss/Base - Profiles, Guide curves",
    "hole_wizard": "Hole Wizard - Counterbore, Countersink, Straight",
    "shell": "Shell - Multiple face selection, thickness",
    "rib": "Rib - Drafted, Straight",
    "dome": "Dome - Elliptical, Spherical",
    "wrap": "Wrap - Emboss, Deboss, Swept",
    "freeform": "Freeform Feature - Control points",
    
    # Part Design - Editing
    "fillet": "Fillet - Constant radius, Variable radius, Face fillet",
    "chamfer": "Chamfer - Distance-Distance, Distance-Angle",
    "draft": "Draft - Neutral plane, Pull direction",
    "mirror_feature": "Mirror - Feature, Body, Face",
    "scale": "Scale - Uniform, Non-uniform",
    "move_face": "Move Face - Translate, Rotate",
    
    # Assembly Design
    "insert_component": "Insert Component - Part, Assembly",
    "move_component": "Move Component - Standard, Cone, Distance",
    "rotate_component": "Rotate Component - Free rotate",
    "mate": "Add Mate - Standard, Advanced, Mechanical",
    "smart_mate": "Smart Mate - Auto-detect",
    "smart_fastener": "Smart Fasteners - Auto-insert bolts",
    "interference_check": "Interference Detection",
    "component_pattern": "Component Pattern - Linear, Circular",
    
    # Drawing
    "create_drawing": "Create new drawing",
    "add_standard_view": "Add Standard View - Front, Top, Right, etc.",
    "add_projected_view": "Add Projected View - Third/First angle",
    "add_section_view": "Add Section View - Full, Half, Offset",
    "add_detail_view": "Add Detail View - Circular, Rectangular",
    "add_break_view": "Add Break View - Horizontal, Vertical",
    "add_exploded_view": "Add Exploded View",
    "add_dimension": "Add Dimension - Auto, Reference, Baseline",
    "add_geometric_tolerance": "Add Geometric Tolerance",
    "add_surface_finish": "Add Surface Finish Symbol",
    "add_weld_symbol": "Add Weld Symbol",
    "add_note": "Add Note",
    "add_datum": "Add Datum Target",
    
    # Simulation
    "create_study": "Create Study - Static, Thermal, Frequency",
    "assign_material": "Assign Material",
    "add_fixture": "Add Fixture - Fixed, Roller, Bearing",
    "add_load": "Add Load - Force, Pressure, Torque, Gravity",
    "mesh_control": "Mesh Control - Local mesh, Parameters",
    "run_analysis": "Run Analysis",
    "view_results": "View Results - Stress, Strain, Displacement",
    "factor_safety": "Factor of Safety",
    
    # Sheet Metal
    "base_flange": "Base Flange - Sheet metal setup, K-factor",
    "edge_flange": "Edge Flange - Position, Length",
    "miter_flange": "Miter Flange - Profile, Overlap",
    "hem": "Hem - Closed, Open, Tear drop",
    "fold": "Fold - Bend, Flat pattern",
    "unfold": "Unfold",
    "punch": "Punch - Tab, Louver",
    "corner_seam": "Corner Seam - Gap, Overlap",
    "flat_pattern": "Flat Pattern - Bend table",
    
    # Weldments
    "structural_member": "Structural Member - Profiles",
    "gusset": "Gusset - Triangle, Non-standard",
    "end_cap": "End Cap - Flush, Offset",
    "weld_bead": "Weld Bead - Fillet, Groove",
    "cut_list": "Cut List - Properties",
    
    # Surfacing
    "boundary_surface": "Boundary Surface - Directional options",
    "fill_surface": "Fill Surface - Constraints",
    "swept_surface": "Swept Surface",
    "lofted_surface": "Lofted Surface",
    "planar_surface": "Planar Surface",
    "knit_surface": "Knit Surface - Combine",
    "thicken": "Thicken - Single/Double side",
    "offset_surface": "Offset Surface - Variable",
    
    # Mold Tools
    "parting_line": "Parting Line - Auto, Manual",
    "parting_surface": "Parting Surface",
    "core_cavity": "Core/Cavity - Extraction direction",
    "shut_off": "Shut-off Tangents",
    
    # Routing
    "auto_route": "Auto-Route - Pipes, Tubes",
    "manual_route": "Manual Route",
    "add_fitting": "Add Fitting - Elbow, Reducer",
    
    # Motion Analysis
    "add_motor": "Add Motor - Rotary, Linear",
    "add_spring": "Add Spring - Compression, Extension",
    "add_contact": "Add Contact - Physical, Frictionless",
    "motion_results": "Motion Results - Velocity, Acceleration",
    
    # Data Management
    "check_in": "Check In - Version control",
    "check_out": "Check Out",
    "revision": "Revision - Numbering",
    "search": "Search - Properties",
    
    # General
    "new_part": "New Part",
    "new_assembly": "New Assembly",
    "new_drawing": "New Drawing",
    "save": "Save",
    "save_as": "Save As",
    "export": "Export - STEP, IGES, STL, PDF",
    "mass_properties": "Mass Properties",
    "measure": "Measure",
    "section_mask": "Section View",
    "rename_feature": "Rename Feature",
    "suppress": "Suppress Feature",
    "delete": "Delete",
    "rebuild": "Rebuild",
}

# Tool definitions for MCP
def get_tools() -> list[Tool]:
    """Return list of all SolidWorks tools."""
    tools = []
    for tool_id, description in SOLIDWORKS_TOOLS.items():
        tools.append(
            Tool(
                name=tool_id,
                description=description,
                inputSchema={
                    "type": "object",
                    "properties": {},
                }
            )
        )
    return tools


# Server class
class SolidWorksMCPServer:
    def __init__(self):
        self.server = Server("solidworks-mcp")
        self._setup_handlers()
    
    def _setup_handlers(self):
        @self.server.list_tools()
        async def list_tools() -> list[Tool]:
            return get_tools()
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: dict) -> list[TextContent]:
            return await self._execute_tool(name, arguments)
    
    async def _execute_tool(self, name: str, arguments: dict) -> list[TextContent]:
        """Execute a SolidWorks tool."""
        tool_info = SOLIDWORKS_TOOLS.get(name, "Unknown tool")
        
        result = {
            "status": "success",
            "tool": name,
            "message": f"Tool: {name}\nDescription: {tool_info}",
            "note": "This is an MCP simulation. In production, this would interface with SolidWorks via API."
        }
        
        return [TextContent(type="text", text=json.dumps(result, indent=2))]
    
    async def run(self):
        """Run the MCP server."""
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options()
            )


async def main():
    """Main entry point."""
    server = SolidWorksMCPServer()
    await server.run()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
