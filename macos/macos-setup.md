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

## Terminal colors
To change general text color, have to adjust that in the terminal settings
yellow cmyk updates: 32% cyan, 80% magenta, 20% yellow, 9% black
pink cmyk updates: 63% cyan, 67% magenta, 0% yellow & black

## Autocompletion setup for kubernetes
Supposed to be able to add these lines to bashrc and install `bash-completion` with brew
```
alias k='kubectl'
source <(kubectl completion bash)
complete -o default -F __start_kubectl k
```

It was not playing nice. Had to run 'kubectl completion bash > ~/.kubectl_completion.sh` then `source ~/.kubectl_completion.sh` then add these lines to bashrc and source it
```
## Enable kubectl completion
[ -f ~/.kubectl_completion.sh ] && source ~/.kubectl_completion.sh
alias k='kubectl'
complete -o default -F __start_kubectl k
```

## git-delta
Installed via brew. Customize the colors per his [readme](https://dandavison.github.io/delta/custom-themes.html)

## bash functions
had to use function keyword to define a bash function. Just the function name and () immediately afterward wasn't working
