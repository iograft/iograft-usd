# Copyright 2023 Fabrica Software, LLC

import iograft
import iobasictypes
import subprocess


class LaunchUSDView(iograft.Node):
    """
    Open USDView with the given usd file loaded.

    Optionally, wait for the user to close usdview before marking this
    node as complete.
    """
    usd_file = iograft.InputDefinition("usd_file", iobasictypes.Path())
    wait_for_exit = iograft.InputDefinition("wait_for_exit",
                                            iobasictypes.Bool(),
                                            default_value=False)

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("launch_usdview")
        node.SetNamespace("usd")
        node.SetMenuPath("USD")
        node.AddInput(cls.usd_file)
        node.AddInput(cls.wait_for_exit)
        return node

    @staticmethod
    def Create():
        return LaunchUSDView()

    def Process(self, data):
        # Get the input usd file.
        usd_file = iograft.GetInput(self.usd_file, data)
        wait_for_exit = iograft.GetInput(self.wait_for_exit, data)

        # Build the subprocess command.
        subprocess_cmd = "usdview"
        subprocess_cmd += " " + usd_file
        proc = subprocess.Popen(subprocess_cmd, shell=True)

        # If we are waiting for the subprocess to complete before marking
        # the node as done, wait here.
        if wait_for_exit:
            proc.wait()

            # Check the return code.
            return_code = proc.returncode
            if return_code != 0:
                raise RuntimeError("usdview exited with non-zero exit code:"
                                   " {}".format(return_code))


def LoadPlugin(plugin):
    node = LaunchUSDView.GetDefinition()
    plugin.RegisterNode(node, LaunchUSDView.Create)
