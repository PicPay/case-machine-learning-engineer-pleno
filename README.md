

# **Case Machine Learning Engineer**


## Escopo

Este teste consiste em criar uma solução de transformação de dados, treino de modelo e escoragem online. Para isso deverá ser entregue um **link de um repositório Git** (GitHub, BitBucket, etc.) contendo a seguinte estrutura:



* **/src/** - Códigos da API
* **/notebook/** - Contém o arquivo notebook com as transformações do dado, respostas das perguntas e treinamento do modelo
* **/docs/** - Desenho da arquitetura
* **/tests/** - Testes unitários

Abaixo estão as regras/orientações para a entrega:



* Você terá **15 dias corridos** a partir do recebimento deste email para fazer a entrega final via `Github`, em um repositório público e o link do repositório deverá ser enviado para a plataforma Gupy em resposta ao email de recebimento do desafio;
* Durante todo o período o **time estará disponível** para dúvidas no email `data.mlops@picpay.com`;
* O foco do teste é avaliar como você se sai em um desafio de rotinas de Engenheiro de Machine Learning bem como você lida ao aprender novas tecnologias;
* Caso não consiga terminar 100% do proposto, recomendamos que faça as entregas mesmo assim para que o time possa avaliar seu desempenho;
* O uso de ferramentas como **Google** e **ChatGPT** é permitido porém, iremos avaliar e questionar a solução entregue durante a entrevista técnica;
* A API deverá ser feito em **Python (Falar dos endpoints)**;
* As **transformações de dado** deverão ser feitas utilizando **spark** (PySpark);
* O **desenho** da arquitetura pode ser uma **imagem** (.png, .jpg);
* Voce deverá apresentar a solução durante a entrevista técnica


## Ambiente

Para a execução das tarefas que utilizam spark, você pode utilizar o ambiente da sua preferência ou escolher uma das opções abaixo:



* **Databricks Community Edition** (recomendado) - Acesse o [Databricks Community Edition,](https://www.databricks.com/try-databricks#account) cadastre-se com seu e-mail e verifique sua conta. A partir daí, vá ao painel inicial clique em **Home**, depois em **Create** e escolha **Notebook;**
* **Google Colab** - O Google Colab é uma plataforma de desenvolvimento interativo. Porém, ele não possui spark nativamente configurado. Você pode seguir o tutorial [desse link](https://www.alura.com.br/artigos/iniciando-projeto-spark-no-colab) para habilitar o spark e fazer seu teste por lá


## Base de Dados


### Base de Informações de Voos

A base de dados de voos contém informações detalhadas sobre voos ocorridos em 2013. Ela pode ser obtida através [deste link](https://github.com/PedroDubas/Batalha_dados_Fia/raw/master/flights.csv.zip). As colunas do conjunto de dados são:


<table>
  <tr>
   <td><strong>Coluna</strong>
   </td>
   <td><strong>Descrição </strong>
   </td>
  </tr>
  <tr>
   <td>id
   </td>
   <td>Um identificador único para cada registro de voo.
   </td>
  </tr>
  <tr>
   <td>year
   </td>
   <td>O ano em que o voo ocorreu (2013 neste conjunto de dados).
   </td>
  </tr>
  <tr>
   <td>month
   </td>
   <td>O mês em que o voo ocorreu (1 a 12).
   </td>
  </tr>
  <tr>
   <td>day
   </td>
   <td>O dia do mês em que o voo ocorreu (1 a 31).
   </td>
  </tr>
  <tr>
   <td>dep_time
   </td>
   <td>O horário local real de partida do voo, no formato 24 horas (hhmm).
   </td>
  </tr>
  <tr>
   <td>sched_dep_time
   </td>
   <td>O horário local programado de partida do voo, no formato 24 horas (hhmm).
   </td>
  </tr>
  <tr>
   <td>dep_delay
   </td>
   <td>A diferença entre os horários real e programado de partida do voo, em minutos. Um valor positivo indica uma partida atrasada, enquanto um valor negativo indica uma partida adiantada.
   </td>
  </tr>
  <tr>
   <td>arr_time
   </td>
   <td>O horário local real de chegada do voo, no formato 24 horas (hhmm).
   </td>
  </tr>
  <tr>
   <td>sched_arr_time
   </td>
   <td>O horário local programado de chegada do voo, no formato 24 horas (hhmm).
   </td>
  </tr>
  <tr>
   <td>arr_delay
   </td>
   <td>A diferença entre os horários real e programado de chegada do voo, em minutos. Um valor positivo indica uma chegada atrasada, enquanto um valor negativo indica uma chegada adiantada.
   </td>
  </tr>
  <tr>
   <td>carrier
   </td>
   <td>O código de duas letras da companhia aérea do voo.
   </td>
  </tr>
  <tr>
   <td>flight
   </td>
   <td>O número do voo.
   </td>
  </tr>
  <tr>
   <td>tailnum
   </td>
   <td>O identificador único da aeronave usada no voo.
   </td>
  </tr>
  <tr>
   <td>origin
   </td>
   <td>O código de três letras do aeroporto de origem do voo.
   </td>
  </tr>
  <tr>
   <td>dest
   </td>
   <td>O código de três letras do aeroporto de destino do voo.
   </td>
  </tr>
  <tr>
   <td>air_time
   </td>
   <td>A duração do voo, em minutos.
   </td>
  </tr>
  <tr>
   <td>distance
   </td>
   <td>A distância entre os aeroportos de origem e destino, em milhas.
   </td>
  </tr>
  <tr>
   <td>hour
   </td>
   <td>O componente da hora do horário programado de partida, no horário local.
   </td>
  </tr>
  <tr>
   <td>minute
   </td>
   <td>O componente dos minutos do horário programado de partida, no horário local.
   </td>
  </tr>
  <tr>
   <td>time_hour
   </td>
   <td>O horário programado de partida do voo, no formato local e de data-hora (yyyy-mm-dd hh
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td>O nome da companhia aérea do voo.
   </td>
  </tr>
</table>



### Base de Coordenadas e Clima

Para enriquecer a base de dados, você precisará utilizar duas APIs externas:



1. **Weatherbit API**: Fornece dados históricos sobre as condições meteorológicas.
    * **Site**:[ Weatherbit API](https://www.weatherbit.io/)
    * **Como se cadastrar**: Crie uma conta no site para obter a chave da API (API Key).
    * 
2. **AirportDB API**: Fornece informações detalhadas sobre aeroportos, incluindo coordenadas geográficas.
    * **Site**:[ AirportDB API](https://airportdb.io/)
    * **Como se cadastrar**: Crie uma conta no site para obter a chave da API (API Token).


## **Perguntas**

Responda às seguintes perguntas utilizando PySpark:



1. Qual é o número total de voos no conjunto de dados?
2. Quantos voos foram cancelados? (Considerando que voos cancelados têm **<code>dep_time</code></strong> e <strong><code>arr_time</code></strong> nulos)
3. Qual é o atraso médio na partida dos voos (<strong><code>dep_delay</code>)</strong>?
4. Quais são os 5 aeroportos com maior número de pousos?
5. Qual é a rota mais frequente (par <strong>origin</strong>-<strong>dest</strong>)?
6. Quais são as 5 companhias aéreas com maior tempo médio de atraso na chegada? (Exiba também o tempo)
7. Qual é o dia da semana com maior número de voos?
8. Qual o percentual mensal dos voos tiveram atraso na partida superior a 30 minutos?
9. Qual a origem mais comum para voos que pousaram em Seattle (<strong>SEA</strong>)?
10. Qual é a média de atraso na partida dos voos (<strong><code>dep_delay</code>)</strong> para cada dia da semana?
11. Qual é a rota que teve o maior tempo de voo médio (<strong>air_time</strong>)?
12. Para cada aeroporto de origem, qual é o aeroporto de destino mais comum?
13. Quais são as 3 rotas que tiveram a maior variação no tempo médio de voo (<strong>air_time</strong>) ?
14. Qual é a média de atraso na chegada para voos que tiveram atraso na partida superior a 1 hora?
15. Qual é a média de voos diários para cada mês do ano?
16. Quais são as 3 rotas mais comuns que tiveram atrasos na chegada superiores a 30 minutos?
17. Para cada origem, qual o principal destino?


## <strong>Enriquecimento da Base de Dados</strong>

Usando as APIs do Weatherbit e AirportDB, enriqueça a base de dados de voos com informações sobre a velocidade do vento para os aeroportos de origem e destino. Utilize as coordenadas dos aeroportos fornecidas pela API AirportDB e obtenha os dados meteorológicos históricos da API Weatherbit para as datas correspondentes aos voos.


### **Weatherbit API**

**Campos Relevantes:**



* `wind_spd`: Velocidade do vento em metros por segundo (m/s).

**Exemplo de Chamada:**


```
import requests

weatherbit_key = 'SUA_WEATHERBIT_API_KEY'
latitude = 40.7128
longitude = -74.0060
start_date = '2023-01-01' 
end_date = '2023-01-02'  # Sempre adicione +1 dia em relação ao start_date

url = 'https://api.weatherbit.io/v2.0/history/daily'
params = {
   'lat': latitude,
   'lon': longitude,
   'start_date': start_date,
   'end_date': end_date,
   'key': weatherbit_key,
}
headers = {
   'Accept': 'application/json',
}
response = requests.get(url, params=params, headers=headers)
data = response.json()

if 'data' in data and len(data['data']) > 0:
   wind_speed = data['data'][0]['wind_spd']
   print("Velocidade do vento:", wind_speed)
else:
   print("Dados meteorológicos não encontrados.")
```



### **AirportDB API**

**Campos Relevantes:**



* `latitude_deg`: Latitude do aeroporto.
* `longitude_deg`: Longitude do aeroporto.

**Exemplo de Chamada:**


```
import requests
airportdb_key = 'SUA_AIRPORTDB_API_KEY'
airport_code = 'JFK' 
url = f"https://airportdb.io/api/v1/airport/K{airport_code}?apiToken={airportdb_key}"
response = requests.get(url)
data = response.json()

if 'latitude_deg' in data and 'longitude_deg' in data:
   latitude = data['latitude_deg']
   longitude = data['longitude_deg']
   print("Coordenadas do aeroporto (latitude, longitude):", latitude, ",", longitude)
else:
   print("Informações do aeroporto não encontradas.")
```


Observe que é necessário adicionar a letra K antes de realizar a chamada ao endpoint.

**Pergunta final:** Enriqueça a base de dados de voos com as condições meteorológicas (velocidade do vento) para os aeroportos de origem e destino. Mostre as informações enriquecidas para os 5 voos com maior atraso na chegada.


## **Modelo de Ml**

O objetivo desse teste não é avaliar a capacidade de criar modelo ou a performance, isso não será levado em consideração durante o teste. Apenas a gestão do arquivo **<code>.pkl </code></strong>(Save, load, Predict).

Sinta-se à vontade para criar o modelo da forma que preferir utilizando os campos que preferir, 

Vamos deixar aqui um caminho simples para fazer uma regressão linear para prever o arr_delay


### **Instruções para Criar um Modelo de Regressão Linear **

Estas instruções irão guiá-lo através do processo de criação de um modelo de regressão linear para prever o atraso na chegada (`arr_delay`) de voos. Você usará `pandas` para manipulação de dados, `scikit-learn` para modelagem.


#### **Passo a Passo**



1. Converta o DataFrame do Spark para um DataFrame do pandas, selecionando as colunas relevantes (`dep_delay`, `air_time`, `distance`, `hour`, `minute`, `arr_delay`).
2. Remova quaisquer valores nulos do DataFrame do pandas.
3. Separe os dados em `X` (features) e `y` (target), onde `X` contém as colunas de features e `y` contém a coluna `arr_delay`.
4. Divida os dados em conjuntos de treinamento e teste usando `train_test_split` da lib `scikit-learn`. (`from sklearn.model_selection import train_test_split`)

    ```
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    ```


5. Crie um objeto `LinearRegression` `from sklearn.linear_model import LinearRegression`
6. Treine o modelo usando o conjunto de treinamento (`X_train` e `y_train`).

    ```
    model = LinearRegression()
    model.fit(X_train, y_train)

    ```


      7. Faça previsões no conjunto de teste (`X_test`).

	`y_pred = model.predict(X_test)`

     8.  Calcule o erro quadrático médio (MSE) entre as previsões e os valores reais (`y_test`).


```
    from sklearn.metrics import mean_squared_error
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')
```


      9.  Salve o modelo treinado em um arquivo pickle usando a biblioteca `pickle`.


```
    import pickle
