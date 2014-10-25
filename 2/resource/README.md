How to setup
------------

### Generate `tweets.txt`

#### 0. Install Perl and Carton

Install perl5.18 or later. And next step, install the Carton like so;

```
$ cpanm Carton
```

#### 1. install deps

```
$ carton install
```

#### 2. write `auth_info.pl`

Sample:

```perl
+{
    consumer_key    => '<CONSUMER KEY>',
    consumer_secret => '<CONSUMER SECRET>',
    token           => '<TOKEN>',
    token_secret    => '<TOKEN SECRET>',
};
```

#### 3. run script

```
$ carton exec -- perl crawler4twitter.pl
```

