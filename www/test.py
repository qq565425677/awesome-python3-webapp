import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    await orm.create_pool(loop,user='www-data', password='www-data', db='awesome')

    #u = User(id=12138, name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    #await u.save()
    #u = User(id=1, name='Sun', email='565425677@qq.com', passwd='7758521', image='about:blank')
    #await u.save()
    #
    #user=await User.find('12138')
    #print(user)
    
    #user=await User.find('12138')
    #await user.remove()
    #print('--------------------------')
    #user=await User.find('12138')
    #print(user)
    
if __name__=='__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    print('Test finished.')
    #loop.close()貌似自动关闭了，重复关闭会报错。