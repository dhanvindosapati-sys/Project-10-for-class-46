
# ==================================
# MY ART GALLERY COLLECTION MANAGER
# Class 10 - Object-Oriented Programming
# ==================================

class ArtGallery:

    # STEP 1 - Parameterized Constructor
    def __init__(self, gallery_name, location):
        self.gallery_name = gallery_name
        self.location = location

        # Default attribute initialization
        self.artworks = []

        print(f"Welcome to {self.gallery_name}!")
        print(f"Location: {self.location}")
        print("Art gallery collection is ready.")

    # STEP 2 - Add artwork
    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print(f"'{artwork}' has been added to the gallery.")

    # STEP 3 - Remove artwork
    def remove_artwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print(f"'{artwork}' has been removed.")
        else:
            print(f"'{artwork}' was not found in the gallery.")

    # STEP 4 - Display all artworks
    def display_artworks(self):
        print(f"\n--- {self.gallery_name} Art Collection ---")

        if self.artworks:
            for number, artwork in enumerate(self.artworks, 1):
                print(f"{number}. {artwork}")
        else:
            print("No artworks have been added yet.")

    # STEP 5 - Destructor
    def __del__(self):
        print(f"Gallery '{self.gallery_name}' is closing. Goodbye!")


# Create the ArtGallery object
gallery = ArtGallery("Creative Canvas Gallery", "Bengaluru")


# STEP 6 - Menu-driven OOP program
while True:
    print("\n========= ART GALLERY MENU =========")
    print("1. Add Artwork")
    print("2. Remove Artwork")
    print("3. Display Art Collection")
    print("4. Delete & Quit")
    print("====================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        artwork = input("Enter artwork name: ")
        gallery.add_artwork(artwork)

    elif choice == "2":
        artwork = input("Enter artwork to remove: ")
        gallery.remove_artwork(artwork)

    elif choice == "3":
        gallery.display_artworks()

    elif choice == "4":
        del gallery
        break

    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")
