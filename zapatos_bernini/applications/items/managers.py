from django.db import models

class ItemInShoppingCartManager(models.Manager):
    """ We recover the items in the cart by the user """
    
    def get_items_list(self, user):
        return self.filter(
            user=user
        )