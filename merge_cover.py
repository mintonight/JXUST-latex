"""Convert the Word cover page to PDF and merge it with the thesis PDF."""
import subprocess
import sys
import os

def doc_to_pdf(doc_path, out_dir):
    """Use Microsoft Word (via win32com) to convert .doc to .pdf in out_dir."""
    import win32com.client

    doc_path = os.path.abspath(doc_path)
    pdf_name = os.path.splitext(os.path.basename(doc_path))[0] + ".pdf"
    pdf_path = os.path.join(out_dir, pdf_name)

    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    try:
        doc = word.Documents.Open(doc_path)
        doc.SaveAs(os.path.abspath(pdf_path), FileFormat=17)  # 17 = wdFormatPDF
        doc.Close()
    finally:
        word.Quit()

    return pdf_path


def merge_pdfs(cover_pdf, thesis_pdf, output_pdf):
    """Merge cover PDF + thesis PDF using pdfunite."""
    subprocess.run(
        ["pdfunite", cover_pdf, thesis_pdf, output_pdf],
        check=True,
    )


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(base_dir, "output")
    os.makedirs(out_dir, exist_ok=True)

    cover_doc = os.path.join(base_dir, "附件6.本科毕业设计（论文）封面和封底.doc")
    thesis_pdf = os.path.join(out_dir, "thesis_template.pdf")
    final_pdf = os.path.join(out_dir, "final_thesis.pdf")

    if not os.path.exists(cover_doc):
        print(f"[SKIP] Cover file not found: {cover_doc}")
        sys.exit(0)

    if not os.path.exists(thesis_pdf):
        print(f"[SKIP] Thesis PDF not found: {thesis_pdf}")
        sys.exit(1)

    print("Converting cover page Word to PDF ...")
    cover_pdf = doc_to_pdf(cover_doc, out_dir)
    print(f"  -> {cover_pdf}")

    print("Merging cover + thesis PDF ...")
    merge_pdfs(cover_pdf, thesis_pdf, final_pdf)
    print(f"  -> {final_pdf}")


if __name__ == "__main__":
    main()
