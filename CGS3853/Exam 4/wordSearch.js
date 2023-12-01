//Thurmond Guy
//U5440-0189

"use strict";
//variables used
var selectedLetters = "";
var selectedCells = [];
var allCells;
var solutionsShown = false;
var found = false;
/*
   Word Search Game Script
   
   Global Variables
   
   allCells
      References all of the cells in the word search table
      
   found
      Stores a Boolean value indicating whether the currently
      selected letters represents a word in the word search list.
     
   Function List
   
   function drawWordSearch(letters, words)
      Returns the HTML code for a word search table based on the entries
      in the letters array and the location of the words
      in the words array
      
   showList(list)
      Returns the HTML for code for an unordered list of words based
      on the items in the list array

*/

window.onload = init;

function init() {
   document.querySelectorAll("aside h1")[0].innerHTML = wordSearchTitle;
   document.getElementById("wordTable").innerHTML = drawWordSearch(letterGrid, wordGrid);
   document.getElementById("wordList").innerHTML = showList(wordArray);

   allCells = document.querySelectorAll("table#wordSearchTable td");
 
   // Mouse Pointer Cursor
   for (var i = 0; i < allCells.length; i++) {
      allCells[i].addEventListener("mouseover", function (event) {
         event.target.style.cursor = "pointer";
      });
   }
   
   //The default browser selection (blue background) is removed. 
   document.addEventListener("mousedown", function (event) {
      event.preventDefault();
      if (event.target.nodeName === "TD") {
         isMouseDown = true;
         handleCellClick(event);
      }
   });

   //Click
   document.addEventListener("mousedown", startSelection); 
   //Drag
   document.addEventListener("mouseover", continueSelection); 
   //Release
   document.addEventListener("mouseup", endSelection); 
   // Show Solution button
   document.getElementById("showSolution").addEventListener("click", showSolutions);

}

// Click function
function startSelection(event) {
   if (event.target.nodeName === "TD") { 
      var letter = event.target.innerHTML; 
      selectedLetters += letter;
      selectedCells.push(event.target); 
      //checks if the cell has been a found word
      if (event.target.style.backgroundColor !== "lightgreen") {
         event.target.style.backgroundColor = "pink"; 
      }
      document.getElementById("pickedLetters").value = selectedLetters;
   }
}

// Drag function
function continueSelection(event) {
   if (event.target.nodeName === "TD" && selectedCells.indexOf(event.target) === -1 && event.buttons === 1) { 
      var letter = event.target.innerHTML;
      selectedLetters += letter; //adds the letter to input box
      selectedCells.push(event.target); 
      if (event.target.style.backgroundColor !== "lightgreen") {
         event.target.style.backgroundColor = "pink";
      }
      document.getElementById("pickedLetters").value = selectedLetters;
   }
}

// Release function
function endSelection(event) {
   var wordIndex = wordArray.indexOf(selectedLetters); //checks if the selected letters are in the word array
   if (wordIndex !== -1) { 
      document.querySelectorAll("ul#wordSearchList li")[wordIndex].style.textDecoration = "line-through"; //crosses out the word in the list
      for (var i = 0; i < selectedCells.length; i++) {
         selectedCells[i].style.backgroundColor = "lightgreen"; //changes the background color of the selected cells to green
      }
      found = true; 
   } else { 
      for (var i = 0; i < selectedCells.length; i++) {
         if (selectedCells[i].style.backgroundColor !== "lightgreen") {
            selectedCells[i].style.backgroundColor = ""; // resets the background color
         }
      }
      found = false;
   }

   selectedLetters = "";  //resets the selected letters
   selectedCells = [];  //resets the selected cells
   document.getElementById("pickedLetters").value = "";  //resets the input box

   //Checks if all the words have been found
   var wordList = document.querySelectorAll("ul#wordSearchList li");
   var isComplete = true;

   for (var i = 0; i < wordList.length; i++) {
      if (wordList[i].style.textDecoration !== "line-through") {
         isComplete = false;
         break;
      }
   }
   if (isComplete) {
      // Delaying the alert so the last word can be highlighted
      setTimeout(function() {
         // alerting the user 
         alert("You solved the puzzle!");
         resetGame(); //resets the game after you hit OK on the alert
      }, 10);
   }
}

// Show Solution button
function showSolutions() {
   if (!solutionsShown) {
      allCells.forEach(cell => {
         cell.dataset.originalColor = cell.style.backgroundColor; // Store the original color
         if(cell.classList.contains("wordCell")) {
            cell.style.backgroundColor = "#a5d7e3";
         }
         cell.style.pointerEvents = "none"; // Disable click events
      });
      solutionsShown = true;
   } else {
      allCells.forEach(cell => {
         cell.style.backgroundColor = cell.dataset.originalColor || "#ffffff"; // Revert to the original color
         cell.style.pointerEvents = ""; // Enable click events
      });
      solutionsShown = false;
   }
}

// Reset the game
function resetGame() {
   // Reset the game state
   selectedLetters = "";
   selectedCells = [];
   solutionsShown = false;
   found = false;

   // Reset the UI
   document.getElementById("pickedLetters").value = "";
   allCells.forEach(cell => {
       cell.style.backgroundColor = "";
       cell.style.pointerEvents = "";
   });
   document.querySelectorAll("ul#wordSearchList li").forEach(li => {
       li.style.textDecoration = "";
   });
}

/*============================================================*/

function drawWordSearch(letters, words) {
   var rowSize = letters.length;
   var colSize = letters[0].length;

   var htmlCode = "<table id='wordSearchTable'>";
   htmlCode += "<caption>Word Search</caption>";

   for (var i = 0; i < rowSize; i++) {
      htmlCode += "<tr>";

      for (var j = 0; j < colSize; j++) {
         if (words[i][j] == " ") {
            htmlCode += "<td>";
         } else {
            htmlCode += "<td class='wordCell'>";
         }
         htmlCode += letters[i][j];
         htmlCode += "</td>";
      }

      htmlCode += "</tr>";
   }
   htmlCode += "</table>";

   return htmlCode;
}

function showList(list) {
   var htmlCode = "<ul id='wordSearchList'>";

   for (var i = 0; i < list.length; i++) {
      htmlCode += "<li>" + list[i] + "</li>";
   }

   htmlCode += "</ul>";

   return htmlCode;
}