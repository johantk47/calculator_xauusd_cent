import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Kalkulator Resiko XAUUSD Cent", layout="wide")

st.markdown("<h2 style='text-align: center;'>⚖️ Kalkulator Resiko XAUUSD (Akun Cent)</h3>", unsafe_allow_html=True)
st.markdown("Masukkan Lot Size yang ingin Anda gunakan untuk melihat seberapa besar resiko uang dan persentasenya terhadap saldo akun.")

st.divider()

# Input Parameter
col1, col2 = st.columns(2)
with col1:
    saldo = st.number_input("Saldo Akun Saat Ini (USC)", min_value=0.0, value=600.0, step=100.0)
    # Input Risiko diganti menjadi Input Lot Size
    lot_size = st.number_input("Lot Size (Akun Cent)", min_value=0.01, value=0.06, step=0.01)

with col2:
    sl_pips = st.number_input("Jarak Stop Loss (Pips)", min_value=1.0, value=10.0, step=1.0)
    contract_size = st.number_input("Contract Size", value=100, disabled=True)

# Konstanta perhitungan untuk XAUUSD Akun Cent
# Pergerakan 1 pip (0.10) pada 1 Lot = 10 USC
NILAI_PIP_PER_LOT = 10.0 

st.write("") # Spacing
if st.button("Hitung Resiko", type="primary", use_container_width=True):
    
    # 1. Hitung nilai nominal per 1 pip dari lot yang diinput
    nilai_pip_aktual = lot_size * NILAI_PIP_PER_LOT
    
    # 2. Hitung total kerugian uang jika terkena SL (USC)
    risk_uang = sl_pips * nilai_pip_aktual
    
    # 3. Hitung persentase kerugian dari saldo
    if saldo > 0:
        resiko_persen = (risk_uang / saldo) * 100
    else:
        resiko_persen = 0.0
        
    st.success("Kalkulasi Berhasil!")
    
    # Menampilkan output dengan layout metrik yang baru
    res1, res2, res3 = st.columns(3)
    res1.metric("Resiko Uang", f"{risk_uang:.2f} USC")
    res2.metric("Resiko Persentase", f"{resiko_persen:.2f} %")
    res3.metric("Nilai per Pip", f"{nilai_pip_aktual:.2f} USC")
    
    st.info(f"💡 **Catatan Eksekusi:** Dengan open posisi sebesar {lot_size:.2f} Lot, jika stop loss Anda tersentuh ({sl_pips} pips), saldo Anda akan berkurang sebesar {risk_uang:.2f} USC, yang berarti akun Anda mengalami minus {resiko_persen:.2f}%.")