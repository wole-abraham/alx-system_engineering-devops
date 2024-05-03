# executes a command to terminate a process

exec {'kill_killmenow_process':
        command => '/usr/bin/pkill killmenow',
        }
