#Data Enginnering

####  Spark
![zz](https://img.favpng.com/21/18/13/apache-spark-apache-hadoop-big-data-scala-apache-http-server-png-favpng-EpaM9khCpGC32E7uRV7fuaWpy.jpg) </br></br>
If you want to see metadata or get more detailed information on the data set, please refer to the link below.</br>
<https://spark.apache.org/docs/latest/>



#### 해당 블로그에는 제가 cloud computing부터 hadoop, spark까지 순차적으로 정리되어있습니다.
<https://blog.naver.com/mk_crew/222075444353>


Windows 위에 VM(VMWare)을 활용하여 Linux(Ubuntu 18.04.05 LTS) 를 설치 하였습니다. <br>
 Linux위에 도커(v19.03.13)를 컨테이너를 띄워 스파크환경이 구성된 컨테이너에서 예제를 진행하였습니다. <br>
 

## 스파크란 ?
아파치 스파크(Apache Spark)는 오픈소스 클러스터 컴퓨팅 프레임워크입니다.. <br>
UC Berkeley에서 개발되었습니다. 대학 랩에서 이러한 프레임워크 환경을 구축했다는거 자체가 우리나라 대학들도 기업과 협력하여 다양한 솔류션 및 논문을 발재하고있지만 다시 한번 갭과 더욱더 노력해야겠음을 느꼈습니다 <br>
아래는 스칼라 스파크 설명이 있는 위키독스로 필요하면 참고하면 좋을것 같습니다.<br>
<https://wikidocs.net/book/2350>

 ## 스파크 실습
 우선 내가 스파크가 있는 환경은 root/spark 이다. spark 는 Scala, Python, Java 를 지원한다.<br>
 따라서 pwd를 쳤을때 root/spark 안에서 ls bin을 활용해보면 다양한 소스들을 확인할수 있다. <br>
./bin/spark-shell 을 사용하면 <scala> 를 사용할수있고 해당 창이나온다. <br>
 나는 스칼라 언어에 무지하므로 python으로 사용하였다. <br>
 python의 경우에는 ./bin/pyspark 를 이용하면 된다. <br>
 파이썬을 이용하여 Dataframe 을 만들고 이러한 데이터프레임을 SQL으로 바꾸어주어 SQL 쿼리들에 응답할수있는 실습을 진행해보았다. <br>
 아래 그림들은 위의 img 파일안에 업로드해놓았다.
 
 ### 처리하고자 하는 데이터
 <img width="310" alt="zzz" src="https://user-images.githubusercontent.com/41941627/99473867-d163b700-298e-11eb-8688-9fb16d126ca5.png">
 
 ### JSON 파일을 DATAFRAME으로 바꾼 각각의 테이블(instructor , department) 이다.
 
<img width="239" alt="df show(department)" src="https://user-images.githubusercontent.com/41941627/99472267-9ca23080-298b-11eb-8904-b4b6645e0ac9.png">
<img width="238" alt="df show(instructor)" src="https://user-images.githubusercontent.com/41941627/99472271-9dd35d80-298b-11eb-8f3a-9ae14dd4a92c.png">

 ### Find the names of all instructors with salary is >= $90,000 and <=$100,000

<img width="433" alt="3번질문" src="https://user-images.githubusercontent.com/41941627/99472274-a035b780-298b-11eb-82b0-cbb5fb2fa725.png">

 ### Find the names and average salaries of all departments whose average salary is greater than 80000


<img width="164" alt="4번질문" src="https://user-images.githubusercontent.com/41941627/99472278-a166e480-298b-11eb-97ea-806ba2fab95f.png">

 ### Find the ID, name, department name of instructors whose department is located at ‘Taylor’ building

<img width="277" alt="5번질문" src="https://user-images.githubusercontent.com/41941627/99472283-a2981180-298b-11eb-97ab-85571b463d04.png">

 ### Find names of instructors with salary greater than that of some (at least one) instructor in the ‘Biology’ department

<img width="384" alt="6번질문" src="https://user-images.githubusercontent.com/41941627/99472284-a3c93e80-298b-11eb-9aed-9e4fc4c2e7d4.png">
