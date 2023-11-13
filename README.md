# **Garvin card shop**

The Marisol Furniture website serves as a portfolio and blog platform designed for potential customers interested in bespoke furniture. This project is developed using the Django framework and incorporates various features that facilitate interaction between customers and furniture specialists. Marisol Furniture offers users the ability to request a consultation call with an expert who can provide insights into custom furniture options, pricing, materials, and more.

[Garvin](https://garvin-df2eed558b96.herokuapp.com/) - The live site can be viewed here.

![Am I Responsive?](/media/responsive.png)

<hr>

## **TABLE OF CONTENTS**

 - [**User Experience (UX)**](#user-experience-ux)
    * [User Stories](#user-stories)
    * [Agile Methodology](#agile-methodology)
    * [The Scope](#the-scope)
 - [**Design**](#design)
    * [Styling and Aesthetics](#styling-and-aesthetics)
    * [Color Scheme](#colour-scheme)
    * [Typography](#typography)
    * [Wireframes](#wireframes)
 - [**Features**](#features)
   * [Navigation](#navigation)
   * [Footer](#footer)
   * [Home Page](#home-page)
   * [Homepage Display](#homepage-display)
   * [Product Page](#product-page)
   * [Product Edit and Delete](#product-edit-delete)
   * [Bag Page](#bag-page)
   * [Profile Page](#profile-page)
   * [Wishlist Page](#wishlist-page)
   * [Administrative Panel](#administrative-panel)
   * [Signup Page](#signup-page)
   * [Future Additions](#future-additions)
 - [**Testing**](#testing)
 - [**Technologies Used**](#technology-used)
 - [**Deployment**](#deployment)
 - [**Credits**](#credits)

<hr>

## **USER EXPERIENCE (UX)**

### **User Stories**

**Unregistered Site User:**

- As a user, I want to immediately grasp the site's purpose upon landing on the homepage.
- As a user, I need to navigate the site effortlessly, without confusion.
- As a user, I wish to browse a selection of available postcards.
- As a user, I want to view the details of each postcard, including price and design.
- As a user, I expect to see customer reviews and ratings for postcards.
- As a user, I should be able to access and follow the shop's social media links.
- As a user, I want the option to register for an account on the site.

**Registered Site User:**

- As a registered user, I want to perform all actions available to an unregistered user.
- As a registered user, I should be able to log in and manage my account details.
- As a registered user, I want to add postcards to a shopping cart.
- As a registered user, I need to be able to check out and pay for my selections securely.
- As a registered user, I want to view my past orders and their statuses.
- As a registered user, I wish to leave reviews and rate the postcards I've purchased.

**Site Admin/Superuser:**

- As an admin, I can perform all functionalities available to unregistered and registered users.
- As an admin, I need to manage the product listings, including adding, editing, and removing postcards.
- As an admin, I want to view, approve, and manage user reviews to maintain content quality.
- As an admin, I should be able to track and manage orders, handling any customer service issues that arise.
- As an admin, I need the capability to update site content, such as special offers or new arrivals, to keep the site current.

<hr>

### **Agile Methodology**

For planning the development and implementation of the Marisol website, a project kanban board was used as an Agile Tool through Github. This project board utilised issues as 'User Stories', a link can be found [here](https://github.com/users/Julia-cloudname/projects/8).

To help define the functionalities and prioritise key features, these 'User Stories' were broken down into 4 categories of importance; 'Must Have', 'Should Have',  'Could Have' and 'Won't have'.

'Must Have' represents a feature or functionality that is essential to the site, 'Should Have' is a defined requirement needed for the site, 'Could Have' is determined to be optional and 'Won't have' - future functionality that I'm going to do later.

<hr>

### **The Scope**

#### **The Site's Main Goals:**

- **Positive User Experience:** The primary goal of the Garvin Card Shop website is to ensure a delightful and smooth experience for users. From browsing the unique collection of postcards to completing a purchase, the site is designed to facilitate an easy and enjoyable user journey.

- **Clear Purpose and Offerings:** The website clearly showcases its extensive range of creative postcards for various occasions. Users can swiftly grasp the shop's offerings, browse through different categories, and find the perfect postcard for their needs.

- **Efficient and Secure Shopping Process:** Garvin Card Shop prioritizes a hassle-free shopping experience. Registered users can easily add items to their cart, proceed to a secure checkout, and track their orders, ensuring a reliable and trustworthy process.

- **Engagement and Community Interaction:** The site allows users to read and post reviews, offering a platform for community interaction. This feature not only enhances customer engagement but also provides valuable feedback for continuous improvement.

- **Regular Updates and New Arrivals:** Keeping the content fresh and updated, the site frequently introduces new postcard designs and special offers. This approach keeps the inventory dynamic and encourages repeat visits from customers.

<hr>

## DESIGN

### Styling and Aesthetics
The Garvin Card Shop website is designed with a focus on user experience and visual appeal. Utilizing modern CSS practices, the site offers a clean, intuitive interface.

### Color Scheme
The color palette is dominated by shades of gray (#555 for main text and buttons, #333 for hover effects), creating a professional and elegant look. White text on darker backgrounds ensures high readability and a contemporary feel.

### Typography
"Lato" font is used throughout the site, providing a modern and clean appearance. The font style and sizes are carefully chosen to ensure readability and visual harmony.

### Wireframes

Wireframes for pages are linked here:

![Main page](/media/wareframe.png)

## **FEATURES**

### **Navigation**

#### **Desktop Navigation**
- The Garvin Card Shop website offers a clear and user-friendly navigation menu, including links to 'Home', 'Products', 'Special Offers', 'Contact Us', and 'About Us'.
- For registered users, the menu includes additional options like 'Profile' for account management and a 'Log Out' option.
- Unregistered users see a 'Register' option to encourage account creation and access to more features.

![Navigation](/media/all-cards.png)

#### **Mobile Navigation**
- The mobile version features a responsive burger menu for easier navigation on smaller screens.
- Tapping the burger icon reveals the same essential links as on the desktop version, maintaining a consistent user experience across devices.

### **Footer**
- The footer includes social media links and additional information about Garvin Card Shop.
- Users can connect with the shop on platforms like Facebook, Instagram, and Twitter.

![Footer](/media/footer.png)

### **Home Page**
- Features a banner promoting the latest card collections and special offers.
- A 'Featured Products' section showcases select items, encouraging users to explore more.

### **Products Page**
- Displays a variety of cards for different occasions. Each product has a thumbnail image and a brief description.
- Users can click on a product to view more details and purchase options.

![Products](/media/all-products.png)

### **Special Offers Page**
- Highlights current promotions and discounts.
- This section is updated regularly to showcase the latest deals.

### **Contact Us Page**
- Provides a contact form for user inquiries.
- Includes essential contact information like email and phone number.

### **About Us**
- Details about Garvin Card Shop.
- Provides background information about the shop and its unique selling points.

### **Profile Page (For Registered Users)**
- Displays user information and order history.
- Allows users to manage their account details.

### **Wishlist Page**
- Registered users can add products to their wishlist for future reference.

### **Administrative Panel (For Admin Users)**
- Admins can manage product listings, user accounts, and view sales data.
- The panel allows for adding, editing, and removing products.

### **Signup Page**
- New users can sign up easily through a user-friendly registration form.

### **Login/Logout Functionality**
- Allows users to securely access their accounts and manage their shopping activities.

### **Reviews**
- Allows users to share their expirience 

![Reviews](/media/reviews.png)
<hr>

## **Testing**

[TESTING DETAILS](TESTING.md)

<hr>

## **TECHNOLOGIES USED**

### Languages and Libraries used:

- HTML
- CSS3
- Javascript
- Python
- Django


### Libraries and Programs Used

- [Gitpod](https://www.gitpod.io/)<br>
   Used for version control alongside GitHub.
- [GitHub](https://github.com/)<br>
   Used to store the project and utilise git version control.
- [Heroku](https://id.heroku.com)<br>
   Used to deploy project.
- [AWS](https://aws.amazon.com/)<br>
   Cloud based storage, used for storing any media submitted by users.
- [ElephantSQL](https://www.elephantsql.com/)<br>
   Used to host the PostgreSQL database.
- [SQLite3](https://www.sqlite.org/index.html)<br>
   Used to host the SQLite3 database.
- [W3C - HTML](https://validator.w3.org/)<br>
   Used to validate all HTML code.
- [W3C - CSS](https://jigsaw.w3.org/css-validator/)<br>
   Used to validate all CSS code.
- [CI PEP8 Testing](https://pep8ci.herokuapp.com/)<br>
   Used to validate all Python code.
- [Google Fonts](https://fonts.google.com/)<br>
   Used to provide the font styling.
- [Bootstrap](https://getbootstrap.com/)<br>
   Used to for helping with the HTML design and layout.
- [Fontawesome](https://fontawesome.com/)<br>
   Used to implement effective icons.
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)<br>
   Used during the development to debug and test responsiveness.
- [marvelapp](https://marvelapp.com)<br>
   Used for creation wireframes.
  
<hr>



## **DEPLOYMENT**

### ** Create Github Repository **
- Log in to your Github account.
- Navigate to repositories and select 'New'.
- Select the 'Code Institute' template from the 'Repository Template' menu.
- Give your repository a name and select 'Create Repository'.
- When the repository has been created select 'Gitpod' to open a new workspace.

### ** Heroku **
- Log in to your Heroku account [Heroku](https://id.heroku.com).
- From the home page select 'New', then select 'Create New App' from the drop-down.
- Provide a name for your app and selectyour regrion.
- Add 3 new keys along with your relevant value information: 'SECRET_KEY', 'DATABASE_URL' and 'ClOUDINARY_URL'. 
- At the top of the page select the 'Deploy' tab.
- For the preferred deployment method select 'Github'.
- Search for your repository name and connect.
- Additionally, automatic deploys can be enabled for deployment after each push to Github.

### ** Fork this project **
- Sign in to Github and go to my [repository](https://github.com/Julia-cloudname/garvin-shop-v1)
- At the top of the page select 'Fork'.
- The Fork will now be added to your repositories.

### ** Clone this project **
- Sign in to Github and go to my [repository](https://github.com/Julia-cloudname/garvin-shop-v1)
- Select the green 'Code' button.
- Select from one of the cloning options HTTPS, SSH or Github CLI. Click the clipboard icon to copy the URL.
- Open git bash
- Enter ‘git clone’ into the text box and then paste the respository URL and select enter. 

For more information on cloning please read the github documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## **CREDITS**

The images of products sourced from http://garvin.pp.ua. 