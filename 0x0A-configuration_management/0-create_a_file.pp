#create a file school with the content i love school

file {'/tmp/school':
        ensure  => file,
        group   => 'www-data',
        owner   => 'www-data',
        content => 'I love puppet',
        mode    => '0744',
        }
