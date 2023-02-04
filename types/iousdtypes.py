# Copyright 2023 Fabrica Software, LLC

import iograft
from pxr import Usd, Sdf


class UsdStage(iograft.PythonType):
    """
    Type representing a Usd Stage (pxr.Usd.Stage).
    """
    type_id = iograft.TypeId("UsdStage")
    value_type = Usd.Stage

    def __init__(self):
        super(UsdStage, self).__init__(UsdStage.type_id,
                                       value_type=UsdStage.value_type)


class SdfLayer(iograft.PythonType):
    """
    Type representing an USD SdfLayer (pxr.Sdf.Layer).
    """
    type_id = iograft.TypeId("SdfLayer")
    value_type = Sdf.Layer

    def __init__(self):
        super(SdfLayer, self).__init__(SdfLayer.type_id,
                                       value_type=SdfLayer.value_type)


class SdfLayerList(iograft.PythonListType):
    """
    Type representing a list of USD SdfLayer objects.
    """
    def __init__(self):
        super(SdfLayerList, self).__init__(SdfLayer.type_id,
                                           base_value_type=SdfLayer.value_type)


class UsdPrim(iograft.PythonType):
    """
    Type representing a USD Prim (pxr.Usd.Prim).
    """
    type_id = iograft.TypeId("UsdPrim")
    value_type = Usd.Prim

    def __init__(self):
        super(UsdPrim, self).__init__(UsdPrim.type_id,
                                      value_type=UsdPrim.value_type)


class UsdPrimList(iograft.PythonListType):
    """
    Type representing a list of Usd Prim objects.
    """
    def __init__(self):
        super(UsdPrimList, self).__init__(UsdPrim.type_id,
                                          base_value_type=UsdPrim.value_type)


def LoadPlugin(plugin):
    # Register the Usd.Stage type with iograft.
    stage_type = plugin.RegisterPythonType(UsdStage.type_id,
                                           UsdStage(),
                                           iograft.ValueToString,
                                           menu_path="USD")

    # Register the Sdf.Layer type with iograft.
    layer_type = plugin.RegisterPythonType(SdfLayer.type_id,
                                           SdfLayer(),
                                           iograft.ValueToString,
                                           menu_path="USD")
    # Also register a list type for Sdf.Layer objects.
    plugin.RegisterPythonListType(layer_type,
                                  SdfLayerList(),
                                  iograft.ValueToString,
                                  menu_path="USD")

    # Register the Usd.Prim type with iograft.
    prim_type = plugin.RegisterPythonType(UsdPrim.type_id,
                                          UsdPrim(),
                                          iograft.ValueToString,
                                          menu_path="USD")
    # Also register a list type for the Sdf.Layer objects.
    plugin.RegisterPythonListType(prim_type,
                                  UsdPrimList(),
                                  iograft.ValueToString,
                                  menu_path="USD")
