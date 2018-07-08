# web-scraper
This is a Scrapy project to scrape phone numbers from webpages on klsdiversified.com.

This project is only meant for educational purposes.

## Extracted data
This project extracts phone numbers using regex.
The extracted data looks like this sample:

     {
          'phone_num': 'xxx.xxx.xxxx'
     }

## Spiders
This project contains one spider and you can find it by running the `list` command:

     $ scrapy list
     phonenums
  
The spider extracts the data from each web page and looks for a phone number pattern.

You can learn more about the spiders by going through the
[Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html).

## Running the spiders
You can run a spider using the `scrapy crawl` command, such as:

     $ scrapy crawl phonenums

If you want to save the scraped data to a file, you can pass the `-o` option:

     $ scrapy crawl phonenums -o phonenums.json
