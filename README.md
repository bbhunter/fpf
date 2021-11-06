<p align="center"><img src="https://github.com/whoamisec75/fpf/blob/main/static/fpf_logo.jpg"/></p>

<h1 align="center">Fast Pattern Fetcher (fpf)</h1>
<i><b><p align="center">Coded with <3 by HS Devansh Raghav</p></b></i>

`Fast Pattern Fetcher`, Takes a URLs list and outputs the URLs which contains the parameters according to the specified pattern.

* fpf/ <= ***Folder***
  * main.py <= ***It's a file that calls all the functions and runs the fetcher with threads.*** 
  * init.py <= ***Common file.***
  * scripts/ <= ***Folder.***
    * init.py <= ***Common file.***
    * fetcher.py <= ***Matches the URL parameters to db/db.py parameters.*** 
    * colors.py <= ***Colors and Style.***
    * args.py <= ***Arguments for this tool.***
  * db/ <= ***Folder***
    * db.py <= ***This file contains list of parameters.*** 
    * init.py <= ***Common file.***
  * static/ <= ***Folder***
    * fpf_logo.jpg <= ***Logo.***
* .gitignore <= ***.gitingnore file for python.***
* setup.py <= ***setup file for this tool.***
* LICENCE <= ***MIT licence***
* README.md <= ***Tool discription, installation, usage etc.***

## Installation

```
$ git clone https://github.com/whoamisec75/fpf.git
$ cd fpf
$ sudo python3 setup.py install
$ fpf -h
```
Before running these commands make sure that you have python3 and setuptools installed. 

## Usage

You can use this tool like this:
```
$ fpf [URLs file] [Pattern] 
```

For example:
```
$ fpf urls.waybackurls xss
```

## Arguments

|Args             | Discription                          |
|-----------------|--------------------------------------|
| file            |Specify the file which contains URLs  |   
| Pattern         |Specify the pattern                   |
| -c/--concurrency|Specify the concurrency, default is 20|

## Patterns

These are all available patterns:

* db/
  * db.py
    * xss_patterns
    * ssti_patterns
    * ssrf_patterns
    * sqli_patterns
    * lfi_patterns
    * rce_patterns
    * idor_patterns
    * redirect_patterns

## How to use patterns?

Finding `Cross-site scripting (XSS)` parameters using `xss` pattern:

```
$ fpf urls.waybackurls xss
```
Finding `SQLi` parameters using `sqli` pattern:

```
$ fpf urls.waybackurls sqli
```
Finding `Server side request forgery (SSRF)` parameters using `ssrf` pattern:

```
$ fpf urls.waybackurls ssrf
```
Finding `Local File inclusion (LFI)` parameters using `lfi` pattern:

```
$ fpf urls.waybackurls lfi
```
Finding `Remote code execution (RCE)` parameters using `rce` pattern:

```
$ fpf urls.waybackurls rce
```
Finding `Insecure direct object references (IDOR)` parameters using `idor` pattern:

```
$ fpf urls.waybackurls idor
```
Finding `Open redirect` parameters using `redirect` pattern:

```
$ fpf urls.waybackurls redirect
```
Finding `Server side template injection (SSTI)` parameters using `ssti` pattern:

```
$ fpf urls.waybackurls ssti
```






