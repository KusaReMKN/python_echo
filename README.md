# python_echo
TCP based ECHO server and client written in Python3

# How to run

## Server
Usage:

```console
$ ./server.py port
```

For example, to listen on port 12345:

```console
$ ./server.py 12345
```

## Client
Usage:

```console
$ ./client.py host port message [...]
```

For example, to send the message **Hello** to port 12345 on **localhost**:

```console
$ ./client.py localhost 12345 Hello
```

Another example, to send the message **X Y Z** to port 23456 on **192.0.2.1**:

```console
$ ./client.py 192.0.2.1 23456 X Y Z
```

# License
MIT
