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


class TestMainFunction(unittest.TestCase):
    @patch("app.st")
    @patch("app.extract_text_from_pdf")
    @patch("app.load_dotenv")
    def test_main_with_pdf_file(self, load_dotenv_mock, extract_text_mock, st_mock):
        # Load the environment variable from .env file
        load_dotenv()

        # Mock the necessary objects and functions
        pdf_file_mock = Mock()
        extract_text_mock.return_value = "Fake extracted text"
        st_file_uploader_mock = st_mock.file_uploader
        st_file_uploader_mock.return_value = pdf_file_mock
        st_text_input_mock = st_mock.text_input 
        st_text_input_mock.return_value = "Fake user question"

        # Call the main function
        main()

        # Perform assertions on the mocked objects and functions
        load_dotenv_mock.assert_called_once()
        st_mock.set_page_config.assert_called_once_with(page_title="ASK YOUR PDF")
        st_mock.header.assert_called_once_with("ASK your PDF 💬")
        st_file_uploader_mock.assert_called_once_with("Upload your pdf", type="pdf")
        extract_text_mock.assert_called_once_with(pdf_file_mock) 
        st_text_input_mock.assert_called_once_with("Ask a question about your PDF:")


if __name__ == "__main__":
    unittest.main()

