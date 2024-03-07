def 품목_목록():

    광물 = ["청금석", "레드스톤", "금", "철", "구리", "다이아", "금 원석"]
    농작물 = ["가지", "파인애플", "홉", "토마토", "고추", "마늘", "양배추", "배추", "포도", "옥수수"]
    물고기 = ["강꼬치고기", "개복치", "금붕어", "농어", "다랑어", "메기", "문어", "숭어", "연어", "잉어", "잡어", "적색통돔", "정어리"]
    기타 = ["조미료", "가죽", "닭고기", "생고기"]

    return 광물, 농작물, 물고기, 기타

def 축약어():
    축약어_모음 = {
        '구': '구리',  'ㄱㄹ': '구리',
        '다': '다이아', 'ㄷㅇㅇ': '다이아',
        '금원': '금 원석', 'ㄱㅇㅅ': '금 원석','금원석': '금 원석',
        'ㅊㄱㅅ': '청금석', 'ㅊㄳ': '청금석','청': '청금석',
        '레': '레드스톤','ㄹㄷㅅㅌ': '레드스톤','fpemtmxhs':'레드스톤','fetx':'레드스톤',
        'ㅊ': '철','cjf':'철', 'c':'철',
        'ㄱ': '금', 'r':'금', 'rma':'금', 
        
        
        '가': '가지', 'ㄱㅈ': '가지', 'rw':'가지', 'rkwl':'가지','rk':'가지',
        '파': '파인애플', 'ㅍㅇㅇㅍ': '파인애플', 'vddv' : '파인애플', 'vkdlsdovmf' : '파인애플','vk':'파인애플',
        'ㅎ': '홉', 'ghq' : '홉', 'g':'홉',
        'ㅌㅁㅌ': '토마토', '토': '토마토','xax':'토마토', 'xhakxh' : '토마토','xh':'토마토',
        'ㄱㅊ':'고추', '고': '고추' , 'rc' : '고추', '꼬추' : '고추', 'rhcn':'고추', 'rh':'고추',
        'ㅁㄴ': '마늘', '마': '마늘','aksmf':'마늘', 'as':'마늘', 'a':'마늘', 'ak':'마늘',
        'ㅇㅂㅊ': '양배추', '양': '양배추', 'dqc':'양배추','didqocn' : '양배추', 'did':'양배추',
        'ㅂㅊ':'배추', '배':'배추','qc' : '배추', 'qocn' : '배추', 'qo':'배추',
        '포': '포도', 'ㅍㄷ': '포도','ve':'포도', 'vheh':'포도','vh':'포도', 
        '옥': '옥수수', 'ㅇㅅㅅ': '옥수수', 'dhrtntn':'옥수수','dhr':'옥수수','dtt':'옥수수',
        

        '강': '강꼬치고기', 'ㄱㄲㅊ': '강꼬치고기', '개': '개복치', 'ㄱㅂㅊ': '개복치',
        
        '조': '조미료', 'ㅈㅁㄹ': '조미료', '생' : '생고기', '닭':'닭고기'
    }

    return 축약어_모음