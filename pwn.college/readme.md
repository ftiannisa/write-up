# WRITE-UP FOR pwn.college

**by klarsynt**

Website: https://pwn.college

## How to access the service?

- Use pwn.college's [Workspace](https://pwn.college/workspace) or [Desktop](https://pwn.college/desktop)

  but in my case, it's kinda laggy (maybe it's bcs my potato pc🥔) so I'm using the 2nd method which is

- SSH!

  Here's how to setup:

  0. Run `$ ssh-keygen -f key -N ''` in your terminal
  1. You'll get 2 files: `key` and `key.pub`
  2. Copy the content of `key.pub` to your pwn.college settings ([Settings > SSH Key](https://pwn.college/settings#ssh-key))
  3. Run `$ ssh -i key hacker@dojo.pwn.college` to connect.
