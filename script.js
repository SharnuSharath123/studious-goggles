document.addEventListener('DOMContentLoaded', () => {
    const quizForm = document.getElementById('quiz-form');
    quizForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const answers = new FormData(quizForm);
        // Process the answers, send to the server, etc.
    });
});
