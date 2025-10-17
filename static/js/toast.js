function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');

    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-red-50', 'border-red-200', 'text-red-700',
        'bg-green-50', 'border-green-200', 'text-green-700',
        'bg-pink-50', 'border-pink-200', 'text-pink-700'
    );

    // Set type styles and icon
    if (type === 'success') {
        toastComponent.classList.add('bg-green-50', 'border-green-200', 'text-green-700');
        toastIcon.textContent = '✅';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-50', 'border-red-200', 'text-red-700');
        toastIcon.textContent = '⚠️';
    } else { // normal/info
        toastComponent.classList.add('bg-pink-50', 'border-pink-200', 'text-pink-700');
        toastIcon.textContent = 'ℹ️';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Show toast
    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    // Hide after duration
    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}
