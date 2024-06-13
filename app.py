import streamlit as st
import base64

prefixes = {
  'MTN': ['0803', '0806', '0703', '0706', '0810', '0813', '0814', '0816', '0903', '0906', '07025', '07026', '0704', '0707', '0913', '0916'],
  'GLO': ['0705','0805', '0807', '0811', '0815', '0905', '0915'],
  '9Mobile': ['0809', '0817', '0818', '0908', '0909'],
  'Airtel': ['0802', '0808', '0708', '0812', '0701', '0902', '0907', '0901', '0904', '0907', '0911', '0912']
}

def identify_network(phone_number):
  for network, network_prefixes in prefixes.items():
    if phone_number.startswith(tuple(network_prefixes)):
      return network
  return 'unknown'

def get_base64_of_bin_file(bin_file):
  """Reads and encodes a binary file (image) as base64 string."""
  with open(bin_file, 'rb') as f:
    data = f.read()
  return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
  """Sets the provided image (any format supported by Streamlit) as the app's background."""
  bin_str = get_base64_of_bin_file(png_file)
  page_bg_img = '''
  <style>
  body {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
  }
  </style>
  ''' % bin_str
  st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
  # Set background image
  set_png_as_page_bg('./dial.png')  # Assuming your image is in the same directory

  st.title('Identify Network Service Provider')
  phone_number = st.text_input('Enter phone number', max_chars=11)
  if st.button('Identify'):
    if phone_number:
      if len(phone_number) > 11:
        st.error('Phone number must not exceed 11 digits!')
      else:
        network = identify_network(phone_number)
        st.write(f'This Number belongs to the {network} network')
    else:
      st.error('Invalid input')

if __name__ == '__main__':
  main()
