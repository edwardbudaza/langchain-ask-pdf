 
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


def extract_text_from_pdf(pdf):
    """
    Extracts text from a PDF file.

    Args:
        pdf (File): The PDF file to extract text from.

    Returns:
        str: Extracted text from the PDF.
    """
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def main():
    load_dotenv()
    st.set_page_config(page_title="ASK YOUR PDF")
    st.header("ASK your PDF 💬")

    # Upload file
    pdf = st.file_uploader("Upload your pdf", type="pdf")

    # Extract the text from the PDF
    if pdf is not None:
        text = extract_text_from_pdf(pdf)

        # Split the text into chunks that overlap
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        # Create embeddings from the chunks to form our knowledge base
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # Ask user's question
        user_question = st.text_input("Ask a question about your PDF:")

        if user_question:
            # Perform similarity search in the knowledge base
            docs = knowledge_base.similarity_search(user_question)

            # Load the question-answering chain
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")

            # Run the question-answering chain with OpenAI callback
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=user_question)
                print(cb)

            # Display the response
            st.write(response)

if __name__ == "__main__":
    main()