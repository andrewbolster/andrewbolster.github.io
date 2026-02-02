---
date: 2021-11-10T18:00:00+00:00
layout: post
tags:
- 'Web Development'
title: UUIDs and You
---

> The guts of this document was originally created as part of my work at NTT Application Security stripped of its specificity and retained for my own reference.

## Background

Entities need to be identifiable, but the existence of entities should not be predictible, and it should not be easy for an external user/attacker to infer anything about the number of or presence of entities.

Conventional auto-increment integer ID’s were historically de-rigeur for (now largely spurious) database performance optimisation reasons, however, they are succeptible to both presence estimation, and scale estimation.

If a potential customer creates an entity with the integer id `180`, we can infer that globally, there are `179` existant entities of that type, and that then next one will probably be `181`.

Also, if implemented as a distributed/ scalable system, then contention for global ID generation becomes a limiting factor (and a challenge to any stateless expectations on such a system).

### What about using nested structures like `/customer/10/entity/1`

This is an option, however it couples the customer state to the individual state of a given entity, which introduces unnecessary dependency. Also, establishing the ‘schema’ for addressing arbitrary objects in this way becomes challenging, for instance; if a `customer` object has several `reading_list` mappings with multiple `book` objects within with potential (realised or not) many to many mappings, there are many ways to reference an particular book.

* `/book/123`
* `/customer/10/book/123`
* `/customer/10/reading_list/5/book/123`

### UUIDS!

Universally Unique Identifiers ([UUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier)) are 128bit cryptographically generated values, intended for the generation of globally unique identifiers without dependency on a central authority or coordination between services generating them.

There are a range of UUID generation types, summarised below (v1-5 based on [RFC4122](https://www.rfc-editor.org/rfc/inline-errata/rfc4122.html)

| Version | Description                                  | Usecase                                            |
| ---
---
- | ---
---
---
---
---
---
---
---
---
---
---
---
---
---
-- | ---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
-- |
| 1       | Date Time (100ns) + MAC address              | Basically guaranteed uniqueness between nodes      |
| 2       | Date Time (7min) + MAC + Namespace/Domain ID | Security (but pretty useless)                      |
| 3/5     | Namespace + Name + Hash (MD5/SHA1)           | Actively designed to enable “same uuid generation” |
| 4       | Random                                       | Identity Generation                                |
| *6,7,8  | v1 with Time Ordering                        | Guarantees Uniqueness, Ordering and Proximity      |

*[IETF Proposal](https://www.ietf.org/archive/id/draft-peabody-dispatch-new-uuid-format-01.html)

### Sidebar on Collisions

They’re just stupidly unlikely, stop worrying about them:
> Thus, the probability to find a duplicate within 103 trillion version-4 UUIDs is one in a billion.

Within most reasonable data models, it would be sufficient (or, overkill to the point of paranoia) to check for the existence of an entity as part of it’s initial creation, and to just ‘reroll’ in the rare case this emerges, although this in and of itself would mitigate a significant amount of the advantage of UUID in distributed/delay tolerant systems.

However, for timeseries variants (1/2/6,7,8), once you leave their ‘tick’, no future-collision is possible, and so as long as your generating nodes have unique MAC addresses, all will be well.

### Sidebar on Storage

Naively, UUID’s look huge with 36bit chars, vs our teeny integer or even uint or int32 fields we could use in other ID schemes, but compared to the size of the objects these keys will be referencing, this is a miniscule consideration. Even then, we can also change the representation of these 128 bits in any number of ways, mapping them directly to bin16 blobs, or encoding them as base64 values.

What’s more relevant is the impact of the use of UUID’s in back end storage considerations. Much hay has been made about these critiques over the years, here’s a couple of highlights.

* [UUIDs are Popular, but Bad for Performance — Let’s Discuss](https://www.percona.com/blog/2019/11/22/uuids-are-popular-but-bad-for-performance-lets-discuss/)
  * Highlights different compromises to storage, in terms of impact on InnoDB insertion rates (Char is worst, bin16 is best), and on the ordering of ID’s for query lookup performance (injecting ‘order’ into random id generation makes proximal lookups more efficient (Note, this is basically what UUIDv6 does))
*  [int4 vs int8 vs uuid vs numeric performance on bigger joins](https://www.cybertec-postgresql.com/en/int4-vs-int8-vs-uuid-vs-numeric-performance-on-bigger-joins/)
   * UUID introduces a 13% increase in join spec and significant increase to Index scaling. (note; `numeric` type was even worse in the join case with a 34% drop in join rates)
* [UUIDs and Compressibility](https://richardstartin.github.io/posts/uuids-and-compressibility)
  * Because UUIDs are generally ‘random’, they’re practically impossible to meaningfully compress
  * Also, string representation makes a big difference in key size scaling (binary->16b, UTF-8-> 36b)

### Sidebar on applicability of this to the microservices/persistence architectures

Within a service/state domain, noone cares what the underlying storage is doing; **there is no reason that a persistence service couldn’t use auto-increment PK’s for its internal state storage** etc.

However, when entities are referenced, or expressed on the boundaries of that service, they should be referred to and stored using some kind of globally unique identifier.

### Sidebar on intepretability

One valid criticism leveled at UUID is that it’s difficult / taxing for a human to tell if two UUID’s are the same, and similarly, they can be difficult to ‘share around’, i.e. shout across the offices we no longer use (greetings from COVID '21).

Even if the entity references are encoded a full-throated UUID, there’s no reason we can’t have other tools to support the recognition and similarity.

One approach is [‘hashvatars’](https://francoisbest.com/posts/2021/hashvatars), i.e. functionally generated visual representations of large, un-friendly, numbers.

![](/img/2021/hashvatar.png)

These can be mapped such that while ‘close’ hashes look similar, (the author uses the word ‘soul’ to describe this), that nearby-differences can be highlighted, so that it is clear that two findings are very different.

But visual verification isn’t a solution for interpretability. Git has exactly the same problem, with even longer, 40 character SHA1 hash’s representing commits. However, for the vast majority of projects, [7 characters of that hash is sufficient to represent the commit](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection) *within the project* without colliding with project-external commits.

This kind of contextual reference (i.e. permitting the use of shortcodes or similar) to identify, for instance, a 'book' associated with a 'customer', even if several ‘global’ entities still match that ‘shortcode’, that querier should not have access to those entities, so the storage backend can still resolve that case.

## Bolsters General Rule of Thumb

For stateful entities such as Customer or Clients records, or the long term objects they create, etc, these should be referred to by truely-random identifiers, as one ‘client’ does not need to be proximal or relatable to another client, just being held distinctly. IMO these should be UUIDv4 values.

For stateless events or ephemeral data or observations, these should be referred to by values that have lexical sorting and proximity, so as to support efficient window-range querying, caching and rollup. IMO these should be UUIDv6, (alternatives do exist, see [UUIDv6 Background section](https://www.ietf.org/archive/id/draft-peabody-dispatch-new-uuid-format-01.html#name-background))

(Other versions of uuid libraries supporting v6 exist in a range of languages, such as [PHP](https://uuid.ramsey.dev/en/latest/nonstandard/version6.html),[Python, Zig, Dart, Javascript and Go](https://github.com/uuid6/prototypes#prototypes), however, since UUIDv6 is simply and endianness-flip of UUIDv1, there should be no trouble in applying this to other languages/frameworks)

## UUIDv4 for Entity ID's

```python
import uuid

def id_gen():
    return uuid.uuid4()

id_gen()
>>> UUID('d9c11c39-4bdf-4903-83e5-163b77f6df23')
```
## UUIDv4 for Event ID's

```python
import uuid

def uuidv1tov6(u):
  ## UUIDV1 has it's time-based components in 'little endian', i.e.
  # Least significant words first
  # see https://datatracker.ietf.org/doc/html/rfc4122#section-4.1.2
  # Equivalent to writing timestamps as SS.MM:HH DD-MM-YYYY
  # Makes them time based but not lexically sortable or proximal
  # This simple rearrangement fixes that
  uh = u.hex
  tlo1 = uh[:5]    #LSB
  tlo2 = uh[5:8]
  tmid = uh[8:12]
  # uh[12] contains the version number, i.e. 1, this is manually replaced below
  thig = uh[13:16] #MSB
  rest = uh[16:]
  uh6 = thig + tmid + tlo1 + '6' + tlo2 + rest
  return uuid.UUID(hex=uh6)

def id_gen():
    return uuidv1tov6(uuid.uuid1())

id_gen()
>>>    UUID('1ebd8241-29fe-63bc-87f1-000d3a45a647')
```

> Just because you're paranoid doesn't mean they're not after you

```python
from time import sleep
from tqdm.auto import tqdm

generated_ids = list()

for i in tqdm(range(10_000)):
    generated_ids.append(id_gen())
    sleep(0.01) # Simulate actual time / work done

for i in range(len(generated_ids)-1):
    # Validate monotonicity, order, and uniqueness
    assert str(generated_ids[i]) < str(generated_ids[i+1])
```
