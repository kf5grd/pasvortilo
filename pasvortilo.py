#!/usr/bin/python

import click
import hashlib

# check if s is an integer
def check_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# hash to_enc into md5
def md5_enc(to_enc):
    m = hashlib.md5()
    m.update(to_enc.encode('utf-8'))
    return m.hexdigest()

# apply custom formatting based on format_string
def format_str(password, site, format_string):
    # %s = site
    # %p = password
    s = format_string.replace('%s',site)
    p = s.replace('%p',password)
    return p

# derive length from the last digit in the hash over 3
# or default to 8 if none found
def derive_length(md5_string):
    for c in reversed(md5_string):
        if check_int(c) and int(c) >= 4:
            return int(c)
            break
    return 8

# generate password based on md5_string, length, and punct_mark
def genpw(md5_string, length, punct_mark):
    i=0
    uc_count=0
    pwbuff=''
    for c in md5_string:
        if i == length:
            pwbuff = pwbuff + punct_mark
            i+=1
            uc_count=0
        elif i == (length*2)+1:
            break
        else:
            if c.isalpha() == True and uc_count == 0:
                c = c.upper()
                uc_count=1
            pwbuff = pwbuff + c
            i+=1
    return pwbuff

@click.command()
@click.argument('site', required=1)
@click.option('--format', '-f',
              default='%p%s',
              help='Format string (%p = password, %s = site, Default: %p%s)')
@click.option('--length', '-l',
              type=click.IntRange(4,18),
              help='Number of characters on each side of the punctuation character (Min: 4, Max: 18, Default: derived)')
@click.option('--password', '-p',
              prompt=True,
              hide_input=True,
              confirmation_prompt=True,
              help='Base password used to salt the hash. Leave blank to be prompted at runtime')
@click.option('--verbose', '-v',
              is_flag=True,
              help='Enable verbose output')
def cli(password, site, format, length, verbose):
    """Generate secure passwords which are unique to each system you use, and do not need to be memorized."""
    xmd5 = md5_enc(format_str(password,site,format))
    length_derived = False

    if not length:
        length = derive_length(xmd5)
        length_derived = True

    print(genpw(xmd5, length, "."))

    if verbose:
        print("")
        print("MD5:    %s" % xmd5)
        print("Format: %s" % format)
        print("Length: %d, Derived: %s" % (length, str(length_derived)))

if __name__ == "__main__":
    cli()
