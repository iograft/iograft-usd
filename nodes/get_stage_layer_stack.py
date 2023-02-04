# Copyright 2023 Fabrica Software, LLC

import iograft
import iobasictypes
import iousdtypes


class GetStageLayerStack(iograft.Node):
    """
    Retrieve the layer stack and output a list of SdfLayers for the given
    USD stage.

    If `include_session_layers` is True, the stage's session layer will
    also be included.
    """
    stage = iograft.InputDefinition("stage", iousdtypes.UsdStage())
    include_session_layers = iograft.InputDefinition("include_session_layers",
                                                     iobasictypes.Bool(),
                                                     default_value=True)

    layer_stack = iograft.OutputDefinition("layer_stack",
                                           iousdtypes.SdfLayerList())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("get_stage_layer_stack")
        node.SetNamespace("usd")
        node.SetMenuPath("USD")
        node.AddInput(cls.stage)
        node.AddInput(cls.include_session_layers)
        node.AddOutput(cls.layer_stack)
        return node

    @staticmethod
    def Create():
        return GetStageLayerStack()

    def Process(self, data):
        stage = iograft.GetInput(self.stage, data)
        include_session_layers = iograft.GetInput(self.include_session_layers,
                                                  data)

        # Get the layer stack.
        layer_stack = stage.GetLayerStack(
                                includeSessionLayers=include_session_layers)
        iograft.SetOutput(self.layer_stack, data, layer_stack)


def LoadPlugin(plugin):
    node = GetStageLayerStack.GetDefinition()
    plugin.RegisterNode(node, GetStageLayerStack.Create)
