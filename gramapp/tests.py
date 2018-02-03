
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Image, Comment

# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    Test case for the Profile class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''
        # Create instance of Profile class
        self.new_profile = Profile(bio="I am Groot")

    def test_instance(self):
        '''
        Test case to check if self.new_profile in an instance of Profile class
        '''
        self.assertTrue( isinstance(self.new_profile, Profile) )

    def test_get_profiles(self):
        '''
        Test case to check if all profiles are gotten from the database
        '''
        gotten_profiles = Profile.get_profiles()
        profiles = Profile.objects.all()
        self.assertTrue( len(gotten_profiles) == len(profiles))

    def test_get_other_profiles(self):
        '''
        Test case to check if all profiles are gotten from the database
        '''
        self.james = User(username="kiki")
        self.james.save()

        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_profile = Profile(user=self.jane,bio="Another Profile")
        gotten_profiles = Profile.get_other_profiles(self.james.id)
        profiles = Profile.objects.all()

class ImageTestClass(TestCase):
    '''
    Test case for the Image class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''
        # Create a Image instance
        self.new_Image = Image(caption ='Python James is Muriuki who wrote Python content for Moringa School')

    def test_instance(self):
        '''
        Test case to check if self.new_Image in an instance of Image class
        '''
        self.assertTrue( isinstance(self.new_Image, Image) )

    def test_get_Images(self):
        '''
        Test case to check if all Images are gotten from the database
        '''
        gotten_images = Image.get_Images()

        images = Image.objects.all()

        self.assertTrue( len(gotten_Images) == len(images))

    def test_get_profile_Images(self):
        '''
        Test case to check if all Images for a specific profile are gotten from the database
        '''
        self.james = User(username="kiki")
        self.james.save()

        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_profile = Profile(user=self.jane,bio="Another Profile")

        self.test_image = Image(user=self.jane,caption="Another Profile")

        gotten_profile = Image.get_profile_images(self.jane.id)

        profiles = Image.objects.all()

        self.assertTrue( len(gotten_profile) == len(profiles))

class FollowTestClass(TestCase):
    '''
    Test case for the Follow class
    '''
    def test_instance(self):
        '''
        Test case to check if self.new_Image in an instance of Follow class
        '''
        self.james = User(username="kiki")
        self.james.save()

        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_profile = Profile(user=self.jane,bio="Another Profile")

        self.new_follow = Follow(user=self.jane, profile=self.test_profile)

        self.assertTrue( isinstance(self.new_follow, Follow) )

    def test_get_following(self):
        '''
        Test case to check if get following is getting profiles a specific user is following
        '''
        self.james = User(username="kiki")
        self.james.save()

        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_profile = Profile(user=self.jane,bio="Another Profile")

        self.test_Image = Image(user=self.jane,caption="Another Profile")

        self.new_follow = Follow(user=self.jane, profile=self.test_profile)

        gotten_following = Follow.get_following(self.jane.id)

        followings = Follow.objects.all()

        self.assertTrue( len(gotten_following) == len(followings))

class CommentTestClass(TestCase):
    '''
    Test case for the Comment class
    '''
    def setUp(self):
        '''
        Method that creates an instance of Comment class
        '''
        # Create a Comment instance
        self.new_comment = Comment(comment_content ='Python James is Muriuki who wrote Python content for Moringa School')

    def test_instance(self):
        '''
        Test case to check if self.new_comment in an instance of Comment class
        '''
        self.assertTrue( isinstance(self.new_comment, Comment) )

    def test_get_Image_comments(self):
        '''
        Test case to check if get Image comments is getting comments for a specific Image
        '''
        self.james = User(username="kiki")
        self.james.save()

        self.jane = User(username="ja-ne")
        self.jane.save()

        self.test_profile = Profile(user=self.jane,bio="Another Profile")

        self.test_Image = Image(user=self.jane,caption="Another Profile")

        self.test_comment = Comment(Image=self.test_Image,comment_content="Wow")

        gotten_comments = Comment.get_Image_comments(self.test_Image.id)

        comments = Comment.objects.all()

        # No comments were saved so expect True
        self.assertTrue( len(gotten_comments) == len(comments))

class LikeTestClass(TestCase):
    '''
    Test class to test the Like class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        # Create a Like instance
        self.new_like = Like(likes_number=0 )

    def test_instance(self):
        '''
        Test case to check if self.new_like is an instance of Like
        '''

        self.assertTrue( isinstance( self.new_like, Like) )

    def test_get_Image_likes(self):
        '''
        Test case to check if get Image likes is getting the likes for a specific Image
        '''

        gotten_likes = Like.get_Image_likes(4990826417581240726341234)

        self.assertFalse( len(gotten_likes) , 1)

    def test_num_likes(self):
        '''
        Test to check if num likes is getting the number of likes a Image is getting
        '''
        gotten_likes = Like.num_likes(123412312351123412341234123412341234)

        self.assertEqual( gotten_likes , 0)
