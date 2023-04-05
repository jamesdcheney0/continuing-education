# troubleshooting with logs
- as sudo, `tail /var/log/messages` and/or `tail /var/log/secure` 
    - for ssh issues, etc 

# searching for files
rg nessus_scanner_sg */account.hcl | sort