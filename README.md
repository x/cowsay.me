# [Cowsay.me](http://www.cowsay.me/)

The web equivilent of doing...
```
$ fortune | cowsay
 _________________________________________
/ If you don't like the way I drive, stay \
\ off the sidewalk!                       /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

The original version fit into a tweet:
> https://twitter.com/dproi/status/507177515446960128

Unfortunately, that version required a dedicated linux instance. And, I've spun
those down. So, this is the new version deployed to heroku and using flask
instead of netcat and python equivilents to cowsay and fortune. It's not as
magical as the tweet-length one-liner, but I still own the domain so I feel I
should at least get it working again.


## Run Locally

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Deploy

```
git push heroku master
```
