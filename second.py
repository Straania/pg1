def cislo_text(cislo):
    delka_cislo=len(cislo)
    if(delka_cislo==3):
        return "sto"
    
    cislo_list=[]
    for x in str(cislo):
        cislo_list.append(x)

    final_str=[]
    if(delka_cislo==2):
        if(cislo_list[0]=="2"):
            final_str.append("dvacet ")
        if(cislo_list[0]=="3"):
            final_str.append("třicet ")
        if(cislo_list[0]=="4"):
            final_str.append("čtyřicet ")
        if(cislo_list[0]=="5"):
            final_str.append("padesát ")
        if(cislo_list[0]=="6"):
            final_str.append("šedesát ")
        if(cislo_list[0]=="7"):
            final_str.append("sedmdesát ")
        if(cislo_list[0]=="8"):
            final_str.append("osmdesát ")
        if(cislo_list[0]=="9"):
            final_str.append("devadesát ")

        if(cislo_list[0]!="1"):
            if(cislo_list[1]=="1"):
                final_str.append("jedna")
            if(cislo_list[1]=="2"):
                final_str.append("dva")
            if(cislo_list[1]=="3"):
                final_str.append("tři")
            if(cislo_list[1]=="4"):
                final_str.append("čtyři")
            if(cislo_list[1]=="5"):
                final_str.append("pět")
            if(cislo_list[1]=="6"):
                final_str.append("šest")
            if(cislo_list[1]=="7"):
                final_str.append("sedm")
            if(cislo_list[1]=="8"):
                final_str.append("osm")
            if(cislo_list[1]=="9"):
                final_str.append("devět")

        elif(cislo_list[0]=="1"):
            if(cislo_list[1]=="0"):
                final_str.append("deset")
            if(cislo_list[1]=="1"):
                final_str.append("jedenáct")
            if(cislo_list[1]=="2"):
                final_str.append("dvanáct")
            if(cislo_list[1]=="3"):
                final_str.append("třináct")
            if(cislo_list[1]=="4"):
                final_str.append("čtrnáct")
            if(cislo_list[1]=="5"):
                final_str.append("patnáct")
            if(cislo_list[1]=="6"):
                final_str.append("šestnáct")
            if(cislo_list[1]=="7"):
                final_str.append("sedmnáct")
            if(cislo_list[1]=="8"):
                final_str.append("osmnáct")
            if(cislo_list[1]=="9"):
                final_str.append("devatenáct")

    

            

    if(delka_cislo==1):
        if(cislo_list[0]=="0"):
            final_str.append("nula")
        if(cislo_list[0]=="1"):
            final_str.append("jedna")
        if(cislo_list[0]=="2"):
            final_str.append("dva")
        if(cislo_list[0]=="3"):
            final_str.append("tři")
        if(cislo_list[0]=="4"):
            final_str.append("čtyři")
        if(cislo_list[0]=="5"):
            final_str.append("pět")
        if(cislo_list[0]=="6"):
            final_str.append("šest")
        if(cislo_list[0]=="7"):
            final_str.append("sedm")
        if(cislo_list[0]=="8"):
            final_str.append("osm")
        if(cislo_list[0]=="9"):
            final_str.append("devět")

    return "".join(final_str)

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)