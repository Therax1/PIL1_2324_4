// Pour le texte avant tout 

document.addEventListener("DOMContentLoaded", function() {
    const textElement = document.getElementById('Accrocheur');
    const text = textElement.textContent;
    textElement.textContent = ''; // Clear the text content to start with an empty paragraph
    let index = 0;
    const speed = 13; // Speed in milliseconds
  
    function typeWriter() {
      if (index < text.length) {
        textElement.textContent += text.charAt(index);
        index++;
        setTimeout(typeWriter, speed);
      }
    }
  
    // Intersection Observer callback function
    function onIntersection(entries, observer) {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          typeWriter();
          observer.disconnect(); // Stop observing once animation has started
        }
      });
    }
  
    // Create an Intersection Observer
    const observer = new IntersectionObserver(onIntersection, {
      threshold: 1.0
    });
  
    // Start observing the text element
    observer.observe(textElement);
  });


  
// Pour les Image des filles là 
// Première image 

document.addEventListener('DOMContentLoaded', () => {
    const target = document.querySelector('.container1');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                target.classList.add('visible');
            } else {
                target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    observer.observe(target);
});

// Deuxièeme Fille image 

document.addEventListener('DOMContentLoaded', () => {
    const target = document.querySelector('.container2');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                target.classList.add('visible');
            } else {
                target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    observer.observe(target);
});

// Troisième Fille image 

document.addEventListener('DOMContentLoaded', () => {
    const target = document.querySelector('.container3');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                target.classList.add('visible');
            } else {
                target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    observer.observe(target);
});

// Quatrième Fille image 

document.addEventListener('DOMContentLoaded', () => {
    const target = document.querySelector('.container4');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                target.classList.add('visible');
            } else {
                target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    observer.observe(target);
});


// Cinquième Fille image 

document.addEventListener('DOMContentLoaded', () => {
    const target = document.querySelector('.container5');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                target.classList.add('visible');
            } else {
                target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    observer.observe(target);
});


// Pour les Image des avis
// Première Image 
document.addEventListener('DOMContentLoaded', () => {
    const target = document.querySelector('.avi1');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                target.classList.add('visible');
            } else {
                target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    observer.observe(target);
});

// Deuxième image 

document.addEventListener('DOMContentLoaded', () => {
    const target = document.querySelector('.avi2');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                target.classList.add('visible');
            } else {
                target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    observer.observe(target);
});

// Troisième image 

document.addEventListener('DOMContentLoaded', () => {
    const target = document.querySelector('.avi3');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                target.classList.add('visible');
            } else {
                target.classList.remove('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    observer.observe(target);
});

