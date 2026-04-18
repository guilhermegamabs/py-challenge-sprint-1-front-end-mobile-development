import streamlit as st

EQUIPAMENTOS_INICIAIS = [
    {"TAG": "EQ-001", "Modelo": "XR-200",    "Fabricante": "Siemens",   "Potência (W)": 1500, "Tensão (V)": 220},
    {"TAG": "EQ-002", "Modelo": "Alpha-50",  "Fabricante": "WEG",       "Potência (W)":  750, "Tensão (V)": 380},
    {"TAG": "EQ-003", "Modelo": "TurboMax",  "Fabricante": "ABB",       "Potência (W)": 3000, "Tensão (V)": 220},
    {"TAG": "EQ-004", "Modelo": "ProLine-1", "Fabricante": "Schneider", "Potência (W)": 2200, "Tensão (V)": 127},
    {"TAG": "EQ-005", "Modelo": "XR-200",    "Fabricante": "Siemens",   "Potência (W)": 1500, "Tensão (V)": 220},
    {"TAG": "EQ-006", "Modelo": "Compact-R", "Fabricante": "WEG",       "Potência (W)":  550, "Tensão (V)": 380},
    {"TAG": "EQ-007", "Modelo": "Delta-V",   "Fabricante": "ABB",       "Potência (W)": 4000, "Tensão (V)": 440},
    {"TAG": "EQ-008", "Modelo": "ProLine-2", "Fabricante": "Schneider", "Potência (W)": 1800, "Tensão (V)": 220},
]


def get_equipamentos():
    if "equipamentos" not in st.session_state:
        st.session_state["equipamentos"] = list(EQUIPAMENTOS_INICIAIS)
    return st.session_state["equipamentos"]


def tag_existe(tag: str) -> bool:
    return any(eq["TAG"].upper() == tag.upper() for eq in get_equipamentos())


def adicionar_equipamento(equipamento: dict):
    get_equipamentos().append(equipamento)


def remover_equipamento(tag: str):
    st.session_state["equipamentos"] = [
        eq for eq in get_equipamentos() if eq["TAG"].upper() != tag.upper()
    ]