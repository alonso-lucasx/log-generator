# This script will gather 10 names from a website and add them to a text file.

import requests

response = requests.get('https://ledgernote.com/blog/interesting/best-flute-players-in-the-world/')

with open('Flute_html.txt', 'w') as file:
    file.write(response.text)
#The HTML code of the website is now stored on the Flute_html.txt file.

names = open('Names.txt', 'w') #Create Names.txt file, where the 10 names will be stored.

def create_namefile(html_file, names_file):
#Goes through each line of the Flute_html.txt file and gathers only the 10 names on the
#titles, adding them to the Names.txt file.        
    names = open(names_file, 'w')
    with open(html_file) as file:
        for linea in file.readlines():
            if "<h2>#" in linea:
                nombre = linea.split('</h2>')
                nombres = nombre[0][9:].strip()
                names.write(nombres + '\n')
                
                        
create_namefile('Flute_html.txt', 'Names.txt')
     
            
            
