from contents.babynames import BabyNames


def main():
    """
    Main function to execute the tests for the BabyNames class.

    """
    # Instance of the BabyNames class
    baby_names = BabyNames()

    # Test for the m_f_names method
    print("Testing m_f_names method...")
    baby_names.m_f_names()
    print("m_f_names method tested successfully.\n")

    # Test for the most_popular_ever method
    print("Testing most_popular_ever method...")
    baby_names.most_popular_ever()
    print("most_popular_ever method tested successfully.\n")

    # Test for the unisex method
    print("Testing unisex method...")
    baby_names.unisex()
    print("unisex method tested successfully.\n")

    # Test for the unisex_evolution method

    print("Testing unisex_evolution method...")
    try:
        baby_names.unisex_evolution()
    except Exception as e:
        print(f"An error occurred during unisex_evolution method testing: {e}")
    else:
        print("unisex_evolution method tested successfully.\n")


if __name__ == "__main__":
    main()
