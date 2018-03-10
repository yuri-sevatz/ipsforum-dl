```
usage: ipsforum-dl [-h] --username USERNAME --password PASSWORD
                   [--output OUTPUT] [--reverse] [--incremental] [--full]
                   [--checkpoint CHECKPOINT] [--begin BEGIN] [--end END]
                   [--simulate]
                   url [url ...]

IpsForum Downloader

positional arguments:
  url                   sequence of urls to access, of format:
                        ['<ips_root>/index.php?/login/',
                        '<ips_root>/index.php?/forums/',
                        '<ips_root>/index.php?/forums/forum/<forum_id>',
                        '<ips_root>/index.php?/forums/topic/<topic_id>']

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME, -u USERNAME
                        username to supply to remote server if logging in
  --password PASSWORD, -p PASSWORD
                        password to supply to remote server if logging in
  --output OUTPUT, -o OUTPUT
                        output directory
  --reverse, -r         archive older topics first
  --incremental, -i     save/load progress in <output>/timestamp.chk
  --full, -f            restart progress in <output>/timestamp.chk
  --checkpoint CHECKPOINT, -c CHECKPOINT
                        override progress on start with date/time (e.g.
                        2018-03-10T18:28:04-0500)
  --begin BEGIN, -b BEGIN
                        begin post date/time range (e.g.
                        2018-03-10T18:28:04-0500)
  --end END, -e END     end post date/time range (e.g.
                        2018-03-10T18:28:04-0500)
  --simulate, -s        simulate execution without writing to disk
```
