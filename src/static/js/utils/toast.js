export function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.textContent = message;
    toast.className = `
            fixed bottom-6 left-1/2 -translate-x-1/2 px-4 py-3 rounded-lg shadow-lg text-white text-sm font-medium
            transition-all duration-500 transform
            ${type === 'success' ? 'bg-green-600' : 'bg-red-600'}
            opacity-0 translate-y-3
        `;
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.classList.remove('opacity-0', 'translate-y-3');
        toast.classList.add('opacity-100', 'translate-y-0');
    }, 50);
    setTimeout(() => {
        toast.classList.remove('opacity-100', 'translate-y-0');
        toast.classList.add('opacity-0', 'translate-y-3');
        setTimeout(() => toast.remove(), 500);
    }, 3000);
}
