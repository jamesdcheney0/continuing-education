#!/bin/bash
set -e

DOTFILES_DIR="$(cd "$(dirname "$0")"; pwd)"

ln -sf "$DOTFILES_DIR/zshrc" "$HOME/.zshrc"
ln -sf "$DOTFILES_DIR/vimrc" "$HOME/.vimrc"
ln -sf "$DOTFILES_DIR/p10k.zsh" "$HOME/.p10k.zsh"
ln -sf "$DOTFILES_DIR/gitconfig" "$HOME/.gitconfig"
ln -sf "$DOTFILES_DIR/inputrc" "$HOME/.inputrc"
ln -sf "$DOTFILES_DIR/themes.gitconfig" "$HOME/.themes.gitconfig"
ln -sf "$DOTFILES_DIR/tmux.conf" "$HOME/.tmux.conf"

# Vim colors
mkdir -p "$HOME/.vim/colors"
ln -sf "$DOTFILES_DIR/vim/colors/jellybeans.vim" "$HOME/.vim/colors/jellybeans.vim"
