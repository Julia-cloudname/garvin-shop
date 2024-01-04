#### **Garvin Card Shop Testing Documentation**

## **Table of contents**
 - [**HTML Validation**](#html-validation)
 - [**CSS Validation**](#css-validation)
 - [**Python Validation**](#python-validation)
 - [**Lighthouse**](#lighthouse)
 - [**Manual testing**](#manual-testing)
 - [**Bugs and Issues**](#bugs-and-issues)

<hr>

## **HTML Validation**

* No errors detected when run through the official [W3C HTML Validation Service](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgarvin-df2eed558b96.herokuapp.com%2F)

<hr>

## **CSS Validation**

* CSS – no errors were found when passing through the official [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgarvin-df2eed558b96.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=0&vextwarning=&lang=en#errors)

<hr>

## **Python Validation**

All Python code has been run through the [PEP8 Online Testing](https://pep8online.com/) validator and has returned no errors.

<hr>

## **Lighthouse**
Results from Lighthouse testing for both Mobile and Desktop versions show high performance, accessibility, best practices, and SEO scores.

<details>

<summary> Lighthouse </summary>

![Lighthouse](/media/lighthous-desktop.png)

</details>

<hr>

## **Manual testing** 

#### **Devices:**
- Tested on various devices including laptops, smartphones, and tablets.

#### **Browsers:**
- Chrome
- Safari
- Firefox
- Edge

#### **Features Tested:**

#### **Navigation**

- Navigation links (Home, Products, Special Offers, Contact Us, About Us) are active and functional.
- Additional options for registered users (Profile, Log Out) are functioning correctly.
- Responsive burger menu on smaller screens functions properly.

#### **Products Page**

- Product listings are correctly displayed.
- Each product has a functional link to its detailed view.

#### **Reviews**

- Functionality for displaying and adding reviews is working as expected.

#### **Special Offers Page**

- Special offers and promotions are prominently displayed.
- Links to products on offer are functioning correctly.

#### **Contact Us Page**

- Contact form is functioning as expected.
- Essential contact information is clearly displayed.

#### **About Us Page**

- Provides detailed information about Garvin Card Shop.
- Content is well-structured and informative.

#### **Profile Page (For Registered Users)**

- Displays user information and order history correctly.
- Allows for efficient account management.

#### **Wishlist Page**

- Functionality for adding and viewing wishlist items is working as expected.

#### **History Views Page**

- Functionality for displaying and deleting items is working as expected.

#### **Administrative Panel (For Admin Users)**

- Admins can effectively manage product listings, user accounts, and view order data.

#### **Signup and Login Functionality**

- Users can sign up, log in, and log out without issues.

#### **Footer**

- Social media links are functional and direct users to the respective platforms.

#### **Newsletter sign up**

- Functionality for Newsletter sign-up is working as expected.

#### **Get in touch**

- Functionality for sending messages is working as expected.

<hr>

## **Bugs and Issues**

During testing, I encountered a TypeError: unsupported format string passed to NoneType.__format__ error in the product_detail view of Django application. This error was triggered when attempting to display the rating of a product as a formatted string. The issue arose because the product.rating could be None if there were no reviews for the product, and the code attempted to format this None value using string formatting, which is not supported for NoneType.

Resolution

To address this issue, the product_detail view was updated with a conditional check that verifies if product.rating is None. If it is not None, the rating is formatted as a floating-point number with one decimal place. If it is None, indicating that there are no reviews and therefore no rating, a default string "No rating" is assigned. This approach ensures that the application can gracefully handle products without reviews without encountering a TypeError.

<hr>
