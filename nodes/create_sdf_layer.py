# Copyright 2023 Fabrica Software, LLC

import iograft
import iobasictypes
import iousdtypes

from pxr import Sdf


class CreateSdfLayer(iograft.Node):
    """
    Create a new usd Sdf Layer. This node wraps the Sdf.Layer.CreateNew and
    Sdf.Layer.CreateAnonymous functions. This node does not support a
    custom asset resolver.

    If the "filename" input is an empty string, an anonymous layer will
    be created.

    Outputs the generated Sdf Layer object.
    """
    filename = iograft.InputDefinition("filename",
                                       iobasictypes.Path(),
                                       default_value="")
    layer = iograft.OutputDefinition("layer", iousdtypes.SdfLayer())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("create_sdf_layer")
        node.SetNamespace("usd")
        node.SetMenuPath("USD")
        node.AddInput(cls.filename)
        node.AddOutput(cls.layer)
        return node

    @staticmethod
    def Create():
        return CreateSdfLayer()

    def Process(self, data):
        filename = iograft.GetInput(self.filename, data)

        # If the filename arg is provided, create the new layer with that
        # path; otherwise create a new anonymous layer.
        if filename:
            layer = Sdf.Layer.CreateNew(filename)
            if layer is None:
                raise IOError("Could not find Sdf Layer with"
                              " identifier: {}".format(filename))
        else:
            layer = Sdf.Layer.CreateAnonymous()

        # Pass the layer through to the output.
        iograft.SetOutput(self.layer, data, layer)


def LoadPlugin(plugin):
    node = CreateSdfLayer.GetDefinition()
    plugin.RegisterNode(node, CreateSdfLayer.Create)
