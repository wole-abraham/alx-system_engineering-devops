file {'school':
        ensure  => present,
        path    => '/tmp/school',
        group   => 'www-data',
        owner   => 'www-data',
        content => 'I love puppet',
        }
