
import streamlit as st
import pandas as pd



st.set_page_config(
    page_title="CLT na Prática – Painel de Direitos Trabalhistas",
    page_icon=None,
    layout="wide"
)




def carregar_base():
    dados_direitos = [
        {
            "nome": "Férias anuais remuneradas",
            "categoria": "Remuneração",
            "descricao": "Direito a 30 dias de férias a cada 12 meses de trabalho, com pagamento de um terço adicional sobre a remuneração normal.",
            "fundamento_legal": "Constituição Federal de 1988, art. 7º, XVII; Consolidação das Leis do Trabalho, arts. 129 a 153",
            "tempo_minimo_meses": 12
        },
        {
            "nome": "Décimo terceiro salário",
            "categoria": "Remuneração",
            "descricao": "Parcela paga anualmente, correspondente a um doze avos da remuneração por mês trabalhado, usualmente quitada em até duas parcelas.",
            "fundamento_legal": "Constituição Federal de 1988, art. 7º, VIII; Lei n.º 4.090/1962",
            "tempo_minimo_meses": 1
        },
        {
            "nome": "Depósito de FGTS",
            "categoria": "Remuneração",
            "descricao": "Obrigação do empregador de depositar mensalmente o equivalente a 8% da remuneração em conta vinculada ao Fundo de Garantia do Tempo de Serviço.",
            "fundamento_legal": "Lei n.º 8.036/1990",
            "tempo_minimo_meses": 0
        },
        {
            "nome": "Jornada máxima de 44 horas semanais",
            "categoria": "Jornada de trabalho",
            "descricao": "Regra geral que limita a duração do trabalho a 8 horas diárias e 44 horas semanais, ressalvadas hipóteses específicas previstas em lei.",
            "fundamento_legal": "Constituição Federal de 1988, art. 7º, XIII; CLT, arts. 58 e 59",
            "tempo_minimo_meses": 0
        },
        {
            "nome": "Horas extras",
            "categoria": "Jornada de trabalho",
            "descricao": "Horas trabalhadas além da jornada normal, que devem ser remuneradas com adicional mínimo de 50% sobre a hora ordinária.",
            "fundamento_legal": "Constituição Federal de 1988, art. 7º, XVI; CLT, art. 59",
            "tempo_minimo_meses": 0
        },
        {
            "nome": "Adicional noturno",
            "categoria": "Jornada de trabalho",
            "descricao": "Trabalho urbano prestado entre 22h e 5h, com acréscimo remuneratório mínimo de 20% em relação à hora diurna.",
            "fundamento_legal": "CLT, arts. 73 e seguintes",
            "tempo_minimo_meses": 0
        },
        {
            "nome": "Intervalo intrajornada",
            "categoria": "Saúde e segurança",
            "descricao": "Período mínimo de repouso e alimentação durante a jornada diária, cujo tempo varia conforme a duração do trabalho.",
            "fundamento_legal": "CLT, art. 71",
            "tempo_minimo_meses": 0
        },
        {
            "nome": "Aviso prévio",
            "categoria": "Rescisão contratual",
            "descricao": "Comunicação antecipada da rescisão sem justa causa, com prazo mínimo de 30 dias, acrescido de três dias por ano de serviço após o primeiro ano.",
            "fundamento_legal": "Constituição Federal de 1988, art. 7º, XXI; Lei n.º 12.506/2011",
            "tempo_minimo_meses": 12
        },
        {
            "nome": "Multa de 40% sobre o FGTS",
            "categoria": "Rescisão contratual",
            "descricao": "Indenização devida pelo empregador na dispensa sem justa causa, correspondente a 40% do total dos depósitos efetuados na conta de FGTS do trabalhador.",
            "fundamento_legal": "Lei n.º 8.036/1990, art. 18, § 1º",
            "tempo_minimo_meses": 0
        },
        {
            "nome": "Seguro-desemprego",
            "categoria": "Rescisão contratual",
            "descricao": "Benefício de natureza alimentar destinado ao trabalhador dispensado sem justa causa, condicionado ao cumprimento de requisitos legais mínimos.",
            "fundamento_legal": "Lei n.º 7.998/1990",
            "tempo_minimo_meses": 12
        },
        {
            "nome": "Licença-maternidade",
            "categoria": "Licenças",
            "descricao": "Afastamento remunerado da empregada gestante, em regra por 120 dias, com possibilidade de ampliação em hipóteses definidas em lei ou programas específicos.",
            "fundamento_legal": "Constituição Federal de 1988, art. 7º, XVIII; ADCT, art. 10, II, b",
            "tempo_minimo_meses": 0
        },
        {
            "nome": "Licença-paternidade",
            "categoria": "Licenças",
            "descricao": "Afastamento remunerado do empregado em razão do nascimento de filho, com prazo mínimo de cinco dias, ampliável por normas coletivas ou programas empresariais.",
            "fundamento_legal": "Constituição Federal de 1988, art. 7º, XIX; ADCT, art. 10, § 1º",
            "tempo_minimo_meses": 0
        },
    ]

    return pd.DataFrame(dados_direitos)





def main():
    df = carregar_base()

    st.title("CLT na Prática – Painel Interativo de Direitos Trabalhistas")

    st.write(
        """
        Este aplicativo foi desenvolvido como projeto da disciplina **Programação para Advogados**.
        Seu propósito é oferecer uma ferramenta de consulta a alguns direitos trabalhistas básicos de forma prática,
        a partir de uma **base de dados própria** elaborada pelo discente Vitor Presto, com destaque para o
        fundamento normativo de cada instituto.
        """
    )

    st.markdown("---")

    
    st.sidebar.header("Parâmetros de consulta")

    busca_texto = st.sidebar.text_input(
        "Buscar por palavra-chave",
        placeholder="Exemplo: férias, FGTS, horas extras"
    )

    categorias = sorted(df["categoria"].unique())
    categorias_escolhidas = st.sidebar.multiselect(
        "Filtrar por categoria de direito",
        options=categorias,
        default=categorias
    )

    tempo_casa = st.sidebar.slider(
        "Meses trabalhados no vínculo atual",
        min_value=0,
        max_value=60,
        value=0,
        help="Alguns direitos pressupõem tempo mínimo de vínculo. Utilize este parâmetro para simular tais exigências."
    )

    st.sidebar.info(
        "Sugestão: combine a busca por palavra-chave com o filtro de categoria "
        "e o tempo de vínculo para refinar a pesquisa."
    )

    
    df_filtrado = df.copy()

    
    if busca_texto:
        texto = busca_texto.lower()
        df_filtrado = df_filtrado[
            df_filtrado["nome"].str.lower().str.contains(texto)
            | df_filtrado["descricao"].str.lower().str.contains(texto)
            | df_filtrado["fundamento_legal"].str.lower().str.contains(texto)
        ]

    
    df_filtrado = df_filtrado[df_filtrado["categoria"].isin(categorias_escolhidas)]

    
    df_filtrado = df_filtrado[df_filtrado["tempo_minimo_meses"] <= tempo_casa]

    
    st.subheader("Resultados da consulta")

    if df_filtrado.empty:
        st.warning("Não foram encontrados direitos com os parâmetros selecionados. Recomenda-se ampliar ou ajustar os filtros.")
    else:
        
        df_exibicao = df_filtrado.copy()
        df_exibicao["Exigência de tempo de vínculo"] = df_exibicao["tempo_minimo_meses"].apply(
            lambda x: "Sem exigência mínima de tempo de serviço" if x == 0 else f"{x} meses de vínculo"
        )

        st.dataframe(
            df_exibicao[["nome", "categoria", "Exigência de tempo de vínculo"]],
            use_container_width=True
        )

        st.markdown("### Detalhamento normativo")

        for _, linha in df_filtrado.iterrows():
            tempo_legivel = (
                "Sem exigência mínima de tempo de serviço"
                if linha["tempo_minimo_meses"] == 0
                else f"{linha['tempo_minimo_meses']} meses de vínculo"
            )

            with st.expander(f"{linha['nome']}  –  {linha['categoria']}"):
                st.markdown(f"**Descrição sintética do direito:** {linha['descricao']}")
                st.markdown(f"**Fundamento normativo principal:** {linha['fundamento_legal']}")
                st.markdown(f"**Exigência de tempo de vínculo:** {tempo_legivel}")

    st.markdown("---")
    st.caption(
        "Aplicativo de uso acadêmico, destinado exclusivamente a fins didáticos. "
        "A consulta não substitui a orientação individualizada de profissional habilitado."
    )


if __name__ == "__main__":
    main()
