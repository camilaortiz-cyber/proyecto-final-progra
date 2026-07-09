
// ======================================================
// CERRAR SESIÓN GLOBAL Y SEGURO
// ======================================================
// Este bloque captura cualquier botón que diga "Cerrar sesión".
// No depende de variables internas como experienceApp.
// Limpia toda la sesión y regresa al login.

document.addEventListener("click", function (event) {
    const elemento = event.target;

    if (!elemento) {
        return;
    }

    const textoBoton = elemento.textContent.trim().toLowerCase();

    if (textoBoton === "cerrar sesión" || textoBoton === "cerrar sesion") {
        event.preventDefault();
        event.stopPropagation();
        event.stopImmediatePropagation();

        localStorage.clear();
        sessionStorage.clear();

        window.location.href = "/";
    }
}, true);

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
            preloader.style.display = "none";
        }
    }, 650);
});

setTimeout(function () {
    if (preloader) {
        preloader.classList.add("hide");
        preloader.style.display = "none";
    }
}, 2500);

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

// Agrega ID a movimientos antiguos que fueron creados antes de esta mejora.
for (let i = 0; i < demoMovements.length; i++) {
    if (!demoMovements[i].id) {
        demoMovements[i].id = Date.now() + "-" + i;
    }
}

// Guarda los movimientos antiguos ya corregidos con ID.
saveDemoMovements();

function formatCurrency(amount) {
    let currency = "Q";

    try {
        const settings = JSON.parse(localStorage.getItem("finflowCompanySettings"));

        if (settings && settings.currency) {
            currency = settings.currency;
        }
    } catch (error) {
        currency = "Q";
    }

    return currency + " " + Number(amount).toLocaleString("es-GT");
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
    // Agrega un ID único a movimientos antiguos que no lo tengan.
    for (let i = 0; i < demoMovements.length; i++) {
        if (!demoMovements[i].id) {
            demoMovements[i].id = "movement-" + Date.now() + "-" + i;
        }
    }

    // Guarda movimientos corregidos con ID.
    saveDemoMovements();

    // Calcula los totales actuales de ingresos, gastos y utilidad.
    const totals = calculateDemoTotals();

    // Actualiza el total de ingresos en el dashboard.
    if (demoIncomeTotal) {
        demoIncomeTotal.textContent = formatCurrency(totals.income);
    }

    // Actualiza el total de gastos en el dashboard.
    if (demoExpenseTotal) {
        demoExpenseTotal.textContent = formatCurrency(totals.expense);
    }

    // Actualiza la utilidad si existe ese elemento en el HTML.
    if (demoProfit) {
        demoProfit.textContent = formatCurrency(totals.profit);
    }

    // Actualiza la cantidad de movimientos.
    if (demoMovementCount) {
        demoMovementCount.textContent = demoMovements.length;
    }

    // Si no existe la lista de movimientos, detiene la función.
    if (!movementList) {
        return;
    }

    // Limpia la lista antes de volver a pintarla.
    movementList.innerHTML = "";

    // Si no hay movimientos, muestra mensaje vacío.
    if (demoMovements.length === 0) {
        movementList.innerHTML = '<p class="empty-demo-message">Todavía no hay movimientos registrados.</p>';
        return;
    }

    // Recorre movimientos del más nuevo al más antiguo.
    for (let i = demoMovements.length - 1; i >= 0; i--) {
        const movement = demoMovements[i];

        // Crea la tarjeta del movimiento.
        const item = document.createElement("div");
        item.classList.add("movement-item");
        item.dataset.movementId = movement.id;

        // Crea la etiqueta de tipo: ingreso o gasto.
        const type = document.createElement("span");
        type.classList.add("movement-type");

        // Personaliza etiqueta según tipo.
        if (movement.type === "income") {
            type.classList.add("income");
            type.textContent = "Ingreso";
        } else {
            type.classList.add("expense");
            type.textContent = "Gasto";
        }

        // Crea el detalle del movimiento.
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

        // Crea el monto del movimiento.
        const amount = document.createElement("div");
        amount.classList.add("movement-amount");
        amount.textContent = formatCurrency(movement.amount);

        // Crea el menú de acciones.
        const menuWrapper = document.createElement("div");
        menuWrapper.classList.add("action-menu-wrapper");

        // Crea el botón de tres puntos.
        const menuButton = document.createElement("button");
        menuButton.type = "button";
        menuButton.textContent = "⋯";
        menuButton.classList.add("action-menu-button");
        menuButton.setAttribute("aria-label", "Abrir acciones del movimiento");

        // Crea el menú desplegable.
        const menu = document.createElement("div");
        menu.classList.add("action-menu");

        // Agrega la opción de eliminar movimiento usando ID, no índice.
        menu.innerHTML =
            '<button type="button" class="movement-delete-button danger" data-movement-id="' +
            movement.id +
            '">Eliminar movimiento</button>';

        // Une botón y menú.
        menuWrapper.appendChild(menuButton);
        menuWrapper.appendChild(menu);

        // Agrega elementos a la tarjeta.
        item.appendChild(type);
        item.appendChild(detail);
        item.appendChild(amount);
        item.appendChild(menuWrapper);

        // Agrega tarjeta a la lista.
        movementList.appendChild(item);
    }
}

function addDemoMovement(type, description, category, amount) {
    // Crea un movimiento nuevo con un ID único para poder eliminarlo correctamente.
    const movement = {
        id: Date.now() + "-" + Math.random().toString(16).slice(2), // ID único del movimiento.
        type: type, // Tipo del movimiento: income o expense.
        description: description, // Descripción escrita por el usuario.
        category: category, // Categoría del movimiento.
        amount: Number(amount), // Monto convertido a número.
        date: new Date().toLocaleDateString("es-GT") // Fecha visual del movimiento.
    };

    // Agrega el movimiento a la lista principal.
    demoMovements.push(movement);

    // Guarda movimientos en localStorage.
saveDemoMovements();

if (typeof refreshBusinessBrain === "function") {
    refreshBusinessBrain();
} else {
    renderDemoApp();
}

if (typeof renderMonthlyReports === "function") {
    renderMonthlyReports();
}

    // Muestra mensaje de éxito.
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

// ===== EXPERIENCIA LOGIN + ROLES =====
// Este bloque hace que FinFlow tenga una experiencia tipo app interna.
// Antes de iniciar sesión se ve la landing.
// Después de iniciar sesión se oculta la landing y se muestra solo la app.

// Diccionario de usuarios demo disponibles en la experiencia web.
const experienceUsers = {
    admin: {
        password: "1234", // Contraseña demo del administrador.
        roleName: "Administrador", // Nombre visual del rol.
        description: "Gestiona la empresa, módulos, usuarios, reportes y configuración general.", // Descripción elegante del rol.
        modules: ["ingresos", "gastos", "reportes", "reportes_mensuales", "ia", "clientes", "proveedores", "presupuestos", "metas", "alertas", "neon"] // Módulos visibles para admin.
    },
    gerente: {
        password: "1234", // Contraseña demo del gerente.
        roleName: "Gerente", // Nombre visual del rol.
        description: "Consulta indicadores, flujo financiero, reportes y alertas para tomar decisiones.", // Descripción del rol.
        modules: ["reportes", "reportes_mensuales", "ia", "metas", "alertas", "neon"] // Módulos visibles para gerente.
    },
    contador: {
        password: "1234", // Contraseña demo del contador.
        roleName: "Contador", // Nombre visual del rol.
        description: "Registra, revisa y analiza ingresos, gastos, presupuestos y reportes financieros.", // Descripción del rol.
        modules: ["ingresos", "gastos", "reportes", "reportes_mensuales", "ia", "presupuestos", "metas"] // Módulos visibles para contador.
    },
    empleado: {
        password: "1234", // Contraseña demo del empleado.
        roleName: "Empleado", // Nombre visual del rol.
        description: "Registra ventas, ingresos diarios y gastos operativos de caja chica.", // Descripción sin decir acceso limitado.
        modules: ["ingresos", "gastos", "reportes_mensuales", "ia"] // Módulos visibles para empleado.
    }
};

// Mensajes personalizados del asistente financiero según el rol.
const roleAiMessages = {
    admin: "Hola, puedo ayudarte a revisar la operación completa de la empresa, reportes, usuarios, módulos y decisiones generales.",
    gerente: "Hola, puedo ayudarte a interpretar indicadores financieros, utilidad, flujo de caja, metas y alertas importantes.",
    contador: "Hola, puedo ayudarte a revisar ingresos, gastos, presupuestos, categorías y reportes financieros.",
    empleado: "Hola, puedo ayudarte a registrar ventas, ingresos del día y gastos de caja chica de forma ordenada."
};

// Obtiene el formulario de login desde el HTML.
const experienceLoginForm = document.getElementById("experienceLoginForm");

// Obtiene el input donde se escribe el usuario.
const experienceUsername = document.getElementById("experienceUsername");

// Obtiene el input donde se escribe la contraseña.
const experiencePassword = document.getElementById("experiencePassword");

// Obtiene el espacio donde se muestra error de login.
const experienceLoginError = document.getElementById("experienceLoginError");

// Obtiene la tarjeta completa del login.
const experienceLogin = document.getElementById("experienceLogin");

// Obtiene la app interna que se desbloquea después del login.
const finflowAppShell = document.getElementById("finflowAppShell");

// Obtiene la tarjeta donde se muestra la sesión activa.
const sessionRoleCard = document.getElementById("sessionRoleCard");

// Obtiene el texto donde se coloca el nombre del rol.
const sessionRoleName = document.getElementById("sessionRoleName");

// Obtiene el texto donde se coloca la descripción del rol.
const sessionRoleDescription = document.getElementById("sessionRoleDescription");

// Obtiene el botón para cerrar sesión.
const logoutExperienceButton = document.getElementById("logoutExperienceButton");

// Obtiene el selector de IA por rol, si existe en el HTML.
const roleAiSelect = document.getElementById("roleAiSelect");

// Obtiene el cuadro donde se muestra la respuesta de IA por rol, si existe.
const roleAiResponse = document.getElementById("roleAiResponse");

// ===== CONFIGURACIÓN EMPRESA =====

const COMPANY_SETTINGS_KEY = "finflowCompanySettings";

const companySettingsTrigger = document.getElementById("companySettingsTrigger");
const companySettingsPanel = document.getElementById("companySettingsPanel");
const closeCompanySettingsButton = document.getElementById("closeCompanySettingsButton");
const companySettingsForm = document.getElementById("companySettingsForm");
const companyCurrencySelect = document.getElementById("companyCurrencySelect");
const companyBackgroundColor = document.getElementById("companyBackgroundColor");
const companyChartColor = document.getElementById("companyChartColor");
const companyCardColor = document.getElementById("companyCardColor");
const resetCompanySettingsButton = document.getElementById("resetCompanySettingsButton");
const companySettingsStatus = document.getElementById("companySettingsStatus");
const chartVariantOne = document.getElementById("chartVariantOne");
const chartVariantTwo = document.getElementById("chartVariantTwo");
const chartVariantThree = document.getElementById("chartVariantThree");

function getDefaultCompanySettings() {
    return {
        currency: "Q",
        backgroundColor: "#fbf8f1",
        chartColor: "#d8bd76",
        cardColor: "#ffffff"
    };
}

function getCompanySettings() {
    try {
        const savedSettings = JSON.parse(localStorage.getItem(COMPANY_SETTINGS_KEY));

        if (savedSettings) {
            return {
                ...getDefaultCompanySettings(),
                ...savedSettings
            };
        }

        return getDefaultCompanySettings();
    } catch (error) {
        return getDefaultCompanySettings();
    }
}

function saveCompanySettings(settings) {
    localStorage.setItem(COMPANY_SETTINGS_KEY, JSON.stringify(settings));
}

function normalizeHexColor(color) {
    if (!color || typeof color !== "string") {
        return "#d8bd76";
    }

    if (color.startsWith("#") && color.length === 7) {
        return color;
    }

    return "#d8bd76";
}

function hexToRgb(color) {
    const safeColor = normalizeHexColor(color).replace("#", "");

    const red = parseInt(safeColor.substring(0, 2), 16);
    const green = parseInt(safeColor.substring(2, 4), 16);
    const blue = parseInt(safeColor.substring(4, 6), 16);

    return red + ", " + green + ", " + blue;
}

function shadeHexColor(color, percent) {
    const safeColor = normalizeHexColor(color).replace("#", "");

    let red = parseInt(safeColor.substring(0, 2), 16);
    let green = parseInt(safeColor.substring(2, 4), 16);
    let blue = parseInt(safeColor.substring(4, 6), 16);

    red = Math.min(255, Math.max(0, red + Math.round((percent / 100) * 255)));
    green = Math.min(255, Math.max(0, green + Math.round((percent / 100) * 255)));
    blue = Math.min(255, Math.max(0, blue + Math.round((percent / 100) * 255)));

    return (
        "#" +
        red.toString(16).padStart(2, "0") +
        green.toString(16).padStart(2, "0") +
        blue.toString(16).padStart(2, "0")
    );
}

function applyCompanySettings(settings) {
    const root = document.documentElement;

    const backgroundColor = normalizeHexColor(settings.backgroundColor);
    const chartColor = normalizeHexColor(settings.chartColor);
    const chartColorTwo = shadeHexColor(chartColor, -24);
    const chartColorThree = shadeHexColor(chartColor, 34);
    const cardColor = normalizeHexColor(settings.cardColor);

    root.style.setProperty("--company-bg-color", backgroundColor);
    root.style.setProperty("--company-bg-rgb", hexToRgb(backgroundColor));

    root.style.setProperty("--company-chart-color", chartColor);
    root.style.setProperty("--company-chart-color-2", chartColorTwo);
    root.style.setProperty("--company-chart-color-3", chartColorThree);
    root.style.setProperty("--company-chart-rgb", hexToRgb(chartColor));

    root.style.setProperty("--company-card-color", cardColor);
    root.style.setProperty("--company-card-rgb", hexToRgb(cardColor));

    root.style.setProperty("--champagne", chartColor);
    root.style.setProperty("--gold", chartColorTwo);
    root.style.setProperty("--gold-light", chartColorThree);

    if (companyCurrencySelect) {
        companyCurrencySelect.value = settings.currency;
    }

    if (companyBackgroundColor) {
        companyBackgroundColor.value = backgroundColor;
    }

    if (companyChartColor) {
        companyChartColor.value = chartColor;
    }

    if (companyCardColor) {
        companyCardColor.value = cardColor;
    }

    if (chartVariantOne) {
        chartVariantOne.style.background = chartColor;
    }

    if (chartVariantTwo) {
        chartVariantTwo.style.background = chartColorTwo;
    }

    if (chartVariantThree) {
        chartVariantThree.style.background = chartColorThree;
    }

    if (companySettingsStatus) {
        companySettingsStatus.textContent = "Cambios guardados automáticamente.";
    }
}

function readCompanySettingsForm() {
    return {
        currency: companyCurrencySelect ? companyCurrencySelect.value : "Q",
        backgroundColor: companyBackgroundColor ? companyBackgroundColor.value : "#fbf8f1",
        chartColor: companyChartColor ? companyChartColor.value : "#d8bd76",
        cardColor: companyCardColor ? companyCardColor.value : "#ffffff"
    };
}

function updateCompanySettingsFromForm() {
    const settings = readCompanySettingsForm();

    saveCompanySettings(settings);
    applyCompanySettings(settings);

    if (typeof refreshBusinessBrain === "function") {
        refreshBusinessBrain();
    }

    if (typeof renderMonthlyReports === "function") {
        renderMonthlyReports();
    }
}

if (companySettingsTrigger && companySettingsPanel) {
    companySettingsTrigger.addEventListener("click", function () {
        companySettingsPanel.hidden = !companySettingsPanel.hidden;
    });
}

if (closeCompanySettingsButton && companySettingsPanel) {
    closeCompanySettingsButton.addEventListener("click", function () {
        companySettingsPanel.hidden = true;
    });
}

if (companySettingsForm) {
    companySettingsForm.addEventListener("input", updateCompanySettingsFromForm);
    companySettingsForm.addEventListener("change", updateCompanySettingsFromForm);
}

if (resetCompanySettingsButton) {
    resetCompanySettingsButton.addEventListener("click", function () {
        const defaultSettings = getDefaultCompanySettings();

        saveCompanySettings(defaultSettings);
        applyCompanySettings(defaultSettings);

        if (typeof refreshBusinessBrain === "function") {
            refreshBusinessBrain();
        }

        if (typeof renderMonthlyReports === "function") {
            renderMonthlyReports();
        }

        if (companySettingsStatus) {
            companySettingsStatus.textContent = "Configuración FinFlow restaurada.";
        }
    });
}

applyCompanySettings(getCompanySettings());

// Función que personaliza textos de formularios según el usuario.
function customizeFormsByRole(username) {
    const incomeDescription = document.getElementById("incomeDescription"); // Input de descripción de ingreso.
    const incomeCategory = document.getElementById("incomeCategory"); // Input de categoría de ingreso.
    const expenseDescription = document.getElementById("expenseDescription"); // Input de descripción de gasto.
    const expenseCategory = document.getElementById("expenseCategory"); // Input de categoría de gasto.
    const assistantLine = document.getElementById("assistantLine"); // Mensaje principal del asistente.

    if (username === "empleado") { // Personaliza la experiencia del empleado.
        if (incomeDescription) {
            incomeDescription.placeholder = "Ejemplo: Venta del día"; // Placeholder enfocado en ventas.
        }

        if (incomeCategory) {
            incomeCategory.placeholder = "Ejemplo: Ventas"; // Categoría sugerida.
        }

        if (expenseDescription) {
            expenseDescription.placeholder = "Ejemplo: Gasto de caja chica"; // Placeholder enfocado en caja chica.
        }

        if (expenseCategory) {
            expenseCategory.placeholder = "Ejemplo: Caja chica"; // Categoría sugerida.
        }

        if (assistantLine) {
            assistantLine.textContent = "Puedo ayudarte a registrar ventas, ingresos diarios y gastos de caja chica de forma clara.";
        }
    } else { // Para los demás roles, deja placeholders generales.
        if (incomeDescription) {
            incomeDescription.placeholder = "Descripción del ingreso";
        }

        if (incomeCategory) {
            incomeCategory.placeholder = "Categoría";
        }

        if (expenseDescription) {
            expenseDescription.placeholder = "Descripción del gasto";
        }

        if (expenseCategory) {
            expenseCategory.placeholder = "Categoría";
        }

        if (assistantLine) {
            assistantLine.textContent = roleAiMessages[username];
        }
    }
}

// Función que aplica visualmente el rol del usuario que inició sesión.
function applyExperienceRole(username) {
    const user = experienceUsers[username]; // Busca el usuario dentro del diccionario.

    if (!user) { // Si el usuario no existe, detiene la función.
        return;
    }

    document.body.classList.add("finflow-session-active"); // Activa el modo app interna en toda la página.

    if (experienceLogin) { // Si existe la tarjeta de login...
        experienceLogin.style.display = "none"; // La oculta después de iniciar sesión.
    }

    if (finflowAppShell) { // Si existe la app interna...
        finflowAppShell.classList.add("is-unlocked"); // La muestra agregando la clase is-unlocked.
    }

    if (sessionRoleCard) { // Si existe la tarjeta de sesión...
        sessionRoleCard.hidden = false; // La muestra.
    }

    if (sessionRoleName) { // Si existe el texto del rol...
        sessionRoleName.textContent = user.roleName; // Coloca el nombre del rol.
    }

    if (sessionRoleDescription) { // Si existe la descripción del rol...
        sessionRoleDescription.textContent = user.description; // Coloca una descripción profesional.
    }

if (companySettingsTrigger) {
    companySettingsTrigger.hidden = username !== "admin";
}

if (companySettingsPanel && username !== "admin") {
    companySettingsPanel.hidden = true;
}

  // Obtiene los módulos que el usuario había dejado activos antes de recargar.
const savedModules = getActiveModules();

// Verifica si ya había módulos guardados para respetar la selección del usuario.
const hasSavedModules = savedModules.length > 0;

// Recorre todos los checkboxes de módulos existentes en la demo.
for (let i = 0; i < moduleToggles.length; i++) {
    const toggle = moduleToggles[i]; // Guarda el checkbox actual.
    const label = toggle.closest("label"); // Busca el label que contiene ese checkbox.
    const isAllowed = user.modules.includes(toggle.value); // Verifica si el módulo pertenece al rol.

    if (!isAllowed) { // Si el módulo no pertenece al rol...
        toggle.checked = false; // Lo deja apagado.
    } else if (hasSavedModules) { // Si sí pertenece al rol y ya había selección guardada...
        toggle.checked = savedModules.includes(toggle.value); // Respeta lo que el usuario dejó marcado.
    } else { // Si no había selección guardada...
        toggle.checked = true; // Activa por defecto los módulos permitidos.
    }

    if (label) { // Si el checkbox tiene label...
        label.style.display = isAllowed ? "flex" : "none"; // Muestra solo módulos permitidos.
    }
}

    if (roleAiSelect && roleAiResponse) { // Si existe el módulo visual de IA por rol...
        roleAiSelect.value = username; // Selecciona el rol actual.
        roleAiResponse.textContent = roleAiMessages[username]; // Muestra el mensaje del rol.
    }

        customizeFormsByRole(username);

    localStorage.setItem("finflowExperienceUser", username); // Guarda la sesión en el navegador.

    if (typeof renderModules === "function") {
    renderModules();
}

setTimeout(function () {
    if (typeof refreshBusinessBrain === "function") {
        refreshBusinessBrain();
    }

    if (typeof renderMonthlyReports === "function") {
        renderMonthlyReports();
    }
}, 0);

    
    window.scrollTo({ // Mueve la pantalla arriba para que parezca cambio de página.
        top: 0,
        behavior: "smooth"
    });
}

// Escucha cuando el usuario envía el formulario de login.
if (experienceLoginForm) {
    // Conecta el login visual original con Neon.
// Primero valida contra la base de datos real usando Flask.
// Si Flask no está disponible, usa el login demo como respaldo.
experienceLoginForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const inputsLogin = experienceLoginForm.querySelectorAll("input");

    if (inputsLogin.length < 2) {
        experienceLoginError.textContent = "No se encontraron los campos de usuario y contraseña.";
        return;
    }

    const username = inputsLogin[0].value.trim().toLowerCase();
    const password = inputsLogin[1].value.trim();

    experienceLoginError.textContent = "";

    if (username === "" || password === "") {
        experienceLoginError.textContent = "Ingrese usuario y contraseña.";
        return;
    }

    try {
        const respuesta = await fetch("/api/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                usuario: username,
                password: password
            })
        });

        const datos = await respuesta.json();

        if (datos.success) {
            localStorage.setItem("finflow_usuario_neon", JSON.stringify(datos.user));

            let usuarioVisual = datos.user.usuario;

            if (datos.user.rol === "administrador" || datos.user.rol === "admin") {
                usuarioVisual = "admin";
            } else if (datos.user.rol === "gerente") {
                usuarioVisual = "gerente";
            } else if (datos.user.rol === "contador") {
                usuarioVisual = "contador";
            } else if (datos.user.rol === "empleado") {
                usuarioVisual = "empleado";
            }

            localStorage.setItem("finflow_active_user", usuarioVisual);

            applyExperienceRole(usuarioVisual);
            startFinflowApp();

            setTimeout(function () {
                aplicarIdentidadRealNeon();
                agregarBotonUsuariosAdminNeon();
            }, 300);

            return;
        }

        experienceLoginError.textContent = datos.message || "Usuario o contraseña incorrectos.";

    } catch (error) {
        console.error(error);

        if (!experienceUsers[username] || experienceUsers[username].password !== password) {
            experienceLoginError.textContent = "Usuario o contraseña incorrectos.";
            return;
        }

        localStorage.setItem("finflow_active_user", username);

        applyExperienceRole(username);
        startFinflowApp();
    }
});
}

// Escucha el botón de cerrar sesión.
if (logoutExperienceButton) {

    // Cierra sesión limpiando tanto el usuario demo como el usuario conectado a Neon.
    logoutExperienceButton.addEventListener("click", function () {
    localStorage.removeItem("finflow_active_user");
    localStorage.removeItem("finflow_usuario_neon");
    localStorage.removeItem("finflow_usuario");
    localStorage.removeItem("finflowActiveUser");
    localStorage.removeItem("activeUser");
    localStorage.removeItem("usuarioActivo");

    sessionStorage.clear();

    const inputsLogin = experienceLoginForm.querySelectorAll("input");

    inputsLogin.forEach(function (input) {
        input.value = "";
    });

    experienceLoginError.textContent = "";

    experienceApp.hidden = true;
    experienceLoginSection.hidden = false;
});
} 

// Escucha cambios manuales en el selector de IA por rol, si ese módulo existe.
if (roleAiSelect && roleAiResponse) {
    roleAiSelect.addEventListener("change", function () {
        const selectedRole = roleAiSelect.value; // Obtiene el rol seleccionado.
        roleAiResponse.textContent = roleAiMessages[selectedRole]; // Cambia el mensaje de IA.
    });
}

// ===== CEREBRO EMPRESARIAL FINFLOW =====
// Este bloque controla clientes, proveedores, presupuestos, metas, alertas,
// movimientos, menús de tres puntos y eliminaciones.
// Debe existir una sola vez en el archivo.

const STORAGE_KEY_CLIENTS = "finflowClients";
const STORAGE_KEY_SUPPLIERS = "finflowSuppliers";
const STORAGE_KEY_BUDGETS = "finflowBudgets";
const STORAGE_KEY_GOALS = "finflowGoals";
const STORAGE_KEY_DELETED_LOG = "finflowDeletedLog";

const clientForm = document.getElementById("clientForm");
const clientName = document.getElementById("clientName");
const clientContact = document.getElementById("clientContact");
const clientPhone = document.getElementById("clientPhone");
const clientStatus = document.getElementById("clientStatus");
const clientList = document.getElementById("clientList");
const clientCountBadge = document.getElementById("clientCountBadge");

const supplierForm = document.getElementById("supplierForm");
const supplierName = document.getElementById("supplierName");
const supplierService = document.getElementById("supplierService");
const supplierAmount = document.getElementById("supplierAmount");
const supplierStatus = document.getElementById("supplierStatus");
const supplierList = document.getElementById("supplierList");
const supplierCountBadge = document.getElementById("supplierCountBadge");

const budgetForm = document.getElementById("budgetForm");
const budgetCategory = document.getElementById("budgetCategory");
const budgetMonth = document.getElementById("budgetMonth");
const budgetLimit = document.getElementById("budgetLimit");
const budgetOwner = document.getElementById("budgetOwner");
const budgetList = document.getElementById("budgetList");
const budgetCountBadge = document.getElementById("budgetCountBadge");
const totalBudgetLimit = document.getElementById("totalBudgetLimit");
const totalBudgetUsed = document.getElementById("totalBudgetUsed");
const totalBudgetRemaining = document.getElementById("totalBudgetRemaining");

const goalForm = document.getElementById("goalForm");
const goalName = document.getElementById("goalName");
const goalType = document.getElementById("goalType");
const goalTarget = document.getElementById("goalTarget");
const goalMonth = document.getElementById("goalMonth");
const goalList = document.getElementById("goalList");
const goalCountBadge = document.getElementById("goalCountBadge");

const alertList = document.getElementById("alertList");
const alertCountBadge = document.getElementById("alertCountBadge");

let finflowClients = JSON.parse(localStorage.getItem(STORAGE_KEY_CLIENTS)) || [];
let finflowSuppliers = JSON.parse(localStorage.getItem(STORAGE_KEY_SUPPLIERS)) || [];
let finflowBudgets = JSON.parse(localStorage.getItem(STORAGE_KEY_BUDGETS)) || [];
let finflowGoals = JSON.parse(localStorage.getItem(STORAGE_KEY_GOALS)) || [];
let finflowDeletedLog = JSON.parse(localStorage.getItem(STORAGE_KEY_DELETED_LOG)) || [];

function saveClients() {
    localStorage.setItem(STORAGE_KEY_CLIENTS, JSON.stringify(finflowClients));
}

function saveSuppliers() {
    localStorage.setItem(STORAGE_KEY_SUPPLIERS, JSON.stringify(finflowSuppliers));
}

function saveBudgets() {
    localStorage.setItem(STORAGE_KEY_BUDGETS, JSON.stringify(finflowBudgets));
}

function saveGoals() {
    localStorage.setItem(STORAGE_KEY_GOALS, JSON.stringify(finflowGoals));
}

function saveDeletedLog() {
    localStorage.setItem(STORAGE_KEY_DELETED_LOG, JSON.stringify(finflowDeletedLog));
}

function registerDeletedItem(type, name) {
    finflowDeletedLog.unshift({
        type: type,
        name: name,
        date: new Date().toLocaleString("es-GT")
    });

    saveDeletedLog();
}

function normalizeBusinessText(value) {
    return String(value).trim().toLowerCase();
}

function getCurrentBusinessMonth() {
    const currentDate = new Date();
    const year = currentDate.getFullYear();
    const month = String(currentDate.getMonth() + 1).padStart(2, "0");

    return year + "-" + month;
}

function getBusinessMovementMonth(dateText) {
    const currentMonth = getCurrentBusinessMonth();
    const parts = String(dateText).split("/");

    if (parts.length !== 3) {
        return currentMonth;
    }

    const month = parts[1];
    const year = parts[2];

    if (!month || !year) {
        return currentMonth;
    }

    return year + "-" + String(month).padStart(2, "0");
}

function createActionMenu(buttonLabel, optionsHtml) {
    return (
        '<div class="action-menu-wrapper">' +
            '<button type="button" class="action-menu-button" aria-label="' + buttonLabel + '">⋯</button>' +
            '<div class="action-menu">' +
                optionsHtml +
            '</div>' +
        '</div>'
    );
}

function ensureMovementIds() {
    for (let i = 0; i < demoMovements.length; i++) {
        if (!demoMovements[i].id) {
            demoMovements[i].id = "movement-" + Date.now() + "-" + i;
        }
    }

    saveDemoMovements();
}

function refreshBusinessBrain() {
    renderDemoApp();
    renderClients();
    renderSuppliers();
    renderBudgets();
    renderGoals();
    renderAlerts();

    if (typeof renderMonthlyReports === "function") {
        renderMonthlyReports();
    }
}

function addDemoMovement(type, description, category, amount) {
    const movement = {
        id: "movement-" + Date.now() + "-" + Math.random().toString(16).slice(2),
        type: type,
        description: description,
        category: category,
        amount: Number(amount),
        date: new Date().toLocaleDateString("es-GT")
    };

    demoMovements.push(movement);
    saveDemoMovements();
    refreshBusinessBrain();

    if (demoStatus) {
        demoStatus.textContent = type === "income" ? "Ingreso agregado correctamente" : "Gasto agregado correctamente";
    }
}

function renderDemoApp() {
    ensureMovementIds();

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

        const actionHtml = createActionMenu(
            "Abrir acciones del movimiento",
            '<button type="button" class="movement-delete-button danger" data-movement-id="' + movement.id + '">Eliminar movimiento</button>'
        );

        const actionHolder = document.createElement("div");
        actionHolder.innerHTML = actionHtml;

        item.appendChild(type);
        item.appendChild(detail);
        item.appendChild(amount);
        item.appendChild(actionHolder.firstElementChild);

        movementList.appendChild(item);
    }
}

function renderClients() {
    if (!clientList) {
        return;
    }

    clientList.innerHTML = "";

    if (clientCountBadge) {
        clientCountBadge.textContent = finflowClients.length + " clientes";
    }

    if (finflowClients.length === 0) {
        clientList.innerHTML = '<p class="empty-demo-message">Todavía no hay clientes registrados.</p>';
        return;
    }

    for (let i = finflowClients.length - 1; i >= 0; i--) {
        const client = finflowClients[i];

        const item = document.createElement("div");
        item.classList.add("business-item", "client-item");

        const info = document.createElement("div");
        info.innerHTML =
            "<strong>" +
            client.name +
            "</strong><span>" +
            client.contact +
            " · " +
            client.phone +
            "</span>";

        const actions = document.createElement("div");
        actions.classList.add("client-actions");

        const status = document.createElement("div");
        status.classList.add("business-status");
        status.textContent = client.status;

        const actionHolder = document.createElement("div");
        actionHolder.innerHTML = createActionMenu(
            "Abrir acciones del cliente",
            '<button type="button" class="client-status-button" data-client-index="' + i + '" data-client-status="activo">Marcar activo</button>' +
            '<button type="button" class="client-status-button" data-client-index="' + i + '" data-client-status="pendiente">Marcar pendiente</button>' +
            '<button type="button" class="client-status-button" data-client-index="' + i + '" data-client-status="potencial">Marcar potencial</button>' +
            '<button type="button" class="client-delete-button danger" data-client-index="' + i + '">Eliminar cliente</button>'
        );

        actions.appendChild(status);
        actions.appendChild(actionHolder.firstElementChild);

        item.appendChild(info);
        item.appendChild(actions);

        clientList.appendChild(item);
    }
}

function renderSuppliers() {
    if (!supplierList) {
        return;
    }

    supplierList.innerHTML = "";

    if (supplierCountBadge) {
        supplierCountBadge.textContent = finflowSuppliers.length + " proveedores";
    }

    if (finflowSuppliers.length === 0) {
        supplierList.innerHTML = '<p class="empty-demo-message">Todavía no hay proveedores registrados.</p>';
        return;
    }

    for (let i = finflowSuppliers.length - 1; i >= 0; i--) {
        const supplier = finflowSuppliers[i];

        const item = document.createElement("div");
        item.classList.add("business-item", "supplier-item");

        const info = document.createElement("div");
        info.innerHTML =
            "<strong>" +
            supplier.name +
            "</strong><span>" +
            supplier.service +
            " · " +
            formatCurrency(supplier.amount) +
            "</span>";

        const actions = document.createElement("div");
        actions.classList.add("supplier-actions");

        const status = document.createElement("div");
        status.classList.add("business-status");
        status.textContent = supplier.status;

        const actionHolder = document.createElement("div");
        actionHolder.innerHTML = createActionMenu(
            "Abrir acciones del proveedor",
            '<button type="button" class="supplier-status-button" data-supplier-index="' + i + '" data-supplier-status="activo">Marcar activo</button>' +
            '<button type="button" class="supplier-status-button" data-supplier-index="' + i + '" data-supplier-status="revisar">Marcar revisar</button>' +
            '<button type="button" class="supplier-status-button" data-supplier-index="' + i + '" data-supplier-status="pagado">Marcar pagado</button>' +
            '<button type="button" class="supplier-delete-button danger" data-supplier-index="' + i + '">Eliminar proveedor</button>'
        );

        actions.appendChild(status);
        actions.appendChild(actionHolder.firstElementChild);

        item.appendChild(info);
        item.appendChild(actions);

        supplierList.appendChild(item);
    }
}

function calculateBudgetUsed(category, month) {
    let totalUsed = 0;

    for (let i = 0; i < demoMovements.length; i++) {
        const movement = demoMovements[i];
        const sameCategory = normalizeBusinessText(movement.category) === normalizeBusinessText(category);
        const sameMonth = getBusinessMovementMonth(movement.date) === month;
        const isExpense = movement.type === "expense";

        if (isExpense && sameCategory && sameMonth) {
            totalUsed = totalUsed + Number(movement.amount);
        }
    }

    return totalUsed;
}

function getBudgetHealth(percentage) {
    if (percentage >= 100) {
        return "Superado";
    }

    if (percentage >= 80) {
        return "En observación";
    }

    return "Bajo control";
}

function renderBudgets() {
    if (!budgetList) {
        return;
    }

    budgetList.innerHTML = "";

    let totalLimit = 0;
    let totalUsed = 0;

    if (budgetCountBadge) {
        budgetCountBadge.textContent = finflowBudgets.length + " presupuestos";
    }

    if (finflowBudgets.length === 0) {
        budgetList.innerHTML = '<p class="empty-demo-message">Todavía no hay presupuestos registrados.</p>';
    }

    for (let i = finflowBudgets.length - 1; i >= 0; i--) {
        const budget = finflowBudgets[i];
        const used = calculateBudgetUsed(budget.category, budget.month);
        const remaining = Number(budget.limit) - used;
        const percentage = Number(budget.limit) > 0 ? (used / Number(budget.limit)) * 100 : 0;
        const safePercentage = Math.min(Math.max(percentage, 0), 100);
        const health = getBudgetHealth(percentage);

        totalLimit = totalLimit + Number(budget.limit);
        totalUsed = totalUsed + used;

        const item = document.createElement("div");
        item.classList.add("budget-item");

        item.innerHTML =
            '<div class="budget-item-header">' +
                '<div>' +
                    '<strong>' + budget.category + '</strong>' +
                    '<span>Mes: ' + budget.month + ' · Responsable: ' + budget.owner + '</span>' +
                '</div>' +
                '<div class="budget-health">' + health + '</div>' +
            '</div>' +
            '<div class="budget-progress"><span style="width: ' + safePercentage + '%"></span></div>' +
            '<div class="budget-numbers">' +
                '<div><span>Límite</span><strong>' + formatCurrency(budget.limit) + '</strong></div>' +
                '<div><span>Usado</span><strong>' + formatCurrency(used) + '</strong></div>' +
                '<div><span>Disponible</span><strong>' + formatCurrency(remaining) + '</strong></div>' +
            '</div>' +
            '<div class="item-action-row">' +
                createActionMenu(
                    "Abrir acciones del presupuesto",
                    '<button type="button" class="budget-delete-button danger" data-budget-index="' + i + '">Eliminar presupuesto</button>'
                ) +
            '</div>';

        budgetList.appendChild(item);
    }

    if (totalBudgetLimit) {
        totalBudgetLimit.textContent = formatCurrency(totalLimit);
    }

    if (totalBudgetUsed) {
        totalBudgetUsed.textContent = formatCurrency(totalUsed);
    }

    if (totalBudgetRemaining) {
        totalBudgetRemaining.textContent = formatCurrency(totalLimit - totalUsed);
    }
}

function calculateGoalProgress(goal) {
    const totals = calculateDemoTotals();
    const target = Number(goal.target);

    if (target <= 0) {
        return {
            current: 0,
            target: target,
            remaining: 0,
            percentage: 0
        };
    }

    let current = 0;

    if (goal.type === "ventas") {
        current = totals.income;
    }

    if (goal.type === "ahorro") {
        current = Math.max(totals.income - totals.expense, 0);
    }

    if (goal.type === "utilidad") {
        current = totals.profit;
    }

    return {
        current: current,
        target: target,
        remaining: target - current,
        percentage: (current / target) * 100
    };
}

function getGoalHealth(percentage) {
    if (percentage >= 100) {
        return "Alcanzada";
    }

    if (percentage >= 70) {
        return "Avanzando";
    }

    if (percentage >= 30) {
        return "En proceso";
    }

    return "Requiere impulso";
}

function renderGoals() {
    if (!goalList) {
        return;
    }

    goalList.innerHTML = "";

    if (goalCountBadge) {
        goalCountBadge.textContent = finflowGoals.length + " metas";
    }

    if (finflowGoals.length === 0) {
        goalList.innerHTML = '<p class="empty-demo-message">Todavía no hay metas registradas.</p>';
        return;
    }

    for (let i = finflowGoals.length - 1; i >= 0; i--) {
        const goal = finflowGoals[i];
        const progress = calculateGoalProgress(goal);
        const safePercentage = Math.min(Math.max(progress.percentage, 0), 100);
        const health = getGoalHealth(progress.percentage);

        const item = document.createElement("div");
        item.classList.add("goal-item");

        item.innerHTML =
            '<div class="goal-item-header">' +
                '<div>' +
                    '<strong>' + goal.name + '</strong>' +
                    '<span>Tipo: ' + goal.type + ' · Mes: ' + goal.month + '</span>' +
                '</div>' +
                '<div class="goal-health">' + health + '</div>' +
            '</div>' +
            '<div class="goal-progress"><span style="width: ' + safePercentage + '%"></span></div>' +
            '<div class="goal-numbers">' +
                '<div><span>Actual</span><strong>' + formatCurrency(progress.current) + '</strong></div>' +
                '<div><span>Objetivo</span><strong>' + formatCurrency(progress.target) + '</strong></div>' +
                '<div><span>Faltante</span><strong>' + formatCurrency(Math.max(progress.remaining, 0)) + '</strong></div>' +
            '</div>' +
            '<div class="item-action-row">' +
                createActionMenu(
                    "Abrir acciones de la meta",
                    '<button type="button" class="goal-delete-button danger" data-goal-index="' + i + '">Eliminar meta</button>'
                ) +
            '</div>';

        goalList.appendChild(item);
    }
}

function buildAutomaticAlerts() {
    const alerts = [];
    const totals = calculateDemoTotals();

    if (totals.expense > totals.income) {
        alerts.push({
            title: "Gastos superiores a ingresos",
            message: "Los gastos actuales superan los ingresos registrados. Conviene revisar egresos operativos y flujo de caja.",
            priority: "Alta"
        });
    }

    for (let i = 0; i < finflowBudgets.length; i++) {
        const budget = finflowBudgets[i];
        const used = calculateBudgetUsed(budget.category, budget.month);
        const percentage = Number(budget.limit) > 0 ? (used / Number(budget.limit)) * 100 : 0;

        if (percentage >= 100) {
            alerts.push({
                title: "Presupuesto superado: " + budget.category,
                message: "El presupuesto de " + budget.category + " ya superó el límite mensual definido.",
                priority: "Alta"
            });
        } else if (percentage >= 80) {
            alerts.push({
                title: "Presupuesto en observación: " + budget.category,
                message: "El presupuesto de " + budget.category + " ya alcanzó " + Math.round(percentage) + "% de uso.",
                priority: "Media"
            });
        }
    }

    for (let i = 0; i < finflowSuppliers.length; i++) {
        const supplier = finflowSuppliers[i];
        const status = normalizeBusinessText(supplier.status);

        if (status.includes("revisar") || status.includes("pendiente")) {
            alerts.push({
                title: "Proveedor requiere seguimiento",
                message: supplier.name + " está marcado como " + supplier.status + ". Conviene revisar pagos, contrato o servicio.",
                priority: "Media"
            });
        }
    }

    for (let i = 0; i < finflowGoals.length; i++) {
        const goal = finflowGoals[i];
        const progress = calculateGoalProgress(goal);

        if (progress.percentage < 30) {
            alerts.push({
                title: "Meta con avance bajo: " + goal.name,
                message: "La meta lleva menos del 30% de avance. Conviene revisar ventas, gastos o acciones comerciales.",
                priority: "Media"
            });
        }
    }

    return alerts;
}

function renderAlerts() {
    if (!alertList) {
        return;
    }

    const alerts = buildAutomaticAlerts();
    alertList.innerHTML = "";

    if (alertCountBadge) {
        alertCountBadge.textContent = alerts.length + " alertas";
    }

    if (alerts.length === 0) {
        alertList.innerHTML = '<p class="empty-demo-message">No hay alertas activas por ahora.</p>';
        return;
    }

    for (let i = 0; i < alerts.length; i++) {
        const alert = alerts[i];

        const item = document.createElement("div");
        item.classList.add("alert-item");

        item.innerHTML =
            '<strong>' + alert.title + '</strong>' +
            '<span>' + alert.message + '</span>' +
            '<div class="alert-priority">Prioridad ' + alert.priority + '</div>';

        alertList.appendChild(item);
    }
}

if (clientForm) {
    clientForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const newClient = {
            name: clientName.value.trim(),
            contact: clientContact.value.trim(),
            phone: clientPhone.value.trim(),
            status: clientStatus.value.trim()
        };

        if (!newClient.name || !newClient.contact || !newClient.phone || !newClient.status) {
            return;
        }

        finflowClients.push(newClient);
        saveClients();
        refreshBusinessBrain();
        clientForm.reset();
    });
}

if (supplierForm) {
    supplierForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const newSupplier = {
            name: supplierName.value.trim(),
            service: supplierService.value.trim(),
            amount: Number(supplierAmount.value),
            status: supplierStatus.value.trim()
        };

        if (!newSupplier.name || !newSupplier.service || newSupplier.amount <= 0 || !newSupplier.status) {
            return;
        }

        finflowSuppliers.push(newSupplier);
        saveSuppliers();
        refreshBusinessBrain();
        supplierForm.reset();
    });
}

if (budgetForm) {
    budgetForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const newBudget = {
            category: budgetCategory.value.trim(),
            month: budgetMonth.value || getCurrentBusinessMonth(),
            limit: Number(budgetLimit.value),
            owner: budgetOwner.value.trim()
        };

        if (!newBudget.category || newBudget.limit <= 0 || !newBudget.owner) {
            return;
        }

        finflowBudgets.push(newBudget);
        saveBudgets();
        refreshBusinessBrain();
        budgetForm.reset();

        if (budgetMonth) {
            budgetMonth.value = getCurrentBusinessMonth();
        }
    });
}

if (goalForm) {
    goalForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const newGoal = {
            name: goalName.value.trim(),
            type: goalType.value,
            target: Number(goalTarget.value),
            month: goalMonth.value || getCurrentBusinessMonth()
        };

        if (!newGoal.name || newGoal.target <= 0) {
            return;
        }

        finflowGoals.push(newGoal);
        saveGoals();
        refreshBusinessBrain();
        goalForm.reset();

        if (goalMonth) {
            goalMonth.value = getCurrentBusinessMonth();
        }
    });
}

document.addEventListener("click", function (event) {
    const menuButton = event.target.closest(".action-menu-button");
    const actionButton = event.target.closest(".action-menu button");

    if (menuButton) {
        event.preventDefault();
        event.stopPropagation();

        const currentWrapper = menuButton.closest(".action-menu-wrapper");
        const openMenus = document.querySelectorAll(".action-menu-wrapper.is-open");

        for (let i = 0; i < openMenus.length; i++) {
            if (openMenus[i] !== currentWrapper) {
                openMenus[i].classList.remove("is-open");
            }
        }

        if (currentWrapper) {
            currentWrapper.classList.toggle("is-open");
        }

        return;
    }

    if (actionButton) {
        event.preventDefault();

        if (actionButton.classList.contains("movement-delete-button")) {
            const movementId = actionButton.dataset.movementId;
            const movementIndex = demoMovements.findIndex(function (movement) {
                return movement.id === movementId;
            });

            if (movementIndex !== -1) {
                const deletedMovement = demoMovements[movementIndex];

                registerDeletedItem(deletedMovement.type === "income" ? "Ingreso" : "Gasto", deletedMovement.description);

                demoMovements.splice(movementIndex, 1);
                saveDemoMovements();
                refreshBusinessBrain();

                if (demoStatus) {
                    demoStatus.textContent = "Movimiento eliminado";
                }
            }
        }

        if (actionButton.classList.contains("client-status-button")) {
            const clientIndex = Number(actionButton.dataset.clientIndex);
            finflowClients[clientIndex].status = actionButton.dataset.clientStatus;
            refreshBusinessBrain();
        }

        if (actionButton.classList.contains("client-delete-button")) {
            const clientIndex = Number(actionButton.dataset.clientIndex);
            registerDeletedItem("Cliente", finflowClients[clientIndex].name);
            finflowClients.splice(clientIndex, 1);
            saveClients();
            refreshBusinessBrain();
        }

        if (actionButton.classList.contains("supplier-status-button")) {
            const supplierIndex = Number(actionButton.dataset.supplierIndex);
            finflowSuppliers[supplierIndex].status = actionButton.dataset.supplierStatus;
            refreshBusinessBrain();
        }

        if (actionButton.classList.contains("supplier-delete-button")) {
            const supplierIndex = Number(actionButton.dataset.supplierIndex);
            registerDeletedItem("Proveedor", finflowSuppliers[supplierIndex].name);
            finflowSuppliers.splice(supplierIndex, 1);
            saveSuppliers();
            refreshBusinessBrain();
        }
        if (actionButton.classList.contains("budget-delete-button")) {
            const budgetIndex = Number(actionButton.dataset.budgetIndex);
            registerDeletedItem("Presupuesto", finflowBudgets[budgetIndex].category);
            finflowBudgets.splice(budgetIndex, 1);
            saveBudgets();
            refreshBusinessBrain();
        }


        if (actionButton.classList.contains("goal-delete-button")) {
            const goalIndex = Number(actionButton.dataset.goalIndex);
            registerDeletedItem("Meta", finflowGoals[goalIndex].name);
            finflowGoals.splice(goalIndex, 1);
            saveGoals();
            refreshBusinessBrain();
        }

        const openMenus = document.querySelectorAll(".action-menu-wrapper.is-open");

        for (let i = 0; i < openMenus.length; i++) {
            openMenus[i].classList.remove("is-open");
        }

        return;
    }

    const openMenus = document.querySelectorAll(".action-menu-wrapper.is-open");

    for (let i = 0; i < openMenus.length; i++) {
        openMenus[i].classList.remove("is-open");
    }
});

if (budgetMonth) {
    budgetMonth.value = getCurrentBusinessMonth();
}

if (goalMonth) {
    goalMonth.value = getCurrentBusinessMonth();
}

// ===== REPORTES MENSUALES EJECUTIVOS POR ROL =====

let monthlyTrendChart = null;
let monthlyMixChart = null;
let monthlyCategoryChart = null;

function getMonthlyActiveUser() {
    const savedUser = localStorage.getItem("finflowExperienceUser");

    if (savedUser && experienceUsers[savedUser]) {
        return {
            username: savedUser,
            roleName: experienceUsers[savedUser].roleName
        };
    }

    return {
        username: "admin",
        roleName: "Administrador"
    };
}

function setMonthlyText(id, value) {
    const element = document.getElementById(id);

    if (element) {
        element.textContent = value;
    }
}

function getMonthlyReportData() {
    const savedMovements = Array.isArray(demoMovements) ? demoMovements : [];
    const savedClients = Array.isArray(finflowClients) ? finflowClients : [];
    const savedSuppliers = Array.isArray(finflowSuppliers) ? finflowSuppliers : [];
    const savedBudgets = Array.isArray(finflowBudgets) ? finflowBudgets : [];
    const savedGoals = Array.isArray(finflowGoals) ? finflowGoals : [];

    let income = 0;
    let expenses = 0;
    let incomeCount = 0;
    let expenseCount = 0;
    let biggestIncome = 0;
    let biggestExpense = 0;
    let categoryExpenses = {};
    let cumulativeProfit = [];
    let runningProfit = 0;

    for (let i = 0; i < savedMovements.length; i++) {
        const movement = savedMovements[i];
        const amount = Number(movement.amount || movement.monto || 0);
        const category = movement.category || movement.categoria || "Sin categoría";

        if (movement.type === "income" || movement.tipo === "ingreso") {
            income = income + amount;
            incomeCount = incomeCount + 1;
            runningProfit = runningProfit + amount;

            if (amount > biggestIncome) {
                biggestIncome = amount;
            }
        }

        if (movement.type === "expense" || movement.tipo === "gasto") {
            expenses = expenses + amount;
            expenseCount = expenseCount + 1;
            runningProfit = runningProfit - amount;

            if (amount > biggestExpense) {
                biggestExpense = amount;
            }

            if (!categoryExpenses[category]) {
                categoryExpenses[category] = 0;
            }

            categoryExpenses[category] = categoryExpenses[category] + amount;
        }

        cumulativeProfit.push(runningProfit);
    }

    const profit = income - expenses;
    const movements = savedMovements.length;
    const average = movements > 0 ? (income + expenses) / movements : 0;
    const margin = income > 0 ? (profit / income) * 100 : 0;
    const expenseRatio = income > 0 ? (expenses / income) * 100 : 0;

    const supplierCost = savedSuppliers.reduce(function (total, supplier) {
        return total + Number(supplier.amount || 0);
    }, 0);

    let alerts = 0;

    if (typeof buildAutomaticAlerts === "function") {
        alerts = buildAutomaticAlerts().length;
    }

    let totalGoalProgress = 0;

    for (let i = 0; i < savedGoals.length; i++) {
        if (typeof calculateGoalProgress === "function") {
            const progress = calculateGoalProgress(savedGoals[i]);
            totalGoalProgress = totalGoalProgress + Math.min(Math.max(progress.percentage, 0), 100);
        }
    }

    const averageGoalProgress = savedGoals.length > 0 ? totalGoalProgress / savedGoals.length : 0;

    let healthScore = 50;

    if (profit > 0) {
        healthScore = healthScore + 20;
    }

    if (margin >= 30) {
        healthScore = healthScore + 15;
    } else if (margin >= 10) {
        healthScore = healthScore + 8;
    }

    if (alerts === 0) {
        healthScore = healthScore + 10;
    } else if (alerts >= 3) {
        healthScore = healthScore - 12;
    }

    if (averageGoalProgress >= 70) {
        healthScore = healthScore + 10;
    }

    if (expenseRatio > 90) {
        healthScore = healthScore - 15;
    }

    healthScore = Math.min(Math.max(Math.round(healthScore), 0), 100);

    const categoryLabels = Object.keys(categoryExpenses);
    const categoryValues = categoryLabels.map(function (category) {
        return categoryExpenses[category];
    });

    return {
        income: income,
        expenses: expenses,
        profit: profit,
        movements: movements,
        incomeCount: incomeCount,
        expenseCount: expenseCount,
        average: average,
        margin: margin,
        expenseRatio: expenseRatio,
        clients: savedClients.length,
        suppliers: savedSuppliers.length,
        budgets: savedBudgets.length,
        goals: savedGoals.length,
        alerts: alerts,
        biggestIncome: biggestIncome,
        biggestExpense: biggestExpense,
        supplierCost: supplierCost,
        averageGoalProgress: averageGoalProgress,
        healthScore: healthScore,
        categoryLabels: categoryLabels,
        categoryValues: categoryValues,
        cumulativeProfit: cumulativeProfit
    };
}

function renderMonthlyReports() {
    const user = getMonthlyActiveUser();
    const data = getMonthlyReportData();

    setMonthlyText("monthlyRoleName", user.roleName);
    setMonthlyText("monthlyIncome", formatCurrency(data.income));
    setMonthlyText("monthlyExpenses", formatCurrency(data.expenses));
    setMonthlyText("monthlyProfit", formatCurrency(data.profit));
    setMonthlyText("monthlyMovements", data.movements);
    setMonthlyText("monthlyAverage", formatCurrency(data.average));
    setMonthlyText("monthlyClients", data.clients);
    setMonthlyText("monthlySuppliers", data.suppliers);
    setMonthlyText("monthlyBudgets", data.budgets);
    setMonthlyText("monthlyGoals", data.goals);
    setMonthlyText("monthlyAlerts", data.alerts);
    setMonthlyText("monthlyMargin", Math.round(data.margin) + "%");
    setMonthlyText("monthlyHealthScore", data.healthScore + "/100");

    renderMonthlyRoleSummary(user, data);
    renderMonthlyExecutiveInsight(data);
    renderMonthlyCharts(data);
}

function renderMonthlyRoleSummary(user, data) {
    const roleTitle = document.getElementById("roleReportTitle");
    const roleContent = document.getElementById("roleReportContent");

    if (!roleTitle || !roleContent) {
        return;
    }

    if (user.username === "admin") {
        roleTitle.textContent = "Resumen ejecutivo para administrador";
        roleContent.innerHTML =
            "<ul>" +
                "<li>Ingresos: " + formatCurrency(data.income) + " en " + data.incomeCount + " registros.</li>" +
                "<li>Gastos: " + formatCurrency(data.expenses) + " en " + data.expenseCount + " registros.</li>" +
                "<li>Utilidad: " + formatCurrency(data.profit) + " con margen de " + Math.round(data.margin) + "%.</li>" +
                "<li>Costo estimado de proveedores: " + formatCurrency(data.supplierCost) + ".</li>" +
                "<li>Salud financiera: " + data.healthScore + "/100. Alertas activas: " + data.alerts + ".</li>" +
            "</ul>";
    } else if (user.username === "gerente") {
        roleTitle.textContent = "Resumen operativo para gerente";
        roleContent.innerHTML =
            "<ul>" +
                "<li>Resultado mensual: " + formatCurrency(data.profit) + ".</li>" +
                "<li>Clientes registrados: " + data.clients + ". Proveedores: " + data.suppliers + ".</li>" +
                "<li>Metas registradas: " + data.goals + " con avance promedio de " + Math.round(data.averageGoalProgress) + "%.</li>" +
                "<li>Alertas que requieren seguimiento: " + data.alerts + ".</li>" +
            "</ul>";
    } else if (user.username === "contador") {
        roleTitle.textContent = "Resumen financiero para contador";
        roleContent.innerHTML =
            "<ul>" +
                "<li>Total de ingresos: " + formatCurrency(data.income) + ".</li>" +
                "<li>Total de gastos: " + formatCurrency(data.expenses) + ".</li>" +
                "<li>Resultado neto: " + formatCurrency(data.profit) + ".</li>" +
                "<li>Ticket promedio por movimiento: " + formatCurrency(data.average) + ".</li>" +
                "<li>Mayor ingreso: " + formatCurrency(data.biggestIncome) + ". Mayor gasto: " + formatCurrency(data.biggestExpense) + ".</li>" +
            "</ul>";
    } else {
        roleTitle.textContent = "Resumen operativo para empleado";
        roleContent.innerHTML =
            "<ul>" +
                "<li>Movimientos registrados: " + data.movements + ".</li>" +
                "<li>Ingresos registrados: " + data.incomeCount + ".</li>" +
                "<li>Gastos registrados: " + data.expenseCount + ".</li>" +
                "<li>Vista enfocada en actividad operativa diaria.</li>" +
            "</ul>";
    }
}

function renderMonthlyExecutiveInsight(data) {
    const insight = document.getElementById("monthlyExecutiveInsight");

    if (!insight) {
        return;
    }

    if (data.movements === 0) {
        insight.textContent = "Todavía no hay datos suficientes. Registra ingresos, gastos, clientes, proveedores y metas para generar un diagnóstico empresarial.";
        return;
    }

    if (data.profit < 0) {
        insight.textContent = "El negocio muestra pérdida mensual. La prioridad debe ser reducir gastos críticos, revisar proveedores y aumentar ingresos recurrentes.";
        return;
    }

    if (data.healthScore >= 85) {
        insight.textContent = "El negocio muestra una posición fuerte: utilidad positiva, margen saludable y bajo nivel de alerta. Es buen momento para analizar expansión o inversión.";
        return;
    }

    if (data.expenseRatio > 80) {
        insight.textContent = "Los gastos consumen gran parte de los ingresos. Conviene revisar categorías con mayor gasto y renegociar costos operativos.";
        return;
    }

    if (data.alerts > 0) {
        insight.textContent = "La operación está generando alertas. El enfoque debe estar en presupuestos, proveedores pendientes y avance de metas.";
        return;
    }

    insight.textContent = "El negocio se mantiene estable. Conviene seguir monitoreando margen, flujo acumulado, categorías de gasto y avance de metas.";
}

function destroyMonthlyCharts() {
    if (monthlyTrendChart) {
        monthlyTrendChart.destroy();
        monthlyTrendChart = null;
    }

    if (monthlyMixChart) {
        monthlyMixChart.destroy();
        monthlyMixChart = null;
    }

    if (monthlyCategoryChart) {
        monthlyCategoryChart.destroy();
        monthlyCategoryChart = null;
    }
}

function renderMonthlyCharts(data) {
    if (typeof Chart === "undefined") {
        return;
    }

    const trendCanvas = document.getElementById("monthlyTrendChart");
    const mixCanvas = document.getElementById("monthlyMixChart");
    const categoryCanvas = document.getElementById("monthlyCategoryChart");

    if (!trendCanvas || !mixCanvas || !categoryCanvas) {
        return;
    }

    destroyMonthlyCharts();

    const textColor = "rgba(255,255,255,0.74)";
    const gridColor = "rgba(255,255,255,0.08)";
    const rootStyles = getComputedStyle(document.documentElement);
    const gold = rootStyles.getPropertyValue("--company-chart-color").trim() || "#d8bd76";
    const goldDark = rootStyles.getPropertyValue("--company-chart-color-2").trim() || "#8a641f";
    const whiteSoft = rootStyles.getPropertyValue("--company-chart-color-3").trim() || "rgba(255,255,255,0.72)";

    let trendLabels = [];
    let trendValues = [];

    if (data.cumulativeProfit.length > 0) {
        for (let i = 0; i < data.cumulativeProfit.length; i++) {
            trendLabels.push("Mov " + (i + 1));
            trendValues.push(data.cumulativeProfit[i]);
        }

        const lastValue = trendValues[trendValues.length - 1];
        const averageChange = trendValues.length > 1 ? (lastValue - trendValues[0]) / trendValues.length : lastValue;

        trendLabels.push("Proy. 1");
        trendValues.push(lastValue + averageChange);

        trendLabels.push("Proy. 2");
        trendValues.push(lastValue + averageChange * 2);
    } else {
        trendLabels = ["Sin datos"];
        trendValues = [0];
    }

    monthlyTrendChart = new Chart(trendCanvas, {
        type: "line",
        data: {
            labels: trendLabels,
            datasets: [
                {
                    label: "Flujo acumulado",
                    data: trendValues,
                    borderColor: gold,
                    backgroundColor: "rgba(216, 189, 118, 0.15)",
                    fill: true,
                    tension: 0.38,
                    pointRadius: 3,
                    pointBackgroundColor: gold
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: {
                        color: textColor
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: textColor
                    },
                    grid: {
                        color: gridColor
                    }
                },
                y: {
                    ticks: {
                        color: textColor
                    },
                    grid: {
                        color: gridColor
                    }
                }
            }
        }
    });

    monthlyMixChart = new Chart(mixCanvas, {
        type: "doughnut",
        data: {
            labels: ["Ingresos", "Gastos", "Utilidad"],
            datasets: [
                {
                    data: [
                        Math.max(data.income, 0),
                        Math.max(data.expenses, 0),
                        Math.max(data.profit, 0)
                    ],
                    backgroundColor: [gold, goldDark, whiteSoft],
                    borderColor: "rgba(255,255,255,0.08)",
                    borderWidth: 2
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: {
                        color: textColor
                    }
                }
            }
        }
    });

    let categoryLabels = data.categoryLabels;
    let categoryValues = data.categoryValues;

    if (categoryLabels.length === 0) {
        categoryLabels = ["Sin gastos"];
        categoryValues = [0];
    }

    monthlyCategoryChart = new Chart(categoryCanvas, {
        type: "bar",
        data: {
            labels: categoryLabels,
            datasets: [
                {
                    label: "Gastos por categoría",
                    data: categoryValues,
                    backgroundColor: "rgba(216, 189, 118, 0.78)",
                    borderRadius: 10
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: textColor
                    },
                    grid: {
                        display: false
                    }
                },
                y: {
                    ticks: {
                        color: textColor
                    },
                    grid: {
                        color: gridColor
                    }
                }
            }
        }
    });
}

function startFinflowApp() {
    const savedUser = localStorage.getItem("finflowExperienceUser");

    if (savedUser && experienceUsers[savedUser]) {
        applyExperienceRole(savedUser);
        return;
    }

    if (typeof renderModules === "function") {
        renderModules();
    }

    if (typeof refreshBusinessBrain === "function") {
        refreshBusinessBrain();
    }

    if (typeof renderMonthlyReports === "function") {
        renderMonthlyReports();
    }
}

setTimeout(startFinflowApp, 250);

document.addEventListener("submit", function () {
    setTimeout(function () {
        if (typeof refreshBusinessBrain === "function") {
            refreshBusinessBrain();
        }

        if (typeof renderMonthlyReports === "function") {
            renderMonthlyReports();
        }
    }, 150);
});

document.addEventListener("click", function () {
    setTimeout(function () {
        if (typeof renderMonthlyReports === "function") {
            renderMonthlyReports();
        }
    }, 150);
});

// ======================================================
// APLICAR IDENTIDAD REAL DE NEON EN EL DASHBOARD
// ======================================================
// Cuando un usuario creado en Neon inicia sesión, el dashboard visual
// puede abrir como admin, gerente, contador o empleado.
// Esta función muestra también el usuario real que inició sesión,
// por ejemplo cam1, su nombre, correo y carnet.

function aplicarIdentidadRealNeon() {
    const usuarioTexto = localStorage.getItem("finflow_usuario_neon");

    if (!usuarioTexto) {
        return;
    }

    let usuarioNeon = null;

    try {
        usuarioNeon = JSON.parse(usuarioTexto);
    } catch (error) {
        return;
    }

    const posiblesTarjetas = Array.from(document.querySelectorAll("div, section, aside"));

    const tarjetaSesion = posiblesTarjetas.find(function (elemento) {
        const texto = elemento.textContent || "";

        return texto.includes("Sesión activa") && texto.includes("Cerrar sesión");
    });

    if (!tarjetaSesion) {
        return;
    }

    const tituloRol = Array.from(tarjetaSesion.querySelectorAll("h1, h2, h3")).find(function (titulo) {
        const texto = titulo.textContent.trim();

        return texto === "Administrador" || texto === "Gerente" || texto === "Contador" || texto === "Empleado";
    });

    if (tituloRol) {
        tituloRol.textContent = (usuarioNeon.nombre || usuarioNeon.usuario) + " (" + usuarioNeon.usuario + ")";
    }

    let detalleNeon = document.getElementById("detalle-identidad-neon");

    if (!detalleNeon) {
        detalleNeon = document.createElement("div");
        detalleNeon.id = "detalle-identidad-neon";

        detalleNeon.style.marginTop = "14px";
        detalleNeon.style.marginBottom = "18px";
        detalleNeon.style.fontSize = "14px";
        detalleNeon.style.lineHeight = "1.5";
        detalleNeon.style.color = "rgba(255,255,255,0.75)";
        detalleNeon.style.fontWeight = "700";

        const botonCerrar = Array.from(tarjetaSesion.querySelectorAll("button")).find(function (boton) {
            return boton.textContent.trim().toLowerCase().includes("cerrar");
        });

        if (botonCerrar) {
            botonCerrar.insertAdjacentElement("beforebegin", detalleNeon);
        } else {
            tarjetaSesion.appendChild(detalleNeon);
        }
    }

    detalleNeon.innerHTML = `
        <div>Rol real: ${usuarioNeon.rol}</div>
        <div>Usuario: ${usuarioNeon.usuario}</div>
        <div>Carnet: ${usuarioNeon.carnet || "Sin carnet"}</div>
        <div>Correo: ${usuarioNeon.correo || "Sin correo"}</div>
    `;
}


// ======================================================
// MÓDULO WEB DE ADMINISTRACIÓN DE USUARIOS NEON
// ======================================================
// Permite que cualquier usuario con rol administrador pueda crear
// empleados, contadores, gerentes y administradores desde el dashboard web.

document.addEventListener("click", function (event) {
    const elemento = event.target;

    if (!elemento) {
        return;
    }

    const texto = elemento.textContent.trim().toLowerCase();

    if (texto === "usuarios") {
        event.preventDefault();

        const usuarioTexto = localStorage.getItem("finflow_usuario_neon");

        if (!usuarioTexto) {
            alert("Debe iniciar sesión como administrador.");
            return;
        }

        let usuarioActual = null;

        try {
            usuarioActual = JSON.parse(usuarioTexto);
        } catch (error) {
            alert("No se pudo leer la sesión actual.");
            return;
        }

        const rol = usuarioActual.rol.toLowerCase();

        if (rol !== "administrador" && rol !== "admin") {
            alert("Solo un administrador puede administrar usuarios.");
            return;
        }

        mostrarPanelCrearUsuariosNeon(usuarioActual);
    }
});


async function mostrarPanelCrearUsuariosNeon(usuarioActual) {
    let panelAnterior = document.getElementById("panel-admin-usuarios-neon");

    if (panelAnterior) {
        panelAnterior.remove();
    }

    const panel = document.createElement("section");
    panel.id = "panel-admin-usuarios-neon";

    panel.style.background = "white";
    panel.style.borderRadius = "32px";
    panel.style.padding = "32px";
    panel.style.margin = "30px 0";
    panel.style.boxShadow = "0 25px 70px rgba(0,0,0,0.08)";

    panel.innerHTML = `
        <h2 style="margin-top:0;">Administración de usuarios</h2>
        <p style="color:#666; font-weight:700;">
            Crear usuarios nuevos conectados a Neon.
        </p>

        <form id="form-crear-usuario-neon" style="
            display:grid;
            grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));
            gap:16px;
            margin-top:24px;
        ">
            <input name="nombre" placeholder="Nombre completo" required style="padding:16px; border-radius:18px; border:1px solid #ddd; font-weight:700;">
            <input name="correo" placeholder="Correo" required style="padding:16px; border-radius:18px; border:1px solid #ddd; font-weight:700;">
            <input name="usuario" placeholder="Usuario" required style="padding:16px; border-radius:18px; border:1px solid #ddd; font-weight:700;">
            <input name="password" placeholder="Contraseña" required type="password" style="padding:16px; border-radius:18px; border:1px solid #ddd; font-weight:700;">

            <select name="rol" required style="padding:16px; border-radius:18px; border:1px solid #ddd; font-weight:700;">
                <option value="">Seleccione rol</option>
                <option value="administrador">Administrador</option>
                <option value="gerente">Gerente</option>
                <option value="contador">Contador</option>
                <option value="empleado">Empleado</option>
            </select>

            <input name="empresa_id" placeholder="Empresa ID, opcional" style="padding:16px; border-radius:18px; border:1px solid #ddd; font-weight:700;">

            <button type="submit" style="
                border:none;
                background:#111;
                color:white;
                padding:16px;
                border-radius:999px;
                font-weight:900;
                cursor:pointer;
            ">
                Crear usuario
            </button>
        </form>

        <p id="mensaje-crear-usuario-neon" style="font-weight:900; margin-top:18px;"></p>

        <div id="tabla-usuarios-neon-web" style="margin-top:30px;"></div>
    `;

    const main = document.querySelector("main") || document.body;
    main.appendChild(panel);

    panel.scrollIntoView({
        behavior: "smooth"
    });

    const form = document.getElementById("form-crear-usuario-neon");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const formData = new FormData(form);

        const nuevoUsuario = {
            nombre: formData.get("nombre"),
            correo: formData.get("correo"),
            usuario: formData.get("usuario"),
            password: formData.get("password"),
            rol: formData.get("rol"),
            empresa_id: formData.get("empresa_id"),
            admin_actual: usuarioActual
        };

        const mensaje = document.getElementById("mensaje-crear-usuario-neon");

        try {
            const respuesta = await fetch("/api/usuarios", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(nuevoUsuario)
            });

            const datos = await respuesta.json();

            mensaje.textContent = datos.message;

            if (datos.success) {
                mensaje.style.color = "green";
                form.reset();
                cargarTablaUsuariosNeonWeb();
            } else {
                mensaje.style.color = "#b91c1c";
            }

        } catch (error) {
            console.error(error);
            mensaje.textContent = "No se pudo crear el usuario.";
            mensaje.style.color = "#b91c1c";
        }
    });

    cargarTablaUsuariosNeonWeb();
}


async function cargarTablaUsuariosNeonWeb() {
    const contenedor = document.getElementById("tabla-usuarios-neon-web");

    if (!contenedor) {
        return;
    }

    const respuesta = await fetch("/api/usuarios");
    const usuarios = await respuesta.json();

    let html = `
        <h3>Usuarios registrados</h3>
        <div style="overflow-x:auto;">
        <table style="width:100%; border-collapse:collapse; margin-top:16px;">
            <thead>
                <tr>
                    <th style="text-align:left; padding:12px; border-bottom:1px solid #ddd;">Nombre</th>
                    <th style="text-align:left; padding:12px; border-bottom:1px solid #ddd;">Correo</th>
                    <th style="text-align:left; padding:12px; border-bottom:1px solid #ddd;">Usuario</th>
                    <th style="text-align:left; padding:12px; border-bottom:1px solid #ddd;">Rol</th>
                    <th style="text-align:left; padding:12px; border-bottom:1px solid #ddd;">Carnet</th>
                    <th style="text-align:left; padding:12px; border-bottom:1px solid #ddd;">Estado</th>
                </tr>
            </thead>
            <tbody>
    `;

    usuarios.forEach(function (usuario) {
        html += `
            <tr>
                <td style="padding:12px; border-bottom:1px solid #eee;">${usuario.nombre || "-"}</td>
                <td style="padding:12px; border-bottom:1px solid #eee;">${usuario.correo || "-"}</td>
                <td style="padding:12px; border-bottom:1px solid #eee;">${usuario.usuario}</td>
                <td style="padding:12px; border-bottom:1px solid #eee;">${usuario.rol}</td>
                <td style="padding:12px; border-bottom:1px solid #eee;">${usuario.carnet || "-"}</td>
                <td style="padding:12px; border-bottom:1px solid #eee;">${usuario.estado}</td>
            </tr>
        `;
    });

    html += `
            </tbody>
        </table>
        </div>
    `;

    contenedor.innerHTML = html;
}


// ======================================================
// BOTÓN VISIBLE DE USUARIOS PARA ADMINISTRADORES
// ======================================================
// Agrega un botón "Administrar usuarios" dentro de la tarjeta de sesión
// solo cuando el usuario real de Neon tiene rol administrador.

function agregarBotonUsuariosAdminNeon() {
    const usuarioTexto = localStorage.getItem("finflow_usuario_neon");

    if (!usuarioTexto) {
        return;
    }

    let usuarioNeon = null;

    try {
        usuarioNeon = JSON.parse(usuarioTexto);
    } catch (error) {
        return;
    }

    const rol = usuarioNeon.rol.toLowerCase();

    if (rol !== "administrador" && rol !== "admin") {
        return;
    }

    if (document.getElementById("boton-admin-usuarios-neon")) {
        return;
    }

    const posiblesTarjetas = Array.from(document.querySelectorAll("div, section, aside"));

    const tarjetaSesion = posiblesTarjetas.find(function (elemento) {
        const texto = elemento.textContent || "";

        return texto.includes("Sesión activa") && texto.includes("Cerrar sesión");
    });

    if (!tarjetaSesion) {
        return;
    }

    const botonCerrar = Array.from(tarjetaSesion.querySelectorAll("button")).find(function (boton) {
        return boton.textContent.trim().toLowerCase().includes("cerrar");
    });

    const botonUsuarios = document.createElement("button");
    botonUsuarios.id = "boton-admin-usuarios-neon";
    botonUsuarios.textContent = "Administrar usuarios";

    botonUsuarios.style.width = "100%";
    botonUsuarios.style.marginTop = "18px";
    botonUsuarios.style.marginBottom = "12px";
    botonUsuarios.style.padding = "16px";
    botonUsuarios.style.borderRadius = "999px";
    botonUsuarios.style.border = "none";
    botonUsuarios.style.background = "#d6c06a";
    botonUsuarios.style.color = "#111";
    botonUsuarios.style.fontWeight = "900";
    botonUsuarios.style.cursor = "pointer";

    botonUsuarios.addEventListener("click", function (event) {
        event.preventDefault();
        event.stopPropagation();

        mostrarPanelCrearUsuariosNeon(usuarioNeon);
    });

    if (botonCerrar) {
        botonCerrar.insertAdjacentElement("beforebegin", botonUsuarios);
    } else {
        tarjetaSesion.appendChild(botonUsuarios);
    }
}
