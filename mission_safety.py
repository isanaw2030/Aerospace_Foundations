try :
    def collect_stats():
        name = input("Enter name of a rocket : ").strip()
        return(name)


    def is_meaningful_name(name):
        name_lower = name.lower()
        
        # reject short names

        if len(name_lower) < 3:
            return False

        # rejects pure digits

        if name_lower.isdigit():
            return False

        # accept classic structured names (Falcon, Saturn-v, Mk-18)
        # if it contains a hyphen and atleast one letter, is highly likely valid

        if "-" in name_lower and any(char.isalpha() for char in name_lower):
            return True

        # rejects random keyboards smashes (kjhb, fghd ) by checking vowels

        vowels = "aeiouy"
        has_vowels = any(char in vowels for char in name_lower)

        if not has_vowels:
            return False

        return True

        
    def is_collect_stats():
        rocket = collect_stats()

        while rocket == "" or not is_meaningful_name(rocket):
            print("Please enter a meaningful name")
            print("Avoid simple numbers/letters (kjhg, 1, 2f)")
            rocket = collect_stats()
        return rocket
        
    

except:
    def print_error():
        return ("Error!")
    


      
