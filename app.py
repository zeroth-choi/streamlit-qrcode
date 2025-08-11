import streamlit as st
import qrcode

# Configure Streamlit page settings
st.set_page_config(
    page_title="QR code",
    layout="wide",  # Page layout option
)

st.sidebar.title('QR code 생성하기')

st.markdown('왼쪽에서 입력창에 공백 포함 1000자 이내의 글을 입력하고 **QR code 생성** 버튼을 누르면 QR code가 생성되고 이미지를 다운로드할 수 있습니다.')

qr_data = st.sidebar.text_area('글을 입력하세요 (공백 포함 1000자 이내)')
create_button = st.sidebar.button("QR code 생성")

if create_button:
    qr_img = qrcode.make(qr_data)
    delim = ','
#    st.text('이미지 크기:' + delim.join(qr_img.size))
 
    save_path = 'qr.png'
    qr_img.save(save_path)
    st.image(save_path)

    # 성공 문구 
    st.sidebar.success("생성됨!")
