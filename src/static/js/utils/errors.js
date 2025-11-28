export function showError(err) {
    if (err.erro) {
        alert(`Erro: ${err.erro}`);
    } else {
        alert('Erro inesperado. Tente novamente.');
    }
}