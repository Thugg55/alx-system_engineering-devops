# A puppet manifest to kill a process using the pkill command

exec { 'killmenow':
 command => 'pkill killmenow',
 provider => 'shell'
}
