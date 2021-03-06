{ config, lib, pkgs, ... }: with config;

{

  flyingcircus.load_enc = false;
  flyingcircus.agent.enable = false;
  flyingcircus.agent.steps = "--channel";

  flyingcircus.roles.nginx.enable = true;
  flyingcircus.roles.postgresql96.enable = true;
  networking.firewall.enable = false;

  # We want that postgres is listen everywhere in vagrant. Default on
  # FCIO nix is ethsrv -- internal network only.
  environment.etc."local/postgresql/9.4/listen.conf".text = ''
    listen_addresses = '*'
  '';

  users.users.vagrant.extraGroups = ["service"];

}
