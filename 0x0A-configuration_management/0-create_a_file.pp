# manifest to create a file owned by www-data with permission 744

file { '/tmp/school':
ensure => 'file',
mode => '0744',
owner => 'www-data',
group => 'www-data',
content => 'I love Puppet',
path => '/tmp/school',
}
