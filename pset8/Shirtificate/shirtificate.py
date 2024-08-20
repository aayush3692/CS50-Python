from fpdf import FPDF

class Shirtificate:
    def __init__(self, name):
        self.name = name
        self.generate()  # Generate the PDF immediately upon initialization

    @classmethod
    def get(cls):
        name = input("Name: ").strip()  # Prompt user for their name and remove leading/trailing spaces
        return cls(name)  # Create an instance of Shirtificate with the provided name

    def generate(self):
        pdf = FPDF()  # Create a new PDF object
        pdf.add_page()  # Add a new page to the PDF
        pdf.set_auto_page_break(auto="False", margin=0)  # Disable automatic page breaks

        # Set the font to Helvetica, bold, size 50
        pdf.set_font("Times", "B", 50)
        # Add a centered title "CS50 Shirtificate" at the top of the page
        pdf.cell(0, 50, txt="CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

        # Insert an image (e.g., shirtificate.png) positioned at (x=5, y=80) with a width of 200
        pdf.image("shirtificate.png", x=5, y=80, w=200)

        # Change the font to Helvetica, bold, size 30
        pdf.set_font("Times", "B", size=30)
        # Set the text color to white (RGB: 255, 255, 255)
        pdf.set_text_color(255, 255, 255)
        # Add the student's name with the text "took CS50" centered near the bottom of the page
        pdf.cell(0, 180, align="C", txt=f"{self.name} took CS50")

        # Save the PDF to a file named "shirtificate.pdf"
        pdf.output("shirtificate.pdf")

def main():
    Shirtificate.get()  # Prompt the user for their name and generate the shirtificate

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly
