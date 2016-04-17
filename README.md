# dotfiles

Inspired by the method described at https://developer.atlassian.com/blog/2016/02/best-way-to-store-dotfiles-git-bare-repo/. I'm extending this pattern by using branches to encapsulate the differences between platforms, with `master` containing pieces common to all supported platforms. I also have a homebrew pattern for breaking up the initialization into organized modules.

# Notes

## ~/.bash

This directory holds all initialization for the Bash shell. Its contents are sourced by both `~/.bashrc` and `~/.bash_profile` which handles both login and non-login shells.

### ~/.bash/init

The starting point for my Bash initialization.

## ~/.bash/applications

This directory contains modules to be sourced, named for the application it configures.