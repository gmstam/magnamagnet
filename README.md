# MagnaMagnet

Obtain a Magnet link for torrenting could be frustrating: 
- Close a lot of ads/popups
- Lots of redirects

MagnaMagnet is a simple Python script to search torrents from the popular website 1337x and get the magnet link in a fast way from command line.
The requests to 1337x are made by RequestsTor.

## Requirements

Python >= 3.10
Tor Browser opened and connected or, in alternative, for Linux users,
install the package following this guide:

https://support.torproject.org/it/apt/

Supported OS:
- Linux
- MacOS

Windows is not currently supported

## Usage 

Clone this repository and go into the folder of `magnamagnet`. Open a terminal inside the folder and run:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```sh
python3 magnamagnet.py -k 'terminator' 
```

Results of the first page will be displayed in a table.


```
+--------+------------------------------------------------------------------------+-------+------+-----------+
| choice | name                                                                   |   se  |  le  | size info |
+--------+------------------------------------------------------------------------+-------+------+-----------+
|   0    | Terminator: Dark Fate (2019) [WEBRip] [1080p] [YTS] [YIFY]13           | 10132 | 3680 |    2.2 GB |
|   1    | Terminator: Dark Fate (2019) [WEBRip] [720p] [YTS] [YIFY]7             |  6969 | 2416 |    1.1 GB |
|   2    | Terminator: Dark Fate (2019) [BluRay] [1080p] [YTS] [YIFY]5            |  5923 | 1797 |    2.2 GB |
|   3    | Terminator: Dark Fate (2019) [BluRay] [720p] [YTS] [YIFY]6             |  4748 | 1520 |    1.1 GB |
|   4    | Terminator Dark Fate.2019.HDRip.XviD.AC3-EVO[TGx] ⭐18                 |  2973 | 963  |    1.3 GB |
|   5    | Terminator.Dark.Fate.2019.720p.WEBRip.900MB.x264-GalaxyRG ⭐18         |  1915 | 573  |  897.1 MB |
|   6    | Terminator.Dark.Fate.2019.1080p.WEB-DL.DD5.1.x264-CMRG[TGx] ⭐17       |  1232 | 364  |    6.1 GB |
|   7    | Terminator.Dark.Fate.2019.1080p.WEBRip.x264-RARBG1                     |  1133 | 834  |    2.4 GB |
|   8    | Terminator: Dark Fate (2019) [2160p] [4K] [BluRay] [5.1] [YTS] [YIFY]4 |  841  | 336  |    4.2 GB |
+--------+------------------------------------------------------------------------+-------+------+-----------+
Press a key from 0 to 8 to select a torrent. (CTRL + C to exit)
```

You can select the desiderd torrent by pressing from 0 to the N-result.
The magnet link will be printed in the console.

## Bug

The script is tested on MacOS Sonoma and Ubuntu 24.04.
Please feel free to report issues or contribute to this script with a pull request

### Build Executable

```sh
pyinstaller --onefile --collect-all pyfiglet run.py
```

## Troubleshooting

### ConnectionRefusedError: [Errno 61] Connection refused

Just open TorBrowser and click `Connect`
