#create a file school with the content i love school

file {'school':
        ensure  => present,
        path    => '/tmp/school',
        group   => 'www-data',
        owner   => 'www-data',
        content => 'I love puppet',
        }
