import streamlit as st

def cabecalho(titulo: str, pagina_voltar: str | None = None):
    col_logo, _ = st.columns([1, 5])
    with col_logo:
        st.image("img/logo-forzy-preta.svg", use_container_width=True)

    col_titulo, col_acao = st.columns([5, 1])
    with col_titulo:
        st.markdown(
            f'<h1 style="color:#FFB300; font-family:Inter,sans-serif; font-weight:900; margin-top:4px;">'
            f'{titulo}</h1>',
            unsafe_allow_html=True,
        )
    if pagina_voltar:
        with col_acao:
            st.write("")
            if st.button("← Voltar", use_container_width=True):
                st.switch_page(pagina_voltar)

    st.markdown(
        '<hr style="border:none; border-top:2px solid #FFB300; margin:6px 0 18px 0;">',
        unsafe_allow_html=True,
    )