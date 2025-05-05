# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="Certificate of Achievement", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""This is to certify that

Sunny Rajput

has successfully completed the requirements and demonstrated the knowledge and skills necessary to be recognized as a
Certified Diet and Nutrition Specialist.

Awarded on April 19, 2025

Presented by:

Dr. Amelia Hart
Director of Health Programs
Global Institute of Nutrition & Health Sciences

Signature: ___________________
""")

pdf.output("Certificate_of_Diet_and_Nutrition_Specialist_Sunny_Rajput.pdf")
