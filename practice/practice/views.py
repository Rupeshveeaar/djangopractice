from django.http import HttpResponse
from django.shortcuts import render


"""def index(request):
    return HttpResponse("<h1>Amazon</h1>"
    "<p>Amazon.com, Inc.[6] (/ˈæməzɒn/ AM-ə-zon) is an American multinational technology company which focuses "
                        "on e-commerce, cloud computing, digital streaming, and artificial "
                        "intelligence. It is one of the Big Five companies in the U.S. information "
                        "technology industry, along with Google (Alphabet), Apple, Meta (Facebook), "
                        "and Microsoft.[7][8][9][10] The company has been referred to as </p>")

def history(request):
    return HttpResponse("<h1>History</h1>"
                     '''<p>Jeff Bezos founded Amazon in July 1994, choosing Seattle because of technical talent as Microsoft is located there.[30] Mackenzie Scott played a big role in the founding of Amazon and drove across the country with Jeff to start it. After Scott graduated, she applied to work for D. E. Shaw & Co., a quantitative hedge fund in New York City, as a research associate to "pay the bills while working on her novels".[31][32] She was interviewed by Jeff Bezos, who was then a vice-president at the firm. The interview was her first meeting with him.[33][31]

In May 1997, Amazon went public. It began selling music and videos in 1998, at which time it began operations internationally by acquiring online sellers of books in United Kingdom and Germany. The following year, Amazon began selling items including video games, consumer electronics, home improvement items, software, games, and toys.

In 2002, Amazon launched Amazon Web Services (AWS), which provided data on website popularity, Internet traffic patterns and other statistics for marketers and developers. In 2006, Amazon grew its AWS portfolio when Elastic Compute Cloud (EC2), which rents computer processing power as well as Simple Storage Service (S3), that rents data storage via the Internet, were made available. That same year, Amazon started Fulfillment by Amazon which managed the inventory of individuals and small companies selling their belongings through the company internet site. In 2012, Amazon bought Kiva Systems to automate its inventory-management business, purchasing Whole Foods Market supermarket chain five years later in 2017.[34]</p>''')
def amazon(request):
     return HttpResponse('''<h1>Amazon</h1><a href="https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydr1-21&ref=pd_sl_4mi4ljzku9_b&adgrpid=60469107993&hvpone=&hvptwo=&hvadid=294134852299&hvpos=&hvnetw=s&hvrand=5872541942309754450&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061702&hvtargid=kwd-297902904867&hydadcr=5839_1738693&gclid=CjwKCAiA1uKMBhAGEiwAxzvX9wAJuGbLISMbYafUDXE6dGoFFhLVcmAYT8BcXSyz2XrGs9MgcuChIBoC7IMQAvD_BwE">Amazon</a>''')"""

"""new code for pipeline"""
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext= request.Get.get('text','defult')
def removepunc(request):
    return HttpResponse('removepunc')


