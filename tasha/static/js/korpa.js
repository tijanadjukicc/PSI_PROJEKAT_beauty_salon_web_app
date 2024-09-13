document.addEventListener('DOMContentLoaded', function () {
    const updateSummary = () => {
        let totalItems = 0;
        let totalPrice = 0;

        document.querySelectorAll('.main').forEach(item => {
            const quantity = parseInt(item.querySelector('.quantity').textContent) || 0;
            const price = parseFloat(item.querySelector('.price').textContent) || 0;

            totalItems += quantity;
            totalPrice += quantity * price;
        });

        document.getElementById('total-items').textContent = totalItems + ' artikla';
        document.getElementById('item-count').textContent = totalItems;
        document.getElementById('total-price').textContent = totalPrice.toFixed(2);
        document.getElementById('final-price').textContent = totalPrice.toFixed(2); // Update this line if you have discounts or shipping
    };

    document.querySelectorAll('.increase').forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const quantityElement = this.previousElementSibling;
            let quantity = parseInt(quantityElement.textContent) || 0;
            quantity++;
            quantityElement.textContent = quantity;
            updateSummary();
        });
    });

    document.querySelectorAll('.decrease').forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const quantityElement = this.nextElementSibling;
            let quantity = parseInt(quantityElement.textContent) || 0;
            if (quantity > 1) {
                quantity--;
                quantityElement.textContent = quantity;
                updateSummary();
            }
        });
    });

    document.getElementById('discount-select').addEventListener('change', updateSummary);
    document.getElementById('shipping-select').addEventListener('change', updateSummary);

    updateSummary();
});
