# FE02 - 100pts

## Briefing

> We're sure there's a flag at `cfta-fe02.allyourbases.co` - can you find it?

## Solution

1. The provided domain does not resolve to any server. Therefore, the flag must be somewhere in the DNS records. Note that a second version of the challenge does resolve to an IP address hosting a website.

2. The flag is in a TXT record. It can be found with `dig` like so: `dig TXT cfta-fe02.allyourbases.co` The TXT record has the value `flag=unlimited_free_texts`.

3. A public DNS service can be used instead of `dig` like [Google's public DNS](https://dns.google.com/query?name=cfta-fe02.allyourbases.co&rr_type=TXT).

### Flag

`unlimited_free_texts`
