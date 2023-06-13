import unittest
from unittest.mock import Mock, patch
from io import BytesIO
from app import extract_text_from_pdf, main
import os
from dotenv import load_dotenv

class TestPDFTextExtraction(unittest.TestCase):
    def test_extract_text_from_pdf(self):
        # Mock the PdfReader and pages
        pdf_reader_mock = Mock()
        pdf_reader_mock.pages = [
            Mock(extract_text=Mock(return_value="Page 1 text")),
            Mock(extract_text=Mock(return_value="Page 2 text")),
        ]

        # Mock the PdfReader initialization
        with patch("app.PdfReader", return_value=pdf_reader_mock):
            # Create a BytesIO object as a fake PDF file
            pdf_file = BytesIO(b"Fake PDF content")

            # Call the extract_text_from_pdf function
            extracted_text = extract_text_from_pdf(pdf_file)

        # Check that the extracted test matches the expected result
        expected_text = "Page 1 textPage 2 text"
        self.assertEqual(extracted_text, expected_text)   


if __name__ == "__main__":
    unittest.main()

