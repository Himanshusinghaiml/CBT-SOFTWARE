$(document).ready(function () {
        let currentQuestionId = 0; // Initialize with the first question's ID
        
        function loadQuestion(questionId) {
            $.ajax({
                url: `/get_next_question/${questionId}/`,
                method: 'GET',
                success: function (data) {
                    if (data.question_text) { 
                        $('#question_no').next('label').text(data.id);
                        $('#question-text').text(`Question ${data.id}: ${data.question_text}`);
                        $('#option1').next('label').text(data.option1);
                        $('#option2').next('label').text(data.option2);
                        $('#option3').next('label').text(data.option3);
                        $('#option4').next('label').text(data.option4);
                    } else {
                        alert('No more questions.');
                    }
                },
                error: function () {
                    alert('Failed to load the question.');
                }
            });
        }

        $('#next-button').click(function () {
            currentQuestionId += 1;
            loadQuestion(currentQuestionId);
        });

        $('#prev-button').click(function () {
            if (currentQuestionId >= 1) {
                currentQuestionId -= 1;
                loadQuestion(currentQuestionId);
            } else {
                alert('This is the first question.');
            }
        });

        // Load the initial question
        loadQuestion(currentQuestionId);
    });

