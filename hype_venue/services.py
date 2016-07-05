from django.db.models import Count

from hype_venue.models import ScoreParameters, VenueRegion, Venue


def calc_venue_hype_score(venue, all_venue_fb_stat_by_venue_id, all_venue_twitter_stat_by_venue_id):

    params = ScoreParameters.objects.get(name='FIT_score')

    fb_stat = all_venue_fb_stat_by_venue_id.get(venue.id)
    twitter_stat = all_venue_twitter_stat_by_venue_id.get(venue.id)

    if fb_stat:
        fb_score = ((fb_stat.likes * float(params.data['fb_likes_weight'])) +
                    (fb_stat.checkins * float(params.data['fb_checkins_weight']))) * float(params.data['fb_overall_weight'])
    else:
        fb_score = 0

    if twitter_stat:
        twitter_score = (twitter_stat.followers_count * float(params.data['twitter_followers_weight'])) * \
                        float(params.data['twitter_overall_weight'])
    else:
        twitter_score = 0

    score = fb_score + twitter_score

    return score


def get_venue_regions():
    all_venue_regions = VenueRegion.objects.annotate(num_venues=Count('venue')).order_by('-num_venues')

    return all_venue_regions[:6]


def get_venues():
    venue_regions = get_venue_regions()

    all_venues = Venue.objects.filter(venue_region__in=venue_regions)

    return all_venues
