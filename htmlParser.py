from html.parser import HTMLParser
import os

# setup project home folder
os.chdir(r'D:\Users\tizalien\PycharmProjects\htmlParser')
home_directory = os.getcwd()
print(home_directory)

# example of HTMLParser class
class MyHTMLParser(HTMLParser):

    # this function will extract the web map service
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag     :", tag)
        for attr in attrs:
            print("                         attr:", attr)
            print("                         attr1:", attr[0])
            print("                         attr2:", attr[1])
            if tag == "a" and attr[0] == 'href':
                print("**************************************************************************")


    def handle_endtag(self, tag):
        print("Encountered an end tag      :", tag)

    def handle_data(self, data):
        print("Encountered some data       :", data)

    def handle_startendtag(self, tag, attrs):
        print("Encountered a joined tag    :", tag)

    # NON PICKED UP
    # def handle_entityref(self, name):
    #     print("Encountered entity reference:", name)
    #
    # def unknown_decl(self, data):
    #     print("Unrecognised declaration    :", data)


def testData(input):
    # test data options
    # result = '<html><head><title>Test</title></head>'' \
    #         ''<body><h1>Parse me!</h1></body></html>'
    result = input
    return result



def main():

    # read open file and read
    f = open(home_directory + r'\_in\aus_geoscience_services.html', 'r')
    contents = f.read()
    # # print(contents)
    # testData(contents)

    # create HTMLParser object
    parser = MyHTMLParser()
    parser.feed(testData(contents))



if __name__== '__main__':
    main()
