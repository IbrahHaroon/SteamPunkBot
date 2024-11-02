#phidata

from phi.agent import Agent
# from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
# from phi.vectordb.pgvector import PgVector
from phi.model.ollama import Ollama
# from phi.embedder.ollama import OllamaEmbedder
# from phi.playground import Playground, serve_playground_app

# doc_path = "./docs/"
# db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# pdf_kb = PDFKnowledgeBase(
#     path=doc_path,
#     vector_db = PgVector(
#         table_name = "steampunk_docs",
#         db_url = db_url,
#         embedder = OllamaEmbedder(),
#     ),
#     reader = PDFReader(chunk = True)
# )

# pdf_kb.load(recreate=False)

agent = Agent(
    name = "Steampunk Agent",
    description="You are an autonomous machine made in a steampunk world, with knowledge of everything steampunk, especially technology and fashion",
    model = Ollama(id = "llama3.2"),
    instructions = ["Respond as if you were calculating your ideas as you go"],
    add_history_to_messages = True,
    # knowledge_base = pdf_kb,
    # search_knowledge = True,
    markdown = False, #formatting text
)

exit_msg = ("exit", "goodbye", "bye") #expandable responses
while (True):
    msg = input("Enter your message: ")
    response = agent.run(msg)
    print("-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+")
    print(response.content)
    print("-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+-+=+")
    if msg.lower() in exit_msg:
        break

print("~~~ Shut down sequence successful ~~~")