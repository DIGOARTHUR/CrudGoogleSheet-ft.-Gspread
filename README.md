# Py-01-DesafioTunts [Estágio Processo Seletivo 2021]  <img  alt="skills"  width="35" height="35" src="https://user-images.githubusercontent.com/59892368/106386750-4acb4d00-63b5-11eb-8d43-be0469cc0a3c.PNG">


 

 <!------------------------------------STACKS-->
#### Stacks:
<p align="left">

 <a href="https://www.python.org"><img  alt="Python"  width="50" height="50" src="https://user-images.githubusercontent.com/59892368/226100266-f8737e64-823d-4931-ae06-e64a0856a503.svg"><a/>






 <!------------------------------------TOOLS-->
 #### Tools:
 <a href="https://www.jetbrains.com/pycharm/"><img  alt="Pycharm"  width="50" height="50" src="https://user-images.githubusercontent.com/59892368/226100500-2b181c49-6314-4772-bb33-6b7711d86096.svg"><a/>
 <a href="https://git-scm.com/"><img  alt="Git"  width="50" height="50" src="https://user-images.githubusercontent.com/59892368/223381109-88617798-75ae-4f3a-bc4a-1210637f818c.svg"><a/>
 <a href="https://docs.google.com/spreadsheets/u/0/"><img  alt="GoogleSheets"  width="50" height="50" src="https://user-images.githubusercontent.com/59892368/226121477-c3391608-b31a-4b5e-9b38-036467ee352b.svg"><a/>

   
<hr> 



   <!------------------------------------SUMMARY-->
<p align="center">
  <a href="https://github.com/DIGOARTHUR/Dashgo#--sobre-a-aplicação-">About the application</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/DIGOARTHUR/Py-01-DesafioTunts-CRUDGoogleSheets-#--creating-your-application-">Creating your application</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/DIGOARTHUR/Py-01-DesafioTunts-CRUDGoogleSheets-#--gspread-"> Gspread</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
   <a href="https://github.com/DIGOARTHUR/Dashgo#-Stacks-"> Stacks</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/DIGOARTHUR/Dashgo#-rodando-a-aplicação">References</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  
</p>  

   <!------------------------------------DESCRIPTION-->

# <img  alt="skills"  width="40" height="40" src="https://user-images.githubusercontent.com/59892368/148622497-164365e8-f6b0-4f40-bc75-a0ed4da6059b.png"> About the application <!---write here : talk a little about project: what's does, example.  -->
> Using the Google spreadsheet and the 'gspread' API, an automation was made using the Python language for reading, analyzing and inserting data in a specific data spreadsheet available here. I will take the opportunity to leave the entire documented process and examples so that anyone can do it. Use your creativity and experience. Come on!

 
 <p>
    <h2 align="rigth"> <img  alt="skills"  width="50" height="50" src="https://user-images.githubusercontent.com/59892368/106370447-d783f580-6338-11eb-88b2-9886b1b0f8b3.png"></img> How to run the program? </h2>
</p>
 <ul>
   <li><img  alt="iconDownload"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/106370136-08166000-6336-11eb-8327-6fabcd50044a.png"></img>
If the system does not have python 3, install python 3 via the link: <a href="https://www.python.org/downloads/">Download Python 3</a>  
  <p align="center">
   <img  alt="gif_"  width="524" height="332" src="https://user-images.githubusercontent.com/59892368/106393036-67767d80-63d3-11eb-9e21-615b3c3bbf9f.png"></img>
</p>

</li>

   <li><img  alt="img_CommandPropt"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/106384969-86154e00-63ac-11eb-9c87-ce0e8d227ef6.png"></img> Open CMD, type or copy and paste " pip install gspread " and press Enter. [Obs: The execution has to be as administrator.]
   <p align="center">
   <img  alt="gif_"  width="516" height="452" src="https://user-images.githubusercontent.com/59892368/106384311-ee623080-63a8-11eb-9bf6-da6618680e6d.gif"></img>
   
   
</p>
   </li>
  
  
  
  
   
   <li><img  alt="img_PowerShell"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/106384881-0e472380-63ac-11eb-8243-54a2d45fa919.png"></img>
   Open the file folder CRUDGoogleSheets and in the address bar type " powershell ", in powershell window type " python main.py " and press Enter.  DONE ! Link: <a href="https://docs.google.com/spreadsheets/d/1Zeb0XsDxwcDERDv86uqenam2hBoerbu0Sagk6q4CzZ0/edit?usp=sharing"  target="_blank">Access to spreadsheets</a> 

 <p align="center">
   <img  alt="gif_"  width="800" height="500" src="https://user-images.githubusercontent.com/59892368/106386415-a0065f00-63b3-11eb-8e86-2f55ebadf5a3.gif"></img>
</p>


 <p align="center">
  <video  alt="gif_"  src="https://user-images.githubusercontent.com/59892368/158033052-ccbabac1-adb3-4480-a3eb-3c40ddc7d613.mp4"></video>
</p>
   
</li>
</ul>

<hr/>




<!-- --------------------------------------------------------------------------------------------->
<!-- --------------------------------------------  CREATE YOUY APPLICATION  ------------------------>
<!-- --------------------------------------------------------------------------------------------->
 <p>
    <h1 align="rigth"> <img  alt="icon_CreatingApplication"  width="50" height="50" src="https://user-images.githubusercontent.com/59892368/106482690-753c0980-648c-11eb-90bb-fce9aa3dc602.png"></img> Creating your application: </h1>
</p>

<p>
<img  alt="icon_Ideia"  width="35" height="35" src="https://user-images.githubusercontent.com/59892368/106907676-49fc2900-66dd-11eb-9f06-9cb7815aff69.png"></img> 
The file available here can be reused as long as you change the SpreadSheets access addresses. We'll see that in the topics below.
</p>

Here we will show you step by step from creating a project on Google Cloud Platform to use the APIs to running the Python program interacting with GoogleSheets.



 <p>
    <h3 align="rigth"> <img  alt="icon_Ideia"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/107301296-fdf11180-6a59-11eb-9315-a3eb7fade08b.png"></img> | Google Cloud Platform |</h3>
</p>


<ul>

<li>
<h3> 1st Step: Creating a project on Google Cloud Platform</h3>
  
  
Link access: <a href="https://console.cloud.google.com/home/dashboard"  >Access Google Cloud Platform</a> 


 <video  alt="gif_"  src="https://user-images.githubusercontent.com/59892368/115083007-26bfd800-9edd-11eb-99e8-f74586e532d1.mp4"></video>
 
 </li>


 
 <li>
  <h3>2nd Step: Enable the APIs  </h3>
 
  
 <video  alt="gif_"  src="https://user-images.githubusercontent.com/59892368/115083311-8ae29c00-9edd-11eb-9bdf-595b319ec31f.mp4"></video>
 
 
  

 
 </li>
 
 <li>
  <h3>3rd Step: Creation of credentials to generate the spreadsheet access certificate using a key.  </h3>
 
 
    
 <video  alt="gif_"  src="https://user-images.githubusercontent.com/59892368/115083985-9b474680-9ede-11eb-8f40-af7c6fc72d1d.mp4"></video>
 


 
 </li>
 
 <li>
  <h3> 4th Step: Create a key to access the spreadsheet.  </h3>

 
  <video  alt="gif_"  src="https://user-images.githubusercontent.com/59892368/115084001-a0a49100-9ede-11eb-98ef-02724b76d05a.mp4"></video>
 
 
 
 
 </li>

</ul>


<p>
<h3><img  alt="icon_GoogleSheets"  width="18" height="25" src="https://user-images.githubusercontent.com/59892368/107689797-1181bf80-6c88-11eb-8b71-3af7d1c8216b.png"></img> 
| GoogleSheets |</h3>
</p>

<ul>

<li>
  <h3>5th Step: Create GoogleSheets and configure the communication between the spreadsheet and the Python code using an email contained in the JSON file. Let's see:  </h3>
 
  
  <video  alt="gif_"  src="https://user-images.githubusercontent.com/59892368/115084008-a39f8180-9ede-11eb-9216-aca9c4380091.mp4"></video>
 
 

</li>
</ul>





<p>
 <h3 align="rigth"> <img  alt="icon_PyCharm"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/107302685-7c4eb300-6a5c-11eb-9020-c56443bd93d7.png"></img> | PyCharm |</h3>
</p>


<ul>
<li>
  <h3>6th Step: Download PyCharm  </h3>
 
 <a href="https://www.jetbrains.com/pt-br/pycharm/download/#section=windows"  target="_blank">Download</a> 
 
 
  <p align="center">
  <img  alt="img_downloadPyCharm"  width="800" height="400" src="https://user-images.githubusercontent.com/59892368/107673911-2dc83100-6c75-11eb-92b5-949672e8c788.PNG"></img>
</p>
 
 
</li>

<li>
  <h3>7th Step: Open PyCharm, New Project and Choose virtual environment venv  </h3>

 
   <video  alt="gif_"  src="https://user-images.githubusercontent.com/59892368/115084019-a7330880-9ede-11eb-99ba-1c09dad542c9.mp4"></video>
 

</li>

<li>
  <h3>8th Step: Install Gspread API in the virtual environment of the project so that it is possible to import into Python. Wait for installation ...  </h3>


 
   <video  alt="gif_"  src="https://user-images.githubusercontent.com/59892368/115084024-a9956280-9ede-11eb-8f71-a74a7caf95b8.mp4"></video>
 
 
</li>

<li>
  <h3>9th Step: Rename JSON file of the 4th step and insert in the project that is in PyCharm.  </h3>
 
   <video  alt="gif_"  src="https://user-images.githubusercontent.com/59892368/115084035-ab5f2600-9ede-11eb-9caa-8b7982e7590f.mp4"></video>
 


 
</li>



<li>
  <h3>10th Step: Start writing Python code. Import Gspread, configure it to access the spreadsheet using the JSON file and the spreadsheet's URL key. Come on:  </h3>

 
 ~~~ python
#importing gspread library
import gspread

#here, access to the credentials file, which contains all the data for the connection. Python <->GoogleCloudPlatform<->Spreadsheet
gc = gspread.service_account(filename='credentials.json') 

#specifies the spreadsheet using the URL key.
sh= gc.open_by_key('1TDlSR0yofAQsg7hpYjWUPbCXihbJAfIeySQdOYAet8I') 
~~~
 
 
 
 <video  alt="gif_"  src="https://user-images.githubusercontent.com/59892368/115084044-aef2ad00-9ede-11eb-9084-86e6351d366e.mp4"></video>
 
 


</li>



<li>
  <h3> 11th Step: Proceeding with the same code. Create an object directed to the sheet you wanted to work with. We will start by accessing sheet1, soon we will see how to create and access other sheets.  </h3>

 
 ~~~ python
 #....
 worksheet = sh.sheet1   #Access by sheet name.
 
 #OR
 
 worksheet = sh.get_worksheet(0) # Access by the index of each sheet.
 
~~~

 <h1 align="center"> <img  alt="icon_API_Gspread"  width="300" height="300" src="https://user-images.githubusercontent.com/59892368/107996958-6f801100-6fc0-11eb-810d-3b2fb7ec18d5.png"></img></h1>





 
</li>
<li>
  <h3>Done ! We can now play with all the CRUD functions in the worksheet through the created object called here as "worksheet."  </h3>
 
</li> 




</ul>

<!-- ------------------------------------------------------------------------------------->
<!-- -------------------------------------------- CREATE GSPREAD  ------------------------>
<!-- ------------------------------------------------------------------------------------->
 

 
 <p>
    <h1 align="rigth"> <img  alt="icon_API_Gspread"  width="50" height="50" src="https://user-images.githubusercontent.com/59892368/106465617-f4274700-6478-11eb-84ff-02f8a39fbc69.png"></img> GSPREAD </h1>
</p>

 >Gspread is an API that allows access to Google Spreadsheet, being for.

Following the steps of previous configurations, the starting point for using the Gspread functions is from this code:

~~~ python
import gspread

gc = gspread.service_account(filename='credentials.json')

sh= gc.open_by_key('1TDlSR0yofAQsg7hpYjWUPbCXihbJAfIeySQdOYAet8I')

worksheet = sh.get_worksheet(0)
 
~~~



<ul>
<li>
 <img  alt="icon_Create"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/106473765-f1c9ea80-6482-11eb-9b4d-ba4c77baa29f.png"></img> Creation
 </li>
 
 ~~~ python
 ...
                                            
worksheet = sh.add_worksheet(title="A worksheet", rows="25", cols="7")

#tittle = Spreadsheet name
#rows = Number of rows
#cols = Number of columns 
~~~
 
 
 <li>
  <img  alt="icon_Read"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/106475094-546fb600-6484-11eb-85b6-127f64e7b574.png"></img> Read
 </li>
 
 ~~~ python
 ...

worksheet = sh.get_worksheet(0)
   
val = worksheet.acell('B1').value
                                                 
~~~
OR

~~~ python
 ...

worksheet = sh.get_worksheet(0)
   
val = worksheet.cell(1, 2).value
                                                 
~~~



 <li>
 <img  alt="icon_Update"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/106475083-5174c580-6484-11eb-99f2-f7b54af686d6.png"></img> Update
 </li>
 
 ~~~ python
 ...

worksheet = sh.get_worksheet(0)
   
val = worksheet.cell(1, 2).value
                                                 
~~~
 
 <li>
 <img  alt="icon_Delete"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/106475088-52a5f280-6484-11eb-9bb1-0c3a62a494bc.png"></img> Delete
 </li>
 
  ~~~ python
 ...

worksheet = sh.get_worksheet(0)
   
worksheet.delete_row(10)
                                                 
~~~
 
 

</ul>

<!-- ------------------------------------------------------------------------------------->
<!------------------------------------LIST: STACKS , LIBS & TOOLS-->
<!-- ------------------------------------------------------------------------------------->

## <img  alt="skills"  width="40" height="40" src="https://user-images.githubusercontent.com/59892368/197614534-e12fb94a-b5cf-44ff-8d57-debad7299b0b.png"> Stacks <!---write here: learned concepts; -->

  
### Linguagem
  <a href="https://www.python.org"> ![Alt ou título da imagem](https://img.shields.io/badge/-Python-/?logo=Python&logoColor=white&color=yellow)<a/>
  * Language chosen to build this challenge.

  
### API
 [`Gspread`](https://docs.gspread.org/en/v5.7.0/) 
   * API used to access Google spreadsheets. Enabling actions of a CRUD through the Python language. 
### Sheets
 <a href="https://docs.google.com/spreadsheets/u/0/"> ![Alt ou título da imagem](https://img.shields.io/badge/-GoogleSheets-/?logo=GoogleSheets&logoColor=white&color=success)<a/>
   * Spreadsheet used to manipulate the information
 
 ### Versionameto
 <a href="https://git-scm.com"> ![Alt ou título da imagem](https://img.shields.io/badge/-Git-/?logo=Git&logoColor=white&color=red)<a/>
  * Tool used for code versioning.
 ### IDE
 <a href="https://code.visualstudio.com"> ![Alt ou título da imagem](https://img.shields.io/badge/-PyCharm-/?logo=PyCharm&logoColor=white&color=brightgreen)<a/> 
   * Tool used to build the project.



<!-- ------------------------------------------------------------------------------------->
<!-- -------------------------------------------- SOURCES  ------------------------>
<!-- ------------------------------------------------------------------------------------->


<h3 align="center"><img  alt="icon_Sources"  width="35" height="35" src="https://user-images.githubusercontent.com/59892368/106905459-11f3e680-66db-11eb-9c4d-6b45c1cb8c16.png"></img>BIBLIOGRAPHY:</h3>

<p > 1. PYTHON ENGINEER. Google Sheets and Python - Tutorial, 2020. Available in: <<a href="https://youtu.be/T1vqS1NL89E">https://youtu.be/T1vqS1NL89E</a>> . Access in: 29 de jan. de 2021.   </p>

<p > 2. GSPREAD. Read the Docs, 2021. Home page. Available in: <<a href="https://gspread.readthedocs.io/en/latest/">https://gspread.readthedocs.io/en/latest/</a>> . Access in: 29 de jan. de 2021.   </p>

<hr>
<p>
<h1> <img  alt="icon_Sources"  width="35" height="35" src="https://user-images.githubusercontent.com/59892368/108534741-3fcf5280-72b9-11eb-9d14-e7679c5d81ec.png"></img> I thank Tunts for providing me this challenge!  </h1>
<h2>I put myself in this duty, and I did it! </h2>
</p>



 
 
 
 
