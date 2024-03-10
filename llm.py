import google.generativeai as genai

genai.configure(api_key='AIzaSyC8N_s60VEaXrETjtaYsQihvHvSlfMMW5Q')

model = genai.GenerativeModel('gemini-pro')

while True:
    query = input("ask question?:")
    response = model.generate_content(query + ''' from the table Broker Name            GWP   Planned GWP  Unnamed: 5  Success Rate (%)
9          Kentro  997785.356442  1.496678e+06    0.333333         33.333333
8          Howden  985050.289680  1.477575e+06    0.333333         33.333333
13         Tysers  912122.638088  1.368184e+06    0.333333         33.333333
4          Convex  831935.545568  1.247903e+06    0.333333         33.333333
0            Aon   794263.139962  1.191395e+06    0.333333         33.333333
3           Besso  704360.799245  1.056541e+06    0.333333         33.333333
11         McGill  575548.714484  8.633231e+05    0.333333         33.333333
7      Hendersons  501300.818980  7.519512e+05    0.333333         33.333333
5   Croton Stokes  279452.727487  4.191791e+05    0.333333         33.333333
12        Miller   255148.367257  3.827226e+05    0.333333         33.333333''')
    print(response.text)
    print()