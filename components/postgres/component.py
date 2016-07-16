import batou
import batou.component
import batou.utils
import batou_ext.postgres

class PostgreSQL(batou.component.Component):

    username = None
    password = None
    database = batou.component.Attribute(str, 'partuniverse')
    command_prefix = batou.component.Attribute(str, 'sudo -u postgres')

    def configure(self):
        self.address = batou.utils.Address(self.host.fqdn, 5432)
        self.provide('postgresql', self)

        self += batou_ext.postgres.User(self.username, password=self.password)
        self += batou_ext.postgres.DB(self.database, owner=self.username)

