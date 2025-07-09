from fpdf import FPDF

# Function to clean Unicode characters not supported by Latin-1
def clean_text(text):
    return (text.replace("–", "-")
                .replace("→", "->")
                .replace("“", '"')
                .replace("”", '"')
                .replace("’", "'"))

# Custom PDF class with Unicode-safe setup
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Python List vs Tuple - Complete Guide", ln=True, align='C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", 'B', 12)
        self.set_text_color(0)
        self.cell(0, 10, clean_text(title), ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", '', 11)
        self.multi_cell(0, 8, clean_text(body))
        self.ln()

# Create PDF
pdf = PDF()
pdf.add_page()

# Content for the PDF (same as before but kept as-is, clean_text will sanitize)
content = {
    "Definition": """
List and Tuple are Python data structures used to store multiple items.

- List: [1, 2, 3] → Mutable (can change)
- Tuple: (1, 2, 3) → Immutable (cannot change)
""",
    "Comparison Table": """
| Feature        | List                | Tuple               |
|----------------|---------------------|----------------------|
| Syntax         | [1, 2, 3]           | (1, 2, 3)            |
| Mutable        | Yes                 | No                   |
| Memory usage   | Higher              | Lower                |
| Speed          | Slower              | Faster               |
| Methods        | Many (append, pop)  | Few (count, index)   |
| Dict Key Usage | No                  | Yes                  |
""",
    "Mutability Example": """
List (Mutable):
my_list = [1, 2, 3]
my_list.append(4)  # Works

Tuple (Immutable):
my_tuple = (1, 2, 3)
my_tuple[0] = 10   # Error!
""",
    "Why Tuple is Faster": """
Tuples are faster because:
- Fixed size (no dynamic resizing)
- Fewer operations to support
- More memory efficient

Tuples help optimize performance where data is fixed.
""",
    "Memory Check Example": """
import sys

a = [1, 2, 3]
b = (1, 2, 3)

print(sys.getsizeof(a))  # List memory
print(sys.getsizeof(b))  # Tuple memory
""",
    "When to Use What": """
Use List:
- When you need to change, add, or remove items
- For dynamic data (e.g., user input)

Use Tuple:
- When data is fixed (coordinates, DB rows)
- As dictionary keys (immutable & hashable)
""",
    "Overwriting Concept": """
a = [1, 2, 3]
a = (1, 2, 3)  # List is overwritten by tuple

print(type(a))  # Output: <class 'tuple'>
""",
    "Summary": """
- List: Mutable, slower, uses more memory
- Tuple: Immutable, faster, uses less memory
- Use list for dynamic data, tuple for fixed data
- Variable can be overwritten if reused
"""
}

# Add content to PDF
for title, body in content.items():
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Output file path (update if needed)
pdf_output_path = r"D:\DATA_Science_Master\Python\01_Basic\Notes_ChatGPT\List_vs_Tuple_Comparison_Guide.pdf"
pdf.output(pdf_output_path)

print(f"✅ PDF created successfully at: {pdf_output_path}")
