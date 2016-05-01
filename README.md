# dotfiles

Inspired by the method described at https://developer.atlassian.com/blog/2016/02/best-way-to-store-dotfiles-git-bare-repo/. I'm extending this pattern by using branches to encapsulate the differences between platforms, with `master` containing pieces common to all supported platforms. I also have a homebrew pattern for breaking up the initialization into organized modules.

# Setting up a new host

Clone with this command:

    git clone --bare git@github.com:phasetwenty/dotfiles.git $HOME/.dotfiles-repo

I have the remote available as a shell variable `DOTFILES_REMOTE`. Also, `.dotfiles-repo` is a name that shows up in these instructions and in this repo.


To make running the commands easier, set an alias:

    alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles-repo/ --work-tree=$HOME'

Next, check out with:

    dotfiles checkout
    
If the host has existing dotfiles, you'll need to get them out of the way (git doesn't like them). The Atlassian link has instructions for how to work around this issue. 

Last, check out your platform's branch:

    dotfiles checkout <platform-branch>
    
I recommend restarting the shell to apply the full set of dotfiles.

## Repo problems

I've experienced a problem with the default fetch behavior on new repos. git is not setting up to fetch branches as I'd want. To resolve this, run this command:

    dotfiles config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"

# Notes

## ~/.bash

This directory holds all initialization for the Bash shell. Its contents are sourced by both `~/.bashrc` and `~/.bash_profile` which handles both login and non-login shells.

### ~/.bash/init

The starting point for my Bash initialization.

## ~/.bash/applications

This directory contains modules to be sourced, named for the application it configures.
