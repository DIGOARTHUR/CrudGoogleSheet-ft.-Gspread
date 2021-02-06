# Py-01-DesafioTunts [Estágio Processo Seletivo 2021]  <img  alt="skills"  width="35" height="35" src="https://user-images.githubusercontent.com/59892368/106386750-4acb4d00-63b5-11eb-8d43-be0469cc0a3c.PNG">


 

  <p>
    <h5 align="rigth"> <img  alt="skills"  width="30" height="30" src="https://user-images.githubusercontent.com/59892368/106370549-bc65b580-6339-11eb-9f43-1272219dcb8b.png"></img> Topic for the selection process </h5>
</p>

 
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
<img  alt="icon_Ideia"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/106907676-49fc2900-66dd-11eb-9f06-9cb7815aff69.png"></img> 
The file available here can be reused as long as you change the SpreadSheets access addresses. We'll see that in the topics below.
</p>

Here we will show you step by step from creating a project on Google Cloud Platform to use the APIs to running the Python program interacting with GoogleSheets.

<ul>
<li>
 1º Step: Creating a project on Google Cloud Platform
 
  
Link access: <a href="https://console.cloud.google.com/home/dashboard"  >Access to spreadsheets</a> 

 <p align="center">
   <img  alt="gif_1Step"  width="1000" height="450" src="https://user-images.githubusercontent.com/59892368/106952976-9a40ae80-6710-11eb-9651-52a3029faf2c.gif"></img>
</p>
 
 
 </li>

 
 
 <li>
   2º Step: Enable the APIs
 
  <p align="center">
   <img  alt="gif_2Step"  width="1000" height="450" src="https://user-images.githubusercontent.com/59892368/106958395-0ffc4880-6718-11eb-8ef5-2395290fa5d0.gif"></img>
</p>
 
 </li>
 
 <li>
 3º Step: Creation of credentials to generate the spreadsheet access protocol using a key, for example.
 
  <p align="center">
   <img  alt="gif_3Step"  width="1000" height="450" src="https://user-images.githubusercontent.com/59892368/107101957-ace1e300-67f7-11eb-8618-69c81c39ad81.gif"></img>
</p>
 
 </li>
 
 <li>
 4º Step: Create a key to access the spreadsheet, either publicly or privately.
 
  <p align="center">
   <img  alt="gif_3Step"  width="1000" height="450" src="https://user-images.githubusercontent.com/59892368/107101957-ace1e300-67f7-11eb-8618-69c81c39ad81.gif"></img>
</p>
 
 </li>

</ul>



<!-- ------------------------------------------------------------------------------------->
<!-- -------------------------------------------- CREATE GSPREAD  ------------------------>
<!-- ------------------------------------------------------------------------------------->
 <p>
    <h1 align="rigth"> <img  alt="icon_API_Gspread"  width="50" height="50" src="https://user-images.githubusercontent.com/59892368/106465617-f4274700-6478-11eb-84ff-02f8a39fbc69.png"></img> GSPREAD </h1> Gspread is an API that allows access to Google Spreadsheet, being for:
</p>


<ul>
<li>
 <img  alt="icon_Create"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/106473765-f1c9ea80-6482-11eb-9b4d-ba4c77baa29f.png"></img> Creation
 </li>
 
 <li>
  <img  alt="icon_Read"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/106475094-546fb600-6484-11eb-85b6-127f64e7b574.png"></img> Read
 </li>
 
 <li>
 <img  alt="icon_Update"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/106475083-5174c580-6484-11eb-99f2-f7b54af686d6.png"></img> Update
 </li>
 
 <li>
 <img  alt="icon_Delete"  width="25" height="25" src="https://user-images.githubusercontent.com/59892368/106475088-52a5f280-6484-11eb-9bb1-0c3a62a494bc.png"></img> Delete
 </li>

</ul>


<!-- ------------------------------------------------------------------------------------->
<!-- -------------------------------------------- SOURCES  ------------------------>
<!-- ------------------------------------------------------------------------------------->
<h3><img  alt="icon_Sources"  width="35" height="35" src="https://user-images.githubusercontent.com/59892368/106905459-11f3e680-66db-11eb-9c4d-6b45c1cb8c16.png"></img>
SOURCES:</h3>

<h2><img  alt="icon_CreatingApplication"  width="50" height="50" src="https://user-images.githubusercontent.com/59892368/106508490-37021280-64ab-11eb-81e0-3ca45e0eb38a.png"></img>
... SOON MORE DOCUMENTATION UPDATES</h1>
 
 
 
 
