
async function getProducts() {
    const response = await fetch('/products');
    const data = await response.json();
    return data.data;
}

async function displayProducts() {
    const productsContainer = document.getElementById('products-container');
    productsContainer.innerHTML = '';

    const products = await getProducts();

    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.classList.add('product');
        productElement.innerHTML = `
            <h3>${product.name}</h3>
            <p>Price: $${product.price}</p>
            <p>Quantity: ${product.quantity}</p>
        `;
        productsContainer.appendChild(productElement);
    });
}

displayProducts();
