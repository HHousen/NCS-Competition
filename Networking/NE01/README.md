# NE01 - 100pts

## Briefing

> There is a TCP network service running on `cfta-ne01.allyourbases.co`. Find it to get the flag after you connect. Note: The target has many open ports - only one is the correct one. The correct port will identify itself with `ID: ne01` after you connect.


## Solution

1. Use `nmap` to scan the domain: `nmap -Pn -sT -p1000-10000 -v cfta-ne01.allyourbases.co`

    `nmap` results:

    ```
    Completed Connect Scan at 17:46, 138.11s elapsed (9001 total ports)
    Nmap scan report for cfta-ne01.allyourbases.co (52.210.101.44)
    Host is up (0.11s latency).
    Other addresses for cfta-ne01.allyourbases.co (not scanned): 34.251.231.207
    rDNS record for 52.210.101.44: ec2-52-210-101-44.eu-west-1.compute.amazonaws.com
    Not shown: 8997 filtered ports
    PORT     STATE SERVICE
    1061/tcp open  kiosk
    8012/tcp open  unknown
    8013/tcp open  unknown
    8017/tcp open  unknown

    Nmap done: 1 IP address (1 host up) scanned in 138.19 seconds
    ```

2. Manually connecting to each port with `netcat` shows the flag:

    ```
    $ nc 52.210.101.44 1061
    ID: ne01
    Flag: Nmap_0f_the_W0rld!
    ```

### Flag

`Nmap_0f_the_W0rld!`
