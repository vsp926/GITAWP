from translate import Translator

# translator = Translator(to_lang="ja")
# with open('my_file.txt') as my_file:
#     content=my_file.readlines()
    
# for i in content:
#     print(translator.translate(i))

    
#Function to display the available languages and choose a language


def display_languages():
    languages = {
        "en":"English",
        "es":"Spanish",
        "fr":"French",
        "hi":"Hindi",
        "ja":"Japanees",
        "te":"Telugu",
        "zh":"Chinese"   
    }
    print("\tCode\t Language\n")
    for code,language in languages.items():
        print("\t{}\t{}".format(code,language))

def translate_text(code,text):
    #code = "ja"
    translation = Translator(to_lang=code,from_lang="autodetect")
    print(translation.translate(text))


def main():
    print(" Right Now the System Supports the Following Languages: \n")
    display_languages()
    print("Please Enter a language Code: ")
    code = input()
    print("Awesome, Now enter the text which you would like to translate : ")
    text = input()
    translate_text(code,text)
    
if __name__=="__main__":
    main()