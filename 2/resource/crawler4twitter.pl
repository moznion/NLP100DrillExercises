#!/usr/bin/env perl

use strict;
use warnings;
use utf8;
use AnyEvent;
use AnyEvent::Twitter::Stream;
use Encode qw/encode_utf8/;

my $cv = AE::cv;

my $auth_info = require './auth_info.pl';

open my $fh, '>>', 'tweets.txt';

my $cnt = 0;

my $listener = AnyEvent::Twitter::Stream->new(
    consumer_key    => $auth_info->{consumer_key},
    consumer_secret => $auth_info->{consumer_secret},
    token           => $auth_info->{token},
    token_secret    => $auth_info->{token_secret},
    method          => "filter",
    locations       => "132.2,29.9,146.2,39.0,138.4,33.5,146.1,46.20", # to extract Japanese tweets
    on_tweet        => sub {
        my $tweet = shift;
        my $msg =  encode_utf8("$tweet->{user}{screen_name}\t$tweet->{text}\n");
        print $msg;
        print $fh $msg;

        print ++$cnt . "\n";
        exit(0) if $cnt > 100000;
    },
);

$cv->recv;

__END__

