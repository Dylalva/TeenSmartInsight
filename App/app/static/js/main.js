// Funcionalidades JavaScript para TeenSmartInsight

document.addEventListener('DOMContentLoaded', function() {
    // Solo auto-cerrar alertas de notificación, no las alertas de resultados
    const notificationAlerts = document.querySelectorAll('.alert.alert-dismissible');
    notificationAlerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Validación del lado del cliente para los campos numéricos
    const numericInputs = document.querySelectorAll('input[type="number"], input[type="text"]');
    numericInputs.forEach(function(input) {
        input.addEventListener('input', function(e) {
            const value = e.target.value;
            if (value && isNaN(parseFloat(value))) {
                e.target.classList.add('is-invalid');
            } else {
                e.target.classList.remove('is-invalid');
            }
        });
    });
});