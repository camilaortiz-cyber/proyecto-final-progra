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

// Agrega ID a movimientos antiguos que fueron creados antes de esta mejora.
for (let i = 0; i < demoMovements.length; i++) {
    if (!demoMovements[i].id) {
        demoMovements[i].id = Date.now() + "-" + i;
    }
}

// Guarda los movimientos antiguos ya corregidos con ID.
saveDemoMovements();

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

    // Actualiza dashboard y lista de movimientos.
    renderDemoApp();

    // Actualiza presupuestos si existe el módulo.
    if (typeof renderBudgets === "function") {
        renderBudgets();
    }

    // Actualiza metas si existe el módulo.
    if (typeof renderGoals === "function") {
        renderGoals();
    }

    // Actualiza alertas si existe el módulo.
    if (typeof renderAlerts === "function") {
        renderAlerts();
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

    if (typeof renderExecutiveMonthlyReport === "function") {
        renderExecutiveMonthlyReport();
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
        renderClients();
        renderExecutiveMonthlyReport();
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
        renderSuppliers();
        renderAlerts();
        renderExecutiveMonthlyReport();
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
        renderBudgets();
        renderAlerts();
        renderExecutiveMonthlyReport();
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
        renderGoals();
        renderAlerts();
        renderExecutiveMonthlyReport();
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
            saveClients();
            renderClients();
            renderExecutiveMonthlyReport();
        }

        if (actionButton.classList.contains("client-delete-button")) {
            const clientIndex = Number(actionButton.dataset.clientIndex);
            registerDeletedItem("Cliente", finflowClients[clientIndex].name);
            finflowClients.splice(clientIndex, 1);
            saveClients();
            renderClients();
            renderExecutiveMonthlyReport();
        }

        if (actionButton.classList.contains("supplier-status-button")) {
            const supplierIndex = Number(actionButton.dataset.supplierIndex);
            finflowSuppliers[supplierIndex].status = actionButton.dataset.supplierStatus;
            saveSuppliers();
            renderSuppliers();
            renderAlerts();
            renderExecutiveMonthlyReport();
        }

        if (actionButton.classList.contains("supplier-delete-button")) {
            const supplierIndex = Number(actionButton.dataset.supplierIndex);
            registerDeletedItem("Proveedor", finflowSuppliers[supplierIndex].name);
            finflowSuppliers.splice(supplierIndex, 1);
            saveSuppliers();
            renderSuppliers();
            renderAlerts();
            renderExecutiveMonthlyReport();
        }

        if (actionButton.classList.contains("budget-delete-button")) {
            const budgetIndex = Number(actionButton.dataset.budgetIndex);
            registerDeletedItem("Presupuesto", finflowBudgets[budgetIndex].category);
            finflowBudgets.splice(budgetIndex, 1);
            saveBudgets();
            renderBudgets();
            renderAlerts();
            renderExecutiveMonthlyReport();
        }

        if (actionButton.classList.contains("goal-delete-button")) {
            const goalIndex = Number(actionButton.dataset.goalIndex);
            registerDeletedItem("Meta", finflowGoals[goalIndex].name);
            finflowGoals.splice(goalIndex, 1);
            saveGoals();
            renderGoals();
            renderAlerts();
            renderExecutiveMonthlyReport();
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

// ===== REPORTE MENSUAL EJECUTIVO COMPACTO =====

let execTrendChart = null;
let execMixChart = null;
let execOpsChart = null;

function getExecUser() {
    const savedUser = localStorage.getItem("finflowExperienceUser");

    if (savedUser && experienceUsers[savedUser]) {
        return {
            username: savedUser,
            role: savedUser,
            roleName: experienceUsers[savedUser].roleName
        };
    }

    return {
        username: "admin",
        role: "admin",
        roleName: "Administrador"
    };
}

function getExecMovementAmount(movement) {
    if (movement.amount !== undefined) {
        return Number(movement.amount);
    }

    if (movement.monto !== undefined) {
        return Number(movement.monto);
    }

    return 0;
}

function isExecIncome(movement) {
    return movement.type === "income" || movement.tipo === "ingreso";
}

function isExecExpense(movement) {
    return movement.type === "expense" || movement.tipo === "gasto";
}

function getExecMonthlyMovements() {
    if (Array.isArray(demoMovements)) {
        return demoMovements;
    }

    return [];
}

function getExecData() {
    const movements = getExecMonthlyMovements();

    let alerts = [];

    if (typeof buildAutomaticAlerts === "function") {
        alerts = buildAutomaticAlerts();
    }

    let income = 0;
    let expense = 0;
    let incomeTransactions = 0;
    let expenseTransactions = 0;
    let totalTransactionAmount = 0;
    let biggestTransaction = null;

    for (let i = 0; i < movements.length; i++) {
        const movement = movements[i];
        const amount = Number(movement.amount || movement.monto || 0);

        totalTransactionAmount = totalTransactionAmount + amount;

        if (movement.type === "income" || movement.tipo === "ingreso") {
            income = income + amount;
            incomeTransactions = incomeTransactions + 1;
        }

        if (movement.type === "expense" || movement.tipo === "gasto") {
            expense = expense + amount;
            expenseTransactions = expenseTransactions + 1;
        }

        if (!biggestTransaction || amount > Number(biggestTransaction.amount || biggestTransaction.monto || 0)) {
            biggestTransaction = movement;
        }
    }

    const profit = income - expense;
    const movementCount = movements.length;
    const average = movementCount > 0 ? totalTransactionAmount / movementCount : 0;
    const margin = income > 0 ? (profit / income) * 100 : 0;

    let completedGoals = 0;
    let totalGoalProgress = 0;

    for (let i = 0; i < finflowGoals.length; i++) {
        let progress = 0;

        if (typeof calculateGoalProgress === "function") {
            progress = calculateGoalProgress(finflowGoals[i]).percentage;
        }

        const safeProgress = Math.min(Math.max(progress, 0), 100);

        totalGoalProgress = totalGoalProgress + safeProgress;

        if (safeProgress >= 100) {
            completedGoals = completedGoals + 1;
        }
    }

    const averageGoalProgress = finflowGoals.length > 0 ? totalGoalProgress / finflowGoals.length : 0;

    return {
        movements: movements,
        income: income,
        expense: expense,
        profit: profit,
        movementCount: movementCount,
        incomeTransactions: incomeTransactions,
        expenseTransactions: expenseTransactions,
        average: average,
        margin: margin,
        clients: finflowClients.length,
        suppliers: finflowSuppliers.length,
        budgets: finflowBudgets.length,
        alerts: alerts.length,
        goals: finflowGoals.length,
        completedGoals: completedGoals,
        averageGoalProgress: averageGoalProgress,
        biggestTransaction: biggestTransaction
    };
}
function setExecText(id, value) {
    const element = document.getElementById(id);

    if (element) {
        element.textContent = value;
    }
}

function renderExecutiveMonthlyReport() {
    const user = getExecUser();
    const data = getExecData();

    setExecText("execIncome", formatCurrency(data.income));
    setExecText("execExpenses", formatCurrency(data.expense));
    setExecText("execProfit", formatCurrency(data.profit));
    setExecText("execMovements", data.movementCount);
    setExecText("execAverage", formatCurrency(data.average));
    setExecText("execClients", data.clients);
    setExecText("execSuppliers", data.suppliers);
    setExecText("execBudgets", data.budgets);
    setExecText("execAlerts", data.alerts);
    setExecText("execGoals", data.completedGoals + "/" + data.goals);
    setExecText("execMargin", Math.round(data.margin) + "%");

    renderExecRoleSummary(user, data);
    renderExecInsight(data);
    renderExecCharts(data);
}

function renderExecRoleSummary(user, data) {
    const title = document.getElementById("execRoleTitle");
    const content = document.getElementById("execRoleContent");

    if (!title || !content) {
        return;
    }

    if (user.role === "admin") {
        title.textContent = "Resumen ejecutivo para administrador";
        content.innerHTML =
            "<ul>" +
                "<li>Utilidad mensual: " + formatCurrency(data.profit) + " con margen de " + Math.round(data.margin) + "%.</li>" +
                "<li>Transacciones: " + data.movementCount + " (" + data.incomeTransactions + " ingresos y " + data.expenseTransactions + " gastos).</li>" +
                "<li>Promedio por transacción: " + formatCurrency(data.average) + ".</li>" +
                "<li>Clientes: " + data.clients + ". Proveedores: " + data.suppliers + ".</li>" +
                "<li>Alertas activas: " + data.alerts + ". Metas cumplidas: " + data.completedGoals + " de " + data.goals + ".</li>" +
            "</ul>";
    } else if (user.role === "gerente") {
        title.textContent = "Resumen operativo para gerente";
        content.innerHTML =
            "<ul>" +
                "<li>Resultado mensual: " + formatCurrency(data.profit) + ".</li>" +
                "<li>Actividad del equipo: " + data.movementCount + " movimientos.</li>" +
                "<li>Relación comercial: " + data.clients + " clientes y " + data.suppliers + " proveedores.</li>" +
                "<li>Progreso promedio de metas: " + Math.round(data.averageGoalProgress) + "%.</li>" +
                "<li>Alertas que requieren seguimiento: " + data.alerts + ".</li>" +
            "</ul>";
    } else if (user.role === "contador") {
        title.textContent = "Resumen financiero para contador";
        content.innerHTML =
            "<ul>" +
                "<li>Ingresos contables: " + formatCurrency(data.income) + ".</li>" +
                "<li>Gastos contables: " + formatCurrency(data.expense) + ".</li>" +
                "<li>Flujo neto: " + formatCurrency(data.profit) + ".</li>" +
                "<li>Promedio por movimiento: " + formatCurrency(data.average) + ".</li>" +
                "<li>Transacciones revisables: " + data.movementCount + ".</li>" +
            "</ul>";
    } else if (user.role === "empleado") {
        title.textContent = "Resumen personal para empleado";
        content.innerHTML =
            "<ul>" +
                "<li>Movimientos registrados este mes: " + data.movementCount + ".</li>" +
                "<li>Ingresos registrados: " + data.incomeTransactions + ".</li>" +
                "<li>Gastos registrados: " + data.expenseTransactions + ".</li>" +
                "<li>Vista enfocada en actividad operativa y registros diarios.</li>" +
            "</ul>";
    }
}

function renderExecInsight(data) {
    const element = document.getElementById("execInsight");

    if (!element) {
        return;
    }

    if (data.movementCount === 0) {
        element.textContent = "Todavía no hay suficientes movimientos para generar un análisis ejecutivo. Registra ingresos y gastos para activar el diagnóstico mensual.";
        return;
    }

    if (data.profit < 0) {
        element.textContent = "El mes presenta pérdida operativa. Se recomienda revisar gastos altos, presupuestos y proveedores pendientes.";
        return;
    }

    if (data.alerts > 0 && data.averageGoalProgress < 50) {
        element.textContent = "Hay alertas activas y las metas avanzan lento. El foco debe estar en reducir riesgos y acelerar acciones comerciales.";
        return;
    }

    if (data.margin >= 40 && data.alerts === 0) {
        element.textContent = "El desempeño mensual es fuerte: margen saludable, operación estable y sin alertas activas.";
        return;
    }

    element.textContent = "El mes se mantiene estable. Conviene monitorear margen, metas, presupuestos y comportamiento de proveedores.";
}

function destroyExecCharts() {
    if (execTrendChart) {
        execTrendChart.destroy();
        execTrendChart = null;
    }

    if (execMixChart) {
        execMixChart.destroy();
        execMixChart = null;
    }

    if (execOpsChart) {
        execOpsChart.destroy();
        execOpsChart = null;
    }
}

function renderExecCharts(data) {
    if (typeof Chart === "undefined") {
        return;
    }

    const trendCanvas = document.getElementById("execTrendChart");
    const mixCanvas = document.getElementById("execMixChart");
    const opsCanvas = document.getElementById("execOpsChart");

    if (!trendCanvas || !mixCanvas || !opsCanvas) {
        return;
    }

    destroyExecCharts();

    const chartText = "#ffffff";
    const mutedText = "rgba(255, 255, 255, 0.58)";
    const gold = "#d4af37";
    const softGold = "#fff2b0";
    const darkGold = "#7c5a18";

    const trendLabels = [];
    const trendValues = [];

    for (let i = 0; i < data.movements.length; i++) {
        trendLabels.push("Mov " + (i + 1));
        trendValues.push(getExecMovementAmount(data.movements[i]));
    }

    if (trendLabels.length === 0) {
        trendLabels.push("Sin datos");
        trendValues.push(0);
    }

    execTrendChart = new Chart(trendCanvas, {
        type: "line",
        data: {
            labels: trendLabels,
            datasets: [
                {
                    label: "Monto",
                    data: trendValues,
                    borderColor: gold,
                    backgroundColor: "rgba(212, 175, 55, 0.18)",
                    tension: 0.38,
                    fill: true,
                    pointRadius: 3,
                    pointBackgroundColor: softGold
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
                    ticks: { color: mutedText },
                    grid: { color: "rgba(255,255,255,0.05)" }
                },
                y: {
                    ticks: { color: mutedText },
                    grid: { color: "rgba(255,255,255,0.06)" }
                }
            }
        }
    });

    execMixChart = new Chart(mixCanvas, {
        type: "doughnut",
        data: {
            labels: ["Ingresos", "Gastos"],
            datasets: [
                {
                    data: [data.income, data.expense],
                    backgroundColor: [gold, darkGold],
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
                        color: chartText
                    }
                }
            }
        }
    });

    execOpsChart = new Chart(opsCanvas, {
        type: "bar",
        data: {
            labels: ["Clientes", "Proveedores", "Presup.", "Metas", "Alertas"],
            datasets: [
                {
                    label: "Cantidad",
                    data: [data.clients, data.suppliers, data.budgets, data.goals, data.alerts],
                    backgroundColor: [
                        "rgba(212, 175, 55, 0.85)",
                        "rgba(255, 242, 176, 0.75)",
                        "rgba(212, 175, 55, 0.55)",
                        "rgba(255, 255, 255, 0.62)",
                        "rgba(124, 90, 24, 0.85)"
                    ],
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
                    ticks: { color: mutedText },
                    grid: { display: false }
                },
                y: {
                    ticks: { color: mutedText, precision: 0 },
                    grid: { color: "rgba(255,255,255,0.06)" }
                }
            }
        }
    });
}

document.addEventListener("click", function () {
    setTimeout(renderExecutiveMonthlyReport, 60);
});

document.addEventListener("submit", function () {
    setTimeout(renderExecutiveMonthlyReport, 60);
});

window.addEventListener("load", function () {
    setTimeout(renderExecutiveMonthlyReport, 120);
});

setTimeout(function () {
    refreshBusinessBrain();
    renderModules();
    renderExecutiveMonthlyReport();
}, 150);