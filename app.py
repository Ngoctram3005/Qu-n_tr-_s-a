
import streamlit as st

st.set_page_config(
    page_title="Trà Sữa Nhà Mình",
    page_icon="🧋",
    layout="centered"
)

st.title("🧋 TRÀ SỮA NHÀ MÌNH")
st.write("Chào mừng bạn đến với quán trà sữa!")

# Menu đồ uống
menu = {
    "Trà sữa truyền thống": 25000,
    "Trà sữa trân châu": 30000,
    "Trà sữa matcha": 35000,
    "Trà đào": 28000,
    "Trà vải": 28000,
    "Trà chanh": 20000,
}

st.subheader("📋 Menu đồ uống")

for ten_mon, gia in menu.items():
    st.write(f"🧋 {ten_mon}: {gia:,} VNĐ")

st.divider()

st.subheader("🛒 Đặt món")

ten_khach = st.text_input("Tên khách hàng")

mon = st.selectbox(
    "Chọn đồ uống",
    list(menu.keys())
)

so_luong = st.number_input(
    "Số lượng",
    min_value=1,
    max_value=50,
    value=1,
    step=1
)

them_duong = st.checkbox("Thêm đường")
them_da = st.checkbox("Thêm đá")

if st.button("Tính tiền", use_container_width=True):
    gia_mon = menu[mon]
    tong_tien = gia_mon * so_luong

    st.success("ĐÃ TÍNH TIỀN THÀNH CÔNG!")

    st.write("Khách hàng:", ten_khach or "Khách lẻ")
    st.write("Đồ uống:", mon)
    st.write("Số lượng:", so_luong)
    st.write("Thêm đường:", "Có" if them_duong else "Không")
    st.write("Thêm đá:", "Có" if them_da else "Không")
    st.subheader(f"Tổng tiền: {tong_tien:,} VNĐ")

st.caption("Cảm ơn bạn đã ghé Trà Sữa Nhà Mình!")
