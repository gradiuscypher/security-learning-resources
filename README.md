# security-learning-resources
A collection of learning resources (con talks, slide decks, blog posts, etc) both in human-readable and JSON format.

## Contributors
[gradiuscypher](https://github.com/gradiuscypher)

## Project Goals
This project will collect learning resources for the information security industry. This information will be presented in human-readable format as Markdown and will also be programmatically accessable via JSON files. This will allow the use and format of this data in many ways.

Contained in this project will also be various scripts. For example, converting the JSON files into various human-readable formats, or a command line tool that walks a user through creating a new entry.

## Contributing
Check out the [Contribution Guide](CONTRIBUTING.md) for more information.

## learning_resources.json layout
```json
  {
      "type": "presentations",
      "items": [
        {
          "title": "Example Title Here",
          "description":"Presentation Description",
          "last_updated": "2018-08-20",
          "video_url": "Video URL",
          "slide_url": "Slide Deck URL",
          "presentation": {
            "date": "2018-01-15",
            "location": "Presentation Location String",
            "authors": [
              {
                "name": "Author1",
                "contact": "Social Media URL"
              },
              {
                "name": "Author2",
                "contact": "Email"
              }
            ]
          },
          "tags": [
            "tag1", "tag2", "tag3"
          ],
          "metadata": [
            {"name": "value"},
            {"name": "value"}
          ]
        }
      ]
  }
]
```

Breaking this down a bit: 
* At the top level, I'll have a list of resource types so that I can expand this resource in the future to cover things like blog posts, useful twitter threads, etc.
* Each resource type has a `type` and a list of `items`
* Each `items` list contains an object that matches the format of the resource type
* For presentations, which is my initial resource for this project, I've included:
  * `title`: The presentation title.
  * `description`: A description of the presentation
  * `last_updated`: The date on which this resource was last updated, in the format YYYY-MM-DD
  * `video_url`: A link to the video of the presentation if available. Empty string if not.
  * `slide_url`: A link to the slide deck if available. Empty string if not.
  * `presentation`: An object that contains details about the actual presentation
    * `date`: The date the presentation was made, in the format YYYY-MM-DD
    * `location`: The location (conference, web meeting, etc) where it was presented, if available.
    * `authors`: A list of authors, including their name and their preferred social contact, if available
  * `tags`: Any appropriate tags for the presentation, list of strings
  * `metadata`: A list of fields containing a `name` and `value`, for further metadata addition that might have not been considered previously, or for data that's specific to this object. Example: notes about the talk, warnings about content, etc. A sort of final catch-all, until a metadata field becomes so common it justifies being added to the core structure.
