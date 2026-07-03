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

/* =========================================================
   FINFLOW WEB APP DEMO
   Dashboard fijo + módulos dinámicos
========================================================= */

const STORAGE_KEY_MODULES = "finflowActiveModules";
const STORAGE_KEY_MOVEMENTS = "finflowDemoMovements";

const moduleToggles = document.querySelectorAll(".module-toggle");
const moduleSections = document.querySelectorAll(".module-section");
const activeModulePill = document.getElementById("activeModulePill");
const emptyModulesState = document.getElementById("emptyModulesState");
const resetDemoButton = document.getElementById("resetDemoButton");

const incomeForm = document.getElementById("incomeForm");
const expenseForm = document.getElementById("expenseForm");

const demoIncomeTotal = document.getElementById("demoIncomeTotal");
const demoExpenseTotal = document.getElementById("demoExpenseTotal");
const demoProfit = document.getElementById("demoProfit");
const demoMovementCount = document.getElementById("demoMovementCount");
const movementList = document.getElementById("movementList");
const demoStatus = document.getElementById("demoStatus");

let demoMovements = JSON.parse(localStorage.getItem(STORAGE_KEY_MOVEMENTS)) || [];

function formatCurrency(amount) {
    return "Q " + Number(amount).toLocaleString("es-GT");
}

function saveDemoMovements() {
    localStorage.setItem(STORAGE_KEY_MOVEMENTS, JSON.stringify(demoMovements));
}

function calculateDemoTotals() {
    let totalIncome = 0;
    let totalExpense = 0;

    for (let i = 0; i < demoMovements.length; i++) {
        if (demoMovements[i].type === "income") {
            totalIncome = totalIncome + demoMovements[i].amount;
        } else if (demoMovements[i].type === "expense") {
            totalExpense = totalExpense + demoMovements[i].amount;
        }
    }

    return {
        income: totalIncome,
        expense: totalExpense,
        profit: totalIncome - totalExpense
    };
}

function renderDemoApp() {
    const totals = calculateDemoTotals();

    if (demoIncomeTotal) {
        demoIncomeTotal.textContent = formatCurrency(totals.income);
    }

    if (demoExpenseTotal) {
        demoExpenseTotal.textContent = formatCurrency(totals.expense);
    }

    if (demoProfit) {
        demoProfit.textContent = formatCurrency(totals.profit);
    }

    if (demoMovementCount) {
        demoMovementCount.textContent = demoMovements.length;
    }

    if (!movementList) {
        return;
    }

    movementList.innerHTML = "";

    if (demoMovements.length === 0) {
        movementList.innerHTML = '<p class="empty-demo-message">Todavía no hay movimientos registrados.</p>';
        return;
    }

    for (let i = demoMovements.length - 1; i >= 0; i--) {
        const movement = demoMovements[i];

        const item = document.createElement("div");
        item.classList.add("movement-item");

        const type = document.createElement("span");
        type.classList.add("movement-type");

        if (movement.type === "income") {
            type.classList.add("income");
            type.textContent = "Ingreso";
        } else {
            type.classList.add("expense");
            type.textContent = "Gasto";
        }

        const detail = document.createElement("div");
        detail.classList.add("movement-detail");
        detail.innerHTML =
            "<strong>" +
            movement.description +
            "</strong><span>" +
            movement.category +
            " · " +
            movement.date +
            "</span>";

        const amount = document.createElement("div");
        amount.classList.add("movement-amount");
        amount.textContent = formatCurrency(movement.amount);

        item.appendChild(type);
        item.appendChild(detail);
        item.appendChild(amount);

        movementList.appendChild(item);
    }
}

function addDemoMovement(type, description, category, amount) {
    const movement = {
        type: type,
        description: description,
        category: category,
        amount: Number(amount),
        date: new Date().toLocaleDateString("es-GT")
    };

    demoMovements.push(movement);
    saveDemoMovements();
    renderDemoApp();

    if (demoStatus) {
        if (type === "income") {
            demoStatus.textContent = "Ingreso agregado correctamente";
        } else {
            demoStatus.textContent = "Gasto agregado correctamente";
        }
    }
}

function getActiveModules() {
    const saved = localStorage.getItem(STORAGE_KEY_MODULES);

    if (!saved) {
        return [];
    }

    try {
        const parsed = JSON.parse(saved);

        if (Array.isArray(parsed)) {
            return parsed;
        }

        return [];
    } catch (error) {
        return [];
    }
}

function saveActiveModules(activeModules) {
    localStorage.setItem(STORAGE_KEY_MODULES, JSON.stringify(activeModules));
}

function renderModules() {
    const activeModules = [];

    for (let i = 0; i < moduleToggles.length; i++) {
        if (moduleToggles[i].checked) {
            activeModules.push(moduleToggles[i].value);
        }
    }

    for (let i = 0; i < moduleSections.length; i++) {
        const sectionModule = moduleSections[i].dataset.module;
        const isActive = activeModules.includes(sectionModule);

        if (isActive) {
            moduleSections[i].classList.remove("hidden");
        } else {
            moduleSections[i].classList.add("hidden");
        }
    }

    if (activeModulePill) {
        activeModulePill.textContent = activeModules.length + " módulos activos";
    }

    if (emptyModulesState) {
        if (activeModules.length === 0) {
            emptyModulesState.classList.add("visible");
        } else {
            emptyModulesState.classList.remove("visible");
        }
    }

    saveActiveModules(activeModules);
}

function restoreModules() {
    const activeModules = getActiveModules();

    for (let i = 0; i < moduleToggles.length; i++) {
        moduleToggles[i].checked = activeModules.includes(moduleToggles[i].value);
        moduleToggles[i].addEventListener("change", renderModules);
    }

    renderModules();
}

if (incomeForm) {
    incomeForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const incomeDescription = document.getElementById("incomeDescription").value.trim();
        const incomeCategory = document.getElementById("incomeCategory").value.trim();
        const incomeAmount = Number(document.getElementById("incomeAmount").value);

        if (!incomeDescription || !incomeCategory || incomeAmount <= 0) {
            if (demoStatus) {
                demoStatus.textContent = "Complete correctamente el ingreso";
            }
            return;
        }

        addDemoMovement("income", incomeDescription, incomeCategory, incomeAmount);
        incomeForm.reset();
    });
}

if (expenseForm) {
    expenseForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const expenseDescription = document.getElementById("expenseDescription").value.trim();
        const expenseCategory = document.getElementById("expenseCategory").value.trim();
        const expenseAmount = Number(document.getElementById("expenseAmount").value);

        if (!expenseDescription || !expenseCategory || expenseAmount <= 0) {
            if (demoStatus) {
                demoStatus.textContent = "Complete correctamente el gasto";
            }
            return;
        }

        addDemoMovement("expense", expenseDescription, expenseCategory, expenseAmount);
        expenseForm.reset();
    });
}

if (resetDemoButton) {
    resetDemoButton.addEventListener("click", function () {
        demoMovements = [];
        saveDemoMovements();

        localStorage.removeItem(STORAGE_KEY_MODULES);

        for (let i = 0; i < moduleToggles.length; i++) {
            moduleToggles[i].checked = false;
        }

        renderDemoApp();
        renderModules();

        if (demoStatus) {
            demoStatus.textContent = "Demo reiniciada";
        }
    });
}

renderDemoApp();
restoreModules();

