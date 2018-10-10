import webhoseio

webhoseio.config(token="8d786df0-7885-4818-a4d2-0562b9507f1f")
query_params = {
    "q": "Urovant Sciences language:english site_type:news thread.published:>1535778000000",
    "sort": "crawled"
}
output = webhoseio.query("filterWebContent", query_params)
print(len(output))
print(output['posts'][0]['text']) # Print the text of the first post
print (output['posts'][0]['published']) # Print the text of the first post publication date
print(output)

# Get the next batch of posts

output = webhoseio.get_next()
print(output)
# Print the site of the first post

print (output['posts'][0])
