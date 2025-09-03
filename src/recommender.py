from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt



class AnimeRecommendationSystem:
    def __init__(self,retriever,api_key:str|None,model_name:str|None):
        self.llm = ChatGroq(api_key=api_key,model=model_name,temperature=0)
        self.prompt=get_anime_prompt()
        self.qa_chain=RetrievalQA.from_chain_type(
            chain_type='stuff',
            llm=self.llm,
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={'prompt': self.prompt}
        )

    def get_recommendations(self,user_query):
        result=self.qa_chain.invoke({"query":user_query})
        return result['result']












