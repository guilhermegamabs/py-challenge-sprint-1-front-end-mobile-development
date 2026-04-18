import streamlit as st
from app.services.equipamentos import tag_existe, adicionar_equipamento
from app.components.cabecalho import cabecalho

cabecalho("Novo Equipamento", pagina_voltar="app/pages/consulta_equipamentos.py")
st.caption("Preencha os dados do equipamento e confirme o cadastro.")

with st.form("form_cadastro", border=True):
    col1, col2 = st.columns(2)

    with col1:
        tag      = st.text_input("TAG de Identificação *", placeholder="Ex.: EQ-009")
        modelo   = st.text_input("Modelo *",               placeholder="Ex.: XR-200")
        fab      = st.text_input("Fabricante *",           placeholder="Ex.: Siemens")

    with col2:
        potencia = st.number_input("Potência (W) *", min_value=0, step=50,  value=None, placeholder="Ex.: 1500")
        tensao   = st.number_input("Tensão (V) *",   min_value=0, step=1,   value=None, placeholder="Ex.: 220")

    st.write("")
    col_salvar, col_cancelar = st.columns(2)
    salvar   = col_salvar.form_submit_button("Cadastrar",  type="primary",  use_container_width=True)
    cancelar = col_cancelar.form_submit_button("Cancelar",                  use_container_width=True)

if cancelar:
    st.switch_page("app/pages/consulta_equipamentos.py")

if salvar:
    erros = []

    if not tag.strip():
        erros.append("TAG de Identificação é obrigatória.")
    elif tag_existe(tag.strip()):
        erros.append(f"Já existe um equipamento com a TAG **{tag.strip().upper()}**.")

    if not modelo.strip():
        erros.append("Modelo é obrigatório.")

    if not fab.strip():
        erros.append("Fabricante é obrigatório.")

    if potencia is None:
        erros.append("Potência é obrigatória.")

    if tensao is None:
        erros.append("Tensão é obrigatória.")

    if erros:
        for erro in erros:
            st.error(erro)
    else:
        adicionar_equipamento({
            "TAG":          tag.strip().upper(),
            "Modelo":       modelo.strip(),
            "Fabricante":   fab.strip(),
            "Potência (W)": int(potencia),
            "Tensão (V)":   int(tensao),
        })
        st.session_state["cadastro_sucesso"] = tag.strip().upper()
        st.switch_page("app/pages/consulta_equipamentos.py")