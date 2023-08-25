# Put notes about Vault & test on M1 

# RDP 
## With CAC
xfreerdp `brew install freerdp`
xquartz `brew install --cask xquartz`
had to set display `export DISPLAY=":0"` - set that in my zsh aliases file
then could run `xfreerdp -sec-nla /u:<username> /smartcard /smartcard-logon /d:<domain> /v:<windows.instance.ip.addr>:3389`
can run `sc_auth verifypin` on a machine with a smart card inserted and it'll authenticate the CAC & ask for PIN - this way, the 3 attempt lockout can be avoided with a third good pin 
- verify xQuartz is running 