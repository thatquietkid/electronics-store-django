# Shockit Electronics

![Django](https://img.shields.io/badge/Django-5.1.4-blue)
![Python](https://img.shields.io/badge/Python-3.12.4-yellow)
![Tailwind](https://img.shields.io/badge/Tailwind-2.2.19-aqua)

**Shockit Electronics** is an e-commerce platform designed to offer a seamless shopping experience for electronic products. This project is built using **Django** as the backend framework, **Tailwind CSS** for styling, and **HTMX** to provide dynamic and responsive interactions without the need for complex JavaScript frameworks.

## Features

- **Product Listings**: Browse through a wide range of electronic products.
- **Cart System**: Add products to your cart, view your cart, and modify quantities.
- **User Authentication**: Secure login, registration, and profile management for customers.
- **Responsive Design**: The site is fully responsive, optimized for both desktop and mobile users.
- **Dynamic Content**: Real-time updates of cart items and product details with HTMX.
- **Search & Filtering**: Easily search for products and filter by categories or price range.

## Tech Stack

- **Backend**: Django
- **Frontend**: Tailwind CSS, HTMX
- **Database**: SQLite (for development; can be configured to use other databases)
- **Authentication**: Django's built-in authentication system

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/thatquietkid/electronics-store-django.git
    cd shockit
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Mac/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser** (optional but recommended for admin access):

    ```bash
    python manage.py createsuperuser
    ```

7. **Start the development server**:

    ```bash
    python manage.py runserver
    ```

8. **Open the app in your browser**:
    Visit `http://127.0.0.1:8000/` to access the project.

## Usage

- **Browse Products**: Navigate through different categories and view product details.
- **Add to Cart**: Click on the cart icon to add products to your shopping cart.
- **Checkout**: Go to your cart and proceed with checkout.
- **Admin Panel**: Visit `/admin` and use the superuser credentials to manage products, orders, and users.

## HTMX Integration

HTMX is used to create dynamic updates for cart operations, like adding/removing products from the cart, without reloading the entire page. This improves the user experience and performance.

## Tailwind CSS

Tailwind CSS provides utility-first classes that enable you to create custom designs directly in your HTML, resulting in faster development and easy-to-maintain styles.

## Contributing

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- **Django** for the powerful and flexible backend framework.
- **Tailwind CSS** for efficient and responsive design.
- **HTMX** for enhancing the interactivity without full-page reloads.
