# manifest configure ssh file

file_line {'refuse authentication':
        ensure => present,
        path   => '/etc/ssh/ssh_config',
        line   => '   PasswordAuthentication no',
        }

file_line {'Identify file':
        ensure => present,
        path   => '/etc/ssh/ssh_config',
        line   => '   IdentityFile ~/.ssh/school',
        }

