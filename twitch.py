import asyncio
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator, AuthScope
from twitchAPI.eventsub.websocket import EventSubWebsocket
from twitchAPI.object.eventsub import (
    ChannelPointsCustomRewardRedemptionAddEvent,
    ChannelSubscribeEvent,
    ChannelSubscriptionGiftEvent,
)

CLIENT_ID = 'qemqptjdkahr3rteivz4kf1ktkwt1i'
CLIENT_SECRET = 'ofaw1dcz62aogk0iuij179phuphgkv'
STREAMER_LOGIN = 'tylerthemongus'

FILE_PATH = 'signal.txt' 

# ----- Event Handlers -----

async def on_redeem(event: ChannelPointsCustomRewardRedemptionAddEvent):
    print(f"Channel point redeemed: {event.reward.title} by {event.user_name}")
    if event.reward.title.lower() == "expand border":
        with open(FILE_PATH, 'w') as f:
            f.write('channel_point_redeem\n')

async def on_subscribe(event: ChannelSubscribeEvent):
    print(f"New sub! {event.user_name} just subscribed (tier {event.tier})")
    with open(FILE_PATH, 'w') as f:
        f.write('subscription\n')

async def on_gift_sub(event: ChannelSubscriptionGiftEvent):
    print(f"{event.user_name} gifted a sub! Total gifts this event: {event.total}")
    with open(FILE_PATH, 'w') as f:
        f.write('gift_sub\n')

# ----- Main Async Routine -----

async def main():
    twitch = await Twitch(CLIENT_ID, CLIENT_SECRET)

    auth = UserAuthenticator(
        twitch,
        [
            AuthScope.CHANNEL_READ_REDEMPTIONS,
            AuthScope.CHANNEL_READ_SUBSCRIPTIONS,
        ]
    )
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(
        token,
        [
            AuthScope.CHANNEL_READ_REDEMPTIONS,
            AuthScope.CHANNEL_READ_SUBSCRIPTIONS,
        ],
        refresh_token
    )

    user = [user async for user in twitch.get_users(logins=[STREAMER_LOGIN])][0]
    broadcaster_id = user.id
    print(f"Broadcaster ID: {broadcaster_id}")

    # Setup EventSub WebSocket
    eventsub = EventSubWebsocket(twitch)
    eventsub.start()  # Must come BEFORE adding listeners!

    # Add Event Listeners
    await eventsub.listen_channel_points_custom_reward_redemption_add(broadcaster_id, on_redeem)
    await eventsub.listen_channel_subscribe(broadcaster_id, on_subscribe)
    await eventsub.listen_channel_subscription_gift(broadcaster_id, on_gift_sub)

    # Keep alive
    await asyncio.Event().wait()

# Run
if __name__ == '__main__':
    asyncio.run(main())
