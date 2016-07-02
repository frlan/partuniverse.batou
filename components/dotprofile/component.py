import batou.component
import batou.lib.file
import os


class DotProfile(batou.component.Component):
    def configure(self):
        self += batou.lib.file.File(
            os.path.expanduser('~/.profile'),
            content=(
                'export LD_LIBRARY_PATH=$HOME/.nix-profile/lib:$LD_LIBRARY_PATH \n'
                'export C_INCLUDE_PATH=$HOME/.nix-profile/include:$C_INCLUDE_PATH'
            )
        )
