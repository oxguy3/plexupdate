# plexupdate
A little command-line tool for downloading Plex updates. Simply run the script to download the latest binary for Plex Media Server into your current directory. It also supports automatic checksum validation and downloading Plex Pass-exclusive versions.

## Installation
To use plexupdate, you must have Python 3.* installed with pip.

1. Clone or download this repository somewhere on your server. If you use the "Download ZIP" button on GitHub, be sure to unzip it.
1. Run `pip3 install -r requirements.txt`.
    * On some systems, you might have to write `pip` instead of `pip3`. You can make sure that you're using pip for Python 3 (not Python 2) using `pip --version`.
1. Make plexupdate.py executable (`chmod +x plexupdate.py`) and move it to somewhere on your path (e.g. `/usr/local/bin/plexupdate`).
1. Create your config.json file (see below).
1. Run `plexupdate` to download the latest version of PMS!

## Configuration
Create a config file in one of the following places:
* Linux: `~/.local/share/plexupdate/config.json`
* Mac: `~/Library/Application Support/plexupdate/config.json`
* Windows: `C:\Users\<User>\AppData\Local\Hayden Schiff\plexupdate\config.json`

(If you're having trouble figuring out where your config should go, please see the docs for the [appdirs](https://pypi.org/project/appdirs/) module.)

To create your config.json file, start with the following template:
```
{
    "token": "",
    "distro": "debian",
    "build": "linux-x86_64",
    "enableChecksum": true,
    "enablePlexpass": true
}
```
Use a text editor to change these values to your liking. Here is a brief explanation of each option:
* __token__: Your X-Plex-Token (see [Plex's help docs](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/) if you don't know how to get this). If you don't need Plex Pass downloads, you can leave this blank.
* __distro__: An ID for the operating system or distro you wish to download for (see list of options below).
* __build__: An ID for the build to download (see list of options below).
* __enableChecksum__: Should the script validate the SHA-1 checksum of the downloaded file? (can't think of a good reason you'd disable this but whatever floats your boat)
* __enablePlexpass__: Should the script download Plex Pass-exclusive binaries? If you don't have a valid `token` from a subscriber account, turning this option on won't work.

### Distro and build values
Here is a list of all possible combinations of distro and build (at time of writing). These values were extracted from <https://plex.tv/api/downloads/5.json>.

| OS | `distro` | `build` |
|---|---|---|
| Windows | windows | windows-x86 |
| macOS | macos | darwin-x86_64 |
| Linux: Ubuntu (16.04+) / Debian (8+) - Intel/AMD 32-bit | debian | linux-x86 |
| Linux: Ubuntu (16.04+) / Debian (8+) - Intel/AMD 64-bit | debian | linux-x86_64 |
| Linux: Ubuntu (16.04+) / Debian (8+) - ARMv8 | debian | linux-aarch64 |
| Linux: Ubuntu (16.04+) / Debian (8+) - ARMv7 | debian | linux-armv7hf_neon |
| Linux: Fedora (27+) / CentOS (7+) / SUSE (15+) - Intel/AMD 32-bit | redhat | linux-x86 |
| Linux: Fedora (27+) / CentOS (7+) / SUSE (15+) - Intel/AMD 64-bit | redhat | linux-x86_64 |
| FreeBSD: 64-bit | freebsd | freebsd-x86_64 |
| Synology: Intel 32-bit (x10 Series, DS415play, and DS214play) | synology | linux-x86 |
| Synology: Intel 64-bit (DSM 6.0 and newer) | synology | linux-x86_64 |
| Synology: ARMv8 (x18 Series) | synology | linux-aarch64 |
| Synology: ARMv7 (x13 Series, x14 Series (excluding DS414j), DS115j, RS815, and DS216se) | synology | linux-armv7hf |
| Synology: ARMv7 (x15 Series (excluding DS115j and RS815), x16 Series (excluding DS216se), x17 Series, x18 Series, and DS414j) | synology | linux-armv7hf_neon |
| Netgear: Intel 64-bit | netgear | linux-x86_64 |
| Netgear: ARMv7 | netgear | linux-armv7sf |
| Netgear: ARMv7 (RN2xx Series) | netgear | linux-armv7hf_neon |
| QNAP: Intel/AMD 64-bit (QTS-4.3 and newer) | qnap | linux-x86_64 |
| QNAP: ARMv8 (TS-x28, and TS-x32 Series) | qnap | linux-aarch64 |
| QNAP: ARMv7 (TS-x31, and TS-x31U Series) | qnap | linux-armv7sf |
| QNAP: ARMv7 (TS-x31+, TS-x31P, TS-x31P2, TS-x31X, and TS-x31XU Series) | qnap | linux-armv7hf_neon |
| unRAID: 64-bit | unraid | linux-x86_64 |
| Drobo | drobo | linux-armv7sf |
| ASUSTOR: Intel 32-bit | asustor | linux-x86 |
| ASUSTOR: Intel 64-bit | asustor | linux-x86_64 |
| ASUSTOR: ARMv8 | asustor | linux-aarch64 |
| ASUSTOR: ARMv7 | asustor | linux-armv7hf_neon |
| Seagate: Intel 64-bit | seagate | linux-x86_64 |
| Seagate: ARMv7 | seagate | linux-armv7hf |
| Western Digital: My Cloud DL2100 | wd-dl2100 | linux-x86_64 |
| Western Digital: My Cloud DL4100 | wd-dl4100 | linux-x86_64 |
| Western Digital: My Cloud PR2100 | wd-pr2100 | linux-x86_64 |
| Western Digital: My Cloud PR4100 | wd-pr4100 | linux-x86_64 |
| Western Digital: My Cloud EX2 | wd-ex2 | linux-armv7sf |
| Western Digital: My Cloud EX2100 | wd-ex2100 | linux-armv7sf |
| Western Digital: My Cloud EX2 Ultra | wd-ex2ultra | linux-armv7sf |
| Western Digital: My Cloud EX4100 | wd-ex4100 | linux-armv7sf |
| Western Digital: My Cloud Mirror | wd-mirror | linux-armv7sf |
| Western Digital: My Cloud Mirror Gen2 | wd-mirrorgen2 | linux-armv7sf |

## License
MIT License

Copyright (c) 2020 Hayden Schiff

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
