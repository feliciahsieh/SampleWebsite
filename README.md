# SampleWebsite

Code for sample website

## Table of Contents
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)

## Requirements
* Ubuntu (v14.04 LTS)
* Python (v3)
* Requests (python) module
* nginx

## Installation
```
git clone https://github.com/feliciahsieh/SampleWebsite.git
```

## Usage
The python3 script, compareHeader.py, will compare the HTTP Header info of two URLs provided by the user.
The script format is:

$ python3 compareHeader.py [URL1] [URL2]

```
$ python3 compareHeader.py http://198.41.215.162 http://www.cloudflare.com
```

Here's an example:

<p align="center"><img src="images/compareHeaders.png" width="800px" /></p>
