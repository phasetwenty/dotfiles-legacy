#!/bin/bash
#
# Finds the best python 2 version in the system. If it's not the system python, drop a link to ~/bin to that best one.
#
# Encapsulating in a function to avoid polluting the environment with dead variables
symlink_python() {
  # If we already did this, don't do it again.
  [ -L ~/bin/python ] && return

  local raw_sys_version=$(python -V 2>&1)
  local sys_version=${raw_sys_version#"Python "}
  local major=${sys_version:0:1}
  local minor=${sys_version:2:1}

  # Python 2.7 is what we really want.
  [ $major -eq 2 ] && [ $minor -eq 7 ] && return

  # If 2.7 isn't available, drill down to best you can find.
  local cmd
  local final_python
  local v
  local minor_candidate
  for ((minor_candidate=6; minor_candidate > minor; minor_candidate--)); do
    v="python2$minor_candidate python2.$minor_candidate"
    for cmd in $v; do
      $cmd -V &>/dev/null
      if [ $? -eq 0 ]; then
        final_python=$cmd
        break
      fi
    done
    [ ! -z $final_python ] && break
  done

  [ ! -z $final_python ] && ln -s $(type -P $final_python) ~/bin/python
}
symlink_python