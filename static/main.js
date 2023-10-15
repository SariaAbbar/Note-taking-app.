let userName = localStorage.getItem("name");
//function that take the username if it exist and say welcome back to him
// if its dont exist say just welcome and his name
function sayWelcome(userName, isNewUser) {
  let welcome = document.getElementById("welcome");
  const newWelcome = document.createElement("p");
  newWelcome.innerText =
    (isNewUser ? "Welcome " : "Welcome back, ") + userName + " !";
  welcome.appendChild(newWelcome);
}
if (userName) {
  sayWelcome(userName, false);
} else {
  // If it's not, show the modal dialog asking for the user's name
  let modal = document.getElementById("modal");
  modal.style.display = "block";
  // When clicking on 'OK', save the name in Local Storage and hide the modal
  let saveBtn = document.getElementById("saveBtn");

  // Save the user's name in the local storage and close the modal when the Save button is clicked
  saveBtn.addEventListener("click", function () {
    let nameInput = document.getElementById("nameInput");
    // if his name inside the local storage bring it and put welcome and the name
    if (nameInput.value) {
      localStorage.setItem("name", nameInput.value);
      userName = nameInput.value;
      sayWelcome(userName, true);
      modal.style.display = "none";
    }
  });
}
