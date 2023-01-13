// constant definitions
const dropDownMenu = document.getElementById("options-list");
const selectBtn = document.querySelector(".select-btn");
const dropDownMenuOptions = document.querySelectorAll(".option")

// display informations on screen
console.log("dropDownMenu is: ", dropDownMenu);
console.log("dropDownMenu style is:", dropDownMenu.style.display)
console.log("dropDownMenu display is: ", getComputedStyle(dropDownMenu).display);
console.log("selectBtn is: ", selectBtn);
console.log("dropDownMenuOptions is: ", dropDownMenuOptions);
console.log("dropDownMenu style is:", dropDownMenu.style.display)

// when clicking on menu favicon 
selectBtn.addEventListener("click", () => {
    if (getComputedStyle(dropDownMenu).display == "block") {
        dropDownMenu.style.display = "none"
    }
    else {
        dropDownMenu.style.display = "block"
    }
});

// when selecting an option
dropDownMenuOptions.forEach((option) => {
    option.addEventListener("click", () => {
        let selectedOption = option.querySelector(".option-text").innerText;
        console.log("option selected inner text :", selectedOption);
        dropDownMenu.style.display = "none"
    })
});