import io
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode

st.set_page_config(
    page_title="Excel-like Grid in Streamlit",
    layout="wide",
)

st.markdown("""
<style>
    .block-container {padding-top: 1.2rem; padding-bottom: 2rem;}
    div[data-testid="stMetric"] {
        border: 1px solid #d9d9d9;
        padding: 12px 14px;
        border-radius: 8px;
        background: white;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def sample_data():
    return pd.DataFrame({
        "Risk Factor": [
            "EURUSD Spot", "GBPUSD Spot", "USDJPY Spot",
            "USD 10Y Yield", "EUR 5Y Swap", "S&P 500", "Brent Front"
        ],
        "Desk": ["FX", "FX", "FX", "Rates", "Rates", "Equity", "Commodities"],
        "Current": [1.1734, 1.3491, 149.82, 4.12, 2.73, 6678.4, 70.24],
        "Stressed": [1.1240, 1.2840, 157.40, 4.81, 3.11, 6025.0, 61.85],
        "Breaches": [0, 2, 0, 5, 1, 0, 3],
        "Backtest": ["PASS", "REVIEW", "PASS", "FAIL", "REVIEW", "PASS", "REVIEW"],
    })

def dataframe_to_excel_bytes(df: pd.DataFrame, sheet_name="Backtesting"):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name=sheet_name)
    return output.getvalue()

st.title("Excel-like Spreadsheet in Streamlit")
st.caption(
    "This is a real Streamlit implementation. The main grid uses AG Grid rather than st.dataframe()."
)

with st.sidebar:
    st.header("Workbook")
    uploaded = st.file_uploader("Upload an Excel workbook", type=["xlsx", "xlsm"])
    source = st.radio(
        "Data source",
        ["Sample risk data", "Uploaded workbook"],
        index=0 if uploaded is None else 1,
    )

df = sample_data()
sheet_name = "Backtesting"

if source == "Uploaded workbook" and uploaded is not None:
    try:
        excel = pd.ExcelFile(uploaded)
        sheet_name = st.sidebar.selectbox("Sheet", excel.sheet_names)
        df = pd.read_excel(uploaded, sheet_name=sheet_name)
    except Exception as exc:
        st.error(f"Could not read workbook: {exc}")
        st.stop()
elif source == "Uploaded workbook":
    st.info("Upload an .xlsx or .xlsm file from the sidebar.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Rows", len(df))
c2.metric("Columns", len(df.columns))

if "Breaches" in df.columns:
    numeric_breaches = pd.to_numeric(df["Breaches"], errors="coerce").fillna(0)
    c3.metric("Total breaches", int(numeric_breaches.sum()))
else:
    c3.metric("Total breaches", "—")

if "Backtest" in df.columns:
    c4.metric("Fails", int((df["Backtest"].astype(str).str.upper() == "FAIL").sum()))
else:
    c4.metric("Fails", "—")

tab_grid, tab_native = st.tabs(["Excel-like AG Grid", "Native Streamlit editor"])

with tab_grid:
    st.subheader(sheet_name)

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(
        editable=True,
        sortable=True,
        filter=True,
        resizable=True,
        min_column_width=110,
    )
    gb.configure_selection(
        selection_mode="multiple",
        use_checkbox=True,
    )
    gb.configure_pagination(
        paginationAutoPageSize=False,
        paginationPageSize=20,
    )
    gb.configure_grid_options(
        enableRangeSelection=True,
        rowHeight=34,
        headerHeight=36,
        suppressRowClickSelection=False,
    )

    grid_options = gb.build()

    grid_response = AgGrid(
        df,
        gridOptions=grid_options,
        height=480,
        width="100%",
        data_return_mode=DataReturnMode.AS_INPUT,
        update_mode=GridUpdateMode.VALUE_CHANGED | GridUpdateMode.SELECTION_CHANGED,
        fit_columns_on_grid_load=False,
        allow_unsafe_jscode=False,
        theme="streamlit",
        key=f"grid_{sheet_name}",
    )

    edited_df = pd.DataFrame(grid_response["data"])

    left, right = st.columns([1, 1])
    with left:
        selected_rows = grid_response.get("selected_rows", [])
        if isinstance(selected_rows, pd.DataFrame):
            selected_count = len(selected_rows)
        else:
            selected_count = len(selected_rows or [])
        st.caption(f"Selected rows: {selected_count}")

    with right:
        st.download_button(
            "Download edited Excel",
            data=dataframe_to_excel_bytes(edited_df, sheet_name[:31] or "Sheet1"),
            file_name="edited_workbook.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )

    with st.expander("What makes this different from st.dataframe()?"):
        st.markdown("""
- Cells are editable.
- Excel-style column resizing, filtering and sorting.
- Multi-row selection with checkboxes.
- Range selection.
- Pagination.
- The edited grid can be exported directly back to .xlsx.
        """)

with tab_native:
    st.write(
        "For comparison, this is Streamlit's built-in editor. "
        "It is simpler, but less Excel-like."
    )
    native_df = st.data_editor(
        df,
        use_container_width=True,
        hide_index=True,
        num_rows="dynamic",
        key="native_editor",
    )
    st.download_button(
        "Download native-editor data",
        data=dataframe_to_excel_bytes(native_df, sheet_name[:31] or "Sheet1"),
        file_name="native_editor_output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
