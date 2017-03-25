function IsNum(v)
{
   var ValidChars = "0123456789";
   var IsNumber=true;
   var Char;


   for (i = 0; i < v.length && IsNumber == true; i++)
      {
      Char = v.charAt(i);
      if (ValidChars.indexOf(Char) == -1)
         {
         IsNumber = false;
         }
      }
   return IsNumber;

}
function changeRGB(){
   var r = document.getElementById('txtR').value;
   var g = document.getElementById('txtG').value;
   var b = document.getElementById('txtB').value;
   if(!IsNum(r) || !IsNum(g) || !IsNum(b)){
      document.getElementById('codigoRGB').innerHTML = '<strong style="color=#FF0000">Números inválidos!</strong>';
	  return;
   }
   var rH = eval(r).toString(16);
   var gH = eval(g).toString(16);
   var bH = eval(b).toString(16);
   var code = "#"
   if(rH.length==1)
      code += "0";
   code += rH;
   if(gH.length==1)
      code += "0";
   code += gH;
   if(bH.length==1)
      code += "0";
   code += bH;
   document.getElementById('codigoRGB').innerHTML = "<strong>Código RGB: </strong>"+code+"<div style='background-color:"+code+"; height:50px; width:300px;'>&nbsp;</div>";
}

function changeColor(){
	document.getElementById("representacaoDaCor").style.backgroundColor = document.getElementById('txtCor').value;
}
