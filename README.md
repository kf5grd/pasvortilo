# Pasvortilo

>Generate secure passwords which are unique to each system you use, and do not need to be memorized or written down.
<hr>

## Usage

>`$ pasvortilo [OPTIONS] SITE`
<hr>

## Installation

><pre>
>$ python setup.py
></pre>
<hr>

## Options

><pre>
>  -f, --format
>          Format string (%p = password, %s = site, Default: %p%s)
>          
>  -l, --length
>          Number of characters on each side of the punctuation character (Min: 4, Max: 18, Default: derived)
>
>  -p, --password
>          Base password used to salt the hash. Leave blank to be prompted at runtime
>          
>  -v, --verbose
>          Enable verbose output
>
>  --help
>          Show this message and exit.
></pre>

## Example

><pre>
>$ ./pasvortilo.py -p Passw0rd github.com
>7F001c4.A07b51c
></pre>
