// Funcionalidades JavaScript para TeenSmartInsight

document.addEventListener('DOMContentLoaded', function() {
    // Auto-cerrar alertas después de 5 segundos
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
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