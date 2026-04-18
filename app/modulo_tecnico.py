import streamlit as st
from app.componentes import cabecalho

if "editando" not in st.session_state:
    st.session_state["editando"] = False

if "equipamento_selecionado" not in st.session_state:
    st.warning("Nenhum equipamento selecionado. Volte para a consulta.")
    if st.button("← Voltar à Consulta"):
        st.switch_page("app/consulta_equipamentos.py")
    st.stop()

eq = st.session_state["equipamento_selecionado"]

cabecalho(f'Módulo Técnico — {eq["TAG"]}', pagina_voltar="app/consulta_equipamentos.py")

if not st.session_state["editando"]:

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**TAG de Identificação**")
        st.text(eq["TAG"])

        st.markdown("**Modelo**")
        st.text(eq["Modelo"])

        st.markdown("**Fabricante**")
        st.text(eq["Fabricante"])

    with col2:
        st.markdown("**Potência**")
        st.text(f"{eq['Potência (W)']} W")

        st.markdown("**Tensão**")
        st.text(f"{eq['Tensão (V)']} V")

    st.divider()

    if st.button("Editar", type="primary"):
        st.session_state["editando"] = True
        st.rerun()

else:
    st.subheader("Editar Equipamento")

    with st.form("form_edicao"):
        col1, col2 = st.columns(2)

        with col1:
            tag = st.text_input("TAG de Identificação", value=eq["TAG"], disabled=True)
            modelo = st.text_input("Modelo", value=eq["Modelo"])
            fab = st.text_input("Fabricante", value=eq["Fabricante"])

        with col2:
            potencia = st.number_input("Potência (W)", value=int(eq["Potência (W)"]), min_value=0, step=50)
            tensao = st.number_input("Tensão (V)", value=int(eq["Tensão (V)"]), min_value=0, step=1)

        col_salvar, col_cancelar = st.columns(2)
        salvar = col_salvar.form_submit_button("Salvar", type="primary", use_container_width=True)
        cancelar = col_cancelar.form_submit_button("Cancelar", use_container_width=True)

    if salvar:
        st.session_state["equipamento_selecionado"].update({
            "Modelo": modelo,
            "Fabricante": fab,
            "Potência (W)": potencia,
            "Tensão (V)": tensao,
        })
        st.session_state["editando"] = False
        st.success("Dados atualizados com sucesso!")
        st.rerun()

    if cancelar:
        st.session_state["editando"] = False
        st.rerun()