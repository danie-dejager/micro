module github.com/zyedidia/micro/v2

require (
	github.com/blang/semver v3.5.1+incompatible
	github.com/dustin/go-humanize v1.0.0
	github.com/go-errors/errors v1.0.1
	github.com/kballard/go-shellquote v0.0.0-20180428030007-95032a82bc51
	github.com/mattn/go-isatty v0.0.20
	github.com/mattn/go-runewidth v0.0.7
	github.com/mitchellh/go-homedir v1.1.0
	github.com/sergi/go-diff v1.1.0
	github.com/stretchr/testify v1.4.0
	github.com/yuin/gopher-lua v1.1.1
	github.com/zyedidia/clipper v0.1.1
	github.com/zyedidia/glob v0.0.0-20170209203856-dd4023a66dc3
	github.com/zyedidia/json5 v0.0.0-20200102012142-2da050b1a98d
	github.com/zyedidia/tcell/v2 v2.0.10
	github.com/zyedidia/terminal v0.0.0-20230315200948-4b3bcf6dddef
	golang.org/x/text v0.3.8
	gopkg.in/yaml.v2 v2.2.8
	layeh.com/gopher-luar v1.0.11
)

require (
	github.com/creack/pty v1.1.18 // indirect
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/gdamore/encoding v1.0.0 // indirect
	github.com/lucasb-eyer/go-colorful v1.0.3 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	github.com/rivo/uniseg v0.1.0 // indirect
	github.com/xo/terminfo v0.0.0-20200218205459-454e5b68f9e8 // indirect
	github.com/zyedidia/poller v1.0.1 // indirect
	golang.org/x/sys v0.6.0 // indirect
)

replace github.com/kballard/go-shellquote => github.com/zyedidia/go-shellquote v0.0.0-20200613203517-eccd813c0655

replace github.com/mattn/go-runewidth => github.com/zyedidia/go-runewidth v0.0.12

replace layeh.com/gopher-luar v1.0.11 => github.com/layeh/gopher-luar v1.0.11

go 1.17
