import { showToast } from '../utils/toast.js';
import { showError } from '../utils/errors.js';
import { postData } from '../utils/fetchUtils.js';

export async function createProduct(product, csrfToken) {
    try {
        const data = await postData('/products/cadastrar', product, {
            'X-CSRFToken': csrfToken
        });
        showToast('Product criado com sucesso!', 'success');
        return data;
    } catch (error) {
        showError(error);
        throw error;
    }
}