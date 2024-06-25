
## Courses

* [CS496/596: Network Security](netsec/readme.md)
* [CS493/593: Digital Forensics](forensics/readme.md)
* [CS491/591: Introduction to Computer Security](introsec/readme.md)
* [CS410/510: System Administration and DevOps](secdevops/readme.md)

## Pages

Not all of these pages are complete or useful yet.  I'm working on it.

* [Automation](automation.md)
* [Azure](azure.md)
* [CI/CD and other Topics](ci_cd.md)
* [Containers](containers.md)
* [FreeBSD Setup Script](freebsd_setup.md)
* [Infrastructure as Code](sdi.md)
* [Networking Fundamentals](networking.md)
* [Other Secure Programming languages](secure_other.md)
* [PowerShell](powershell.md)
* [Powershell profile](powershell_profile.md)
* [Secure C Programming](secure_c.md)
* [Software configuration](software.md)
* [Technical Writing](technical_writing.md)
* [Ubuntu configuration](ubuntu.md)
* [VM Setup on Windows](hyper-v.md)
* [VM Setup on macOS](vms_on_macos.md)
* [Virtualization](virtualization.md)
* [Windows Administration](windows_admin.md)
* [Windows File Sharing from Linux](samba.md)
* [tmux config](.tmux.conf.md)

## Useful links for learning

* [tmux cheatsheet](https://tmuxcheatsheet.com/)
* [Linux Handbook on tmux](https://linuxhandbook.com/tmux/)
* [Markdown](https://guides.github.com/features/mastering-markdown/)
* [The C Book](https://publications.gbdirect.co.uk/c_book/)
* [The GNU `make` manual](https://www.gnu.org/software/make/manual/make.pdf)
* [Managing projects with `make`](https://github.com/Vauteck/docs_utils/blob/master/autotools/Oreilly%20-%20Managing%20Projects%20With%20Gnu%20Make%203Rd%20Edition.pdf)
* [The `chmod` calculator](https://chmod-calculator.com/)
* [The Python tutor](https://pythontutor.com/)
* [_The Linux Command Line_](http://linuxcommand.org/tlcl.php) (Direct [PDF link](https://sourceforge.net/projects/linuxcommand/files/TLCL/19.01/TLCL-19.01.pdf/download))
* [_Adventures with the Linux Command Line_](https://sourceforge.net/projects/linuxcommand/files/AWTLCL/21.10/AWTLCL-21.10.pdf/download)
* [_The Linux Development Platform_](https://archive.org/details/ost-computer-science-0130091154/mode/1up)
* [gdb tutorial](http://www.cs.cmu.edu/~gilpin/tutorial/)
* [gef manual](https://hugsy.github.io/gef/)

## Shell setup without sudo privs

```bash
#!/usr/bin/env zsh

#install gef
bash -c "$(curl -fsSL https://gef.blah.cat/sh)"

if [ -e $(which pip) ]; then
    pip install --user keystone-engine ropper capstone unicorn requests
elif [ -e $(which pip3) ]; then
    pip3 install --user keystone-engine ropper capstone unicorn requests
fi

mkdir -p $HOME/bin
mkdir -p $HOME/clones

#install useful additions
#useful little CLI hex viewer
# cargo install hexyl

curl -s -L https://github.com/sharkdp/hexyl/releases/download/v0.13.1/hexyl-v0.13.1-i686-unknown-linux-musl.tar.gz | tar -x -z -C $HOME -f -
mv hexyl-v0.13.1-i686-unknown-linux-musl/hexyl $HOME/bin/
rm -rf hexyl-v0.13.1-i686-unknown-linux-musl

#better pager, called bat
curl -s -L https://github.com/sharkdp/bat/releases/download/v0.23.0/bat-v0.23.0-x86_64-unknown-linux-musl.tar.gz | tar -x -z -C $HOME -f -
mv bat-v0.23.0-x86_64-unknown-linux-musl/bat $HOME/bin/batcat
ln $HOME/bin/batcat $HOME/bin/bat
rm -rf bat-v0.23.0-x86_64-unknown-linux-musl

if [ ! -e $HOME/antigen.zsh ]; then
    curl -L git.io/antigen > $HOME/antigen.zsh
fi

if [ ! -d $HOME/clones/sunwait ]; then
    git clone https://github.com/risacher/sunwait.git $HOME/clones/sunwait
    cd $HOME/clones/sunwait
    make
    cp $HOME/clones/sunwait/sunwait $HOME/bin/sunwait
    cd $HOME
fi

if [ ! -d $HOME/clones/bat-extras ]; then
    git clone https://github.com/eth-p/bat-extras.git $HOME/clones/bat-extras
    cp $HOME/clones/bat-extras/bin/* $HOME/bin/
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

ln -s $HOME/clones/diff-so-fancy $HOME/bin/diff-so-fancy

git config --global user.name "" #fill me in!
git config --global user.email "" #fill me in!
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

chsh -s /bin/zsh

#only if $HOME is on NFS
env GEM_HOME=/disk/scratch/$(whoami) 
gem install colorls

#for all classes except 496:
wget -q -O setup.tar.bz2 http://web.cecs.pdx.edu/~dmcgrath/setup.tar.bz2
#for cs496:
#wget -q -O setup.tar.bz2 http://web.cecs.pdx.edu/~dmcgrath/setup_496.tar.bz2
tar xavf setup.tar.bz2 -C ~/
```
