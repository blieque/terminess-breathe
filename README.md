# Terminess Breathe

Terminus is a great Terminal font, but it lacks some breathing room. When I look at the source code I've pushed to GitHub, I can't help but envy at the letter and line spacing. Unfortunately using Powerline and similar unique characters gets a little ugly sometimes with anti-aliased fonts. This is my solution.

Terminess Breathe is Terminus 6×12 px in a 7×14 px container. This gives it an extra 2 pixels of line spacing, and an extra pixel of letter spacing, which makes more different than you might expect. I've also manually updated all of the shading, box-drawing and Powerline symbols so they'll continue to look just right.

If people would like I may well create another variant or two with more line spacing. Adding more letter spacing gets a bit odd. If you'd like to experiment with different spacings, I built [this](https://file.blieque.co.uk/terminus/) a while ago.

## Installation

This is really a Linux thing, but it might be possible to coax macOS into displaying an X bitmap font. If you're already running with Linux, however, open a terminal and run the following:

    git clone https://github.com/blieque/terminess-breathe.git
    cd terminess-breathe

    mkdir -p ~/.local/share/fonts/X11
    cp terminess-breathe.pcf.gz ~/.local/share/fonts/X11

    fc-cache

You should now be able to select Terminess Breathe in your terminal emulator's preferences. If you're one configured with `.Xresources`, adding this should work:

    
