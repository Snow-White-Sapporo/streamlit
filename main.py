import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門') #タイトルの追加

st.write('プログレスバーの表示')
'Start!!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!'

st.write('DataFrame')

df=pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

st.write(df)
st.dataframe(df,width=100, height=100) #st.dataframeで表の設定ができる　動的なテーブル
st.dataframe(df.style.highlight_max(axis=0), width=800, height=400) #st.dataframeで表の設定ができる
### axis=0  列      axis=1　行
st.table(df.style.highlight_max(axis=0)) #st.tableでstatic(静的)なテーブルを作成
### reference  https://docs.streamlit.io/library/api-reference/data


#magic command
'''
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

'''
### reference  https://docs.streamlit.io/library/api-reference/text
### Excキーの下「`」 back quotation

df=pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

### reference  https://docs.streamlit.io/library/api-reference/charts

df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(df)

st.write('Display Image')
img=Image.open(r"C:\Users\hooch\Pictures\Icons\Flash.ico")
st.image(img, caption='Yeah !', use_column_width=True)     #use_column_width 実際のレイアウトの横幅に合わせて表示
st.image(img, caption='OOrya !')     #use_column_width 実際のレイアウトの横幅に合わせて表示

### reference  https://docs.streamlit.io/library/api-reference/media

if st.checkbox('Show Image'):
    img=Image.open(r"C:\Users\hooch\Pictures\Icons\Flash.ico")
    st.image(img, caption='OOrya !')     #use_column_width 実際のレイアウトの横幅に合わせて表示

option= st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
    )
'あなたの好きな数字は、',option,'です。'

text= st.text_input('あなたの趣味を教えてください。')
'あなたの趣味: ',text

condition= st.slider('あなたの今の調子は？',0,100,50)    #最小値、最大値、Default値
'コンディション: ',condition

### reference  https://docs.streamlit.io/library/api-reference/widgets

origin= st.sidebar.text_input('あなたの出身を教えてください。')
'あなたの出身: ',origin

osaifu= st.sidebar.slider('あなたのお財布の充足度は？',0,100,50)    #最小値、最大値、Default値
'お財布の中身: ',osaifu

left_column, right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1=st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2=st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3=st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')


