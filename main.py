"""ca sert a quoi ?"""
#### Fonction secondaire

def ispalindrome(p):
    """
    Retourne
    Args:
    Returns:
    """
    t1 = str.maketrans("éèêëôÉÈÊËÔàâäÀÂÄçÇ",
                       "eeeeoeeeeoaaaaaacc")
    t2 = str.maketrans(",.;:?!-'", "        ")
    p = p.lower()
    p = p.translate(t1)
    p = p.translate(t2)
    p = p.replace(" ", "")

    reversed_p = p[::-1]
    print (reversed_p)
    if p == reversed_p:
        return True
    return False

#### Fonction principale

def main():
    """
    Retourne
    Args:
    Returns:
    """
    print(ispalindrome("Bbb"))

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor",
                "civique", "deifie","aaa"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
