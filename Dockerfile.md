# To use this Dockerfile: 🐳

1. Save the Dockerfile in the same directory as your `app.py` file.

2. Create a file named `requirements.txt` 📄 in the same directory and add the following lines:

```makefile
    langchain==0.0.198
    openai==0.27.8
    PyPDF2==3.0.1
    python-dotenv==1.0.0
    streamlit==1.23.1
    tiktoken==0.4.0
    faiss-cpu==1.7.4
```

3. Replace `sk-your-openai-api-key` 🔑 in the Dockerfile with your actual OpenAI API key.

   ⚠️ Security Note:
   To protect your API keys, its recommended to use environment variables instead of hardcoding them in the Dockerfile. You can pass the API key as an environment variable during runtime or use a .env file.

4. Build the Docker image by running the following command: 🛠️
   `docker build -t myapp .`

5. After the image is successfully built, you can run a Docker container from the image using the following command: ▶️
   `docker run -p 8501:8501 myapp` 🌐

Make sure to replace `sk-your-openai-api-key` with your actual OpenAI API key in the Dockerfile. This will set the `OPENAI_API_KEY` environment variable within the Docker container.

🔒 Security Tip: When deploying applications, its important to follow security best practices. Consider using tools like Docker secrets, Kubernetes secrets, or other secure ways to manage and protect your API keys.

Let me know if you have any further questions! 😊
