document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.interest-button');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            button.classList.toggle('selected');
        });
    });

    document.querySelector('form').addEventListener('submit', (event) => {
        const selectedInterests = [];
        document.querySelectorAll('.interest-button.selected').forEach(button => {
            selectedInterests.push(button.getAttribute('data-value'));
        });

        const hiddenInput = document.createElement('input');
        hiddenInput.type = 'hidden';
        hiddenInput.name = 'ci';
        hiddenInput.value = selectedInterests.join(',');
        event.target.appendChild(hiddenInput);
    });
});