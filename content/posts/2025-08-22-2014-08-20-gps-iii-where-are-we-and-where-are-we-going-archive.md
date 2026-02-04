---
categories:
- Technology
- Archive
cover:
  image: img/2014/GPS-IIRM.jpg
date: 2025-08-22 03:16:00-04:00
tags:
- GPS
- Navigation
title: 'GPS III: Where Are We? And Where Are We Going? [Archive]'
---

> **Archival Note**: This post preserves an article I originally wrote for MakeUseOf way back in August 2014 while I was at The University of Liverpool doing my PhD. The original published version is at [MakeUseOf: GPS III: Where Are We? And Where Are We Going?](https://www.makeuseof.com/tag/gps-iii-going/). They probably still own everything but this is from my original 'manuscript'.
---

![GPS Satellite](/img/2014/GPS-IIRM.jpg)

Fifteen years ago, the [first GPS-enabled cellphone](http://en.wikipedia.org/wiki/Twig_Com) went on the market. It flopped, but the form factor it pioneered, combining near-military grade communications equipment with a consumer device has stayed with us.

You can't turn a corner without your phone or your [watch](http://www.businessinsider.com/timex-ironman-gps-one-2014-8) or your [shoes](http://www.popularmechanics.com/technology/gadgets/tech-news/these-smart-shoes-vibrate-to-give-turn-by-turn-directions-17033713) telling you where to go because they know exactly where you are. But this wasn't always the case.

## A Brief History Of The GPS

We take GPS for granted as a 'commodity', a grand gift from Reagan-Era Star Wars Cold War [MADness](http://en.wikipedia.org/wiki/Mutual_assured_destruction) that occasionally teaches high schoolers about relativity. The depressing fact is that GPS (or GNSS as it was classified at the time) was only made available to the public after an eerily familiar airline disaster.

In 1983 – just five years after the [first NAVSTAR satellite was launched](http://nssdc.gsfc.nasa.gov/nmc/spacecraftDisplay.do?id=1978-020A) – Korea Air Lines Flight 007 was shot down after crossing into Soviet airspace due to pilot navigation error. The global response to the loss of the 269 souls aboard was anguished but tinged with Cold War Politics, and [President Ronald Reagan](http://www.rand.org/pubs/monograph_reports/MR614/MR614.appb.pdf) announced that GPS would be made available to the world for free to prevent such a tragedy.

The Global Positioning System was originally designed out of a military need to coordinate troop and craft movement in unknown areas (such as the Persian Gulf, where GPS was first used in theatre in [Operation Desert Storm](http://en.wikipedia.org/wiki/Gulf_War)), as well as the Nuclear Detonation Detection System (NUDET).

![Operation Desert Storm Map](/img/2014/operation_desert_storm_map.jpg)

## The 'Selective' Positioning Years

Due to it's use of multiple satellites with extremely accurate clocks, GPS had a positioning accuracy of around 10m right from the start. However, the Department of Defence introduced intentional positioning errors into the Civilian bands citing fears that the technology would be used against them. This, as often happens, backfired almost instantly.

Even during the first operational use of GPS in Desert Storm, the limited number of expensive, energy hungry, heavy GPS receiver units drove many members of the armed forced to snap up 'cheap', light, and almost ubiquitous civilian receivers which were effectively useless in the field due to these intentional errors. This was such a recognised issue that the error-insertion system (called Selective Availability or just SA) was turned off world-wide for the remainder of the Gulf War ('90-'91).

Throughout the 90's, military, corporate and civilian bodies pushed for SA to be removed, with people ranging from trucking-firms to the FAA arguing that the spurious noise in the signal was limiting the usefulness and adaptation of GPS in their respective areas. These errors were [turned off 'permanently' in 2000](http://www.aviationtoday.com/av/issue/feature/The-Real-Reason-Selective-Availability-Was-Turned-Off_12739.html#.U_HYkXVdX0o) by President Bill Clinton.

![Clinton vs Reagan GPS Policy](/img/2014/clintonvsreagan.jpg)

However, a new generation of satellites are being launched, that promise a great increase to not just the accuracy, but also the availability of GPS. Designated as GPS Block III, or just GPS III, this suite of 30 new satellites will replace the ageing Block II's, and the already defunct Block I's. Of 64 Block I/II birds launched, 33 remain operational, the oldest being Navstar IIA-01, at a grand old 23 years of age.

The reasons why these satellites are a massive improvement is more complicated than "it's faster to lock on and more accurate". Here's why.

## How GPS Works

GPS works as a purely broadcast system; it doesn't require any data connection to tell your position (although most apps will need a data connection for the mapping-side). Your phone or SatNav is not talking to the satellite 12,500 miles away, it just listens on a particular frequency for particular codes.

Your phone listens to a particular channel, or 'band' with each satellite broadcasting it's own personal time code based on it's own atomic clock floating up in orbit. However, since each satellite is a different distance away from you, when you receive these 'ticks', they'll be slightly out of sync. Your GPS device then tries to synchronize each stream to an internal clock, so it can work out how far each satellite is from your location.

So, you're X,Y,and Z miles away from three satellites. These are at least 12,500 miles above your head, and are travelling at 14,000 miles an hour, and you've got no idea where they are or where they're going. This isn't massively helpful until we add the time code that each satellite broadcasts, which contains much more information than just the time.

### I know where I am but where are you?

In order to work out where we are based on the satellites 'ticks', we need an extra bit of information that's already transmitted in the time code, what's called an 'Almanac'. This contains information about each satellites' current orbit characteristics. So your phone builds a little model-planetarium based on time that's accurate down to a few nanoseconds. It works out where the satellites are in space, and where you are relative to the satellites. Boom. The nearest Starbucks is 12.6 metres away.

![GPS Trilateration](/img/2014/Trilateration2d.jpg)

Now it gets interesting; that's just one 'band' or channel. There were originally three channels; two (L1/L2) were used for Acquisition and Positioning respectively. These were used in consumer applications, but if you had a particular encryption code (commonly called the Gold code), you got higher accuracy, military only signals.

Finally, the L3 band is reserved for [Nuclear Detonation Detections](http://fas.org/spp/military/program/nssrm/initiatives/usnds.htm), which monitors the globe for high energy infra-red events and is mostly used to enforce nuclear test-ban treaties. But the new versions of the GPS standard come with exciting new features.

## What's New In GPS III?

In the later Block II and new Block III systems, the number of bands available is [increased to 5](http://www.gps.gov/systems/gps/modernization/civilsignals/). L4 is left as a research band, whilst L5 includes the Safety-Of-Life (SoL Data and Pilot signals), which is an extremely dependable version of GPS for aviation, maritime, and 'search and rescue' users.

In the new systems, the method of overlaying data in the same signal using a Gold code (CDMA) is also used to produce extra signals for civilian and military-only channels (L2C and M-Code respectively) which do two very cool things separately.

The L2C code is both 250 times as 'detectable' (which is not the same as 'stronger') and operates on a different band from the one normally used by civilian GPS. Since we'll now have access to two bands, we can compare them in real time to compensate for atmospheric interference, meaning consumers will finally be able to get reliable indoor positioning (within reason).

The [M-Code](http://www.spirent.com/Blogs/Positioning/2011/May/2011-05-02_GPS_Modernization_What_is_M-Code) is the big ticket item justifying the new changes to how GPS works. The two big advances in this regard are directionality and anti-jamming. Rather than the normal system of 'whole earth broadcast', the new Block III satellites will have both Whole Earth and Directional M-Code antennae, providing troops 100x stronger reception within the cone of the beam, which will be (just) several hundred kilometres across.

Related to this power-pump, M-Code signals will also include a series of error correction, anti-jamming, anti-spoofing and data broadcasting techniques to combat local GPS denial systems and ensure that troops always have the best available position data, regardless of weather, location, or enemy.

On top of this, there's the usual upgrades that come when you're buying a new piece of kit; faster Rubidium clocks give more accurate timing and better receiver positioning. Meanwhile, better solar panels will provide more power to stronger antennae, which means more power at the receiving end.

Then you've got the usual additions when governments get involved in things; NASA has asked to stick on a few [laser retro-reflectors](http://ntrs.nasa.gov/search.jsp?R=20120015576) (mirrors) to provide better ground tracking of orbits, and the Air Force is lobbying to add extra Search and Rescue (SAR) capability on top of the existing SoL data channels. This is part of a [global standard for SAR systems](http://www.cospas-sarsat.int/en/) involving 37 countries, and will not only provide instant emergency signal detection and location, but also the ability to send short messages back to the receiver.

## Is It Up In The Air?

A lot of these advances rely not only on updated satellites but also on updated Ground Stations, previously called "Operational Control Segments"(OCS). These ground stations are places across the world and coordinate orbital paths, coverage density, and search and rescue / nuclear detection capabilities for the GPS network, as well as periodically correcting for that [pesky special relativity](https://www.youtube.com/watch?v=ky4RgRvVDoA) time dilation. The new versions of these ground stations (OCX) enable most of these advances as well as enabling the interoperability between US and European GNSS systems (P.S. this is why GPS sucks if you're in Europe compared to the US; we've got less birds over our heads).

Unfortunately it's exactly these awesome new systems that are holding back the release of GPS III. Defense contractor Lockheed Martin has been contracted to build the first of the satellites, but have been delayed by new L2C management and navigation computers from Exelis; whilst Raytheon has been [contracted to build the OCXs](http://gpsworld.com/rayth), which have experienced significant budget overruns.

## Summary and Speculation

The benefits of the new Block III system, including some of the bits on currently launched Block II can be summed up as:

- Decreased Acquisition Time
- Increased Indoor Reception
- Increased Accuracy and Motion sensitivity
- Wider coverage area
- Increased accuracy for military deployment scenarios using a focused beam
- Increased Anti-Jamming capabilities (it's not clear if this applies to both Civilian and Military signals, but I'm optimistic)
- Increased interoperability with Europe's' GALILEO positioning system
- Decreased Search-And-Rescue response time and better global coverage with some messaging capability, which could have prevented the loss of MH370

With delays in both the satellite systems and the ground control segments, it's unlikely we're going to see the full end-user advantages of these systems until late 2015 / mid 2016. However, once they do go up, they have a proposed life of 15 years, So where do we go after that?

The US is no longer the only player in Global Navigation. Russia has had GLONASS since the mid 90's and in the past 5 years both China's BeiDou and Europe's GALILEO systems have come online. Last but not least, the Indian Regional Navigation Satellite System (IRNASS) is scheduled to go live within the next few years.

These all have different regional focuses, so the big question becomes, who will collaborate first? Will it be receiver-makers or global governments? Or will we go back to the days of global travellers having to have a cellphone for each continent?

With the new extensions to GPS, the US has demonstrated a willingness to work with the European system, as has Russia by providing Safety-of-life interoperability with both GPS and GALILEO. The skies are getting busy, and at this rate there are going to be at least 120 satellites in the sky providing positioning to 'somebody'. If all goes well, us poor consumers might even be able to use most of them, getting us down to a accuracy of a few inches, even indoors. That means satisfying the FAA's requirements for precision approach autopilots for aircraft (hint, and drones), as well as enabling much more accurate lane-detection for self-driving cars.

Add this to advances in wearables and IoT devices (however scary that could be), and we're looking at a future of small devices that know where they are and can talk to each other. Smart-Wallets, Intelligent Doorbells that only 'chime' if someone is in the house, keyrings, bags, all these things that can talk to your cellphone and say where they are with an accuracy of a few inches (Then I might finally find out where I left my keys…).

This is just some of my thoughts on where this technology will take us, but what's your story? What could you do with position-aware devices? Should we be afraid?
