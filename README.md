# ECOMMERCE WEBSITE - FASHION SHOP FOR MAN APPARRELS

## Ojective

To build a ECOMMERCE platform for resellers to post their product for sale and for shoppers to do online purchase via the platform. It allows resellers to post, update and remove any listing and keeps a log of the trasaction and will allow both users and resellers to view the purchase history.

_(This current project will be a prototype for the full website as there are many features not fully implemented due to time limitation)_


## Strategy 

Group | Goals | Interface 
--- | --- | --- 
**Online Shoppers** | `Online shoppers who will make purchase online generating revenue` | Online shop for them to search/select/buy online
- | `variety of products` | Increase the range of products, i.e resellers
**Resellers** | `Advertisers or brands who will pay to advertise on platform`| CRUD portal for them to upload/update/remove their product listing
- | `direct sale without handling the transaction` | Allow user to make purchase and payment online, ease of management for resellers
**Owner** | `Generate browsing traffic and profit` | UIUX to make website user-friendly for browsers / resellers

## UX 

#### Key features
- allow resellers to upload/update/remove a product 
- allow resellers to track the trasaction history for their products (non-editable log)
- allow resellers to sum up their profit for the month (future development)
- add Management / staff level so as to allow different assess rights (future development)
- 3-click for a shopper to get to category of items they looking for
- search bar for shopper to find their product (future development)
- light-weight to minimize loading time
- do not allow cart to add if stock level is not sufficient

## Demo

The link for the project is as follow : 
https://donovan-project4.herokuapp.com/

### Technologies Used
1. HTML, CSS & Javascript 
2. Bootstrap 
3. Python 
4. SQLite 
5. Postgres
6. Heroku 
8. Crispy Forms 
9. Cloudinary 
10. Stripe 
11. Whitenoise 
12. Gunicorn 
13. Gitpod online IDE
14. Fontawesome

### Features
		
**Current Design :**
* User able to find the product by clicking on the Category link
* User can add product to the cart by hovering over the product image and click add to cart
* User can increase/reduce/remove the product from cart
* User can make payment online via visa/master card
* Admin console only accessable by SuperUser (assign to resellers) 
, they will have the rights to upload/update/remove the product
* transaction log is only accessable by SuperUser and they can only view their own product transaction.
    
_Current Limitations:_
* Feature / Blog / Social Media / Footer links are not available
* Search bar is currently not build
* summary for individual resellers to consolidate their monthly statement (not available)
* allow resellers to create their staff profile, etc (not available)

## Testing
Manual testing is done for the pages

*No* | *Steps* | *Expected Results* | *Observations*
--- | --- | --- | --- 
1 | Navbar : Click 'Shop' | `View shop listing for all products` | *Pass*
1a | Shop page: Hover over product image  | `show detail of product name and pricing` |  *Pass*
1b | Shop page: Hover over product image AND click 'Add to Cart'  | `Add 1 quantity to the cart for the product` |  *Pass*
2 | Navbar : Click 'Manage' | `View admin panel listing for all products (accessible by SuperUser only)` | *Pass*
2a | Manage page: Click 'Add product' (located top right of table)|`Render form for User to enter new product detail and submit entry`|*Pass*
2b | Manage page: Click 'edit' (located right-end of product row)|`Render form for User to change product detail and submit entry`|*Pass*
2c | Manage page: Click 'remove' (located top right of table)|`Render page for User to confirm removal`|*Pass*
3 | Navbar : Click 'Payment Log' | `View transaction log` | *Pass*
4 | Navbar : Click 'Cart Logo' | `View cart summary of all products selected` |*Pass*
4a | Cart page: Click '+' (located right of quantity in each product row)|`+ 1 to the product's quantity`|*Pass*
4b | Cart page: Click '+' (located right of quantity in each product row) & stock qty is 0 |`notify user the current stock is only with the current number in cart`|*Pass*
4b | Cart page: Click '-' (located right of quantity in each product row)|`- 1 to the product's quantity`|*Pass*
4b | Cart page: Click '-' (located right of quantity in each product row) & product qty is 1 only |`remove product from cart`|*Pass*
4c | Cart page: Click 'x' (located end of each product row)|`remove product immediately from cart`|*Pass*
4d | Cart page: Click 'Checkout' button (located bottom-right of table)|`render checkout page`|*Pass*
5 | Checkout page: Click 'Checkout' (located bottom-right of table)|`render credit card payment form for user to enter, upon successful transaction; (i) clear the cart (ii) adjust the stock qty accordingly (iii) create log in payment log`|*Pass*

### Deployment

All codes are uploaded to GitHub and links are made to Heroku by installing in bash terminal in projects.
Regular commits are push to the Github subsequently push to heroku to deploy.
.gitignore file is added to remove files that are not required or files that we do not wish to be uploaded to Github

To deploy on Heroku:
* To list all the requirements in requirements.txt, run the following command in terminal:
* pip3 freeze --local > requirements.txt
* Procfile need to be created to run gunicorn upon deployment
* Git push to Heroku Master after all the documents are properly set up
* All public keys and private keys for the following need to be added to in Heroku Config Vars settings for Cloudinary, Stripe


### Media
Pictures are randomly search online and used for project purpose and not for commercial use.

### Credits
Uses W3School for many reference (https://www.w3schools.com/)
Uses Fontawesome for the various icons (https://fontawesome.com/)
Uses Bootstrap for templates (https://getbootstrap.com/)
Many reference when facing issues, got the solutions from (https://stackoverflow.com/)

