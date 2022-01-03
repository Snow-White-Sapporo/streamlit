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


