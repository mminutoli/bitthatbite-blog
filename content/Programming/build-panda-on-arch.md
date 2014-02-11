Title: HowTo build PandA on ArchLinux
Author: Marco Minutoli
Date: 2014-02-06
Tags: HLS, PandA, ArchLinux

Somedays ago I moved my laptop from Debian to ArchLinux. Once the
installation has completed I started to install PandA (you know I want
to work on my master thesis ;) ). So the instruction below assume you
are starting from a fresh install.

First of all let's start installing all the dependencies. Before to
start you will need to enable the multilib repository in pacman. If
you don't know how to do it follow [this
link](https://wiki.archlinux.org/index.php/multilib).

After a `pacman -Sy` you can proceed to install part of the
dependencies with

    :::console
    pacman -S base-devel multilib-devel boost iverilog

After this command has completed you only miss mpfi that unfortunately
isn't in the official repositories but you can find it in the AUR at
[this link](https://aur.archlinux.org/packages/mpfi).

If you have never installed something from AUR these are the
instructions.

    :::console
    wget https://aur.archlinux.org/packages/mp/mpfi/mpfi.tar.gz
    tar xzf mpfi.tar.gz
    cd mpfi
    makepkg -s
    sudo pacman -U mpfi-1.5-1-x86_64.pkg.tar.xz

Anyway you can find more information
[here](https://wiki.archlinux.org/index.php/Arch_User_Repository)

Once all the dependencies are installed you're ready to compile panda.
Extract panda from the archive and procede with the usual configure,
make and make install sequence :).

    :::console
    ./configure --with-gcc48=/usr/bin/gcc --enable-bambu \
    --enable-icarus  --prefix=/opt/panda --enable-flopoco \
    --disable-release

    make -j4
    make install

At the time of writing ArchLinux comes with gcc-4.8 but in the future
you will need to pass --with-gcc49 :).

The option --disable-release is necessary because ArchLinux doesn't
distribute static libraries.