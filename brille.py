#!/usr/bin/env python3 -tt
import argparse, sys, re, time, subprocess

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Source file where text is to be tested against regular expression.")
parser.add_argument("regex", help="Regex pattern to test, in single quotes.")

args = parser.parse_args()
f, rx = args.file, args.regex

def main():
    subprocess.Popen(["clear"])
    time.sleep(1)
    print("\n     _               _    _          \n    ( )           _ (_ ) (_ )        \n    | |_    _ __ (_) | |  | |    __  \n    | '_`\ ( '__)| | | |  | |  /'__`\\\n    | |_) )| |   | | | |  | | (  ___/     _  _     _ \n    (_,__/'(_)   (_)(___)(___)`\____)    | |(_)|_|| |\n\n    bril·​le | \\\'bri-lə\\\n    \x1B[3mplural\x1B[23m \033[1;33mbrilles\033[1;m\n    Definition of \x1B[3mbrille\x1B[23m: a transparent, disc-shaped, immobile scale that covers the eye of most snakes and geckos\n\n\n")
    lineno = 0
    if rx.startswith('\'') and rx.endswith('\''):
        r = rx[1:-1]
        pattern = str(re.sub(r"([^\\])\\([^\\])([^\\]*)", r"\1 literal '\2', \3,", r))
        pattern = pattern.replace('\\A',' beginning of a string (not internal line); ').replace('\\b',' zero-width boundary between A-Za-z0-9_ and either non-A-Za-z0-9_ or an edge; ').replace('\\D',' non-digit; ').replace('\\d',' digit; ').replace('\\S',' non white-space character; ').replace('\\s',' whitespace character; ').replace('\\W',' non-alphanumeric character excluding underscore; ').replace('\\w',' A-Za-z, digit or underscore; ').replace('\\z',' end of a string but not internal line; ').replace('[^',' negated character set; ').replace('^',' beginning of pattern; ').replace('$',' end of pattern; ').replace('(','').replace(')',' grouped; ').replace('[','').replace(']',' character set; ').replace('*?',' non-greedy; ').replace('+?',' non-greedy; ').replace('*',' zero or more times; ').replace('+',' one or more times; ').replace('+?',' (optional); ').replace('|',' or ').replace(',  (optional)',' (optional)')
        pattern = str(re.sub(r"([^'])\.([^'])", r"\1  any character except newline, \2,", pattern))
        pattern = str(pattern.replace("  "," ").replace("; one"," one").replace("; zero"," zero").replace("', ","'; ").replace("; ,",";")).strip().strip(";")
        corpat = input('  ---- Expanding regular expression... ---------------------------\n  > The regex pattern provided will match the following pattern structure:\n        {}\n\n  > Do you wish to continue? Y/n '.format(pattern))
        if corpat != 'n':
            time.sleep(1)
            with open(f) as fin:
                print('\n\n  ---- Validating regular expression... ---------------------------\n  > Validating regex \'{}\' through \'{}\'...'.format(r, f))
                lines = fin.readlines()
                if len(lines) > 0:
                    for line in lines:
                        results, lineno = re.findall(r, line), lineno+1
                        time.sleep(1)
                        if len(results) > 0:
                            print('\n    > Regular expression pattern: \'{}\' identified the following results for line {}:'.format(r, lineno))
                            for result in results:
                                print('     > '+str(result))
                            time.sleep(1)
                        else:
                            pass
                    print('\n\n\n  > brille completed successfully.\n\n')
                else:
                    print('\n\n\n  > brille found no matching regex patterns and/or the file is empty.\n  > Please try again.\n\n')
        else:
            print('\n\n\n  > brille will not continue, please provide an alternative regex.\n\n')
            sys.exit()
    else:
        print('  > regex must be wrapped in double and single quotes, such as \"\'r[eg]?ex\'\"\n  > Please try again.\n\n')
        sys.exit()

if __name__ == '__main__':
	main()