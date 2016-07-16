import batou.component
import batou.lib.file
import batou_ext.nix


class Nginx(batou.component.Component):
    server_name = batou.component.Attribute(str, '')

    def configure(self):
        self.app = self.require_one('django', host=self.host)

        self += batou.lib.file.File(
            '/etc/local/nginx/partuniverse.conf',
            source='resources/nginx-host.conf')

        self += batou_ext.nix.Rebuild()
