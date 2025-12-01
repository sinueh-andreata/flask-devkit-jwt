import { createProduct } from '../api/products.js';

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('formProduct');
    const csrfToken = document.getElementById('csrf_token').value;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = Object.fromEntries(new FormData(form).entries()); // Converte os dados do formulário em um objeto

        try {
            const novoProduct = await createProduct(data, csrfToken);
            console.log('Product criado:', novoProduct);
        } catch (error) {
            console.error('Erro ao create product:', error);
        }
    });
});