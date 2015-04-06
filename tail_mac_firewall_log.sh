sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setloggingmode on 
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setloggingopt detail 
sudo tail -f /var/log/appfirewall.log 
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setloggingopt throttled
