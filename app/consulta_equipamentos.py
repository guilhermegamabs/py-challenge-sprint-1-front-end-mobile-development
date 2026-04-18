import streamlit as st
import pandas as pd
from app.dados import get_equipamentos, remover_equipamento
from app.componentes import cabecalho

@st.dialog("Confirmar remoção")
def confirmar_remocao(equipamento: dict):
    st.warning(
        f"Tem certeza que deseja remover o equipamento **{equipamento['TAG']}** "
        f"({equipamento['Modelo']} / {equipamento['Fabricante']})?"
    )
    col1, col2 = st.columns(2)
    if col1.button("Remover", type="primary", use_container_width=True):
        remover_equipamento(equipamento["TAG"])
        st.session_state["remocao_sucesso"] = equipamento["TAG"]
        st.rerun()
    if col2.button("Cancelar", use_container_width=True):
        st.rerun()

cabecalho("Consulta de Equipamentos")

col_novo = st.columns([5, 1])[1]
with col_novo:
    if st.button("+ Novo Equipamento", type="primary", use_container_width=True):
        st.switch_page("app/cadastro_equipamento.py")

st.caption("Selecione um equipamento na tabela para acessar o Módulo Técnico.")

df_base = pd.DataFrame(get_equipamentos())

col1, col2, col3 = st.columns([3, 2, 2])

with col1:
    busca = st.text_input("Buscar por TAG ou Modelo", placeholder="Ex.: EQ-001 ou XR-200")

with col2:
    fabricantes = ["Todos"] + sorted(df_base["Fabricante"].unique().tolist())
    fabricante_sel = st.selectbox("Fabricante", fabricantes)

with col3:
    tensoes = ["Todas"] + sorted(df_base["Tensão (V)"].unique().tolist())
    tensao_sel = st.selectbox("Tensão (V)", tensoes)

df = df_base.copy()

if busca:
    termo = busca.strip().upper()
    df = df[
        df["TAG"].str.upper().str.contains(termo) |
        df["Modelo"].str.upper().str.contains(termo)
    ]

if fabricante_sel != "Todos":
    df = df[df["Fabricante"] == fabricante_sel]

if tensao_sel != "Todas":
    df = df[df["Tensão (V)"] == tensao_sel]

st.caption(f"{len(df)} equipamento(s) encontrado(s)")

evento = st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    on_select="rerun",
    selection_mode="single-row",
    column_config={
        "TAG":          st.column_config.TextColumn("TAG",            width="small"),
        "Modelo":       st.column_config.TextColumn("Modelo",         width="medium"),
        "Fabricante":   st.column_config.TextColumn("Fabricante",     width="medium"),
        "Potência (W)": st.column_config.NumberColumn("Potência (W)", format="%d W", width="small"),
        "Tensão (V)":   st.column_config.NumberColumn("Tensão (V)",   format="%d V", width="small"),
    },
)

linhas_selecionadas = evento.selection.rows

if linhas_selecionadas:
    equipamento = df.iloc[linhas_selecionadas[0]].to_dict()
    st.session_state["equipamento_selecionado"] = equipamento

    st.divider()
    col_info, col_acoes = st.columns([4, 1])
    with col_info:
        st.info(
            f"Selecionado: **{equipamento['TAG']}** — "
            f"{equipamento['Modelo']} / {equipamento['Fabricante']}"
        )
    with col_acoes:
        if st.button("Abrir Módulo Técnico", type="primary", use_container_width=True):
            st.switch_page("app/modulo_tecnico.py")
        if st.button("Dados Brutos", use_container_width=True):
            st.switch_page("app/dados_brutos.py")
        if st.button("Remover", use_container_width=True):
            confirmar_remocao(equipamento)

if "cadastro_sucesso" in st.session_state:
    st.success(f"Equipamento **{st.session_state.pop('cadastro_sucesso')}** cadastrado com sucesso!")

if "remocao_sucesso" in st.session_state:
    st.success(f"Equipamento **{st.session_state.pop('remocao_sucesso')}** removido com sucesso!")