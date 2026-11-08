import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()


def main() -> None:
    print("Let's see summary made by Ollama gemma3:270m")

    information = """
Maria Salomea Skłodowska Curie[a] (née Skłodowska; 7 November 1867 – 4 July 1934),[1] better known as Marie Curie,[b] was a Polish and naturalised-French physicist and chemist. She shared the 1903 Nobel Prize in Physics with her husband, Pierre Curie, "for their joint researches on the radioactivity phenomena discovered by Professor Henri Becquerel".[3] She won the 1911 Nobel Prize in Chemistry "[for] the discovery of the elements radium and polonium, by the isolation of radium and the study of the nature and compounds of this remarkable element".[4]

Curie was the first woman to win a Nobel Prize, the first person to win a Nobel Prize twice and the only person to win a Nobel Prize in two different scientific fields. She and Pierre were the first married couple to win the Nobel Prize, launching the Curie family legacy of five Nobel Prizes.[5] She was, in 1906, the first woman to become a professor at the University of Paris.

Curie was born in Warsaw, Russian Empire, where she studied at the clandestine Flying University and began her practical scientific training. In 1891, Curie followed her elder sister Bronisława to study in Paris, where she earned her higher degrees and conducted her subsequent scientific work. In 1895, Curie married Pierre, with whom she conducted pioneering research on radioactivity—a term she coined.[6][7] Pierre died in 1906 in a Paris street accident.
    """

    summary_template = """
    givent the infroamtion {information} about a person I want you to create:
    1. A short summary
    2. Only Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
