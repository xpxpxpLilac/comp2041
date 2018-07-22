#!/usr/bin/perl -w
print "username: ";
$username = <STDIN>;
chomp $username;
print "password: ";
$password = <STDIN>;
chomp $password;

# sanitize username
$username = substr $username, 0, 256;
$username =~ s/\W//g;
$password_file = "accounts/$username/password";
if (!open F, "<$password_file") {
    print "Unknown username!\n";
} else {
    $correct_password = <F>;
    chomp $correct_password;
    if ($password eq $correct_password) {
        print "You are authenticated.\n";
    } else {
        print "Incorrect password!\n";
    }
}
