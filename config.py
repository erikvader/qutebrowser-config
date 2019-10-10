# -*- eval: (flycheck-mode 0); -*-

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

############################### boring settings ###############################

c.content.autoplay = True
with config.pattern('*://*.youtube.com/*') as p:
   p.content.autoplay = False

c.content.cookies.accept = 'all'
c.content.host_blocking.whitelist = ['thepiratebay.org']
c.content.javascript.can_access_clipboard = True
c.content.notifications = False
c.downloads.open_dispatcher = 'rifle'
c.downloads.position = 'bottom'
c.downloads.location.remember = False
c.downloads.location.suggestion = "both"
c.downloads.remove_finished = 5000
c.editor.command = ['emacsclient', '-c', '-e', '(find-file "{file}")', '-e', '(goto-line {line})', '-e', '(move-to-column {column0})']
c.scrolling.bar = 'always'
c.statusbar.widgets = ['keypress', 'url', 'history', 'tabs', 'progress']
c.tabs.background = True
c.tabs.last_close = 'default-page'
c.tabs.select_on_remove = 'last-used'
c.tabs.new_position.stacking = False
c.url.default_page = str(config.configdir / "startpage.html") # NOTE: recommended way to access?
c.url.start_pages = c.url.default_page
c.url.searchengines = {
   'DEFAULT': 'https://google.se/search?q={}',
   'dd':      'https://duckduckgo.com/?q={}',
   'gif':     'https://giphy.com/search/{}',
   'go':      'https://google.se/search?q={}',
   'ho':      'https://www.haskell.org/hoogle/?hoogle={}',
   'mal':     'https://myanimelist.net/search/all?q={}',
   'py':      'https://docs.python.org/3/search.html?q={}',
   'pyg':     'https://google.se/search?q=python 3 {}',
   'rd':      'https://doc.rust-lang.org/std/index.html?search={}',
   'yt':      'https://www.youtube.com/results?search_query={}'
}
c.window.title_format = '{perc}{current_title}'
c.zoom.default = '100%'
c.zoom.levels = ['25%', '33%', '50%', '60%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']
c.fonts.monospace = '"DejaVu Sans Mono", "xos4 Terminus", Terminus, Monospace, Monaco, "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Fixed, Consolas, Terminal'
c.completion.open_categories = ["quickmarks", "bookmarks", "history"]

################################ emacs bindings ###############################

# Bindings for normal mode

# disable insert mode completely
c.input.insert_mode.auto_enter = False
c.input.insert_mode.auto_leave = False
c.input.insert_mode.plugins = False

# Forward unbound keys
c.input.forward_unbound_keys = "all"

ESC_BIND = 'clear-keychain ;; search ;; fullscreen --leave'

c.bindings.default['normal'] = {}
c.bindings.commands['normal'] = {
   # Navigation
   '<ctrl-j>':      'scroll-px 0 40',
   '<ctrl-k>':      'scroll-px 0 -40',
   '<ctrl-d>':      'scroll-page 0 0.5',
   '<ctrl-u>':      'scroll-page 0 -0.5',
   '<alt-g>':       'scroll-to-perc 0',
   '<alt-shift-g>': 'scroll-to-perc',

   # Commands
   '<ctrl-r>':       'reload',
   '<ctrl-shift-r>': 'reload -f',

   '<alt-x>':          'set-cmd-text :    ',
   '<ctrl-x>b':        'set-cmd-text -s : buffer',
   '<ctrl-x>k':        'tab-close',
   '<ctrl-x>h':        'set-cmd-text -s : help',
   '<ctrl-x>d':        'download-clear',
   '<ctrl-x>c':        'clear-messages',
   '<ctrl-x><ctrl-r>': 'config-source;; message-info "reloaded config"',
   '<ctrl-x>r':        'tab-close ;; undo',
   '<ctrl-x><ctrl-x>': 'fake-key <ctrl-x>',
   '<ctrl-x>i':        'inspector',
   '<ctrl-x>v':        'enter-mode passthrough',

   # searching
   '<ctrl-s>': 'set-cmd-text /',
   # '<ctrl-r>': 'set-cmd-text ?',

   # zoom
   '<ctrl-+>': 'zoom-in',
   '<ctrl-->': 'zoom-out',
   '<ctrl-0>': 'zoom 100',

   # marks
   # '<ctrl-m>':  'enter-mode set_mark',
   # '<ctrl-\'>': 'enter-mode jump_mark',

   # hinting
   '<ctrl-f>': 'hint all',
   '<alt-f>':  'hint all tab-bg',

   # history
   '<ctrl-l>': 'forward',
   '<ctrl-h>': 'back',

   # tabs
   '<alt-j>':   'tab-next',
   '<alt-k>':   'tab-prev',
   '<ctrl-w>':  'tab-close',
   '<ctrl-e>':  'tab-close --next',
   '<ctrl-t>':  'open -t',
   '<ctrl-x>u': 'undo',

   # windows
   '<ctrl-shift-n>': 'open -p',

   # open links
   '<ctrl-o>':       'set-cmd-text -s :open',
   '<ctrl-shift-o>': 'set-cmd-text -s :open -t',
   '<alt-o>':        'set-cmd-text -s :open -t',
   '<ctrl-x>o':      'set-cmd-text :open {url:pretty}',

   '<ctrl-b>':       'set-cmd-text -s :quickmark-load',
   '<ctrl-shift-b>': 'set-cmd-text -s :quickmark-load -t',
   '<alt-b>':        'set-cmd-text -s :quickmark-load -t',

   # clipboard
   '<ctrl-p>':       'open -- {clipboard}',
   '<ctrl-shift-p>': 'open -t -- {clipboard}',
   '<alt-p>':        'open -t -- {clipboard}',
   '<ctrl-y>':       'yank',

   # macro
   # '<ctrl-x>q': 'record-macro',
   # '<ctrl-x>@': 'run-macro',

   # editing
   # '<ctrl-f>': 'fake-key <Right>',
   # '<ctrl-b>': 'fake-key <Left>',
   # '<ctrl-a>': 'fake-key <Home>',
   # '<ctrl-e>': 'fake-key <End>',
   # '<ctrl-n>': 'fake-key <Down>',
   # '<ctrl-p>': 'fake-key <Up>',
   # '<alt-f>': 'fake-key <Ctrl-Right>',
   # '<alt-b>': 'fake-key <Ctrl-Left>',
   # '<ctrl-d>': 'fake-key <Delete>',
   # '<alt-d>': 'fake-key <Ctrl-Delete>',
   # '<alt-backspace>': 'fake-key <Ctrl-Backspace>',
   # '<ctrl-w>': 'fake-key <Ctrl-backspace>',
   # '<ctrl-y>': 'insert-text {primary}',

   # Numbers
   # https://github.com/qutebrowser/qutebrowser/issues/4213
   '1': 'fake-key 1',
   '2': 'fake-key 2',
   '3': 'fake-key 3',
   '4': 'fake-key 4',
   '5': 'fake-key 5',
   '6': 'fake-key 6',
   '7': 'fake-key 7',
   '8': 'fake-key 8',
   '9': 'fake-key 9',
   '0': 'fake-key 0',

   # escape hatch
   '<ctrl-g>': ESC_BIND,
   '<Escape>': ESC_BIND,

   # userscripts
   '<ctrl-x>Y': 'hint links userscript ytdl',
   '<ctrl-x>y': 'spawn --userscript ytdl',

   '<ctrl-x>M': 'hint links userscript openmpv',
   '<ctrl-x>m': 'spawn --userscript openmpv',

   '<ctrl-x>nn': 'spawn --userscript nhentai_tools --download',
   '<ctrl-x>ne': 'spawn --userscript nhentai_tools --exists',
   '<ctrl-x>na': 'spawn --userscript nhentai_tools --add',
   '<ctrl-x>nr': 'spawn --userscript nhentai_tools --random',
   '<ctrl-1>'  : "spawn --userscript nhentai_tools '{url}' --add",

   '<ctrl-x>1': 'hint links userscript instacurrent',
   '<ctrl-x>2': 'hint --rapid links userscript instacurrent',
   '<ctrl-x>3': 'spawn --userscript instacurrent',
   '<ctrl-x>4': 'spawn -u instaall',
   '<ctrl-x>5': 'set-cmd-text --space :spawn -u instaloot --setdir',
   '<ctrl-x>6': ':spawn -u instaloot --cleardir',

   '<ctrl-x>g': 'open -t https://images.google.com/searchbyimage?image_url={clipboard}'

}

c.bindings.commands['normal']['<ctrl-m>'] = c.bindings.commands['normal']['<ctrl-x>M']

c.bindings.commands['normal'].update({'<alt-{}>'.format(i): 'tab-focus {}'.format(i) for i in range(1,10)})

c.bindings.commands['command'] = {
   '<ctrl-s>': 'search-next',
   '<ctrl-r>': 'search-prev',

   '<ctrl-k>': 'completion-item-focus prev',
   '<ctrl-j>': 'completion-item-focus next',

   '<alt-k>': 'command-history-prev',
   '<alt-j>': 'command-history-next',

   # escape hatch
   '<ctrl-g>': 'leave-mode',
   '<Escape>': 'leave-mode'
}

c.bindings.commands['hint'] = {
   # escape hatch
   '<ctrl-g>': 'leave-mode',
   '<Escape>': 'leave-mode'
}

c.bindings.commands['caret'] = {
   # escape hatch
   '<ctrl-g>': 'leave-mode',
   '<Escape>': 'leave-mode'
}

################################ bort med yt ad ###############################
yt_ad_js = 'Array.prototype.slice.call(document.getElementsByClassName("ytp-ad-overlay-slot")).map(x => x.style.display = "None")'
config.bind("<ctrl-x>a", "jseval -q {}".format(yt_ad_js))

############################# massa fake-bindings #############################
from string import ascii_lowercase
c.bindings.commands['normal'].update({"<ctrl-q>{}".format(l): "fake-key <ctrl-{}>".format(l) for l in ascii_lowercase})
c.bindings.commands['normal']['<ctrl-q><Escape>'] = "fake-key <Escape>"
