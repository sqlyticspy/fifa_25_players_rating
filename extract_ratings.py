import asyncio
import re
import json
import os
from crawl4ai import AsyncWebCrawler, JsonCssExtractionStrategy, CrawlerRunConfig, CacheMode


with open("./schemas/schema_rating.json", "r") as f:
    schema = json.load(f)


async def main():

    # Create the extraction strategy
    extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)

    # Setup your crawl config (if needed)
    config=CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        extraction_strategy=extraction_strategy
    )

    async with AsyncWebCrawler(verbose=True) as crawler:

        # run the crawl and extraction
        for page in range(19, 30):
            result = await crawler.arun(
                url=f"https://www.ea.com/en/games/ea-sports-fc/ratings?page={page}",
                config=config
            )

            if not result.success:
                print("Crawl Failed:", result.error_message)
                return
        
            # parse the extracted JSON
            new_data = json.loads(result.extracted_content)

            # Transform player_url values to add the base URL
            for item in new_data:
                item['player_url'] = 'https://www.ea.com' + item['player_url']
                
                # Extract player_id from player_url using regex
                match = re.search(r'/(\d+)/?', item['player_url'])
                item['player_id'] = match.group(1)

            # Read existing data if file exists
            data_file="./data/players_rating.json"
            if os.path.exists(data_file):
                with open(data_file, "r", encoding="utf-8") as f:
                    existing_data=json.load(f)
            else:
                existing_data=[]
            
            # Append the new_data
            existing_data.extend(new_data)

            # Save back to a JSON 
            with open(data_file, "w", encoding="utf-8") as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)

            # Append the scrapped page to the file
            with open("scrapped_log.txt", "a") as f:
                f.write(f"{page}\n")

            print(f"Page {page} has been scrapped.")
            
            await asyncio.sleep(2)  # Wait 2 second before next request

if __name__ == "__main__":
    asyncio.run(main())
