#!/bin/bash
set -e

DOTFILES_DIR="$(
  cd "$(dirname "$0")"
  pwd
)"

ln -sf "$DOTFILES_DIR/zshrc" "$HOME/.zshrc"
ln -sf "$DOTFILES_DIR/vimrc" "$HOME/.vimrc"
ln -sf "$DOTFILES_DIR/p10k.zsh" "$HOME/.p10k.zsh"
ln -sf "$DOTFILES_DIR/gitconfig" "$HOME/.gitconfig"
ln -sf "$DOTFILES_DIR/inputrc" "$HOME/.inputrc"
ln -sf "$DOTFILES_DIR/themes.gitconfig" "$HOME/.themes.gitconfig"
ln -sf "$DOTFILES_DIR/tmux.conf" "$HOME/.tmux.conf"
#ln -sf "$DOTFILES_DIR/init.vim" "$HOME/.config/nvim/init.vim"
ln -sf "$DOTFILES_DIR/lazy.lua" "$HOME/.config/nvim/lua/config/lazy.lua"

# Vim colors
mkdir -p "$HOME/.vim/colors"
mkdir -p "$HOME/.config/nvim/colors"
ln -sf "$DOTFILES_DIR/vim/colors/jellybeans.vim" "$HOME/.vim/colors/jellybeans.vim"
ln -sf "$DOTFILES_DIR/vim/colors/jellybeans.vim" "$HOME/.config/nvim/colors/jellybeans.vim"

# install tmux plugin manager the right way (brew install wasn't working). Also verify if it has already been installed
if [ ! -d "$HOME/.tmux/plugins/tpm" ]; then
  git clone https://github.com/tmux-plugins/tpm "$HOME/.tmux/plugins/tpm"
else
  echo "TPM already installed at $HOME/.tmux/plugins/tpm"
fi

# install LazyVim
# Backup current nvim files
mv ~/.config/nvim ~/.config/nvim.bak
mv ~/.local/share/nvim ~/.local/share/nvim.bak

# clone the starter
git clone https://github.com/LazyVim/starter ~/.config/nvim

# remote the starter .git folder
rm -rf ~/.config/nvim/.git

source ~/.zshrc
