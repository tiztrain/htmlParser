from html.parser import HTMLParser
import urllib.request
import os

# setup project home folder
os.chdir(r'D:\Users\tizalien\PycharmProjects\htmlParser')
home_directory = os.getcwd()
print(home_directory)


# example of HTMLParser class
class MyHTMLParser(HTMLParser):

    # this function will extract the the details I require
    def handle_starttag(self, tag, attrs):

        # # print statements to be able to break down the html code
        # """print the tag"""
        # print("Encountered a start tag     :", tag)

        """print the attributes in the tag"""
        for attr in attrs:
            # for testing what attributes are included in the tag and testing splitting them up

            # print("                         attr:", attr)
        #     print("                         attr1:", attr[0])
        #     print("                         attr2:", attr[1])

            # """ THIS CODE EXTRACTS THE TITLE FOR THE WEBSERVICE"""
            # # TODO import the data tag into this function somehow
            # if tag == 'div' and attr[1] == 'tileTitle':
            #     print(self.handle_data(data))

            # THIS CODE EXTRACTS THE WEB SERVICES LINKS
            # lines with the tag 'a' and the attribute 'href' are the web service links
            if tag == "a" and attr[0] == 'href':
                # print(attr[1])
                # if the link contains '?' it and everything to the right of it will be removed
                if '?' in attr[1]:
                    ws_link = attr[1][:attr[1].find('?')]
                    # print(ws_link)
                    # casefold() is used to state that it does not matter what case the string is in
                    if 'server' in ws_link.casefold():
                        print(ws_link)

    """ not needed yet but maybe for extracting titles and other attributes"""

    # def handle_endtag(self, tag):
    #     print("Encountered an end tag      :", tag)
    #
    # def handle_data(self, data):
    #     print("Encountered some data       :", data)


    #
    # def handle_startendtag(self, tag, attrs):
    #     print("Encountered a joined tag    :", tag)
    #
    # NONE PICKED UP
    # def handle_entityref(self, name):
    #     print("Encountered entity reference:", name)
    #
    # def unknown_decl(self, data):
    #     print("Unrecognised declaration    :", data)




def testData():
    # TEST OPTIONS

    # simple test
    # result = '<html><head><title>Test</title></head>'' \
    #         ''<body><h1>Parse me!</h1></body></html>'

    # CHOOSE ONE real online html test
    f = urllib.request.urlopen('http://services.ga.gov.au/')
    # f = urllib.request.urlopen(
    #     'http://spatialservices.finance.nsw.gov.au/mapping_and_imagery/lpi_web_services/access_lpi_web_services')
    result = str(f.read())

    return result



def main():

    # create HTMLParser object
    parser = MyHTMLParser()
    parser.feed(testData())



if __name__== '__main__':
    main()
