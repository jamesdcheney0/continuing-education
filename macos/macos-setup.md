# Notes about installation of things
- in vim, changed tab to only do 4 spaces
    - set autoindent expandtab tabstop=4 shiftwidth=4
## Docker
- had to install docker desktop `brew install --cask docker` rather than just brew install
- then had to launch the docker app, then I was able to use docker commands on CLI 
## displaylink
- Turning off hardware acceleration in Google Chrome made it so I can watch the videos!!! 

## dotfiles directory
Copied the dotfiles from home to the dotfiles directory and ran this command to link them to where the os expects the dotfiles
`ln -s /Users/jamescheney/Documents/1000-hours/macos/dotfiles/inputrc ~/.inputrc`

source ~/.bashrc and ~/.bash_profile
- source runs commands in whatever file it is pointed at
bind -f ~/.inputrc

