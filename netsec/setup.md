```zsh
#!/usr/bin/env zsh

echo "Updating software..."
sudo apt update
sudo apt upgrade

echo "Installing software..."

#install necessary tools
#install necessary tools

sudo apt -y install autojump\
    curl\
    git\
    bat\
    zsh\
    tmux\
    emacs\
    gdb\
    python3-pip\
    kali-defaults\
    kali-root-login\
    kali-tools-gpu\
    kali-tools-hardware\
    kali-tools-fuzzing\
    kali-tools-sdr\
    kali-tools-rfid\
    kali-tools-information-gathering\
    kali-tools-vulnerability\
    kali-tools-passwords\
    kali-tools-wireless\
    kali-tools-reverse-engineering\
    kali-tools-exploitation\
    kali-tools-forensics\
    cmake\
    lolcat\
    cowsay\
    figlet\
    filters\
    fortunes\
    bsdgames\
    dos2unix\
    asciinema\
    python3-pyx\
    squashfs-tools\
    squashfs-tools-ng\
    zlib1g-dev\
    liblzma-dev\
    liblzo2-dev\
    docker.io\
    xfsprogs\
    libboost-all-dev\
    python3-rpyc\
    fontforge\
    doxygen\
    python3-scipy\
    python3-numpy\
    bpython\
    graphviz\
    ruby-dev\
    autojump\
    fzf\
    gdb-multiarch\
    gdbserver\
    gawk\
    python3-full\
    virtualenv\
    lldb\
    gawk\
    tmuxinator\
    python3-scapy\
    python3-netifaces\
    wireshark\
    voltron\
    chafa
    # forensics-full\
    # forensics-extra\
    # forensics-extra-gui\
    # forensics-samples-all
    # uncomment the above if you want to use this image for forensics work as well

sudo gem install colorls mdless
mkdir -p $HOME/bin
mkdir -p $HOME/clones

#enable i386 and amd64 binary support (ONLY RUN ON ARM HOSTS!)
#uncomment if you desire this functionality
# sudo apt install -y qemu-user-static binfmt-support
# sudo dpkg --add-architecture amd64
# sudo dpkg --add-architecture i386
# sudo apt update
# sudo apt install libc6:amd64
# sudo apt install libc6:i386

# you can also enable arm binary support on amd64 hosts if you want to, for whatever reason
# sudo apt install -y qemu-user-static binfmt-support
# sudo dpkg --add-architecture aarch64
# sudo dpkg --add-architecture armhf
# sudo apt update
# sudo apt install libc6:aarch64
# sudo apt install libc6:armhf


#install gef
bash -c "$(curl -fsSL https://gef.blah.cat/sh)"
#create the virtual environment for running gdb, because debian 12
virtualenv -p python3 ~/.gef
#activate it
source ~/.gef/bin/activate
if [ ! -d $HOME/.config/gef-extras ]; then
    curl -L -o - https://github.com/hugsy/gef/raw/main/scripts/gef-extras.sh | sh
    #we need to run gdb in a virtual environment to use gef, so we have to wrap it in a simple shell script
    echo '#!/usr/bin/env zsh\n\nsource $HOME/.gef/bin/activate\n/usr/bin/gdb "$@"\ndeactivate\n' > $HOME/bin/gdb
    chmod +x $HOME/bin/gdb
    pip3 install -r $HOME/.config/gef-extras/requirements.txt
fi
#deactivate the virtual environment
deactivate

#install rust
if [ ! -d $HOME/.cargo ]; then
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
fi

if [ ! -e $HOME/.cargo/bin/atuin ]; then
    curl -L https://raw.githubusercontent.com/atuinsh/atuin/main/install.sh | bash
fi

if [ ! -d $HOME/clones/fastfetch ]; then
    git clone https://github.com/fastfetch-cli/fastfetch.git $HOME/clones/fastfetch
    cd $HOME/clones/fastfetch
    mkdir -p build
    cd build
    cmake ..
    cmake --build . --target fastfetch --target flashfetch
    sudo make install
    cd
fi

if [ ! -e $HOME/antigen.zsh ]; then
    curl -L git.io/antigen > $HOME/antigen.zsh
fi

if [ ! -d $HOME/clones/sunwait ]; then
    git clone https://github.com/risacher/sunwait.git $HOME/clones/sunwait
    cd $HOME/clones/sunwait
    make
    ln -s $HOME/clones/sunwait/sunwait $HOME/bin/sunwait
    cd $HOME
fi

if [ ! -d $HOME/clones/bat-extras ]; then
    git clone https://github.com/eth-p/bat-extras.git $HOME/clones/bat-extras
    cd $HOME/clones/bat-extras
    sudo ./build.sh --install
    cd $HOME
fi

if [ ! -d $HOME/clones/tmux-powerline ]; then
    git clone https://github.com/erikw/tmux-powerline.git $HOME/clones/tmux-powerline
fi

if [ ! -d $HOME/clones/diff-so-fancy ]; then
    git clone https://github.com/so-fancy/diff-so-fancy.git $HOME/clones/diff-so-fancy
fi

if [ ! -d $HOME/.tmux/plugins/tpm ]; then
    mkdir -p $HOME/.tmux/plugins/tpm
    git clone https://github.com/tmux-plugins/tpm $HOME/.tmux/plugins/tpm
fi

if [ ! -d $HOME/.oh-my-zsh ]; then
    git clone https://github.com/ohmyzsh/ohmyzsh.git $HOME/.oh-my-zsh
fi

if [ ! -d $HOME/clones/nerd-fonts ]; then
    git clone --filter=blob:none --sparse https://github.com/ryanoasis/nerd-fonts.git $HOME/clones/nerd-fonts
    cd $HOME/clones/nerd-fonts
    git sparse-checkout add patched-fonts/Hack
    ./install.sh
    cd $HOME
fi

if [ ! -d $HOME/clones/astral ]; then
    git clone https://github.com/sffjunkie/astral.git $HOME/clones/astral
fi

if [ ! -e $HOME/bin/diff-so-fancy ]; then
    ln -s $HOME/clones/diff-so-fancy/diff-so-fancy $HOME/bin/diff-so-fancy
fi

#fill in and uncomment the first two lines!
#git config --global user.name ""
#git config --global user.email ""
git config --global core.pager "diff-so-fancy | less --tabs=4 -RFX"
git config --global interactive.diffFilter "diff-so-fancy --patch"
git config --global color.ui true
git config --global color.diff-highlight.oldNormal    "red bold"
git config --global color.diff-highlight.oldHighlight "red bold 52"
git config --global color.diff-highlight.newNormal    "green bold"
git config --global color.diff-highlight.newHighlight "green bold 22"
git config --global color.diff.meta       "11"
git config --global color.diff.frag       "magenta bold"
git config --global color.diff.func       "146 bold"
git config --global color.diff.commit     "yellow bold"
git config --global color.diff.old        "red bold"
git config --global color.diff.new        "green bold"
git config --global color.diff.whitespace "red reverse"

# shouldn't need this on Kali, but uncomment if you need it
# echo "Changing shell to zsh...will ask for password..."
# chsh -s $(which zsh)

curl http://web.cecs.pdx.edu/~dmcgrath/setup.tar.bz2 | tar xjvf - -C ~/
```