import subprocess
from gi.repository import GLib

from qubes_tutorial.extensions import (
    GtkTutorialExtension,
    if_tutorial_enabled,
    widget_highlight,
    widget_highlight_wrong,
    widget_highlight_remove
)

class QubesQrexecPolicyGUITutorialExtension(GtkTutorialExtension):

    def __init__(self):
        super().__init__("qrexec_policy_gui")
        self.confirm_rpc_window = None
        self.target_vm_name = None

    def set_rpc_confirmation_window(self, confirm_rpc_window):
        self.confirm_rpc_window = confirm_rpc_window

    @if_tutorial_enabled
    def highlight_entry_on_correct_name(self, entry_box_widget, vm_name):
        # clear previous highlights
        widget_highlight_remove(entry_box_widget)
        widget_highlight_remove(self.confirm_rpc_window._rpc_ok_button)

        if vm_name == None:
            widget_highlight(entry_box_widget)
        elif vm_name == self.target_vm_name:
            widget_highlight(self.confirm_rpc_window._rpc_ok_button)
        else:
            widget_highlight_wrong(entry_box_widget)

    def do_show_tutorial_path_to_vm(self, vm_name):
        """
        Highlights the path to a vm, showing the user a path
        to click it.
        """
        self.target_vm_name = vm_name
        if self.confirm_rpc_window:
            GLib.idle_add(self.confirm_rpc_window._show_tutorial_path_to_vm, vm_name)
            return "highlighted successfully {}".format(vm_name)
        else:
            return "nothing to highlight"