sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setloggingmode on
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setloggingopt detail
multitail -s 2 -i /var/log/appfirewall.log -i /var/log/pffirewall.log
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setloggingopt throttled
