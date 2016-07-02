import batou
import batou.component
import batou.lib.git


class GitCheckout(batou.component.Component):
    git_clone_url = batou.component.Attribute(
        str, 'https://github.com/frlan/partuniverse.git')
    git_revision = 'd2808fc95277cd4884963ec91332cee2fda64114'
    git_target = 'home/vagrant/clone'

    id_rsa = None
    id_rsa_pub = None

    def configure(self):
        self.provide('gitcheckout', self)

        self += batou.lib.git.Clone(
            self.git_clone_url,
            revision=self.git_revision,
            target=self.git_target)

