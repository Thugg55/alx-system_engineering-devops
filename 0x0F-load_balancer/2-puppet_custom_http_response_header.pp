# 2-puppet_custom_http_response_header.pp

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Define a custom template for Nginx configuration
file { '/etc/nginx/sites-available/custom_header':
  ensure  => present,
  content => template('nginx/custom_header.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable the custom configuration
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_header',
  require => File['/etc/nginx/sites-available/custom_header'],
  notify  => Service['nginx'],
}

# Define Nginx service
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  hasstatus  => true,
}
