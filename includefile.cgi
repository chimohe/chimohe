#!/usr/bin/perl

use strict;
use warnings;

sub includefile {
    my $fname = shift;
    my $file_content = '';

    # Remove potentially harmful characters from the file name
    $fname =~ s/([\&;\`'\|\"*\?\~\^\(\)\[\]\{\}\$\n\r])//g;

    # Open the file for reading
    if (open(INCLUDE, $fname)) {
        local $/;
        $file_content = <INCLUDE>;
        close(INCLUDE);
    } else {
        $file_content = '[an error occurred while processing this directive]';
    }

    return $file_content;
}

# Get the "fname" parameter from the query string
my $fname = $ENV{'QUERY_STRING'};
$fname =~ s/^fname=//;

# Set the content type to plain text
print "Content-type: text/plain\n\n";

# Call the includefile subroutine and print the result
print includefile($fname);
