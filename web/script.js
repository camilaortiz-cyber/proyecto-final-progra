const preloader = document.getElementById("preloader");
const spotlight = document.getElementById("spotlight");
const pageProgress = document.getElementById("pageProgress");
const revealElements = document.querySelectorAll(".reveal");
const counterElements = document.querySelectorAll("[data-counter]");
const moduleCards = document.querySelectorAll(".module-card");
const filterButtons = document.querySelectorAll(".filter-button");
const assistantLine = document.getElementById("assistantLine");
const closingQuote = document.getElementById("closingQuote");
const magneticElements = document.querySelectorAll(".magnetic");

window.addEventListener("load", function () {
    setTimeout(function () {
        if (preloader) {
            preloader.classList.add("hide");
        }
    }, 650);
});

window.addEventListener("scroll", function () {
    const scrollTop = window.scrollY;
    const documentHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = documentHeight > 0 ? (scrollTop / documentHeight) * 100 : 0;

    if (pageProgress) {
        pageProgress.style.width = progress + "%";
    }
});

document.addEventListener("mousemove", function (event) {
    if (spotlight) {
        spotlight.style.left = event.clientX + "px";
        spotlight.style.top = event.clientY + "px";
    }
});

const revealObserver = new IntersectionObserver(
    function (entries) {
        for (let i = 0; i < entries.length; i++) {
            if (entries[i].isIntersecting) {
                entries[i].target.classList.add("is-visible");
                revealObserver.unobserve(entries[i].target);
            }
        }
    },
    {
        threshold: 0.16
    }
);

for (let i = 0; i < revealElements.length; i++) {
    revealObserver.observe(revealElements[i]);
}

function formatNumber(number) {
    return Math.floor(number).toLocaleString("es-GT");
}

function animateCounter(element) {
    const target = Number(element.dataset.target);
    const duration = 1400;
    const startTime = performance.now();

    function updateCounter(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easedProgress = 1 - Math.pow(1 - progress, 4);
        const currentValue = target * easedProgress;

        element.textContent = formatNumber(currentValue);

        if (progress < 1) {
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = formatNumber(target);
        }
    }

    requestAnimationFrame(updateCounter);
}

const counterObserver = new IntersectionObserver(
    function (entries) {
        for (let i = 0; i < entries.length; i++) {
            if (entries[i].isIntersecting) {
                animateCounter(entries[i].target);
                counterObserver.unobserve(entries[i].target);
            }
        }
    },
    {
        threshold: 0.6
    }
);

for (let i = 0; i < counterElements.length; i++) {
    counterObserver.observe(counterElements[i]);
}

for (let i = 0; i < moduleCards.length; i++) {
    moduleCards[i].addEventListener("mousemove", function (event) {
        const rect = moduleCards[i].getBoundingClientRect();
        const x = ((event.clientX - rect.left) / rect.width) * 100;
        const y = ((event.clientY - rect.top) / rect.height) * 100;

        moduleCards[i].style.setProperty("--x", x + "%");
        moduleCards[i].style.setProperty("--y", y + "%");
    });

    moduleCards[i].addEventListener("click", function () {
        const moduleName = moduleCards[i].dataset.moduleName;
        const status = moduleCards[i].dataset.status;

        if (assistantLine) {
            if (status === "mvp") {
                assistantLine.textContent =
                    "Módulo seleccionado: " +
                    moduleName +
                    ". Este módulo forma parte del MVP funcional de FinFlow y puede activarse según las necesidades de cada empresa.";
            } else {
                assistantLine.textContent =
                    "Módulo seleccionado: " +
                    moduleName +
                    ". Este módulo pertenece a la visión futura de FinFlow como plataforma financiera escalable.";
            }
        }
    });
}

for (let i = 0; i < filterButtons.length; i++) {
    filterButtons[i].addEventListener("click", function () {
        const filter = filterButtons[i].dataset.filter;

        for (let j = 0; j < filterButtons.length; j++) {
            filterButtons[j].classList.remove("active");
        }

        filterButtons[i].classList.add("active");

        for (let k = 0; k < moduleCards.length; k++) {
            const status = moduleCards[k].dataset.status;

            if (filter === "all" || filter === status) {
                moduleCards[k].classList.remove("hidden");
            } else {
                moduleCards[k].classList.add("hidden");
            }
        }
    });
}

const quotes = [
    "“Cuando los números están claros, trabajar se siente distinto.”",
    "“Una empresa ordenada toma mejores decisiones.”",
    "“Finanzas simples. Operaciones más inteligentes.”",
    "“El control financiero también puede sentirse elegante.”"
];

let quoteIndex = 0;

setInterval(function () {
    if (closingQuote) {
        quoteIndex = quoteIndex + 1;

        if (quoteIndex >= quotes.length) {
            quoteIndex = 0;
        }

        closingQuote.style.opacity = "0";

        setTimeout(function () {
            closingQuote.textContent = quotes[quoteIndex];
            closingQuote.style.opacity = "1";
        }, 300);
    }
}, 4200);

for (let i = 0; i < magneticElements.length; i++) {
    magneticElements[i].addEventListener("mousemove", function (event) {
        const rect = magneticElements[i].getBoundingClientRect();
        const x = event.clientX - rect.left - rect.width / 2;
        const y = event.clientY - rect.top - rect.height / 2;

        magneticElements[i].style.transform =
            "translate(" + x * 0.12 + "px, " + y * 0.18 + "px)";
    });

    magneticElements[i].addEventListener("mouseleave", function () {
        magneticElements[i].style.transform = "translate(0, 0)";
    });
}