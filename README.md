# Cargo-impl
Innovation project. Use Cargo system to dynamically arrange the bus time schedule, and measure how well it is.

Be aware:
Done lists and todo lists should be put in the root folder Document/
If you face any questions, raise an issue
Let's play with Cargo!

File structure:
- Bus-digital-twin: our project file, with some useful tools and API. The usage of tools can be found in README.md in Tools/ folder.
	But currently, it seems that position of bus is down.
- Cargo: simple Cargo platform, DO NOT commit to this folder directly with compiled Cargo, but commit modified source code, In order to reduce size.
	I would do some change to this system using C++, but now there is nothing different with original Cargo.
- Document: put all the documents here, and try to avoid commit non-binary files.
- Ridesharing-Social-Network: our secondary experiment! Let's play with social network!

## Usage

​	I've already put all the compiled files into repo, and you only need to open `example/launcher` to run the simulation.

​	But if you want to re-compile everything, you need to install several things:

```bash
sudo apt install libmetis-dev
sudo apt install libglpk-dev
```

​	To generate organizations from instances, run the `create_organization.py` tool. The result is the social network file.