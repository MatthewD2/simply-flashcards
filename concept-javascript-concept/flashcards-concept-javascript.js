function createFlashcardSet() {
    var i = 0
    while(i < 2) {
        console.log("What do you want on the front?");
        console.log("What do you want on the back?");
        i++;
    }
    return false; 
}

function createFlashcard(chosen_front, chosen_back) {
    if (document.getElementById("create_flashcard") == "Yes") {
        return "You want to create a flashcard";
    }
    const flashcard = {
        "front" : chosen_front,
        "back" : chosen_back
    }; 
    return flashcard;
}

function yes() {
    document.getElementById("create_flashcards").style.display = "none";
    document.getElementById("no_button").style.display = "none";
    document.getElementById("yes_button").style.display = "none";
    document.getElementById("front_option").style.display = "block";
    document.getElementById("front_input").style.display = "block"
    document.getElementById("back_option").style.display = "block";
    document.getElementById("back_input").style.display = "block"
    document.getElementById("submit").style.display = "block";
    document.getElementById("front_option").innerHTML = "What's on the front?";
    document.getElementById("back_option").innerHTML = "What's on the back?";
}

function no() {
    document.getElementById("create_flashcards").style.display = "none";
    document.getElementById("no_button").style.display = "none";
    document.getElementById("yes_button").style.display = "none";
    document.getElementById("front_option").style.display = "none";
    document.getElementById("front_input").style.display = "none";
    document.getElementById("back_option").style.display = "none";
    document.getElementById("back_input").style.display = "none";
    document.getElementById("submit").style.display = "none";
}

function submit() {
    document.getElementById("create_flashcards").style.display = "block";
    document.getElementById("no_button").style.display = "inline";
    document.getElementById("yes_button").style.display = "inline";
    document.getElementById("front_option").style.display = "none";
    var Item = document.getElementById("front_input").value;
    document.getElementById("front_input").style.display = "none";
    document.getElementById("back_option").style.display = "none";
    document.getElementById("back_input").style.display = "none";
    document.getElementById("submit").style.display = "none";
    // const storedFront = localStorage.getItem("front_input");
    // document.getElementById("stored_front").innerHTML = storedFront;
    document.getElementById("stored_front").style.display = "inline";
    // var storedFront = localStorage.getItem("storedFront");
    // localStorage.setItem("storedFront", Item).value;
    // document.getElementById("savedText").innerHTML = Item + " SAVED";
}

const input_stored = document.querySelector(".front_input"),
        side_stored = document.querySelector(".stored_front");
input_stored.addEventListener('keyup', displayInput);

function displayInput() {
    side_stored.innerHTML = input_stored.value;
}

// const form = document.querySelector('form');
console.log(createFlashcard("Hola", "Hello"));

