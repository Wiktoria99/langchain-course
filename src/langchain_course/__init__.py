import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")

    information = """
    Maria Salomea Skłodowska-Curie[a] (ur. 7 listopada 1867 w Warszawie, zm. 4 lipca 1934 w Passy) – polsko-francuska uczona w dziedzinach fizyki doświadczalnej i chemii fizycznej, podwójna noblistka – laureatka Nagrody Nobla z fizyki (1903)[1] i chemii (1911)[2].

W 1891 r. wyjechała do Paryża, by podjąć studia na Sorbonie, gdzie następnie pracowała naukowo. Była prekursorką nowej gałęzi chemii – radiochemii. Do jej dokonań należą: rozwinięcie teorii promieniotwórczości, technik rozdzielania izotopów promieniotwórczych oraz odkrycie dwóch nowych pierwiastków – radu i polonu. Z jej inicjatywy prowadzono także badania nad leczeniem raka za pomocą promieniotwórczości.

Nagrodą Nobla została wyróżniona po raz pierwszy w 1903 r. – z fizyki, wraz z mężem Pierre’em Curie i z Henrim Becquerelem, za badania nad odkrytym przez Becquerela zjawiskiem promieniotwórczości. Po raz drugi została nagrodzona w 1911 r. – z chemii za odkrycie polonu i radu, wydzielenie czystego radu i badanie właściwości chemicznych pierwiastków promieniotwórczych. Należy do grona pięciu osób, które otrzymały więcej niż jedną Nagrodę Nobla. Wśród nich jest jedną z dwóch, które otrzymały nagrody w różnych dyscyplinach, a także jedynym uczonym uhonorowanym w dwóch różnych naukach przyrodniczych[3][b]. Mimo polskiej narodowości i sentymentów do kraju nigdy nie otrzymała polskiego obywatelstwa.

Jest pierwszą kobietą, która spoczęła w paryskim Panteonie w dowód uznania zasług naukowych. Z mężem Pierre’em Curie miała dwie córki: Irène Joliot-Curie i Ève Curie.
    """

    summary_template = """
    givent the infroamtion {information} about a person I want you to create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-5")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
