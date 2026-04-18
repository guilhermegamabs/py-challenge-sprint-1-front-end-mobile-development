import streamlit as st
import pandas as pd
import numpy as np
from app.componentes import cabecalho

if "equipamento_selecionado" not in st.session_state:
    st.warning("Nenhum equipamento selecionado. Volte para a consulta.")
    if st.button("← Voltar à Consulta"):
        st.switch_page("app/consulta_equipamentos.py")
    st.stop()

eq = st.session_state["equipamento_selecionado"]

@st.cache_data
def gerar_dados_brutos(tag: str, n: int = 60):
    rng = np.random.default_rng(seed=abs(hash(tag)) % (2**32))
    timestamps = pd.date_range(end=pd.Timestamp.now(), periods=n, freq="1min")

    tensao_raw = rng.integers(2800, 3200, n)
    corrente_raw = rng.integers( 800, 1200, n)
    rpm_raw = rng.integers(3000, 3500, n)

    return pd.DataFrame({
        "Timestamp": timestamps,
        "Tensão (raw)": tensao_raw,
        "Corrente (raw)": corrente_raw,
        "RPM (raw)": rpm_raw,
    })

CONVERSOES = {
    "Tensão":   {"fundo_escala": eq["Tensão (V)"] * 1.2, "unidade": "V", "col_raw": "Tensão (raw)"},
    "Corrente": {"fundo_escala": 50.0, "unidade": "A", "col_raw": "Corrente (raw)"},
    "RPM":      {"fundo_escala": 3600.0, "unidade": "RPM", "col_raw": "RPM (raw)"},
}

def converter(raw: pd.Series, fundo_escala: float) -> pd.Series:
    return (raw / 4095) * fundo_escala

cabecalho(f'Dados Brutos — {eq["TAG"]}', pagina_voltar="app/consulta_equipamentos.py")
st.caption(f"{eq['Modelo']} / {eq['Fabricante']}  ·  {eq['Potência (W)']} W  ·  {eq['Tensão (V)']} V")
st.divider()

col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    grandeza = st.selectbox("Grandeza", list(CONVERSOES.keys()))

with col2:
    n_pontos = st.slider("Pontos exibidos", min_value=10, max_value=60, value=30, step=5)

with col3:
    exibir_raw = st.toggle("Mostrar sinal bruto (ADC)", value=False)

cfg = CONVERSOES[grandeza]
df_raw = gerar_dados_brutos(eq["TAG"])
df = df_raw.tail(n_pontos).copy()

df[f"{grandeza} ({cfg['unidade']})"] = converter(df[cfg["col_raw"]], cfg["fundo_escala"]).round(2)

st.divider()

st.subheader(f"{grandeza} ao longo do tempo")

col_graf = f"{grandeza} ({cfg['unidade']})"

st.line_chart(
    df.set_index("Timestamp")[[col_graf]],
    use_container_width=True,
    color="#FFB300",
)

st.subheader("Tabela de leituras")

colunas_exibir = ["Timestamp", cfg["col_raw"], col_graf] if exibir_raw else ["Timestamp", col_graf]
df_exibir = df[colunas_exibir].sort_values("Timestamp", ascending=False).reset_index(drop=True)

st.dataframe(
    df_exibir,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Timestamp": st.column_config.DatetimeColumn("Timestamp", format="DD/MM/YYYY HH:mm"),
        cfg["col_raw"]: st.column_config.NumberColumn(cfg["col_raw"], format="%d ADC"),
        col_graf: st.column_config.NumberColumn(col_graf, format="%.2f " + cfg["unidade"]),
    },
)

st.divider()
st.subheader("Estatísticas do período")

serie = df[col_graf]
c1, c2, c3, c4 = st.columns(4)
c1.metric("Mínimo",f"{serie.min():.2f} {cfg['unidade']}")
c2.metric("Máximo",f"{serie.max():.2f} {cfg['unidade']}")
c3.metric("Média",f"{serie.mean():.2f} {cfg['unidade']}")
c4.metric("Desvio",f"{serie.std():.2f} {cfg['unidade']}")