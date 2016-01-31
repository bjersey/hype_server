def calc_venue_hype_score(venue, all_venue_fb_stat_by_venue_id, all_venue_twitter_stat_by_venue_id):
    fb_stat = all_venue_fb_stat_by_venue_id[venue.id]
    twitter_stat = all_venue_twitter_stat_by_venue_id[venue.id]

    fb_score = ((fb_stat.likes * 0.56) + (fb_stat.checkins * 0.44)) * 0.85
    twitter_score = twitter_stat.followers_count * 0.15

    score = fb_score + twitter_score

    return score
