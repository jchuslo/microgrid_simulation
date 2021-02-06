# microgrid_simulation


### Architecture
- Java
- Use graph to represent service modules
- Two choices of nodes: Wind or Solar
	- Each are unique nodes
	- Edges have no attributes **but they are responsible for control interrupts**
- Each node has a capacity, a burn time, and a battery.
	- The battery has a storage capacity with unlimited storage time (for simplicity)
- Each node type (wind/solar) has a rate of power input
- Price per watt of electricity will be normalized to usage/unit of energy
	- This will be relaxed later

- First, this will be a static program
	- Then, user will be able to view the grid in a GUI and be able to turn on/off any node (you'll have to turn off the entire node, generator and battery alike)