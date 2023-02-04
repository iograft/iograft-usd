# Copyright 2023 Fabrica Software, LLC

import iograft
import iousdtypes


class GetRootLayer(iograft.Node):
    """
    Return the root layer of the Usd stage passed into the input.
    """
    stage = iograft.InputDefinition("stage", iousdtypes.UsdStage())
    root_layer = iograft.OutputDefinition("root_layer", iousdtypes.SdfLayer())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("get_stage_root_layer")
        node.SetNamespace("usd")
        node.SetMenuPath("USD")
        node.AddInput(cls.stage)
        node.AddOutput(cls.root_layer)
        return node

    @staticmethod
    def Create():
        return GetRootLayer()

    def Process(self, data):
        stage = iograft.GetInput(self.stage, data)

        # Return the root layer.
        root_layer = stage.GetRootLayer()
        iograft.SetOutput(self.root_layer, data, root_layer)


def LoadPlugin(plugin):
    node = GetRootLayer.GetDefinition()
    plugin.RegisterNode(node, GetRootLayer.Create)
