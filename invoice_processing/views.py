from django.shortcuts import render

# Create your views here.
import os
from django.shortcuts import render
from .forms import InvoiceForm
from pdf2image import convert_from_path
from langchain import HuggingFacePipeline, PromptTemplate
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain import HuggingFacePipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer, pipeline
from auto_gptq import AutoGPTQForCausalLM
import torch
from langchain import HuggingFacePipeline
from transformers import pipeline

DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

# Load the model and embeddings once when the server starts
model_name_or_path = "TheBloke/Llama-2-13B-chat-GPTQ"
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)
model = AutoGPTQForCausalLM.from_quantized(
    model_name_or_path,
    revision="gptq-4bit-128g-actorder_True",
    model_basename="model",
    use_safetensors=True,
    trust_remote_code=True,
    inject_fused_attention=False,
    device=DEVICE,
)


# Assuming your model and tokenizer have been loaded already
text_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=1024,
    temperature=0,
    top_p=0.95,
    repetition_penalty=1.15
)

llm = HuggingFacePipeline(pipeline=text_pipeline, model_kwargs={"temperature": 0})


llm = HuggingFacePipeline(pipeline=text_pipeline, model_kwargs={"temperature": 0})

embeddings = HuggingFaceInstructEmbeddings(
    model_name="hkunlp/instructor-large", model_kwargs={"device": DEVICE}
)

# Main view to handle file uploads and questions
def process_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            pdf = form.cleaned_data['pdf']
            question = form.cleaned_data['question']

            # Save the uploaded PDF locally
            pdf_path = os.path.join('media', pdf.name)
            with open(pdf_path, 'wb+') as destination:
                for chunk in pdf.chunks():
                    destination.write(chunk)

            # Convert PDF to images and extract text
            invoice = convert_from_path(pdf_path, dpi=300)
            # Assuming you want to display the first page
            invoice[0].show()

            # Load the PDF text
            loader = PyPDFDirectoryLoader(os.path.dirname(pdf_path))
            docs = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
            texts = text_splitter.split_documents(docs)

            db = Chroma.from_documents(docs, embeddings, persist_directory="db")

            template = """
            Use the following pieces of context to answer the question at the end.
            If you don't know the answer, just say that you don't know, don't try to make up an answer.

            {context}

            Question: {question}
            """
            prompt = PromptTemplate(template=template, input_variables=["context", "question"])

            qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=db.as_retriever(search_kwargs={"k": 2}),
                return_source_documents=True,
                chain_type_kwargs={"prompt": prompt},
            )

            result = qa_chain({"question": question})

            return render(request, 'output.html', {'result': result})

    else:
        form = InvoiceForm()

    return render(request, 'upload.html', {'form': form})
