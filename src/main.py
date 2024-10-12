from lib.SubstitutionCipher import gen_substitution_mapping

def main():
    substitution_mapping = gen_substitution_mapping()

    # Print the substitution mapping
    print("Substitution Mapping:")
    for original, substituted in substitution_mapping.items():
        print(f"{original}: {substituted}")

if __name__ == "__main__":
    main()