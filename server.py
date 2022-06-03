from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 10

data = {

    "1": {
        "id": "1",
        "title": "Cowspiracy",
        "image": " https://wholepeople.com/wp-content/uploads/2020/05/Cowspiracy-Documentary-Movie-Poster-1.jpg",
        "year": "2014",
        "summary": " Cowspiracy is a 2014 documentary film which explores the impact of animal agriculture on the environment and investigates the policies of a few environmental organizations on this issue. The film looks at various environmental concerns, including climate change, water use, deforestation, and ocean dead zones, and suggests that animal agriculture is the primary source of environmental destruction. Environmental organizations investigated in the film include Greenpeace, Sierra Club, Surfrider Foundation, Rainforest Action Network, and Oceana.",
        "directors": ["Kip Andersen, Keegan Kuhn"],
        "score": "8.2",
        "stream": "netflix",
    },

    "2": {
        "id": "2",
        "title": "Earthlings",
        "image": "https://wholepeople.com/wp-content/uploads/2020/05/Earthlings-Joaquin-Phoenix.jpg",
        "year": "2005",
        "summary": " Covering pet stores, puppy mills, and various animal professions, Earthlings includes footage obtained through the use of hidden cameras to chronicle the day-to-day practices of some of the largest industries in the world, all of which rely on animals. Then, the film draws parallels between speciesism and racism, sexism, and more. A title that will upset, shock and live long in the memory with some of the most graphic and tragic scenes of animal cruelty one is likely to see. Split into five parts, Earthlings gets behind the workings of the main sectors of industry that use animals to reveal how they are treated as mere units of production, their sole purpose to ultimately provide income with no consideration towards their physical and mental wellbeing. Earthlings demonstrates how animals have come to serve mankind where the weak are remorselessly exploited by the strong. In effect, humans are engaging in speciesism on a global scale, that is, discrimination against all other species. All other Earthlings.",
        "directors": ["Shaun Monson, Keegan Kuhn"],
        "score": "8.7",
        "stream": "youtube",
    },

    "3": {
        "id": "3",
        "title": "Forks Over Knives",
        "image": "https://mindbodygreen-res.cloudinary.com/image/upload/w_767,q_auto:eco,f_auto,fl_lossy/ftr/forks-over-knives-image-film.jpg",
        "year": "2011",
        "summary": "Forks Over Knives is a 2011 American advocacy film and documentary that advocates a low-fat, whole-food, vegan diet as a way to avoid or reverse several chronic diseases. The film recommends avoiding overly refined and processed foods, including refined sugars, bleached flours, and oils, and instead eating whole grains, legumes, tubers, vegetables, and fruits. Through an examination of the careers of American physician Caldwell Esselstyn and professor of nutritional biochemistry T. Colin Campbell, Forks Over Knives claims that many diseases, including obesity, cardiovascular diseases, and cancer, can be prevented and treated by eating a whole-food, plant-based diet, avoiding processed food and food from animals. The film includes an overview of the 20-year China–Cornell–Oxford Project that led to Professor Campbell's findings, outlined in his book The China Study (2005), in which he suggests that coronary artery disease, diabetes, obesity, and cancer can be linked to the Western diet of processed and animal-based foods (including dairy products).",
        "directors": ["Lee Fulkerson, John Corry"],
        "score": "7.7",
        "stream": "vudu",
    },

    "4": {
        "id": "4",
        "title": "The Game Changers",
        "image": "https://img.moviesrankings.com/t/p/w1280/wsKBNxC99fHDtsOXA0BJVexZXGr.jpg",
        "year": "2018",
        "summary": "James Wilks is a mixed martial artist and self defense instructor. Having suffered an injury he used his downtime to explore the effects of plant-based diets on health, recovery, and athletic performance. He first explores the vegetarian diet of Roman gladiators before interviewing athletes such as Scott Jurek, Patrik Baboumian, Bryant Jennings, and Derrick Morgan who attribute their success to a plant-based diet. Comments follow from Scott Stoll, a physician for the USA Olympic team, who argues that animal based protein impedes recovery and athletic performance due to certain inflammatory molecules and inflammatory mediators. He contrasts this with plant-based proteins that, he argues, promote gut microbial diversity, reduce inflammation, and optimize recovery and athletic performance. The film dramatizes a comparison of postprandial effects of meals consisting of animal- versus plant-based foods, purporting to show that those who ate meat showed reduced penile function and indications of endothelial dysfunction that could disrupt athletic performance. In an interview, Professor of Epidemiology and Nutrition, Walter Willett, argues that there is accumulating evidence showing that high consumption of protein from dairy sources is related to a higher risk of prostate cancer.",
        "directors": ["Louie Psihoyos, Joseph Pace"],
        "score": "7.8",
        "stream": "netflix",

    },

    "5": {
        "id": "5",
        "title": "Seaspiracy",
        "image": "https://hrflix.eu/img/vertical/large/81014008.jpg",
        "year": "2021",
        "summary": "Seaspiracy is a 2021 documentary film about the environmental impact of fishing directed by and starring Ali Tabrizi, a British filmmaker. The film examines various human impacts on marine life and advocates for ending fish consumption. Tabrizi acts as both the narrator and protagonist of the film, discovering key pieces of information at the same moment as the viewer. The film centers early on the collapse of whale, shark, dolphin and sea turtle populations. The film asserts that the focus of environmental groups on comparatively small consumer plastics like straws has obfuscated the larger problem of plastic waste from fishing gear, or ghost nets, as well as the devastation of bycatch. The film suggests the problem of feed for farmed fish as well as the prevalence of disease and coastal degradation make aquaculture untenable.",
        "directors": ["Ali Tabrizi, Kip Andersen"],
        "score": "8.2",
        "stream": "netflix",
    },

    "6": {
        "id": "6",
        "title": "Dominion",
        "image": "https://sharan-india.org/wp-content/uploads/2018/08/dominion_poster_final.jpg",
        "year": "2018",
        "summary": "The film shows the many ways in which animals are regularly abused. A total of six facets are illuminated: farmed animals, wild animals, companion animals, entertainment animals, fur animals, and animal experimentation.The film mainly uses video from the free online animal rights resource Aussie Farms Repository, which includes footage from hidden cameras and aerial drones. Dominion describes, in 18 clearly structured chapters, how different animal species are used and misused in different ways. The film is divided into segments covering different species: pigs, laying hens and meat chickens, turkeys, cows, sheep, goats, fish, rabbits, mink, foxes, dogs, horses, camels, mice, exotic animals, seals and dolphins, and a conclusion from the narrators.",
        "directors": ["Chris Delforce"],
        "score": "9.0",
        "stream": "youtube",
    },

    "7": {
        "id": "7",
        "title": "Eating Our Way to Extinction",
        "image": "https://panicdots.com/wp-content/uploads/2021/08/86897-upcoming-movie-eating-our-way-to-extinction.jpg",
        "year": "2021",
        "summary": "EATING OUR WAY TO EXTINCTION takes audiences on a cinematic journey around the world, from the depths of the Amazon rainforests to the Taiwanese Mountains, the Mongolian desert, the US Dust Bowl, the Norwegian Fjords and the Scottish coastlines, telling the story of our planet through shocking testimonials, poignant accounts from indigenous people most affected by our ever-changing planet, globally renowned figures and leading scientists. This powerful documentary sends a simple but impactful message by uncovering hard truths and addressing, on the big screen, the most pressing issue of our generation – ecological collapse.Confronting and entertaining, this documentary allows audiences to question their everyday choices, industry leaders and governments. Featuring a wealth of world-renowned contributors, including Sir Richard Branson and Tony Robbins, it has a message of hope that will empower audiences.",
        "directors": ["Ludo Brockway, Otto Brockway"],
        "score": "7.7",
        "stream": "vudu"
    },

    "8": {
        "id": "8",
        "title": "Meat the Truth",
        "image": "https://ecocosas.com/wp-content/uploads/2012/05/meat-the-truth-1.jpg",
        "year": "2007",
        "summary": "Meat the Truth draws attention to intensive livestock production by demonstrating that livestock farming generates more greenhouse gas emissions worldwide than all cars, lorries, trains, boats and planes added together.",
        "directors": ["Karen Soeters, Gertjan Zwanikken"],
        "score": "7.9",
        "stream": "youtube"
    },

    "9": {
        "id": "9",
        "title": "Before the Flood",
        "image": "https://wholepeople.com/wp-content/uploads/2020/05/Before-The-Flood-Documentary-Movie-Poster-1.jpg",
        "year": "2016",
        "summary": "Before the Flood is a 2016 documentary film about climate change directed by Fisher Stevens. The film was produced as a collaboration between Stevens, Leonardo DiCaprio, James Packer, Brett Ratner, Trevor Davidoski, and Jennifer Davisson Killoran. Martin Scorsese is an executive produce. The film shows DiCaprio visiting various regions of the globe[8] exploring the impact of global warming.[9] As a narrator, DiCaprio comments these encounters as well as archive footages. DiCaprio repeatedly references a 15th-century triptych by Hieronymus Bosch, The Garden of Earthly Delights, which, he explains, hung above his crib as an infant, and which he uses as an analogy of the present course of the world toward potential ruin as depicted on its final panel.[10] The film also documents, in part, the production of DiCaprio's 2015 film The Revenant. DiCaprio's comments and inquiries focus extensively on climate change denial, mostly among corporate lobbyists and politicians of the United States. They interview with British-born astronaut Piers Sellers, a NASA scientist who flew on three space missions, discusses his desire to publicize the perils of global warming in the short time he expected he had remaining to live, as he had stage IV pancreatic cancer as he was being filmed. He died on December 23, 2016.",
        "directors": ["Fisher Stevens, Mark Monroe"],
        "score": "8.2",
        "stream": "vudu"
    },

    "10": {
        "id": "10",
        "title": "Lucent",
        "image": "https://www.aussiepigs.com/images/lucent/Poster1.jpg",
        "year": "2014",
        "summary": "Lucent, which many consider to be the prequel to Dominion, uses hidden camera footage to reveal the heartbreaking lives of pigs from birth through to when they are eventually slaughtered for their meat. Although the film was made in Australia, it represents many of the practices of the time used throughout the west. Pigs are naturally intelligent, clean and social animals. The industrial farming practices are employed in such a way that many of the animals’ natural instincts are inhibited. Raised in environments that at every stage of their development lack the required mental stimulation and space, induces unnatural behaviours and physical and mental suffering.",
        "directors": ["Chris Delforce, Gertjan Zwanikken"],
        "score": "8.8",
        "stream": "youtube"

    }

}


# ROUTES


@app.route('/', methods=['GET', 'POST'])
def home_page():

    home_link = []
    empty_arr = {}

    for key, value in data.items():
        if(key == '1' or key == '2' or key == '9'):
            empty_arr[key] = value
    for key, value in empty_arr.items():
        home_link.append(value)

    return render_template('home_page.html', data_first=home_link, lateadd=empty_arr)


@app.route('/results_page/<doc_title>')
def results_page(doc_title=None):

    final_result = []
    second_result = []
    third_result = []

    for key, value in data.items():
        titulo = value["title"].lower()
        diretores = value["directors"]
        assistir = value["stream"].lower()

        for i in range(len(diretores)):
            diretores[i] = diretores[i].lower()
            novodiretores = diretores[i]

            if novodiretores == doc_title or doc_title in novodiretores:
                third_result.append(value)

        if titulo == doc_title or doc_title in titulo:
            final_result.append(value)

        if assistir == doc_title or doc_title in assistir:
            second_result.append(value)

    return render_template('results.html', data_second=final_result, feedback_result=doc_title, second_result=second_result, third_result=third_result)


@app.route('/view/<id>', methods=['GET', 'POST'])
def view(id=None):
    lazycats = []
    random = ""

    if request.method == 'POST':

        ed_title = request.form['serial_title']
        ed_year = request.form['serial_year']
        ed_score = request.form['serial_score']
        ed_image = request.form['serial_image']
        ed_stream = request.form['serial_stream']
        ed_directors = request.form['serial_direc'].split(",")
        ed_summary = request.form['serial_summary']

        edited_data_entry = {
            "id": id,
            "title": ed_title,
            "image":  ed_image,
            "year":  ed_year,
            "summary":  ed_summary,
            "directors":  ed_directors,
            "score":  ed_score,
            "stream":  ed_stream,
        }

        data[id] = edited_data_entry

        print(data)
        print(edited_data_entry)

        #     return data[id]

    for key, value in data.items():
        if value["id"] == id:
            lazycats.append(value)
            random = value["title"]
            print(lazycats)
            print(random)

    return render_template('documentary.html', data_third=lazycats, lazycats=id, lazycats_title=random)


@app.route('/add', methods=['GET', 'POST'])
def add():
    global current_id
    global data

    json_data = request.get_json()

    current_id += 1
    new_id = str(current_id)
    newtitle = json_data["title"]
    newimage = json_data["image"]
    newyear = json_data["year"]
    newsummary = json_data["summary"]
    newdirectors = json_data["directors"]
    newscore = json_data["score"]
    newstream = json_data["stream"]

    new_doc_entry = {

        "id": new_id,
        "title": newtitle,
        "image":  newimage,
        "year":  newyear,
        "summary":  newsummary,
        "directors":  newdirectors,
        "score":  newscore,
        "stream":  newstream,
    }

    data[new_id] = (new_doc_entry)

    print(new_doc_entry)
    print(data)

    return new_doc_entry


@app.route('/add_item_page', methods=['GET', 'POST'])
def add_item_page():

    return render_template('additem.html')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id=None):

    empty_arr = data[id].copy()
    empty_arr["directors"] = ",".join(empty_arr["directors"])

    return render_template('edit_item.html', newdata=empty_arr, id=id)


if __name__ == '__main__':
    app.run(debug=True)
