# Copyright 2023 Fabrica Software, LLC

import iograft
import iousdtypes


class GetStageEditTarget(iograft.Node):
    """
    Return the SdfLayer that is the current edit target of the given USD
    stage.
    """
    stage = iograft.InputDefinition("stage", iousdtypes.UsdStage())
    target_layer = iograft.OutputDefinition("target_layer",
                                            iousdtypes.SdfLayer())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("get_stage_edit_target")
        node.SetNamespace("usd")
        node.SetMenuPath("USD")
        node.AddInput(cls.stage)
        node.AddOutput(cls.target_layer)
        return node

    @staticmethod
    def Create():
        return GetStageEditTarget()

    def Process(self, data):
        stage = iograft.GetInput(self.stage, data)

        # Get the current edit target.
        edit_target = stage.GetEditTarget()
        target_layer = edit_target.GetLayer()
        iograft.SetOutput(self.target_layer, data, target_layer)


def LoadPlugin(plugin):
    node = GetStageEditTarget.GetDefinition()
    plugin.RegisterNode(node, GetStageEditTarget.Create)
