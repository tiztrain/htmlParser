from html.parser import HTMLParser
import os

# setup project home folder
os.chdir(r'D:\Users\tizalien\PycharmProjects\htmlParser')
home_directory = os.getcwd()
print(home_directory)

# example of HTMLParser class
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


def main():

    # create HTMLParser object and test class with test data
    parser = MyHTMLParser()
    parser.feed('<html><head><title>Test</title></head>'
                '<body><h1>Parse me!</h1></body></html>')

    # read open file and read
    f = open(home_directory + r'\_in\aus_geoscience_services.html', 'r')
    print(f)
    contents = f.read()
    print(contents)


if __name__== '__main__':
    main()
