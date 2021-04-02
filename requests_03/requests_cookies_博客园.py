import requests

session = requests.session()

session.cookies.set(".CNBlogsCookie","B557DE94246A273E4A4BC2910E92CA56D020E403C07E2C4BBEDBFC52BF320C083FB296259C92F5538ECC575EB195E65802E0F4F3B160FFD316F27E9763D7F5E815ED86D6524E5A43A5D21B48184053E06108EBAD",domain=".cnblogs.com",path="/")
session.cookies.set(".Cnblogs.AspNetCore.Cookies","CfDJ8EklyHYHyB5Oj4onWtxTnxa6GNprMhFmoPUFRW8ZMJ0A3HplF5EkqfTUHErAdmSwhXCXewr9u1gryXx9TI-ufPIOeswoMPoTQT2ta8lHo9Jwp-wSEpfFt7SVdOeC11OkspP_-Mvcut6Akwu29D-nvVZMBfMBhkHsC5SOzORvKkEtWxgtacok5KJ--v3jf80roTyeVT6aS7-q2wB9TUROS9WuOMfIf3afps9910H5uteOUvY7pb8RPFzQHXYq5H9TYO-a7UKjAJPQXY5Qa2G5XEjqBKpSkefTkxFNzmSiLnTePAvjjEGMmOopXBbRvZHKCy6-5PDOa3Tcpei6jPGyUgrikbc0K29qN80WFBCOO9Roo7ayP9Oydev9ClPhDuR4XoOPzNtGB1hEhZ1sZnL3t7ydFmq6nMIi7RFtnkKN4cYjqYN4vUUFFGFl9hSjW64dFtY_B0NdKUmegmVDv47XmcdVceMLpd9nkUL9WnNUOUvAXdHKn7kpghFXbMTMxTVREhu2DrmvAVpvnVuqab1Ohsd2ElPzwDv1FFNAkVh6VnkSztGFQhpvGD1eb7mMXB6r7Q",domain=".cnblogs.com",path="/")
session.cookies.set(".AspNetCore.Antiforgery.b8-pDmTq1XM","CfDJ8EklyHYHyB5Oj4onWtxTnxZlAToo1OOn5EGjLwiHjbrX1lRN8w-8ASgQjv9g88AeL0NVXR9NAQIm6ltxEvmAi36ITaVFuti8drOGfO3c3qT6Unq6emJ6uzSKmg9Tb6R6q3jjhwnkZpK3DSMbuaR6H_o",domain="www.cnblogs.com",path="/")

header_info={
    "content-type":"application/json; charset=UTF-8",
    "accept":"application/json, text/javascript, */*; q=0.01",
    "x-requested-with":"XMLHttpRequest",
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

post_data = {
	"postId": 14528777,
	"body": "期待作者后续更新",
	"parentCommentId": 0
}

response = session.post(url='https://www.cnblogs.com/df888/ajax/PostComment/Add.aspx',
                        headers = header_info,
                        json=post_data,
                        verify=False)
print( response.content.decode('utf-8') )