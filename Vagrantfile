# -*- mode: ruby -*-
# vi: set ft=ruby :

required_plugins = %w( vagrant-nixos-plugin )
required_plugins.each do |plugin|
      system "vagrant plugin install #{plugin}" unless Vagrant.has_plugin? plugin
end

Vagrant.configure("2") do |config|
  config.vm.box = "flyingcircus/nixos-15.09-x86_64"
  config.vm.box_version = ">= 164"
  # Should be big enough for pu
  config.vm.provider "virtualbox" do |v|
      v.memory = 2048
      v.cpus = 1
  end

  config.vm.hostname = 'default'
  config.vm.network "private_network", ip: "192.168.55.5"

  config.vm.provision :shell, \
    :inline => "
    mkdir -p /var/partuniverse
    nix-channel --add https://hydra.flyingcircus.io/channels/branches/fc-15.09-production// nixos
    nix-channel --update", \
    :run => "always"
  config.vm.provision :nixos, :verbose => true,\
    :path => "provision.nix", \
    :run => "always"

end
