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
        modules: ["ingresos", "gastos", "reportes", "ia", "clientes", "proveedores", "presupuestos", "metas", "alertas", "neon"] // Módulos visibles para admin.
    },
    gerente: {
        password: "1234", // Contraseña demo del gerente.
        roleName: "Gerente", // Nombre visual del rol.
        description: "Consulta indicadores, flujo financiero, reportes y alertas para tomar decisiones.", // Descripción del rol.
        modules: ["reportes", "ia", "metas", "alertas", "neon"] // Módulos visibles para gerente.
    },
    contador: {
        password: "1234", // Contraseña demo del contador.
        roleName: "Contador", // Nombre visual del rol.
        description: "Registra, revisa y analiza ingresos, gastos, presupuestos y reportes financieros.", // Descripción del rol.
        modules: ["ingresos", "gastos", "reportes", "ia", "presupuestos", "metas"] // Módulos visibles para contador.
    },
    empleado: {
        password: "1234", // Contraseña demo del empleado.
        roleName: "Empleado", // Nombre visual del rol.
        description: "Registra ventas, ingresos diarios y gastos operativos de caja chica.", // Descripción sin decir acceso limitado.
        modules: ["ingresos", "gastos", "ia"] // Módulos visibles para empleado.
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

    // Recorre todos los checkboxes de módulos existentes en la demo.
    for (let i = 0; i < moduleToggles.length; i++) {
        const toggle = moduleToggles[i]; // Guarda el checkbox actual.
        const label = toggle.closest("label"); // Busca el label que contiene ese checkbox.
        const isAllowed = user.modules.includes(toggle.value); // Verifica si el módulo pertenece al rol.

        toggle.checked = isAllowed; // Activa o desactiva el checkbox según el rol.

        if (label) { // Si el checkbox tiene label...
            label.style.display = isAllowed ? "flex" : "none"; // Muestra solo módulos permitidos.
        }
    }

    if (roleAiSelect && roleAiResponse) { // Si existe el módulo visual de IA por rol...
        roleAiSelect.value = username; // Selecciona el rol actual.
        roleAiResponse.textContent = roleAiMessages[username]; // Muestra el mensaje del rol.
    }

    customizeFormsByRole(username); // Personaliza formularios y asistente según el rol.

    localStorage.setItem("finflowExperienceUser", username); // Guarda la sesión en el navegador.

    if (typeof renderModules === "function") { // Verifica si existe la función que pinta módulos.
        renderModules(); // Actualiza la vista de módulos activos.
    }

    window.scrollTo({ // Mueve la pantalla arriba para que parezca cambio de página.
        top: 0,
        behavior: "smooth"
    });
}

// Escucha cuando el usuario envía el formulario de login.
if (experienceLoginForm) {
    experienceLoginForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita que la página se recargue.

        const username = experienceUsername.value.trim().toLowerCase(); // Limpia y normaliza el usuario.
        const password = experiencePassword.value.trim(); // Limpia la contraseña.
        const user = experienceUsers[username]; // Busca el usuario ingresado.

        if (!user || user.password !== password) { // Valida usuario y contraseña.
            experienceLoginError.textContent = "Usuario o contraseña incorrectos."; // Muestra error.
            return; // Detiene el login.
        }

        experienceLoginError.textContent = ""; // Limpia cualquier error anterior.
        applyExperienceRole(username); // Aplica la experiencia según el rol.
    });
}

// Escucha el botón de cerrar sesión.
if (logoutExperienceButton) {
    logoutExperienceButton.addEventListener("click", function () {
        localStorage.removeItem("finflowExperienceUser"); // Borra la sesión guardada.

        document.body.classList.remove("finflow-session-active"); // Quita el modo app interna.

        if (finflowAppShell) { // Si existe la app...
            finflowAppShell.classList.remove("is-unlocked"); // La vuelve a ocultar.
        }

        if (experienceLogin) { // Si existe el login...
            experienceLogin.style.display = "grid"; // Lo vuelve a mostrar.
        }

        if (sessionRoleCard) { // Si existe la tarjeta de sesión...
            sessionRoleCard.hidden = true; // La vuelve a ocultar.
        }

        window.scrollTo({ // Regresa arriba de la landing.
            top: 0,
            behavior: "smooth"
        });
    });
}

// Escucha cambios manuales en el selector de IA por rol, si ese módulo existe.
if (roleAiSelect && roleAiResponse) {
    roleAiSelect.addEventListener("change", function () {
        const selectedRole = roleAiSelect.value; // Obtiene el rol seleccionado.
        roleAiResponse.textContent = roleAiMessages[selectedRole]; // Cambia el mensaje de IA.
    });
}

// Revisa si ya había una sesión guardada en el navegador.
const savedExperienceUser = localStorage.getItem("finflowExperienceUser");

// Si había sesión válida, la restaura automáticamente.
if (savedExperienceUser && experienceUsers[savedExperienceUser]) {
    applyExperienceRole(savedExperienceUser);
}




