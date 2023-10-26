const questions = [
    {
        question: "What is your favorite color?",
        options: [" red", "orange 2", "blue 3"]
    },
    {
        question: "What is your favorite animal?",
        options: ["Dog", "Cat", "Bird"]
    },
    {
        question: "What is your favorite food?",
        options: ["Pizza", "Burger", "Sushi"]
    },
    {
        question: "What is your favorite movie genre?",
        options: ["Action", "Comedy", "Drama"]
    },
    {
        question: "What is your favorite season?",
        options: ["Spring", "Summer", "Fall", "Winter"]
    }
];

let currentQuestionIndex = 0;
const questionContainer = document.getElementById("question-container");

function displayQuestion(index) {
    const question = questions[index];
    if (question) {
        questionContainer.innerHTML = `
            <div class="question">
                <p>Question ${index + 1}: ${question.question}</p>
            </div>
            <div class="options">
                ${question.options.map((option, optionIndex) => `
                    <label><input type="radio" name="question${index}" value="option${optionIndex}"> ${option}</label>
                `).join('')}
            </div>
            <div class="button-container">
                <button class="button" onclick="markForReview()">Mark for Review</button>
                <button class="button" onclick="clearResponse()">Clear Response</button>
                <button class="button" onclick="previousQuestion()">Previous</button>
                <button class="button" onclick="saveAndNext()">Save and Next</button>
                <button class="button" id="logout" type="submit"> Submit </button> 
            </div>
        `;
    }
}
function markForReview() {
    // Implement your code for marking the current question for review here.
    
}

function clearResponse() {
    // Implement your code for clearing the response to the current question here.
    const question = questions[currentQuestionIndex];
if (question) {
    const radioButtons = document.getElementsByName(`question${currentQuestionIndex}`);

    for (let i = 0; i < radioButtons.length; i++) {
        radioButtons[i].checked = false;
    }
}
}

function previousQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        displayQuestion(currentQuestionIndex);
    }
}

function saveAndNext() {
    // Implement your code to save the response for the current question here.
    if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        displayQuestion(currentQuestionIndex);
    }
    else {
     
    alert("Your Question is over ! if you sure answer have all done click submit button and finish your exam .");
}
}
displayQuestion(currentQuestionIndex);
