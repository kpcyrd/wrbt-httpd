wrbt-httpd
==========

Authorize peering requests on remote servers

API
---

```
$ http -f POST 127.0.0.1:5000/api auth=changeme method=authorize name=foo
HTTP/1.0 200 OK
Access-Control-Allow-Origin: *
Content-Length: 153
Content-Type: application/json
Date: Wed, 04 Feb 2015 21:46:44 GMT
Server: Werkzeug/0.9.6 Python/2.7.8

{
    "ip": "1.2.3.4",
    "password": "fEZZyT9TwSKtPUDpbOX7vfzAHXGmo3i",
    "pk": "92dyb2331kd5txjucrgwv98zq88rvcf5nnzzknu66sr7vr3pwum0.k",
    "port": "34623"
}
```

License
-------

GPLv3
