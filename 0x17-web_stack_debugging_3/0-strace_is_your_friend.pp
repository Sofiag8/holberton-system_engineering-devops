# fixing error on wp-setting for an extra p on  php extension
# traced trhough apache process 
exec { 'automate php file error':
     command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
     path => '/bin/',
}