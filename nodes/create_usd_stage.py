# Copyright 2023 Fabrica Software, LLC

import iograft
import iobasictypes
import iousdtypes

from pxr import Usd


class CreateUsdStage(iograft.Node):
    """
    Create a new Usd Stage. This node wraps the Usd.Stage.CreateNew and
    Usd.Stage.CreateInMemory functions. This node does not support a
    custom asset resolver.

    If the "filename" input is an empty string, the stage will be created
    in memory.

    Outputs the generated Usd Stage object.
    """
    filename = iograft.InputDefinition("filename",
                                       iobasictypes.Path(),
                                       default_value="")
    stage = iograft.OutputDefinition("stage", iousdtypes.UsdStage())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("create_usd_stage")
        node.SetNamespace("usd")
        node.SetMenuPath("USD")
        node.AddInput(cls.filename)
        node.AddOutput(cls.stage)
        return node

    @staticmethod
    def Create():
        return CreateUsdStage()

    def Process(self, data):
        filename = iograft.GetInput(self.filename, data)

        # If the filename arg is provided, create the new stage with that
        # path; otherwise create the new stage in memory.
        if filename:
            stage = Usd.Stage.CreateNew(filename)
        else:
            stage = Usd.Stage.CreateInMemory()

        # Pass the stage through to the output.
        iograft.SetOutput(self.stage, data, stage)


def LoadPlugin(plugin):
    node = CreateUsdStage.GetDefinition()
    plugin.RegisterNode(node, CreateUsdStage.Create)
