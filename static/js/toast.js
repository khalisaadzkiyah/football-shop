function showToast(title, message, type = 'normal', duration = 3000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toastComponent) return;

    // Remove all type classes first
    toastComponent.classList.remove(
        'bg-[#FFE4EC]', 'border-[#F5A3C0]', 'text-[#831843]',
        'bg-[#FFF0F6]', 'border-[#F5C6DD]', 'text-[#831843]'
    );

    // Set type styles
    if (type === 'success') {
        toastComponent.classList.add('bg-[#FFF0F6]', 'border-[#F5C6DD]', 'text-[#831843]');
        toastComponent.style.border = '1px solid #F5C6DD';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-[#FFE4EC]', 'border-[#F5A3C0]', 'text-[#831843]');
        toastComponent.style.border = '1px solid #F5A3C0';
    } else {
        toastComponent.classList.add('bg-[#FFF0F6]', 'border-[#F5C6DD]', 'text-[#831843]');
        toastComponent.style.border = '1px solid #F5C6DD';
    }

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', 'translate-y-64');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-64');
    }, duration);
}
