# iograft Nodes & Types for USD

This repository contains nodes and types for interacting with Universal Scene Description (USD) [https://graphics.pixar.com/usd/release/index.html](https://graphics.pixar.com/usd/release/index.html).

The nodes/types depend on USD being installed/available (i.e. provided by an application such as Maya, manually built, or installed via a package such as NVIDIA's [prebuilt libraries](https://developer.nvidia.com/usd)).

## Adding USD nodes/types to an environment

These nodes and types do not necessarily require a dedicated environment as long as the USD libraries and executables are available in the environment you are adding them to. For example, Maya 2022 ships with a full USD package and these nodes will work seamlessly in that environment.

To use these nodes with an existing environment that already contains the USD libraries, you will need to add the following settings to an existing environment:
- Add the `nodes` and `types` directories of this repository to the environment's **Plugin Path**.
- Add the `types` directory of this repository to the environment's **Python Path**.

In addition to the steps above, if creating a dedicated USD environment the following items must also be added to the new environment:
- Add the `bin` and `lib` directories of the USD installation to the environment's **Path**. These are the directories containing the USD executables and DLLs/Libs.
- Add a directory containing a compatible Python executable to the environment's **Path** (i.e. C:/Program Files/Python37).
- Add the `lib/python` directory of the USD installation to the environment's **Python Path**.
- Update the **Subcore Command** to `iograftpy_subcore`.
