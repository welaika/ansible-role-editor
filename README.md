Ansible Role Editor
===================

[![Build Status](https://travis-ci.org/welaika/ansible-role-editor.svg?branch=master)](https://travis-ci.org/welaika/ansible-role-editor)

Install vimfiles for a specific user.

Vimfiles are fetch from a git repository.

Requirements
------------

Your vimfiles repository *must* have a `install.sh` files in it. Use it to create symlinks. This role won't create symlinks for you.

The user **must** already exist.

Role Variables
--------------

These are the default variables:


Dependencies
------------

None :)

Example Playbook
----------------

User `john_doe` *must* already exist.

```yaml
- hosts: servers
  roles:
     - role: ansible-role-editor
       vars:
         vimfiles_user: "john_doe"
```

License
-------

MIT

Testing
-------

Install molecule

`$ pip3 install --user 'molecule[docker]'`

Start docker and run

`$ molecule test`

Author Information
------------------

made with ❤️ and ☕️ by [weLaika](https://dev.welaika.com)
