import vobject
from optparse import OptionParser
from bs4 import BeautifulSoup
import os.path

print("=== Facebook_to_vcf ver 1.0 ===")
print("Import facebook data, and outputs a vCard contact file")
print("Use -h for help")

parser = OptionParser()
parser.add_option("-i", "--facebookloc", dest="input_filename",
                  help="Facebook input .html file", metavar="FILE")
parser.add_option("-o", "--vcardloc", dest="output_filename",
                  help="vCard output file", metavar="FILE")

(options, args) = parser.parse_args()

if(options.input_filename == None):
    print("ERROR:")
    print("Please specify an input filename !")
    quit()
if(options.output_filename == None):
    print("ERROR:")
    print("Please specify an output filename !")
    quit()
with open(options.input_filename, 'r') as raw_input_data:
    soup = BeautifulSoup(raw_input_data, "lxml")
    table = soup.table # gets the first table content
                       # in the HTML file, which is the contacts list

    contacts = {}
    for i in range(1, len(table.contents)):
        name = table.contents[i].td.contents[0]
        number = table.contents[i].li.contents[0][9:]
        contacts[name] = number

    print( "Facebook have knowledge of {} contacts".format(len(contacts)) )

    output_string = str()
    for nom in contacts:
        output_vcard = vobject.vCard()

        output_vcard.add('fn')
        output_vcard.fn.value = nom
        output_vcard.add('tel')
        output_vcard.tel.value = contacts[nom]

        output_string += output_vcard.serialize()
    with open(options.output_filename, 'w') as output_file:
        output_file.write(output_string)
        print("Succesfully saved contacts to : {} ".format(options.output_filename))
