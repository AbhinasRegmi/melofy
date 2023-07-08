# melofy

## architecture design - https://medium.com/geekculture/spotify-system-architecture-6bb418db6084
![Diagram1](https://iq.opengenus.org/content/images/2022/02/system_microservices.jpg)
![Diagram2](https://iq.opengenus.org/content/images/2022/02/spotify_design.jpg)


# control flow
login_with_google -> google_callback -> get_access_tokens -> get_user_email_profile
-> check_user_in_db -> if_not_update_db and send_welcome_mail -> then_provide_access_token
-> create login_required, get_current_user and other auth dependencies
