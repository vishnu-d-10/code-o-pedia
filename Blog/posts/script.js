const products = [
    {
        id: 1,
        name: 'Classy Bike',
        description: 'A stylish and modern bike',
        imageUrl: 'bmw-k100-motorcycle.jpg',
        likes: 0,
        comments: []
    },
    {
        id: 2,
        name: 'Asus wallpaper',
        description: 'A stunning HD wallpaper',
        imageUrl: 'zephyrus g14_1920x1080.jpg', // Filename of the image
        likes: 0,
        comments: []
    },
    // Add more products here
];

const productContainer = document.getElementById('product-container');

function renderProducts() {
    productContainer.innerHTML = '';

    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.classList.add('product');
        
        productElement.innerHTML = `
            <img src="${product.imageUrl}" alt="${product.name}">
            <h2>${product.name}</h2>
            <p>${product.description}</p>
            <div class="like-btn ${product.liked ? 'liked' : ''}" data-id="${product.id}">
                <span class="heart-symbol">&hearts;</span> ${product.likes}
            </div>
            <div class="comment-section">
                <textarea placeholder="Add a comment"></textarea>
                <button onclick="addComment(${product.id})">Add Comment</button>
                <ul>
                    ${product.comments.map(comment => `<li>${comment}</li>`).join('')}
                </ul>
            </div>
        `;

        productContainer.appendChild(productElement);
    });
}

function addComment(productId) {
    const product = products.find(prod => prod.id === productId);
    const commentInput = document.querySelector(`[data-id="${productId}"]`).parentNode.querySelector('textarea');
    const newComment = commentInput.value.trim();

    if (newComment !== '') {
        product.comments.push(newComment);
        commentInput.value = '';
        renderProducts();
    }
}

productContainer.addEventListener('click', event => {
    if (event.target.classList.contains('like-btn')) {
        const productId = parseInt(event.target.getAttribute('data-id'));
        const product = products.find(prod => prod.id === productId);
        
        product.liked = !product.liked;
        if (product.liked) {
            product.likes++;
        } else {
            product.likes--;
        }

        renderProducts();
    }
});

renderProducts();