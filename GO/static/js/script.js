let currentProfileIndex = 1;
const totalProfiles = 3;

function loadProfile(index) {
    for (let i = 1; i <= totalProfiles; i++) {
        document.getElementById(`profile-card-${i}`).style.display = i === index ? 'block' : 'none';
        document.getElementById(`profile-details-${i}`).style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    loadProfile(currentProfileIndex);
});

function nextProfile(like) {
    const profileCard = document.getElementById(`profile-card-${currentProfileIndex}`);
    profileCard.style.transform = 'translateX(' + (like ? '100%' : '-100%') + ')';
    profileCard.style.opacity = '0';

    setTimeout(() => {
        currentProfileIndex = (currentProfileIndex % totalProfiles) + 1;
        loadProfile(currentProfileIndex);
        const newProfileCard = document.getElementById(`profile-card-${currentProfileIndex}`);
        newProfileCard.style.transform = 'translateX(0)';
        newProfileCard.style.opacity = '1';
    }, 1000);
}

function toggleDetails(index) {
    const container = document.querySelector('.container');
    const profileDetails = document.getElementById(`profile-details-${index}`);

    if (profileDetails.style.display === 'none' || profileDetails.style.display === '') {
        profileDetails.style.display = 'block';
        setTimeout(() => { // Permet à l'élément de devenir visible avant d'ajouter la classe
            container.classList.add('transformed');
        }, 10); // Petite temporisation pour garantir que l'affichage a bien eu lieu
    } else {
        container.classList.remove('transformed');
        setTimeout(() => { // Permet à la transition de se terminer avant de cacher l'élément
            profileDetails.style.display = 'none';
        }, 1000); // Durée de la transition
    }
}
