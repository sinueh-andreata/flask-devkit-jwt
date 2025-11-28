import { createProduct } from '../api/products.js';

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('formProduct');
    const csrfToken = document.getElementById('csrf_token').value;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            const novoProduct = await createProduct(data, csrfToken); // Passe o token aqui
            console.log('Product criado:', novoProduct);
        } catch (error) {
            console.error('Erro ao create product:', error);
        }
    });
});