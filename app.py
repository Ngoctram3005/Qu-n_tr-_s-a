
import streamlit as st

st.set_page_config(
    page_title="Quản lý quán trà sữa",
    page_icon="🧋",
    layout="centered"
)

# Menu và giá bán
menu = {
    "Trà sữa truyền thống": 25000,
    "Trà sữa trân châu": 30000,
    "Trà sữa matcha": 35000,
    "Trà đào": 28000,
    "Trà vải": 28000,
    "Trà chanh": 20000,
}

# Khởi tạo dữ liệu trong phiên sử dụng
if "orders" not in st.session_state:
    st.session_state.orders = []

if "next_id" not in st.session_state:
    st.session_state.next_id = 1

st.title("🧋 QUẢN LÝ QUÁN TRÀ SỮA")
st.write("Quản lý đơn hàng và doanh thu")

# MENU
st.header("📋 Menu đồ uống")

for ten_mon, gia in menu.items():
    st.write(f"🧋 {ten_mon}: {gia:,} VNĐ")

st.divider()

# TẠO ĐƠN HÀNG
st.header("🛒 Tạo đơn hàng")

with st.form("order_form"):
    ten_khach = st.text_input("Tên khách hàng")

    mon = st.selectbox(
        "Chọn đồ uống",
        list(menu.keys())
    )

    so_luong = st.number_input(
        "Số lượng",
        min_value=1,
        max_value=100,
        value=1,
        step=1
    )

    ghi_chu = st.text_input(
        "Ghi chú",
        placeholder="Ví dụ: ít đường, ít đá"
    )

    submit = st.form_submit_button(
        "TẠO ĐƠN HÀNG",
        use_container_width=True
    )

if submit:
    don_hang = {
        "id": st.session_state.next_id,
        "khach": ten_khach.strip() or "Khách lẻ",
        "mon": mon,
        "so_luong": int(so_luong),
        "gia": menu[mon],
        "ghi_chu": ghi_chu,
        "tong": menu[mon] * int(so_luong),
    }

    st.session_state.orders.append(don_hang)
    st.session_state.next_id += 1

    st.success("Đã tạo đơn hàng thành công!")
    st.rerun()

st.divider()

# THỐNG KÊ
st.header("📊 Thống kê doanh thu")

don_hang_list = st.session_state.orders

tong_doanh_thu = sum(
    don["tong"] for don in don_hang_list
)

tong_so_don = len(don_hang_list)

tong_ly = sum(
    don["so_luong"] for don in don_hang_list
)

col1, col2 = st.columns(2)

col1.metric("Số đơn hàng", tong_so_don)
col2.metric("Tổng số ly", tong_ly)

st.metric(
    "💰 TỔNG DOANH THU",
    f"{tong_doanh_thu:,} VNĐ"
)

st.divider()

# DANH SÁCH ĐƠN HÀNG
st.header("🧾 Danh sách đơn hàng")

if not don_hang_list:
    st.info("Chưa có đơn hàng nào.")

else:
    for don in reversed(don_hang_list):
        with st.container(border=True):
            st.subheader(
                f"Đơn #{don['id']} - {don['khach']}"
            )

            st.write(f"Đồ uống: {don['mon']}")
            st.write(
                f"Số lượng: {don['so_luong']} ly"
            )
            st.write(
                f"Đơn giá: {don['gia']:,} VNĐ"
            )
            st.write(
                f"Thành tiền: {don['tong']:,} VNĐ"
            )

            if don["ghi_chu"]:
                st.write(f"Ghi chú: {don['ghi_chu']}")

            if st.button(
                "🗑️ Xóa đơn này",
                key=f"delete_{don['id']}",
                use_container_width=True
            ):
                st.session_state.orders = [
                    d for d in st.session_state.orders
                    if d["id"] != don["id"]
                ]
                st.rerun()

st.caption(
    "Trà Sữa Nhà Mình - Cảm ơn bạn!"
)
