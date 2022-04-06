import subprocess
from gi.repository import GLib

from qubes_tutorial.extensions import GtkTutorialExtension

class QubesQrexecPolicyGUITutorialExtension(GtkTutorialExtension):

    def __init__(self):
        super().__init__("qrexec_policy_gui")
        self.confirm_rpc_window = None

    def set_rpc_confirmation_window(self, confirm_rpc_window):
        self.confirm_rpc_window = confirm_rpc_window


    def do_show_tutorial_path_to_vm(self, vm_name):
        """
        Highlights the path to a vm, showing the user a path
        to click it.
        """
        if self.confirm_rpc_window:
            GLib.idle_add(self.confirm_rpc_window._show_tutorial_path_to_vm, vm_name)
            return "highlighted successfully {}".format(vm_name)
        else:
            return "nothing to highlight"
