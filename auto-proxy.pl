use 5.016;

# bind 2222
`sudo autossh -M 888 -fN -o "PubkeyAuthentication=yes" -o "StrictHostKeyChecking=false" -o "PasswordAuthentication=no" -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R 0.0.0.0:2222:localhost:22 -i /home/lane/.ssh/id_rsa lane\@vultr.zhanglintc.work`;

# bind 9091
`sudo autossh -M 999 -fN -o "PubkeyAuthentication=yes" -o "StrictHostKeyChecking=false" -o "PasswordAuthentication=no" -o "ServerAliveInterval 60" -o "ServerAliveCountMax 3" -R 0.0.0.0:9091:localhost:9091 -i /home/lane/.ssh/id_rsa lane\@vultr.zhanglintc.work`;


