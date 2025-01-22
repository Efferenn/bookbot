
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    world_count = len(file_contents.split())
    l_dictionary = {"a":0, "b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0," ":0}
    lower = file_contents.lower()
    for count in l_dictionary:
        l_dictionary[count] = lower.count(count)

    #print(l_dictionary)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{world_count} words in this document" )
    for char in l_dictionary:
        if char != " ":
            print(f"The '{char}' character was found {l_dictionary[char]} times")

    print("--- End report ---")
    return l_dictionary, world_count
    


main()

