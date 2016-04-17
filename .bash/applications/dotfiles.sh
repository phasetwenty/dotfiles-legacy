#!/bin/bash
#
init_dotfiles () {
    # Using a function for namespacing.
    local dotfiles_repo_name='.dotfiles-repo'  # Name of the directory that holds our bare repo
    local dotfiles_command='dotfiles'

    alias "$dotfiles_command"="git --git-dir=$HOME/$dotfiles_repo_name/ --work-tree=$HOME"
    "$dotfiles_command" --local status.showUntrackedFiles no
}
init_dotfiles
