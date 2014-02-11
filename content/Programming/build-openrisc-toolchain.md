Title: HowTo build an openrisc toolchain
Author: Marco Minutoli
Date: 2013-08-01
Tags: openrisc, or1k, gcc, toolchain

Working on my master thesis I had the need to build the toolchain for
openrisc. I found out that on the [OpenRISC Community Portal
Wiki](http://opencores.org/or1k/OR1K:Community_Portal) there is a
guide to start with. The original information can be found
[here](http://opencores.org/or1k/OpenRISC_GNU_tool_chain#Installation_of_development_versions).

Unfortunately things never go smoothly as we want and this is what I
did to complete my task.

First of all we have to clone two git repository. The first one is an
aggregate of tools (ie. binutils) and useful libraries
(ie. newlib). The latter is a version of gcc with support to the
openrisc architecture. To clone the two repositories run:

    :::console
    mkdir -p $TOOLCHAIN_SRC_DIR
    cd $TOOLCHAIN_SRC_DIR
    git clone git://github.com/openrisc/or1k-src.git
    git clone git://github.com/openrisc/or1k-gcc.git

where `$TOOLCHAIN_SRC_DIR` is the path under your `$HOME` where you
want to store the toolchain code.

The instruction on the Wiki suggests to install the toolchain under
`/opt/or1k-toolchain` but I prefer to keep all my user stuff in my
home directory so I am going to install in a different path under my
user home directory.

The first step is to create two build directory both repositories.

    :::console
    mkdir $TOOLCHAIN_SRC_DIR/bld-or1k-src
    mkdir $TOOLCHAIN_SRC_DIR/bld-or1k-gcc

The first step in building a toolchain is to build binutils:

    :::console
    cd bld-or1k-src
    ../or1k-src/configure --target=or1k-elf --prefix=$HOME/or1k-toolchain --enable-shared \
      --disable-itcl --disable-tk --disable-tcl --disable-winsup --disable-libgui --disable-rda \
      --disable-sid --disable-sim --disable-gdb --with-sysroot --disable-newlib --disable-libgloss
    make -j4
    make install

Once completed we are ready to build GCC for the first time:

    :::console
    cd ../bld-or1k-gcc
    ../or1k-gcc/configure --target=or1k-elf --prefix=$HOME/or1k-toolchain \
      --enable-languages=c --disable-shared --disable-libssp
    make -j4
    make install

Then we need to compile newlib and gdb, but before we start we need to
had our freshly built GCC to the path:

    :::console
    export PATH=$HOME/or1k-toolchain/bin:$PATH

and then

    :::console
    cd ../bld-or1k-src
    ../or1k-src/configure --target=or1k-elf --prefix=$HOME/or1k-toolchain \
      --enable-shared --disable-itcl \
      --disable-tk --disable-tcl --disable-winsup --disable-libgui --disable-rda --disable-sid \
      --enable-sim --disable-or1ksim \
      --enable-gdb  --with-sysroot --enable-newlib --enable-libgloss
    make
    make install

Note that this time `make` is missing the `-j` option.

Now we are ready for the final step. Build GCC again but this time
with C++ and newlib support:

    :::console
    cd ../bld-or1k-gcc
    ../or1k-gcc/configure --target=or1k-elf --prefix=$HOME/or1k-toolchain \
      --enable-languages=c,c++ --disable-shared --disable-libssp --with-newlib
    make -j4
    make install

The toolchain is built. The last thing to do is to open your text
editor add the toolchain to the path in your .profile like this:

    :::bash
    # set PATH to include or1k-elf
    if [ -d "$HOME/or1k-toolchain/bin" ] ; then
       PATH="$HOME/or1k-toolchain/bin:$PATH"
    fi

That's it.
