import batou.component
import batou.lib.git
import batou.lib.file
import batou.lib.buildout
import batou.lib.python
import batou.utils
import batou_ext.nix
import os

class Django (batou.component.Component):

    # the user the django process should run on.
    user = batou.component.Attribute(str, 'partuniverse')
    group = batou.component.Attribute(str, 'partuniverse')
    address = batou.utils.Address('127.0.0.1', 9001)

    def configure(self):
        self.database = self.require_one('postgresql')
        self.checkout = self.require_one('gitcheckout')
        #self.provide('django', self)

        self.prepared_path = 'prepared-{}'.format(self.checkout.git_revision)

        self += batou.c.dotprofile.DotProfile()

        self += batou.lib.file.SyncDirectory(
            self.prepared_path,
            source=self.checkout.git_target)

        self += batou.lib.file.File(
            os.path.join(
                self.prepared_path,
                'partuniverse/partuniverse/local_settings.py'),
            source='resources/local_settings.py')

        venv = batou.lib.python.VirtualEnv('3.4')
        self += venv
        venv += batou.lib.python.Package(
            'psycopg2',
            version='2.6.2')


        self += DjangoBuild()

        #Ensure, we have a symlink to current code
        self += batou.lib.file.File(
            'current',
            ensure='symlink',
            link_to=self.prepared_path
        )

        # Systemd
        self += batou.lib.file.File(
            '/etc/local/systemd/partuniverse.socket',
            source='resources/partuniverse.socket')
        self += batou.lib.file.File(
            '/etc/local/systemd/partuniverse.service',
            source='resources/partuniverse.service')
        self += batou_ext.nix.Rebuild()


class DjangoBuild(batou.component.Component):

    def verify(self):
        # We need   to rerun the compiling once the checkout has changed.
        self.parent.assert_no_changes()

    def update(self):
        # Here we need to compile node in case of a change above
        # First install node packages.
        self.cmd('bin/pip install --upgrade -r {}'.format(
            os.path.join(self.parent.prepared_path, 'requirements.txt')))
        self.cmd('bin/python {} migrate'.format(
            os.path.join(
                self.parent.prepared_path,
                'partuniverse',
                'manage.py')))
        self.cmd('bin/python {} collectstatic --noinput'.format(
            os.path.join(
                self.parent.prepared_path,
                'partuniverse',
                'manage.py')))
