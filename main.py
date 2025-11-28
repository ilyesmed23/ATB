import flet as ft
import json
import urllib.parse




# =============================================================================
# 1. TEXTES INFORMATIFS PAR SPÉCIALITÉ
# =============================================================================
# =============================================================================
# 1. TEXTES INFORMATIFS PAR SPÉCIALITÉ (INTRODUCTIONS DES RFE 2024)
# =============================================================================
SPECIALTY_INFO = {
    "Neurochirurgie & Neuroradiologie": """
**PRINCIPES GÉNÉRAUX**

Le risque infectieux principal est l'infection cérébro-méningée, difficile à traiter et engageant le pronostic vital ou fonctionnel.
L'antibioprophylaxie a montré une diminution indiscutable du risque pour les craniotomies et les dérivations internes.

**SITUATIONS PARTICULIÈRES**

• **Fuite de LCR post-traumatique :** Pas d'antibioprophylaxie (absence de preuve d'efficacité).

• **Dérivation Externe (DVE) :** Efficacité controversée. La prévention repose surtout sur des protocoles standardisés de pose et de gestion.

• **Rachis non instrumenté :** Preuves insuffisantes pour justifier une antibioprophylaxie systématique.

• **Neuroradiologie interventionnelle :** Infections exceptionnelles, pas d'antibioprophylaxie justifiée.

**ALLERGIES**

• Si Céfazoline -> Clindamycine 900 mg IVL.

• Si Amox-Clav -> **Triméthoprime/Sulfaméthoxazole (Bactrim)** 160/800 mg IVL (Pas de réinjection).

⚠️ **REMARQUES COMPLÉMENTAIRES**

• ** Une épidémiologie locale particulière peut justifier le recours à une molécule alternative, dans le cadre d'un protocole validé localement d'antibioprophylaxie.

• En cas d'ablation de matériel d'ostéosynthèse ou de chirurgie sans pose de matériel exposant à une ouverture de la dure-mère, ou de geste prévu comme difficile/avec temps opératoire long, une antibioprophylaxie par céfazoline peut être discutée au cas par cas.
""",


    "ORL (Oto-Rhino-Laryngologie)": """
**NIVEAU DE RISQUE**

• **Élevé (~30%) :** Chirurgie avec ouverture bucco-pharyngée (notamment carcinologique). L'antibioprophylaxie est indispensable.

• **Faible (<2%) :** Chirurgie rhino-sinusienne.

**DURÉE DU TRAITEMENT**

La grande majorité des études ne montre pas de bénéfice à une antibiothérapie prolongée.
L'antibioprophylaxie doit être limitée au bloc opératoire, ou au maximum 48h post-opératoires.

**ALLERGIES**

• Clindamycine 900 mg IVL (sauf mention contraire dans le tableau).

⚠️ **REMARQUES COMPLÉMENTAIRES**

• * En cas de chirurgie particulièrement longue et d'extension de la prophylaxie aux 48 premières heures postopératoires, il convient de veiller à ne pas dépasser la dose maximale de **1200 mg/j d'acide clavulanique**.

• ** La posologie postopératoire est à moduler en fonction du poids et de la fonction rénale du patient.
""",


    "Stomatologie & Chirurgie Maxillo-Faciale": """
**EFFICACITÉ DES MOLÉCULES**

L'Amoxicilline-Clavulanate et la Céfazoline ont une efficacité supérieure à l'Amoxicilline seule ou la Clindamycine.

**DURÉE ET DRAINAGE**

• Aucun argument pour prolonger l'antibioprophylaxie au-delà de 24h post-opératoires.

• La présence d'un drainage ne justifie PAS la prolongation.

• Pas de différence entre chirurgie avec ou sans ouverture bucco-pharyngée.

**PARTICULARITÉS**

• **Chirurgie alvéolaire (greffes) :** Preuves insuffisantes pour soutenir ou réfuter l'intérêt de l'ATB.

**ALLERGIES**

• Clindamycine 900 mg IVL.

⚠️ **REMARQUES COMPLÉMENTAIRES**

• * Posologie postopératoire pour un patient de poids et fonction rénale standard → à moduler en fonction du poids et de la fonction rénale du patient.

• ** En cas de chirurgie particulièrement longue et d'extension de la prophylaxie aux 48 premières heures postopératoires, il convient de veiller à ne pas dépasser la dose maximale de **1200 mg/j d'acide clavulanique**.

• *** **Alternative orale pour extractions dentaires** : En ambulatoire, une prise per os de 2g d'amoxicilline, entre 120 et 60 minutes avant l'intervention, pourrait remplacer l'administration IV (biodisponibilité ~70%, Tmax ~1h). Veiller à limiter l'apport hydrique pour respecter le jeûne préopératoire.
""",


    "Ophtalmologie": """
**PRINCIPES GÉNÉRAUX**

Le risque majeur est l'endophtalmie (perte de l'œil).
Pour la cataracte, l'injection intracamérulaire de **Céfuroxime** diminue par 2 le risque d'endophtalmie.

**ADMINISTRATION**

• L'antibioprophylaxie par collyres ou injections sous-conjonctivales n'est PAS recommandée.

• Pas de réinjection systémique nécessaire en ophtalmologie.

**ALLERGIES**

• Cataracte : Moxifloxacine intracamérulaire.

• Traumatisme : Vancomycine + Amikacine (intra-vitréenne).

⚠️ **REMARQUES COMPLÉMENTAIRES**

• * **Chirurgies combinées** : Les chirurgies de la cornée, du glaucome, de la rétine et du vitré effectuées dans le même temps opératoire qu'une chirurgie de cataracte suivent le même protocole que la cataracte.

• ** **Traumatismes à globe ouvert** : Pas d'indication à associer une antibiothérapie par voie systémique.
""",


    "Chirurgie Thoracique & Pneumologie": """
**OBJECTIFS**

Prévenir les ISO (paroi, pyothorax) et les Pneumonies Post-Opératoires (PPO).

**FACTEURS DE RISQUE ET BPCO**

Pour les résections pulmonaires, l'incidence des PPO est plus élevée chez les BPCO.
L'utilisation d'**Amoxicilline-Clavulanate** (vs Céfazoline) et une prolongation (24-48h max) peuvent être envisagées pour réduire ce risque spécifique.

**ALLERGIES**

• Clindamycine 900 mg + Gentamicine 6-7 mg/kg.

⚠️ **REMARQUES COMPLÉMENTAIRES**

• * **Pour la prévention des PPO chez les patients BPCO** : Privilégier Amoxicilline/Clavulanate (GRADE 2) et possibilité de prolonger jusqu'à 48h post-opératoires maximum (Avis d'experts).

• ** Le niveau de GRADE porte sur les schémas posologiques proposés, et non pour leur application à chaque intitulé spécifique.

• **TRANSPLANTATION PULMONAIRE** : Pas d'antibioprophylaxie universelle possible. Protocole local indispensable selon l'écologie du centre et les antécédents du patient. Discussion pluridisciplinaire recommandée.
""",


    "Cardiaque & Vasculaire": """
**CHIRURGIE CARDIAQUE**

Chirurgie propre (Classe 1) mais à risque accru par la CEC et la complexité.

• **Mesures associées :** Décolonisation nasale (Mupirocine 2%) et bains de bouche (Chlorhexidine) recommandés 48h avant la chirurgie, pour une durée totale de 5-7 jours.

• **Berges sternales :** L'application locale d'antibiotiques (compresses, etc.) n'a pas prouvé son efficacité.

**CARDIOLOGIE STRUCTURELLE**

La voie d'abord fémorale au triangle de Scarpa augmente le risque infectieux.

**CHIRURGIE VASCULAIRE**

• L'abord du Scarpa augmente le risque.

• L'utilisation de prothèses imprégnées (argent/ATB) ne dispense PAS de l'antibioprophylaxie systémique.

**ALLERGIES**

• Vancomycine 20 mg/kg ou Teicoplanine 12 mg/kg.

⚠️ **REMARQUES COMPLÉMENTAIRES**

• **TRANSPLANTATION & ASSISTANCE** : En cas de contexte de réanimation, d'ECMO, ou d'antécédent d'infection, les modalités de l'antibioprophylaxie (molécule et durée) doivent être discutées individuellement après avis infectiologique spécialisé, tenant compte de la colonisation à SARM ou E-BLSE.
""",


    "Orthopédie & Traumato": """
**OBÉSITÉ ET DOSAGE**

Rappel R1.5 : Pour les céphalosporines (Céfazoline), il est **INUTILE** d'augmenter la dose unitaire jusqu'à un IMC de 50 kg/m² si la réinjection est faite.
Pour la Clindamycine (lipophile), la dose doit être augmentée selon le poids.

**TRAUMATOLOGIE**

• Le risque infectieux est plus élevé qu'en chirurgie programmée.

• **Délai :** L'ATB doit être débutée dès la prise en charge (< 3h après le trauma), sans attendre le bloc.

• **Gustilo :** La contamination (tellurique/fécale) compte autant que la classification de Gustilo pour le choix de l'ATB.

**ALLERGIES**

• Programmée/Fermée : Clindamycine (attention aux résistances Cutibacterium épaule → Vanco/Teico).

• Ouverte/Souillée : Clindamycine + Gentamicine.

⚠️ **REMARQUES COMPLÉMENTAIRES**

• * **Résistance de Cutibacterium acnes** : Du fait de la résistance dans 15 à 20% des cas de Cutibacterium acnes et autres Cutibacterium sp. à la clindamycine, préférer la vancomycine ou la teicoplanine en cas de chirurgie prothétique d'épaule ou de hanche par voie antérieure avec allergie aux bêtalactamines.

• ** **Ablation de matériel d'ostéosynthèse** : L'échec d'ablation de matériel d'ostéosynthèse ne constitue pas une indication d'antibioprophylaxie. Toutefois, en cas d'ablation nécessitant une ouverture articulaire ou de geste prévu comme difficile/avec temps opératoire long, une antibioprophylaxie par céfazoline peut être discutée au cas par cas.

• *** **Épidémiologie locale** : Une épidémiologie locale particulière peut justifier le recours à une molécule alternative, dans le cadre d'un protocole d'antibioprophylaxie validé localement.

• **IMC ≥ 50 kg/m²** : La stratégie doit être discutée collégialement et reposer soit sur l'augmentation de la dose unitaire, soit sur le raccourcissement de l'intervalle de réinjection, soit sur l'utilisation d'une dose d'entretien en perfusion intraveineuse continue.

• **Fractures ouvertes Altemeier 3-4** : En cas de contamination majeure du foyer de fracture et avec un délai de prise en charge prolongé, les fractures Gustilo 2 et 3 peuvent être considérées après avis infectiologique comme de classe Altemeier 3-4, justifiant une antibiothérapie curative étendue au-delà du bloc opératoire.

• **Morsures** : Les morsures sont des plaies avec contamination polymicrobienne qui relèvent d'une antibiothérapie curative (5 jours postopératoires avec réévaluation chirurgicale et infectiologique).
""",

"Chirurgie Digestive": """
**PRINCIPES**

• Sans ouverture du tube digestif : Chirurgie propre (Classe 1).

• Avec ouverture : Chirurgie propre-contaminée (Classe 2).

• La cœlio-chirurgie obéit aux mêmes règles que la laparotomie (risque de conversion).

**CHIRURGIE BARIATRIQUE**

L'obésité morbide est un facteur de risque indépendant d'ISO. L'antibioprophylaxie est justifiée même sans ouverture digestive (anneau).

**ALLERGIES**

• Si Céfazoline prévue : Vancomycine ou Teicoplanine.

• Si Céfoxitine prévue : Gentamicine + Métronidazole.

⚠️ **REMARQUES COMPLÉMENTAIRES**

• * **Obésité (IMC ≤ 50 kg/m²)** : Doses standards jusqu'à un IMC ≤ 50 kg/m² en veillant à bien respecter les intervalles de réinjection (R1.5). Au-delà, stratégie différente à discuter collégialement : augmentation de la dose unitaire (4g), raccourcissement de l'intervalle de réinjection, ou dose d'entretien en intraveineux continue.

• ** **Absence de Céfuroxime** : En l'absence d'étude disponible concernant l'utilisation de céfuroxime pour l'anneau gastrique, cette molécule n'est pas proposée en alternative.

• *** **Chirurgie colorectale** : Le GRADE 1 s'applique au fait d'administrer une antibioprophylaxie en chirurgie colo-rectale ET au fait que cette antibioprophylaxie doit comporter à la fois une prise orale la veille au soir et une administration IV lors de l'intervention.

• **** **Tobramycine per os (hors AMM)** : La tobramycine (Nebcine®, non génériquée) s'utilise hors AMM par voie orale pour la décontamination digestive préopératoire. Utilisation d'un flacon IV de 100 mg par voie orale. Vérifier l'absence d'allergie aux sulfites (excipient). Entente préalable auprès de la CPAM recommandée pour remboursement (coût ~3€/flacon). Le métronidazole per os existe en boite de 4 cp de 500 mg (~1,31€).

• ***** **Portage E-BLSE** : Un dépistage dans le mois précédant la chirurgie est préconisé dans les centres où la prévalence atteint ou dépasse 10% de patients porteurs (R1.7). Dépistage ciblé chez les patients ayant un antécédent de colonisation ou d'infection à entérobactérie BLSE au cours des 6 derniers mois.

• **DRAINAGE BILIAIRE** : En cas de réalisation d'un geste sur les voies biliaires chez un patient à risque de colonisation biliaire (prothèse biliaire), l'antibioprophylaxie doit être adaptée aux antécédents infectieux. En l'absence d'infection documentée : pipéracilline + tazobactam 4g IVL.

• **TRANSPLANTATION** : Spectre à élargir et/ou à adapter à l'écologie locale si facteurs de risque de BMR et/ou antécédent d'infection fongique.
""",


    "Urologie": """
**ECBU PRÉ-OPÉRATOIRE**

Ces recommandations ne traitent PAS du dépistage/traitement des colonisations urinaires.
L'antibioprophylaxie s'administre indépendamment de l'ECBU (et de l'antibiothérapie curative éventuelle).

**ALLERGIES**

• Si Céfazoline → Gentamicine.

• Si Céfoxitine → Gentamicine + Métronidazole.

• Si Prothèse → Gentamicine + Clindamycine.

⚠️ **REMARQUES COMPLÉMENTAIRES**

• * Le GRADE 1 ou 2 s'applique au fait d'administrer une antibioprophylaxie pour les interventions concernées. Les schémas proposés sont en revanche de niveau de preuve « avis d'experts » du fait de l'absence de suffisamment de littérature homogène pour proposer un schéma avec un meilleur niveau de preuve.

• **Colonisation urinaire** : Ces recommandations ne statut pas sur l'intérêt du dépistage par ECBU et du traitement d'une colonisation urinaire avant chirurgie urologique. Ce sujet fera l'objet d'autres recommandations prochainement émises sous l'égide de l'Association Française d'Urologie (AFU).
""",

"Chirurgie Plastique, Reconstructrice & Esthétique": """
**ENJEUX**

Risque infectieux majeur pouvant compromettre le résultat esthétique ou la reconstruction.
Les gestes avec un temps vasculaire (microchirurgie) allongent la durée et l'exposition au risque.

**DURÉE**

La durée ne doit pas excéder celle du geste opératoire. Pas de bénéfice prouvé à prolonger, risque de résistance accru.

**ALLERGIES**

• Clindamycine ou Vancomycine ou Teicoplanine.

⚠️ **REMARQUES COMPLÉMENTAIRES**

• # **Pas d'indication à prolonger l'antibioprophylaxie au-delà de la fin de chirurgie** (GRADE 2) pour les chirurgies avec pose d'implant mammaire ou reconstruction mammaire.

• ** **Acide clavulanique** : En cas de chirurgie particulièrement longue et d'extension de la prophylaxie aux 48 premières heures postopératoires (chirurgie orthognatique), il convient de veiller à ne pas dépasser la dose maximale de **1200 mg/j d'acide clavulanique**.

• *** **Posologie postopératoire** : Proposée pour un patient de poids et fonction rénale standard → à moduler en fonction du poids et de la fonction rénale du patient.

• **Définitions** :
  - **Mastectomie** : Chirurgie non conservatrice, consistant à retirer la totalité du sein y compris l'aréole et le mamelon.
  - **Tumorectomie** : Chirurgie conservatrice, consistant à retirer la tumeur et une petite quantité des tissus environnants de façon à conserver la plus grande partie du sein.
""",


    "Chirurgie des Brûlés": """
**PRINCIPES GÉNÉRAUX**

RPP 2019 : Ne pas administrer d'ATB prophylactique ou préemptive à la phase aiguë en dehors d'un geste chirurgical.

**OBJECTIFS**

Prévenir les bactériémies postopératoires (1,6-60%) et les lyses infectieuses de greffes (4-7%).
Les infections de substituts dermiques atteignent 42%.

**FLORE BACTÉRIENNE**

• **<7 jours après brûlure** : Cocci à Gram positifs.

• **>7 jours** : Bacilles à Gram négatifs (entérobactéries, P. aeruginosa).

• **Long cours** : Dépend de l'écologie locale et de la flore du patient (en constante évolution).

**DURÉE**

Ne probablement pas excéder la durée de la chirurgie. Protocoles locaux indispensables pour encadrer l'autogreffe cutanée.

**BRÛLURES GRAVES (>20%)**

Augmentent le volume de distribution → risque de sous-dosage. Ne pas réduire la posologie, quelle que soit la fonction rénale.

**ALLERGIES**

• Clindamycine ou Vancomycine ou Teicoplanine.

⚠️ **REMARQUES COMPLÉMENTAIRES**

• **ATB curative en cours** : Prophylaxie supplémentaire non indiquée SAUF si l'ATB curative ne couvre pas les germes de la flore cutanée du patient.

• **Séquelles de brûlures** : La prise en charge des séquelles (brides, rétractions, reprises de cicatrices, expandeur, greffes de peau) et l'antibioprophylaxie relèvent du tableau de chirurgie plastique.

• **Autogreffe cutanée** : Considérer une antibioprophylaxie individuelle adaptée à la flore du site opératoire et au risque du patient en cas de parcours de soins prolongé, colonisation à germes multi-résistants, immunodépression sous-jacente, etc.
""",

"Chirurgie d'Affirmation de Genre": """
**ÉTAT DE LA LITTÉRATURE**

Aucune étude comparative disponible. Antibioprophylaxie administrée rarement décrite dans les études observationnelles.

**INCIDENCE DES ISO**

>5% dans les chirurgies à risque → Antibioprophylaxie justifiée.

**GERMES CIBLÉS**

Flore cutanée + digestive + urinaire.

**EXCEPTION**

Chondro-laryngoplastie : Chirurgie propre, faible taux d'ISO.

**ALLERGIES**

• Si Céfazoline → Clindamycine ou Vancomycine ou Teicoplanine.

• Si Amox/Clav → Gentamicine + Métronidazole.

⚠️ **REMARQUES COMPLÉMENTAIRES**

• * **Création de néo-vagin** : Poursuite de l'amoxicilline/clavulanate 1g/6h (si allergie : métronidazole 500mg/8h) chez la patiente de poids standard et de fonction rénale normale, jusqu'à ablation du conformateur vaginal.

• ** **Tobramycine per os (hors AMM)** : Utiliser flacons IV de 100 mg par voie orale pour décontamination digestive. Vérifier allergie aux sulfites. Entente préalable CPAM recommandée (~3€/flacon). Le métronidazole per os existe en boite de 4 cp de 500 mg (~1,31€).

• *** **Portage E-BLSE** : Dépistage dans le mois précédant la chirurgie si prévalence ≥10% (R1.7). Dépistage ciblé chez les patients avec antécédent de colonisation ou infection à E-BLSE dans les 6 derniers mois.

• **** **Chirurgie colorectale** : Le GRADE 1 s'applique au fait d'administrer une antibioprophylaxie ET au fait que cette antibioprophylaxie doit comporter à la fois une prise orale la veille au soir et une administration IV lors de l'intervention.
""",


    "Gynécologie & Obstétrique": """
**CLASSIFICATION ALTEMEIER**

• **Chirurgie propre (Classe 1)** : Chirurgie gynécologique sans ouverture du tractus génital (annexectomie par cœlioscopie, myomectomie).

• **Chirurgie propre-contaminée (Classe 2)** : Hystérectomie (ouverture vaginale), chirurgie de l'endométriose.

• **Chirurgie contaminée (Classe 3)** : Pathologie infectieuse (abcès tubo-ovarien).

**CÉSARIENNE**

• Taux d'ISO de 3 à 15% sans ATB.

• La Céfazoline est supérieure à l'Amoxicilline/Clavulanate (moins d'endométrites).

• **Injection AVANT incision cutanée** : Réduction significative des ISO vs injection après clampage.

• Obésité morbide : Céfazoline 3g recommandée (GRADE 1).

**ALLERGIES**

• Clindamycine 900mg ou Gentamicine 6-7mg/kg (± Métronidazole si besoin).

⚠️ **REMARQUES COMPLÉMENTAIRES**

• * **Chirurgie de l'endométriose profonde** : Pas de différence prouvée entre Amox/Clav et Céfazoline. En cas d'atteinte digestive, privilégier l'Amox/Clav ou Céfoxitine.

• ** **IVG chirurgicale** : Doxycycline per os recommandée (GRADE 1). Alternative : Métronidazole per os (dose unique).

• *** **Procédures de PMA** : Pas d'ATB systématique. En cas de ponction transvaginale à risque (endométriome), Doxycycline 200mg per os (dose unique).

• **** **Cerclage du col** : En l'absence de vaginose bactérienne, pas d'ATB recommandée.
""",

}
# =============================================================================
# 2. RECOMMANDATIONS GÉNÉRALES (SFAR 2024)
# =============================================================================
RFE_GENERALES = {
    "R1.1 - Délai d'administration": {
        "titre": "R1.1 - Délai d'administration",
        "question": "Quand faut-il administrer l'antibioprophylaxie pour diminuer l'incidence des infections du site opératoire ?",
        "reco": "Il est recommandé d'administrer l'antibioprophylaxie par céphalosporine (ou ses alternatives en cas d'allergie, hors vancomycine) au plus tôt 60 minutes avant et au plus tard avant l'incision chirurgicale ou le début de la procédure interventionnelle pour diminuer l'incidence d'infection du site opératoire.",
        "grade": "GRADE 1 (Accord FORT)",
        "argumentaire": "Seule une administration pré-incisionnelle garantit une concentration tissulaire efficace. Une administration post-incisionnelle augmente significativement le risque d'ISO. Le délai optimal est dans les 60 minutes précédant l'incision."
    },
    "R1.2 - Vancomycine": {
        "titre": "R1.2 - Cas de la Vancomycine",
        "question": "Quand faut-il administrer l'antibioprophylaxie pour diminuer l'incidence des infections du site opératoire ? (Spécifique Vancomycine)",
        "reco": "En cas d'utilisation de la vancomycine en antibioprophylaxie, les experts suggèrent d'en débuter l'administration intraveineuse sur 60 minutes chez le patient non obèse au plus tôt 60 minutes avant, et au plus tard 30 minutes avant l'incision chirurgicale ou le début de la procédure interventionnelle, pour diminuer l'incidence d'infection du site opératoire.",
        "grade": "Avis d'experts (Accord FORT)",
        "argumentaire": "La vancomycine nécessite une perfusion lente (1h) pour éviter le « Red Man Syndrome ». Débuter trop tôt (>1h avant) ou trop tard (fin de perfusion après incision) augmente le risque d'ISO. Le compromis idéal est de débuter la perfusion 1h avant l'incision."
    },
    "R1.3 - Réinjection peropératoire": {
        "titre": "R1.3 - Réinjection peropératoire",
        "question": "Faut-il réadministrer une ou plusieurs nouvelle(s) dose(s) d'antibioprophylaxie en cours de procédure (et si oui, quand ?) pour diminuer l'incidence des infections du site opératoire ?",
        "reco": """R1.3.1 : Il est recommandé de réadministrer une à plusieurs dose(s) peropératoire(s) d'antibioprophylaxie en cas de prolongation de la chirurgie ou de l'acte interventionnel pour diminuer l'incidence d'infection du site opératoire.

R1.3.2 : Il est probablement recommandé de réadministrer cette (ces) dose(s) peropératoire(s), à une posologie de la moitié de la dose initiale, toutes les deux demi-vies de l'antibiotique utilisé pour diminuer l'incidence d'infection du site opératoire; soit durant la période peropératoire :
• toutes les 2 heures pour la céfoxitine (1 g), le céfuroxime (0,75 g) et l'amoxicilline/clavulanate (1 g)
• toutes les 4 heures pour la céfazoline (1 g) et la clindamycine (450 mg)
• toutes les 8 heures pour la vancomycine (10 mg/kg).

Du fait de leur demi-vie très longue, la gentamicine, le métronidazole et la teicoplanine ne nécessitent pas de réinjection peropératoire.""",
        "grade": "GRADE 1 & GRADE 2 (Accord FORT)",
        "argumentaire": "La concentration d'antibiotique doit rester efficace jusqu'à la fermeture. L'absence de réinjection lors des chirurgies longues est associée à une hausse des ISO. La règle pharmacocinétique validée est de réinjecter une demi-dose toutes les deux demi-vies de la molécule."
    },
    "R1.4 - Durée de l'antibioprophylaxie": {
        "titre": "R1.4 - Durée totale",
        "question": "Combien de temps faut-il administrer l'antibioprophylaxie pour diminuer l'incidence des infections du site opératoire ?",
        "reco": "Il n'est pas recommandé, dans la très grande majorité des cas (et hors exceptions mentionnées dans chaque tableau), de prolonger l'administration de l'antibioprophylaxie au-delà de la fin de la chirurgie pour diminuer l'incidence d'infection du site opératoire.",
        "grade": "GRADE 1 (Accord FORT)",
        "argumentaire": "La littérature (nombreuses méta-analyses récentes) montre qu'une dose unique préopératoire est aussi efficace qu'une antibioprophylaxie prolongée (24-48h) pour prévenir les ISO, tout en réduisant le risque d'effets secondaires et de sélection de bactéries résistantes."
    },
    "R1.5 - Patient Obèse (Céphalosporines)": {
        "titre": "R1.5 - Obésité & Céphalosporines",
        "question": "Faut-il modifier les modalités de l'antibioprophylaxie chez le patient obèse pour diminuer l'incidence des infections du site opératoire ?",
        "reco": "Il n'est probablement pas recommandé d'augmenter la dose unitaire de céphalosporine utilisée en antibioprophylaxie chez le patient obèse pour diminuer l'incidence d'ISO, en dehors de cas particuliers (IMC supérieur à 50 kg/m²).",
        "grade": "GRADE 2 (Accord FORT)",
        "argumentaire": "Les céphalosporines sont hydrophiles et diffusent peu dans la graisse. Leur volume de distribution n'augmente pas proportionnellement au poids. Les doses standards (ex: 2g Céfazoline) permettent d'atteindre les cibles thérapeutiques chez l'obèse (IMC < 50). Augmenter la dose n'apporte pas de bénéfice prouvé."
    },
    "R1.6 - Obésité (Autres molécules)": {
        "titre": "R1.6 - Obésité (Autres molécules)",
        "question": "Adaptation des alternatives (Clindamycine, Gentamicine, Vancomycine) chez le patient obèse.",
        "reco": """Pour les molécules utilisées en alternatives aux bêtalactamines en cas d'allergie, les experts suggèrent d'utiliser les doses suivantes chez le patient obèse pour diminuer l'incidence d'ISO :
• Clindamycine : 900 mg pour des IMC entre 30 et 45 kg/m² ; 1200 mg pour des IMC entre 45 et 60 kg/m² ; 1600 mg pour des IMC > 60 kg/m²
• Gentamicine : 6 à 7 mg/kg de poids ajusté
• Vancomycine : 20 mg/kg de poids total (comme chez le non-obèse).

Du fait de l'absence de donnée dans cette population, la teicoplanine n'est pas recommandée chez le patient obèse.""",
        "grade": "Avis d'experts (Accord FORT)",
        "argumentaire": "Contrairement aux céphalosporines, la Clindamycine est lipophile et nécessite une augmentation de dose proportionnelle à l'IMC. La Gentamicine se dose sur le poids ajusté. La Vancomycine se dose sur le poids total, mais attention à ne pas dépasser 3-4g et à perfuser lentement."
    },
    "R1.7 - Colonisation E-BLSE": {
        "titre": "R1.7 - Patient porteur d'E-BLSE",
        "question": "Faut-il modifier l'antibioprophylaxie chez le patient colonisé au niveau rectal à entérobactérie productrice de bêta-lactamase à spectre étendu (E-BLSE) pour diminuer l'incidence des infections du site opératoire ?",
        "reco": """R1.7.1 : Dans les centres où la prévalence de colonisation digestive à E-BLSE des patients devant être opérés de chirurgie colorectale est supérieure ou égale à 10%, les experts suggèrent de réaliser un dépistage [...] dans le mois précédant la chirurgie.

R1.7.2 : En cas de positivité du dépistage [...], les experts suggèrent d'administrer, pour une chirurgie colo-rectale, une antibioprophylaxie ciblée active sur la souche d'E-BLSE identifiée [...].

R1.7.3 : [...] les experts suggèrent une prise en charge multidisciplinaire [...] pour individualiser l'antibioprophylaxie des patients colonisés au niveau rectal à E-BLSE.""",
        "grade": "Avis d'experts (Accord FORT)",
        "argumentaire": "Le portage d'E-BLSE augmente le risque d'ISO à E-BLSE, surtout en chirurgie colorectale. Une prophylaxie ciblée (ex: Ertapénème) réduit ce risque si la prévalence locale est élevée."
    }
}

# =============================================================================
# 3. BASE DE DONNÉES CLINIQUES COMPLÈTE
# =============================================================================
SFAR_DATA = {
    "Neurochirurgie & Neuroradiologie": {
        "Craniotomie": {
            "Craniotomie": {"molecule": "Céfazoline", "dose": "2g IVL", "reinjection": "1g / 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900mg IVL"},
            "Ventriculoscopie, visiochirurgie intracrânienne": {"molecule": "Céfazoline", "dose": "2g IVL", "reinjection": "1g / 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg IVL"},
            "Biopsie cérébrale": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"}
        },
        "Chirurgie intracrânienne par voie trans-sphénoïdale ou trans-labyrinthique": {
            "Neurochirurgie par voie trans-sphénoïdale ou trans-labyrinthique": {"molecule": "Céfazoline", "dose": "2g IVL", "reinjection": "1g / 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg IVL"}
        },
        "Dérivation ventriculaire externe": {
            "Dérivation ventriculaire externe (DVE)": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
            "Dérivation lombaire externe (DLE)": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"}
        },
        "Dérivation ventriculaire interne": {
            "Dérivation ventriculo-péritonéale (DVP)": {"molecule": "Céfazoline", "dose": "2g IVL", "reinjection": "1g / 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg IVL"},
            "Dérivation ventriculo-atriale (DVA)": {"molecule": "Céfazoline", "dose": "2g IVL", "reinjection": "1g / 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg IVL"}
        },
        "Plaies cranio-cérébrales et fracture de la base du crâne": {
            "Plaies cranio-cérébrales pénétrantes ou non": {
                "molecule": "Amoxicilline/Clavulanate", 
                "dose": "2g IVL", 
                "reinjection": "1g / 2h", 
                "grade": "Avis d'experts", 
                "allergie": "Triméthoprime/Sulfaméthoxazole (Bactrim) 160/800mg IVL",
                "remarque": "* Possibilité d’étendre l’antibioprophylaxie pour 24h à 48h postopératoires maximum en cas de constatation opératoire d’une plaie souillée (Avis d’experts)"
            },
            "Fracture de la base du crâne avec ou sans otorrhée": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"}
        },
        "Chirurgie du rachis": {
            "Chirurgie instrumentée du rachis avec mise en place de matériel en 1 temps": {"molecule": "Céfazoline", "dose": "2g IVL", "reinjection": "1g / 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900mg IVL"},
            "Chirurgie instrumentée du rachis avec pose de matériel en 2 temps": {
                "molecule": "Céfazoline", 
                "dose": "2g IVL", 
                "reinjection": "1g / 4h", 
                "grade": "Avis d'experts", 
                "allergie": "Clindamycine 900mg IVL",
                "remarque": "** Une épidémiologie locale particulière peut justifier le recours à une molécule alternative, dans le cadre d'un protocole validé localement"
            },
            "Reprise du matériel quel que soit le délai": {
                "molecule": "Céfazoline", 
                "dose": "2g IVL", 
                "reinjection": "1g / 4h", 
                "grade": "Avis d'experts", 
                "allergie": "Clindamycine 900mg IVL",
                "remarque": "** Une épidémiologie locale particulière peut justifier le recours à une molécule alternative, dans le cadre d'un protocole validé localement"
            },
            "Chirurgie du rachis percutanée avec pose de matériel": {"molecule": "Céfazoline", "dose": "2g IVL", "reinjection": "1g / 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg IVL"},
            "Chirurgie du rachis sans mise en place de matériel": {
                "molecule": "PAS D'ANTIBIOPROPHYLAXIE", 
                "dose": "N/A", 
                "reinjection": "N/A", 
                "grade": "Avis d'experts", 
                "allergie": "N/A",
                "remarque": "En cas d’ablation de matériel ou de chirurgie sans pose de matériel exposant à une ouverture de la dure-mère, ou de geste difficile/long, une antibioprophylaxie par céfazoline peut être discutée au cas par cas"
            },
            "Ablation de matériel du rachis": {
                "molecule": "PAS D'ANTIBIOPROPHYLAXIE", 
                "dose": "N/A", 
                "reinjection": "N/A", 
                "grade": "Avis d'experts", 
                "allergie": "N/A",
                "remarque": "En cas d’ablation de matériel ou de chirurgie sans pose de matériel exposant à une ouverture de la dure-mère, ou de geste difficile/long, une antibioprophylaxie par céfazoline peut être discutée au cas par cas"
            }
        },
        "Électrode de stimulation cérébrale ou médullaire et pose de stimulateur": {
            "Pose de pompe à destination médullaire": {"molecule": "Céfazoline", "dose": "2g IVL", "reinjection": "1g / 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg IVL"},
            "Pose d'électrode de stimulation cérébrale ou médullaire": {"molecule": "Céfazoline", "dose": "2g IVL", "reinjection": "1g / 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg IVL"},
            "Pose de stimulateur": {"molecule": "Céfazoline", "dose": "2g IVL", "reinjection": "1g / 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg IVL"}
        },
        "Neuroradiologie interventionnelle": {
            "Angiographie des artères cervicales et cérébrales": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
            "Endoprothèse / Stent / Angioplastie": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
            "Embolisation d'anévrysme, de malformation artério-veineuse cérébrale et spinale": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
            "Thermo-coagulation percutanée du nerf trijumeau": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"}
        }
    },
    "ORL (Oto-Rhino-Laryngologie)": {
    "Chirurgie rhino-sinusienne": {
        "Chirurgie sinusienne de polypose ou sinusite chronique (méatotomie, éthmoïdectomie...)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Chirurgie rhinologique sans mise en place de greffon": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Chirurgie rhinologique avec mise en place d'un greffon ou reprise chirurgicale": {
            "molecule": "Céfazoline (Alternative: Amox/Clav)",
            "dose": "2g IVL",
            "reinjection": "Cefaz: 4h / Amox: 2h",
            "grade": "GRADE 2",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Chirurgie sinusienne tumorale": {
            "molecule": "Céfazoline (Alternative: Amox/Clav)",
            "dose": "2g IVL",
            "reinjection": "Cefaz: 4h / Amox: 2h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        }
    },
    
    "Chirurgie carcinologique cervico-faciale": {
        "Chirurgie carcinologique avec lambeau libre ou pédiculé cervico-facial": {
            "molecule": "Amoxicilline/Clavulanate",
            "dose": "2g IVL",
            "reinjection": "1g / 2h (puis post-op 48h max)",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg IVL",
            "remarque": "* Ne pas dépasser 1200 mg/j d'acide clavulanique si prolongation à 48h. ** Posologie postopératoire à moduler selon poids et fonction rénale"
        },
        "Chirurgie carcinologique sans reconstruction (laryngectomie, pharyngo-laryngectomie...)": {
            "molecule": "Amoxicilline/Clavulanate",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg IVL",
            "remarque": "* Ne pas dépasser 1200 mg/j d'acide clavulanique en cas de prolongation"
        }
    },
    
    "Chirurgie du cou et de la thyroïde": {
        "Cervicotomie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 1",
            "allergie": "N/A"
        },
        "Curage cervical": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Thyroïdectomie totale": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Thyroïdectomie partielle": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Parathyroïdectomie": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Trachéotomie chirurgicale": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Trachéotomie percutanée": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Chirurgie amygdalienne et adénoïdectomie": {
        "Amygdalectomie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 1",
            "allergie": "N/A"
        },
        "Adénoïdectomie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Chirurgie des glandes salivaires": {
        "Chirurgie des glandes salivaires sans accès par la cavité bucco-pharyngée": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Chirurgie des glandes salivaires avec accès par la cavité bucco-pharyngée": {
            "molecule": "Amoxicilline/Clavulanate",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg IVL"
        }
    },
    
    "Laryngoscopie en suspension": {
        "Laryngoscopie en suspension diagnostique sans ou avec biopsies": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Laryngoscopie en suspension avec geste thérapeutique (laser, cordectomie, etc.)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Chirurgie otologique": {
        "Chirurgie des tympans (tympanoplastie, myringoplastie, tympanotomie exploratrice...)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Chirurgie de la chaine ossiculaire, stapédectomie, ossiculoplastie, otospongiose": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Chirurgie de cholestéatome (non infecté)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Implants cochléaires": {
            "molecule": "Céfazoline (Alternative: Amox/Clav)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h (Cef) / > 2h (Amox)",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        }
    }
},

    "Stomatologie & Chirurgie Maxillo-Faciale": {
    "Chirurgie orthognatique": {
        "Chirurgie orthognatique": {
            "molecule": "Céfazoline (Alternative: Amox/Clav)",
            "dose": "2g IVL",
            "reinjection": "Cefaz: 4h / Amox: 2h (puis 1g/6h post-op 48h max)",
            "grade": "GRADE 2",
            "allergie": "Clindamycine 900mg IVL",
            "remarque": "* Posologie postopératoire à moduler selon poids et fonction rénale. ** Ne pas dépasser 1200 mg/j d'acide clavulanique si prolongation à 48h"
        },
        "Ablation de matériel": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Chirurgie alvéolo-dentaire": {
        "Extractions de dents incluses, ectopiques ou en désinclusion": {
            "molecule": "Amoxicilline",
            "dose": "2g IVL (Alternative: 2g per os 1-2h avant)",
            "reinjection": "1g si durée > 2h",
            "grade": "GRADE 1",
            "allergie": "Clindamycine 900mg IVL",
            "remarque": "*** En ambulatoire : possibilité d'administration orale 60-120 min avant l'intervention (biodisponibilité 70%, Tmax 1h). Limiter l'apport hydrique pour respecter le jeûne"
        },
        "Autres extractions dentaires (dents sur arcade, etc.)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 1",
            "allergie": "N/A"
        },
        "Pose de matériel d'ancrage orthodontique": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Chirurgie apicale": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Chirurgie alvéolaire (greffe osseuse, sinus lift, etc.)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Traumatologie maxillo-faciale": {
        "Traumatologie maxillo-faciale (fractures mandibule, Lefort, zygoma...)": {
            "molecule": "Amoxicilline/Clavulanate (Alternative: Céfazoline)",
            "dose": "2g IVL",
            "reinjection": "Amox: 2h / Cefaz: 4h (puis 1g/6h post-op 24h max)",
            "grade": "GRADE 2",
            "allergie": "Clindamycine 900mg IVL",
            "remarque": "* Posologie postopératoire à moduler selon poids et fonction rénale. ** Ne pas dépasser 1200 mg/j d'acide clavulanique"
        }
    }
},

    "Ophtalmologie": {
    "Chirurgie du globe oculaire": {
        "Chirurgie de la cataracte (simple ou combinée)": {
            "molecule": "Céfuroxime (Injection intra-camérulaire)",
            "dose": "1 mg dans 0.1 mL",
            "reinjection": "Dose unique en fin d'intervention",
            "grade": "GRADE 1",
            "allergie": "Moxifloxacine intra-camérulaire (0.480 mg / 0.3 mL) [Avis d'experts]",
            "remarque": "* Chirurgies de la cornée, du glaucome, de la rétine et du vitré effectuées dans le même temps opératoire qu'une chirurgie de cataracte suivent le même protocole"
        },
        "Chirurgies de la cornée, du glaucome, de la rétine et du vitré": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "Remarque : Si combiné à une cataracte, voir protocole Cataracte."
        },
        "Traumatismes à globe ouvert": {
            "molecule": "Vancomycine + Ceftazidime (Injection intra-vitréenne)",
            "dose": "Vanco 1 mg + Ceftaz 2.25 mg (IVT)",
            "reinjection": "Dose unique en fin d'intervention",
            "grade": "Avis d'experts",
            "allergie": "Si allergie Ceftazidime : Remplacer par Amikacine 0.2 mg (IVT).",
            "remarque": "** Pas d'indication à associer une antibiothérapie par voie systémique"
        }
    },
    
    "Chirurgie péri-oculaire": {
        "Chirurgies des paupières, des voies lacrymales, du strabisme ou de l'orbite": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 1",
            "allergie": "N/A"
        }
    }
},

    "Chirurgie Thoracique & Pneumologie": {
    "Chirurgie d'exérèse pulmonaire (par thoracotomie ou cervico-thoracotomie...)": {
        "Pneumonectomies ou lobectomies pulmonaires / Pleuro-pneumonectomies": {
            "molecule": "Choix 1 : Amox-Clav (Si BPCO) / Choix 2 : Céfazoline",
            "dose": "2g (Amox) / 2g (Cefaz)",
            "reinjection": "Amox: 1g/2h | Cefaz: 1g/4h",
            "grade": "GRADE 1 (GRADE 2 pour Amox/Clav si BPCO)",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL.",
            "remarque": "* Pour la prévention des PPO chez les patients BPCO : privilégier Amoxicilline/Clavulanate et possibilité de prolongation jusqu'à 48h post-opératoires maximum"
        },
        "Exérèses partielles non anatomiques simples ou multiples du poumon, par thoracotomie": {
            "molecule": "Choix 1 : Amox-Clav (Si BPCO) / Choix 2 : Céfazoline",
            "dose": "2g (Amox) / 2g (Cefaz)",
            "reinjection": "Amox: 1g/2h | Cefaz: 1g/4h",
            "grade": "GRADE 1",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Segmentectomie pulmonaire unique ou multiple, par thoracotomie": {
            "molecule": "Choix 1 : Amox-Clav (Si BPCO) / Choix 2 : Céfazoline",
            "dose": "2g (Amox) / 2g (Cefaz)",
            "reinjection": "Amox: 1g/2h | Cefaz: 1g/4h",
            "grade": "GRADE 1",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Réduction uni- ou bilatérale de volume pulmonaire": {
            "molecule": "Choix 1 : Amox-Clav (Si BPCO) / Choix 2 : Céfazoline",
            "dose": "2g (Amox) / 2g (Cefaz)",
            "reinjection": "Amox: 1g/2h | Cefaz: 1g/4h",
            "grade": "GRADE 1",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Résection de bulle d'emphysème pulmonaire": {
            "molecule": "Choix 1 : Amox-Clav (Si BPCO) / Choix 2 : Céfazoline",
            "dose": "2g (Amox) / 2g (Cefaz)",
            "reinjection": "Amox: 1g/2h | Cefaz: 1g/4h",
            "grade": "GRADE 1",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Exérèse de kyste hydatique du poumon, par thoracotomie": {
            "molecule": "Choix 1 : Amoxicilline/Clavulanate\nOU Choix 2 : Céfazoline",
            "dose": "2g (Amox) / 2g (Cefaz)",
            "reinjection": "Amox: 1g/2h | Cefaz: 1g/4h",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        }
    },
    
    "Chirurgies médiastinales, pleurales, pariétales (y compris voies thoracoscopiques...)": {
        "Chirurgie du médiastin": {
            "molecule": "Céfazoline (Alternative : Céfuroxime)",
            "dose": "2g IVL (ou 1.5g IVL)",
            "reinjection": "1g si > 4h (Cefaz) / 0.75g si > 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Chirurgie du pneumothorax": {
            "molecule": "Céfazoline (Alternative : Céfuroxime)",
            "dose": "2g IVL (ou 1.5g IVL)",
            "reinjection": "1g si > 4h (Cefaz) / 0.75g si > 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Chirurgie de la plèvre (patient non infecté)": {
            "molecule": "Céfazoline (Alternative : Céfuroxime)",
            "dose": "2g IVL (ou 1.5g IVL)",
            "reinjection": "1g si > 4h (Cefaz) / 0.75g si > 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Chirurgie de paroi thoracique (avec ou sans pose de matériel)": {
            "molecule": "Céfazoline (Alternative : Céfuroxime)",
            "dose": "2g IVL (ou 1.5g IVL)",
            "reinjection": "1g si > 4h (Cefaz) / 0.75g si > 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Médiastinoscopie, avec ou sans biopsie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Thoracoscopie/pleuroscopie, avec ou sans biopsie, avec ou sans abrasion ou talcage": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Drainage thoracique, tunellisé ou non": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Chirurgie des voies aériennes sous-glottiques": {
        "Trachéotomie chirurgicale": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g si durée > 4h",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Suture ou résection-anastomose de bronche, par cervicotomie...": {
            "molecule": "Céfazoline (Alternative: Amox-Clav)",
            "dose": "2g IVL",
            "reinjection": "Cefaz: 4h | Amox: 2h",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Plastie ou fermeture d'orifice de trachéostomie ou de trachéotomie": {
            "molecule": "Céfazoline (Alternative: Amox-Clav)",
            "dose": "2g IVL",
            "reinjection": "Cefaz: 4h | Amox: 2h",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Tuteur trachéal, par cervicotomie": {
            "molecule": "Céfazoline (Alternative: Amox-Clav)",
            "dose": "2g IVL",
            "reinjection": "Cefaz: 4h | Amox: 2h",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Fermeture de plaie ou fistule bronchique, par thoracotomie": {
            "molecule": "Céfazoline (Alternative: Amox-Clav)",
            "dose": "2g IVL",
            "reinjection": "Cefaz: 4h | Amox: 2h",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Plastie de trachée par autogreffe ou lambeau, par cervico- et/ou thoracotomie": {
            "molecule": "Céfazoline (Alternative: Amox-Clav)",
            "dose": "2g IVL",
            "reinjection": "Cefaz: 4h | Amox: 2h",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Remplacement de trachée par prothèse, par cervico- et/ou thoracotomie": {
            "molecule": "Céfazoline (Alternative: Amox-Clav)",
            "dose": "2g IVL",
            "reinjection": "Cefaz: 4h | Amox: 2h",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Résection-anastomose thyro- ou crico-trachéale par cervicotomie": {
            "molecule": "Céfazoline (Alternative: Amox-Clav)",
            "dose": "2g IVL",
            "reinjection": "Cefaz: 4h | Amox: 2h",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Résection-anastomose de trachée ou de la bifurcation trachéale par cervico- et/ou thoracotomie": {
            "molecule": "Céfazoline (Alternative: Amox-Clav)",
            "dose": "2g IVL",
            "reinjection": "Cefaz: 4h | Amox: 2h",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Résection-anastomose de trachée pour sténose congénitale de la trachée, par thoracotomie": {
            "molecule": "Céfazoline (Alternative: Amox-Clav)",
            "dose": "2g IVL",
            "reinjection": "Cefaz: 4h | Amox: 2h",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Clindamycine 900mg + Gentamicine 6-7mg/kg IVL."
        },
        "Trachéotomie percutanée": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Chirurgie œsophagienne (avec ou sans plastie colique)": {
        "Œsophagectomie / Excision de tumeur de l'œsophage / Traitement d'un diverticule": {
            "molecule": "Céfazoline (Alternative : Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si durée > 4h (Cefaz) / 0.75g si > 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Si allergie vraie : Vancomycine 20mg/kg ou Teicoplanine 12mg/kg."
        }
    },
    
    "Radiologie interventionnelle des voies respiratoires ou du poumon": {
        "Destruction d'une ou plusieurs tumeurs bronchopulmonaires par radiofréquence...": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Ponctions, cytoponctions ou biopsies pulmonaires par voie transcutanée...": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Évacuation ou drainages d'une ou plusieurs collections broncho-pulmonaires...": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Injection d'agent pharmacologique intrabronchique ou intrapulmonaire...": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Fibroscopie ou écho-endoscopie diagnostique (LBA, EBUS...)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Pose de prothèse endo-bronchique, trachéale ou mise en place de valves unidirectionnelle": {
        "Valves Zéphyr pour emphysème pulmonaire sévère": {
            "molecule": "Amoxicilline/Clavulanate (Alternative: Pristinamycine)",
            "dose": "1g IVL (Amox) / 1g per os (Pristina)",
            "reinjection": "N/A - Poursuivre 48h per os",
            "grade": "Avis d'experts",
            "allergie": "Si allergie : Pristinamycine."
        },
        "Prothèse trachéo-bronchique": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Endoscopie thérapeutique : dilatation, laser": {
        "Bronchoscopie rigide, désobstruction": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Destruction de lésion par laser, cryothérapie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Dilatation ou résection de sténose avec ou sans laser": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Transplantation mono ou bipulmonaire": {
        "Transplantation avec ou sans circulation extra-corporelle": {
            "molecule": "Pas de recommandation consensuelle",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "Protocole local / Discussion pluridisciplinaire",
            "remarque": "Établir un protocole local selon l'écologie du centre et les antécédents du patient. Discussion pluridisciplinaire recommandée pour personnaliser l'antibioprophylaxie"
        }
    }
},

    "Cardiaque & Vasculaire": {
    "Chirurgie cardiaque": {
        "Actes thérapeutiques des parois, des cavités et des valves du cœur, de l'aorte ascendante et de la crosse aortique avec ou sans CEC": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h (+ 1g lors du priming si CEC)",
            "grade": "GRADE 1",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg",
            "remarque": "Décolonisation nasale (Mupirocine 2%) + bains de bouche (Chlorhexidine) recommandés 48h avant, pour une durée totale de 5-7 jours"
        },
        "Drainage péricardique par thoracotomie ou sternotomie": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Fenêtre pleuro-péricardique ou péritonéo-péricardique": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Hémostase postopératoire de chirurgie cardiaque par sternotomie ou thoracotomie": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        }
    },
    
    "Transplantation cardiaque et assistance circulatoire de longue durée": {
        "Transplantation cardiaque sans assistance mécanique préalable": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Assistance circulatoire gauche (LVAD) ou cœur artificiel, sans contexte de réanimation": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Transplantation cardiaque avec assistance mécanique ou ECMO": {
            "molecule": "Discussion pluridisciplinaire",
            "dose": "Selon avis infectiologique",
            "reinjection": "Selon avis infectiologique",
            "grade": "Avis d'experts",
            "allergie": "Selon avis infectiologique",
            "remarque": "Modalités à discuter individuellement après avis infectiologique spécialisé, tenant compte des antécédents infectieux et de la colonisation à SARM ou E-BLSE"
        },
        "Assistance circulatoire (LVAD, cœur artificiel) avec contexte de réanimation": {
            "molecule": "Discussion pluridisciplinaire",
            "dose": "Selon avis infectiologique",
            "reinjection": "Selon avis infectiologique",
            "grade": "Avis d'experts",
            "allergie": "Selon avis infectiologique",
            "remarque": "Modalités à discuter individuellement après avis infectiologique spécialisé, tenant compte des antécédents infectieux et de la colonisation à SARM ou E-BLSE"
        }
    },
    
    "Assistance circulatoire de courte durée": {
        "Assistance de courte durée avec mise en place percutanée sans abord chirurgical (ECMO, Impella, CPIA, etc.)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Assistance de courte durée avec abord chirurgical (ECMO, Impella, etc.)": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        }
    },
    
    "Cardiologie structurelle": {
        "Bioprothèse de la valve aortique par voie artérielle transcutanée (TAVI)": {
            "molecule": "Amoxicilline/Clavulanate (Alternative: Céfazoline + Amoxicilline)",
            "dose": "2g IVL",
            "reinjection": "1g si > 2h (Amox) / 4h (Cefaz)",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Fermeture d'auricule par voie percutanée avec implantation de matériel": {
            "molecule": "Amoxicilline/Clavulanate (Alternative: Céfazoline + Amoxicilline)",
            "dose": "2g IVL",
            "reinjection": "1g si > 2h (Amox) / 4h (Cefaz)",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Rétrécissement de l'orifice atrioventriculaire gauche (MitraClip)": {
            "molecule": "Amoxicilline/Clavulanate (Alternative: Céfazoline + Amoxicilline)",
            "dose": "2g IVL",
            "reinjection": "1g si > 2h (Amox) / 4h (Cefaz)",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Fermeture de communication interatriale ou de foramen ovale perméable": {
            "molecule": "Amoxicilline/Clavulanate (Alternative: Céfazoline + Amoxicilline)",
            "dose": "2g IVL",
            "reinjection": "1g si > 2h (Amox) / 4h (Cefaz)",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        }
    },
    
    "Rythmologie interventionnelle": {
        "Ablation de fibrillation atriale ou autre trouble du rythme": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Pose de stimulateur cardiaque ou défibrillateur implantable": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "GRADE 1",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Changement de boitier de stimulateur ou défibrillateur": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "GRADE 2",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Extraction de sonde de stimulateur ou défibrillateur": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        }
    },
    
    "Chirurgie vasculaire": {
        "Pontage aorto-bifémoral ou aorto-bi-iliaque": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "GRADE 1",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Pontage fémoro-fémoral croisé": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "GRADE 1",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Pontage fémoro-poplité ou fémoro-distal": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "GRADE 1",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Endartériectomie carotidienne": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "GRADE 2",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Anévrisme de l'aorte abdominale (chirurgie ouverte)": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "GRADE 1",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Création ou révision de fistule artério-veineuse": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        }
    },
    
    "Radiologie vasculaire": {
        "Endoprothèse aortique (EVAR) ou thoracique (TEVAR)": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g si > 4h",
            "grade": "GRADE 2",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Angioplastie avec ou sans stent (carotide, membres inférieurs, etc.)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Embolisation artérielle": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    }
},

    "Orthopédie & Traumato": {
    "Chirurgie du membre inférieur": {
        "Prothèse de hanche ou de genou (dont reprise précoce non septique)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL (ou Vancomycine/Teicoplanine si hanche par voie antérieure)"
        },
        "Gestes osseux avec mise en place de matériel (clou, vis, plaque, etc.), ostéotomie, arthrodèse": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Reconstruction ligamentaire avec utilisation de matériel (vis d'interférence, etc.)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Arthroscopie avec mise en place de matériel": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Plastie ligamentaire (retente, suture, etc.) sans utilisation de matériel": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Arthroscopie diagnostique ou thérapeutique sans mise en place de matériel": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Ablation de matériel d'ostéosynthèse": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A",
            "remarque": "** L'échec d'ablation ne constitue PAS une indication d'ATB. En cas d'ablation nécessitant une ouverture articulaire ou de geste difficile/long, une antibioprophylaxie par céfazoline peut être discutée au cas par cas"
        },
        "Chirurgie des parties molles": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Résection osseuse (sans ostéosynthèse ni remplacement prothétique)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Chirurgie de l'épaule et du coude": {
        "Chirurgie prothétique quelle que soit l'articulation": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL (Préférer Vancomycine/Teicoplanine pour épaule)",
            "remarque": "* En cas de chirurgie prothétique d'épaule et d'allergie aux bêtalactamines : préférer la vancomycine ou la teicoplanine à la clindamycine (résistance de Cutibacterium acnes 15-20%)"
        },
        "Reprise non septique prothétique précoce ou tardive": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL (Préférer Vancomycine/Teicoplanine pour épaule)"
        },
        "Chirurgie de luxation récidivante avec ou sans greffe osseuse": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL (Préférer Vancomycine/Teicoplanine pour épaule)"
        },
        "Geste osseux avec mise en place de matériel, ostéotomie, arthrodèse": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Arthrolyse par arthrotomie": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Arthroscopie avec mise en place de matériel": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Arthroscopie diagnostique ou thérapeutique sans mise en place de matériel": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Ablation de matériel d'ostéosynthèse (épaule/coude)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A",
            "remarque": "** En cas d'ablation nécessitant une ouverture articulaire ou de geste difficile/long, une antibioprophylaxie par céfazoline peut être discutée"
        },
        "Gestes osseux sans mise en place de matériel (résection)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Chirurgie des parties molles (épaule/coude)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Chirurgie de la main": {
        "Chirurgie prothétique ou osseuse avec mise en place de matériel": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Chirurgie des parties molles (main)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Ablation de matériel d'ostéosynthèse (main)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Chirurgie articulaire non prothétique": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Ablation de kyste": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Chirurgie du rachis": {
        "Chirurgie instrumentée du rachis avec pose de matériel en 1 temps": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "GRADE 2",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Chirurgie instrumentée du rachis avec pose de matériel en 2 temps": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL",
            "remarque": "*** Une épidémiologie locale particulière peut justifier le recours à une molécule alternative, dans le cadre d'un protocole validé localement"
        },
        "Reprise du matériel quel que soit le délai": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL",
            "remarque": "*** Une épidémiologie locale particulière peut justifier le recours à une molécule alternative"
        },
        "Chirurgie du rachis percutanée avec pose de matériel": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Chirurgie sans pose de matériel": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A",
            "remarque": "En cas d'ablation de matériel ou de chirurgie sans pose de matériel exposant à une ouverture de la dure-mère, ou de geste difficile/long, une antibioprophylaxie par céfazoline peut être discutée au cas par cas"
        },
        "Ablation de matériel (rachis)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A",
            "remarque": "En cas d'ablation exposant à une ouverture de la dure-mère, ou de geste difficile/long, une antibioprophylaxie par céfazoline peut être discutée au cas par cas"
        }
    },
    
    "Fractures fermées": {
        "Ostéosynthèse par fixateur externe": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Ostéosynthèse par brochage percutané": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Ostéosynthèse à foyer ouvert (tout type de matériel) ou enclouage": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        }
    },
    
    "Fractures ouvertes (hors main)": {
        "Fracture ouverte Gustilo 1, quel que soit le matériel mis en place": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg IVL"
        },
        "Fracture ouverte Gustilo 2 ou 3, quel que soit le matériel mis en place": {
            "molecule": "Amoxicilline/Clavulanate (Alternative: Céfazoline + Gentamicine)",
            "dose": "2g IVL",
            "reinjection": "Amox: 1g/2h | Cefaz: 1g/4h + Genta dose unique",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg IVL",
            "remarque": "En cas de contamination majeure (fécale/tellurique) et délai prolongé, considérer après avis infectiologique comme Altemeier 3-4 justifiant une antibiothérapie curative au-delà du bloc"
        }
    },
    
    "Plaie des parties molles (hors main)": {
        "Plaie des parties molles susceptible d'être contaminée par des germes tellurique/fécal": {
            "molecule": "Amoxicilline/Clavulanate",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "GRADE 1",
            "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg IVL"
        },
        "Autre plaie des parties molles": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Plaie articulaire (quel que soit le degré de contamination)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "GRADE 1",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Morsure": {
            "molecule": "Amoxicilline/Clavulanate",
            "dose": "2g IVL",
            "reinjection": "1g / 2h (puis 5 jours postop)",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg IVL",
            "remarque": "** Les morsures sont des plaies avec contamination polymicrobienne qui relèvent d'une antibiothérapie curative (5 jours postop avec réévaluation chirurgicale et infectiologique)"
        }
    },
    
    "Traumatisme de la main": {
        "Ostéosynthèse de fracture(s) fermée(s) par fixateur externe": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Ostéosynthèse de fracture(s) fermée(s) par brochage percutané": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Ostéosynthèse de fracture(s) fermée(s) à foyer ouvert (tout type de matériel)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Fracture ouverte (quelle que soit la technique d'ostéosynthèse)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg IVL"
        },
        "Plaie de la main non susceptible d'être contaminée par des germes tellurique/fécal": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 1",
            "allergie": "N/A"
        },
        "Plaie de la main susceptible d'être contaminée par des germes tellurique/fécal": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Traumatisme de la dernière phalange": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Traumatisme complexe de la main (replantation, écrasement, injection sous pression, etc.)": {
            "molecule": "Amoxicilline/Clavulanate (Alternative: Céfazoline + Gentamicine)",
            "dose": "2g IVL",
            "reinjection": "Amox: 1g/2h | Cefaz: 1g/4h + Genta dose unique",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg IVL"
        }
    }
},

    "Chirurgie Digestive": {
    "Chirurgie œsophagienne": {
        "Œsophagectomie / Excision de tumeur / Traitement d'un diverticule": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        }
    },
    
    "Chirurgie gastrique non bariatrique": {
        "Gastrectomie totale, totalisation de gastrectomie": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Gastrectomie partielle": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        }
    },
    
    "Chirurgie bariatrique": {
        "Mise en place d'un anneau gastrique": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg",
            "remarque": "* Jusqu'à IMC ≤ 50 kg/m² (R1.5). Au-delà, discuter : dose 4g, raccourcissement intervalle réinjection, ou perfusion continue. ** Céfuroxime non recommandé (absence d'étude)"
        },
        "Court-circuit gastrique ou sleeve gastrectomie": {
            "molecule": "Céfoxitine",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g IVL",
            "remarque": "* Jusqu'à IMC ≤ 50 kg/m². Au-delà, adapter la posologie"
        }
    },
    
    "Chirurgie de l'intestin grêle": {
        "Résection de l'intestin grêle": {
            "molecule": "Céfoxitine",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g IVL"
        },
        "Entérostomie cutanée, par laparotomie": {
            "molecule": "Céfoxitine",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g IVL"
        }
    },
    
    "Chirurgie colorectale et appendiculaire": {
        "Colectomie / Proctectomie / Rétablissement de continuité": {
            "molecule": "La veille : Tobramycine 200mg + Métronidazole 1g (per os) | Lors chirurgie : Céfoxitine 2g IVL",
            "dose": "Voir molécule",
            "reinjection": "Céfoxitine : 1g / 2h",
            "grade": "GRADE 1",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g IVL",
            "remarque": "*** GRADE 1 pour l'ATB ET pour la double administration (orale veille + IV chirurgie). **** Tobramycine per os hors AMM : utiliser flacon IV 100mg par voie orale (décontamination). Vérifier allergie sulfites. Entente préalable CPAM (~3€). ***** Dépistage E-BLSE si prévalence ≥10%"
        },
        "Appendicectomie programmée": {
            "molecule": "Céfoxitine",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g IVL"
        }
    },
    
    "Chirurgie proctologique": {
        "Hémorroïdes": {
            "molecule": "Métronidazole",
            "dose": "1g IVL",
            "reinjection": "Dose unique",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Kyste pilonidal": {
            "molecule": "Métronidazole",
            "dose": "1g IVL",
            "reinjection": "Dose unique",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Fistule anale": {
            "molecule": "Métronidazole",
            "dose": "1g IVL",
            "reinjection": "Dose unique",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Chirurgie de la vésicule biliaire et des voies biliaires": {
        "Cholécystectomie élective par laparoscopie - Patients à haut risque": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg",
            "remarque": "Patients à haut risque : Âge >80 ans, grossesse, immunosuppression, cholécystite aiguë, ictère, calcul voie biliaire, prothèse, conversion, fuite biliaire"
        },
        "Cholécystectomie élective par laparoscopie - Patients à faible risque": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Cholécystectomie par laparotomie": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Cholécystectomie avec ablation de calcul de la voie biliaire principale": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Anastomose bilio-digestive": {
            "molecule": "Céfoxitine",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g IVL"
        }
    },
    
    "Hépatectomie sans chirurgie des voies biliaires": {
        "Résection atypique / Segmentectomie / Lobectomie hépatique": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        }
    },
    
    "Chirurgie des kystes hépatiques": {
        "Résection du dôme saillant / Péri-kystectomie / Chirurgie de kystes hydatiques": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Splénectomie": {
        "Splénectomie programmée ou en urgence": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        }
    },
    
    "Chirurgie pancréatique": {
        "Pancréatectomie gauche / Pancréatectomie totale / Gestes d'épargne pancréatique": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "GRADE 2",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "DPC ou DPT sans geste de drainage biliaire préopératoire": {
            "molecule": "Céfoxitine",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "GRADE 1",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g IVL"
        },
        "DPC ou DPT pour ampullome ou avec drainage biliaire/sphinctérotomie préopératoires": {
            "molecule": "Pipéracilline + Tazobactam",
            "dose": "4g IVL",
            "reinjection": "4g / 4h",
            "grade": "GRADE 2",
            "allergie": "Discussion pluridisciplinaire",
            "remarque": "Adapter l'ATB aux antécédents infectieux biliaires. Spectre à élargir si BMR ou antécédent fongique"
        }
    },
    
    "Transplantation hépatique et pancréatique": {
        "Transplantation de foie total / foie réduit / pancréas / pancréas-rein": {
            "molecule": "Céfoxitine",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Discussion pluridisciplinaire",
            "remarque": "Spectre à élargir et/ou adapter à l'écologie locale si facteurs de risque de BMR et/ou antécédent d'infection fongique"
        }
    },
    
    "Chirurgie de paroi": {
        "Cure de hernie inguinale et crurale avec prothèse": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "GRADE 2",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Cure de hernie de l'aine sans prothèse": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        }
    },
    
    "Endoscopie digestive": {
        "CPRE avec drainage complet satisfaisant": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 1",
            "allergie": "N/A"
        },
        "CPRE avec drainage biliaire incomplet ou cholangioscopie": {
            "molecule": "Céfoxitine",
            "dose": "2g IVL",
            "reinjection": "Dose unique",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g IVL"
        },
        "Ponction de lésion tissulaire pancréatique ou extra-pancréatique": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Ponction de lésion kystique pancréatique sans facteur de risque": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Ponction de lésion kystique pancréatique avec facteur de risque / Kysto-gastrostomie": {
            "molecule": "Céfoxitine",
            "dose": "2g IVL",
            "reinjection": "Dose unique",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g IVL"
        },
        "Fibroscopie œso-gastro-duodénale diagnostique ou thérapeutique": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Pose de gastrostomie par voie transcutanée": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "Dose unique",
            "grade": "GRADE 1",
            "allergie": "Vancomycine 20mg/kg ou Teicoplanine 12mg/kg"
        },
        "Sclérose/ligature de varices œso-gastriques hors période hémorragique": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Sclérose/ligature de varices en période hémorragique": {
            "molecule": "Ciprofloxacine 400mg IV x2/j (7j) OU Ceftriaxone 1g/24h si Child B/C",
            "dose": "Voir molécule",
            "reinjection": "Traitement curatif 7 jours",
            "grade": "GRADE 1",
            "allergie": "Discussion pluridisciplinaire"
        },
        "Coloscopie diagnostique ou thérapeutique": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Radiologie interventionnelle digestive": {
        "Embolisation hépatique / Chimio-embolisation / TIPS": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Drainage biliaire": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    }
},

    "Urologie": {
    "Chirurgie de la prostate": {
        "Résection trans-urétrale de prostate (RTUP)": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "GRADE 1",
            "allergie": "Gentamicine 6-7mg/kg IVL",
            "remarque": "* Le GRADE 1 s'applique au fait d'administrer une ATB. Les schémas proposés sont de niveau « avis d'experts »"
        },
        "Adénomectomie chirurgicale": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg IVL"
        },
        "Traitement HBP par techniques chirurgicales (HoLEP, ThuLEP, GreenLEP, BIPOLEP, UROLIFT, REZUM)": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg IVL"
        },
        "Traitement HBP sans abord direct de la prostate (HIFU, embolisation)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Prostatectomie totale": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Curiethérapie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Biopsies de prostate par voie trans-périnéale": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Biopsies de prostate par voie transrectale": {
            "molecule": "Fosfomycine-trométamol 3g per os (Alternative: Ciprofloxacine 500mg per os)",
            "dose": "Dose unique",
            "reinjection": "Au moins 2h avant le geste",
            "grade": "GRADE 1 (Fosfomycine) | GRADE 2 (Ciprofloxacine)",
            "allergie": "Ciprofloxacine 500mg per os"
        }
    },
    
    "Chirurgie de la vessie": {
        "Cystoscopie diagnostique": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 1",
            "allergie": "N/A"
        },
        "Résection trans-urétrale de vessie (RTUV)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 1",
            "allergie": "N/A"
        },
        "Cure d'incontinence urinaire": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Injection intra-détrusorienne de toxine botulique": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Cure de prolapsus (avec ou sans matériel) / Injection de macroplastique": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg IVL"
        },
        "Cystectomie sustrigonale partielle ou totale (quel que soit le mode de dérivation)": {
            "molecule": "Céfoxitine",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g IVL"
        }
    },
    
    "Chirurgie des organes génitaux de l'homme": {
        "Pose de prothèse pénienne": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Clindamycine 900mg IVL"
        },
        "Pose de prothèse testiculaire": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Clindamycine 900mg IVL"
        },
        "Chirurgie scrotale ou de la verge sans prothèse": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Chirurgie des voies excrétrices": {
        "Urétéroscopie diagnostique et/ou thérapeutique": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "GRADE 1",
            "allergie": "Gentamicine 6-7mg/kg IVL",
            "remarque": "* Le GRADE 1 s'applique au fait d'administrer une ATB. Les schémas proposés sont de niveau « avis d'experts »"
        },
        "Urétrotomie, urétroplastie": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg IVL"
        },
        "Montée de sonde JJ": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg IVL"
        },
        "Pose de sonde de néphrostomie": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg IVL"
        },
        "Néphrolithotomie percutanée": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg IVL"
        },
        "Lithotritie extra-corporelle": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 1",
            "allergie": "N/A"
        }
    },
    
    "Cathéter de dialyse intrapéritonéale": {
        "Pose ou changement de cathéter de dialyse intrapéritonéale": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "GRADE 2",
            "allergie": "Gentamicine 6-7mg/kg IVL",
            "remarque": "* Le GRADE 2 s'applique au fait d'administrer une ATB. Les schémas proposés sont de niveau « avis d'experts »"
        }
    },
    
    "Chirurgies du rein": {
        "Néphrectomie totale ou partielle": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Surrénalectomie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Embolisation des artères rénales": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Thermoablation de tumeur rénale": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Transplantation rénale": {
            "molecule": "Céfazoline (Alternative: Céfuroxime)",
            "dose": "2g IVL",
            "reinjection": "1g / 4h (Cefaz) | 0.75g / 2h (Cefu)",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg IVL"
        }
    }
},

    "Chirurgie Plastique, Reconstructrice & Esthétique": {
    "Chirurgie mammaire plastique ou carcinologique": {
        "Chirurgie d'augmentation mammaire sans pose d'implant (lipofilling < 200mL ET durée ≤ 2h)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Chirurgie d'augmentation mammaire sans pose d'implant (lipofilling > 200mL ou durée > 2h)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Chirurgie d'augmentation mammaire avec pose d'implant (implants siliconés, prothèse d'expansion)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine",
            "remarque": "# Pas d'indication à prolonger l'antibioprophylaxie au-delà de la fin de chirurgie (GRADE 2)"
        },
        "Gonflage d'expandeur": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Chirurgie de réduction mammaire": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Exérèse de gynécomastie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Mastopexie pour ptose simple": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Tumorectomie mammaire sans curage": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Tumorectomie mammaire avec ganglion sentinelle": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Tumorectomie mammaire avec curage": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "GRADE 2",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Mastectomie (avec ou sans curage) sans reconstruction": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "GRADE 2",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Mastectomie avec reconstruction immédiate par prothèse d'expansion": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine",
            "remarque": "# Pas d'indication à prolonger l'antibioprophylaxie au-delà de la fin de chirurgie (GRADE 2)"
        },
        "Mastectomie avec reconstruction immédiate par lambeau (pectoraux, grand dorsaux, DIEP, gracilis, PAP, SCIP, TDAP, SIEA)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine",
            "remarque": "# Pas d'indication à prolonger l'antibioprophylaxie au-delà de la fin de chirurgie (GRADE 2)"
        },
        "Mastectomie avec reconstruction différée": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        }
    },
    
    "Chirurgie de silhouette": {
        "Brachioplastie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Cruroplastie": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Abdominoplastie (durée ≤ 2h)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Abdominoplastie (durée > 2h)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Body-lift": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "GRADE 2",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Lipoaspiration sous anesthésie générale ou locale": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Chirurgie de la tête et du cou": {
        "Otoplastie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Blépharoplastie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Lifting cervico-facial ou mask-lift (durée ≤ 2h)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Lifting cervico-facial ou mask-lift (durée > 2h)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Lifting avec greffon ou remodelage osseux": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Septo-rhinoplastie sans greffe de cartilage": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Septo-rhinoplastie avec greffe de cartilage": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "GRADE 2",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Implants ou appositions modelantes à la face (malaire)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "GRADE 2",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Frontoplastie": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Génioplastie (avec ou sans implant)": {
            "molecule": "Amoxicilline/Clavulanate",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Chirurgie orthognatique": {
            "molecule": "Amoxicilline/Clavulanate",
            "dose": "2g IVL",
            "reinjection": "1g / 2h (puis 1g/6h post-op 48h max)",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine",
            "remarque": "** Ne pas dépasser 1200 mg/j d'acide clavulanique. *** Posologie postop à moduler selon poids et fonction rénale"
        },
        "Autogreffes capillaires de réimplantation": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Chirurgie de la face avec reconstruction par lambeau (abord endo-oral)": {
            "molecule": "Amoxicilline/Clavulanate",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Chirurgie de la face avec reconstruction par lambeau (abord extra-oral, durée ≤ 2h)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Chirurgie de la face avec reconstruction par lambeau (abord extra-oral, durée > 2h)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        }
    },
    
    "Chirurgie générale et carcinologique": {
        "Transfert adipocytaire libre (< 200mL ET durée ≤ 2h)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Transfert adipocytaire libre (> 200mL ou durée > 2h)": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Greffes cutanées (hors brûlure)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Pose de substitut dermique": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Expansion cutanée avec prothèse : Pose de prothèse(s) d'expansion": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Expansion cutanée avec prothèse : Gonflage de prothèse": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Lambeaux libres microchirurgicaux ou pédiculés": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Plastie(s) cutanée(s)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "GRADE 2",
            "allergie": "N/A"
        },
        "Tumorectomie cutanée": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Chirurgie de ganglion sentinelle": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Curage ganglionnaire axillaire ou inguinal seul": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    }
},

    "Chirurgie d'Affirmation de Genre": {
    "Prothèses pénienne et testiculaire": {
        "Pose de prothèse testiculaire": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Pose de prothèse pénienne": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Armature d'un néo-pénis": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Pose de prothèses gonflables (hydrauliques) avec composants extra-caverneux": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Pose de prothèses semi-rigide": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        }
    },
    
    "Vaginoplastie": {
        "Urétroplastie, vaginoplastie et vestibuloplastie avec enfouissement ou réduction du clitoris": {
            "molecule": "Amoxicilline/Clavulanate",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g",
            "remarque": "* En cas de création de néo-vagin : poursuite de l'amoxicilline/clavulanate 1g/6h (si allergie : métronidazole 500mg/8h) jusqu'à ablation du conformateur vaginal"
        },
        "Création d'un néo-vagin et d'une néo-vulve +/- greffe de peau": {
            "molecule": "Amoxicilline/Clavulanate",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g",
            "remarque": "* Poursuite de l'amoxicilline/clavulanate 1g/6h (si allergie : métronidazole 500mg/8h) chez la patiente de poids standard et fonction rénale normale, jusqu'à ablation du conformateur vaginal"
        },
        "Plastie des organes génitaux externes pour transsexualisme masculin": {
            "molecule": "Amoxicilline/Clavulanate",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g"
        },
        "Création d'un néo-vagin avec un segment intestinal": {
            "molecule": "La veille : Tobramycine 200mg + Métronidazole 1g (per os) | Lors chirurgie : Céfoxitine 2g IVL",
            "dose": "Voir molécule",
            "reinjection": "Céfoxitine : 1g / 2h",
            "grade": "GRADE 1",
            "allergie": "Gentamicine 6-7mg/kg + Métronidazole 1g",
            "remarque": "**** GRADE 1 pour l'ATB ET pour la double administration (orale veille + IV chirurgie). ** Tobramycine per os hors AMM : utiliser flacon IV 100mg par voie orale (décontamination). Vérifier allergie sulfites. Entente préalable CPAM (~3€). *** Dépistage E-BLSE si prévalence ≥10%"
        }
    },
    
    "Phalloplastie": {
        "Phalloplastie par lambeau inguinal pédiculé, ou lambeau cutané libre, ou lambeau cutané tubulé pénien": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        }
    },
    
    "Métoïdioplastie": {
        "Métoïdioplastie": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        }
    },
    
    "Chondro-laryngoplastie": {
        "Laryngoplastie par cervicotomie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    }
},

    "Chirurgie des Brûlés": {
    "Pansements et soins de brûlure": {
        "Pansement de brûlure initial (mise à plat de phlyctènes, lavage) et secondaire sans geste chirurgical": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Incisions de décharge": {
        "Escarrotomie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Aponévrotomie": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE (en l'absence de fracture ouverte associée)",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        }
    },
    
    "Excision et couverture": {
        "Excision de brûlure sans couverture ou avec couverture temporaire (allo ou xénogreffe)": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A"
        },
        "Autogreffe cutanée": {
            "molecule": "PAS D'ANTIBIOPROPHYLAXIE",
            "dose": "N/A",
            "reinjection": "N/A",
            "grade": "Avis d'experts",
            "allergie": "N/A",
            "remarque": "Considérer une antibioprophylaxie individuelle adaptée à la flore du site opératoire et au risque du patient en cas de parcours de soins prolongé, colonisation cutanée à germes multi-résistants, immunodépression sous-jacente, etc."
        },
        "Greffe de matrice cutanée artificielle": {
            "molecule": "Céfazoline",
            "dose": "2g IVL",
            "reinjection": "1g / 4h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        }
    },
    
    "Chirurgie complexe": {
        "Arthrodèse avec articulation fermée": {
            "molecule": "Antibioprophylaxie adaptée à la flore du site opératoire et au risque du patient",
            "dose": "Selon flore",
            "reinjection": "Selon flore",
            "grade": "Avis d'experts",
            "allergie": "Selon flore",
            "remarque": "Considérer une antibioprophylaxie individuelle adaptée en cas de parcours de soins prolongé, colonisation à BMR, immunodépression, etc."
        },
        "Amputation": {
            "molecule": "Amoxicilline/Clavulanate",
            "dose": "2g IVL",
            "reinjection": "1g / 2h",
            "grade": "Avis d'experts",
            "allergie": "Clindamycine ou Vancomycine ou Teicoplanine"
        },
        "Enfouissement de cartilage pour reconstruction auriculaire": {
            "molecule": "Antibioprophylaxie adaptée à la flore du site opératoire et au risque du patient",
            "dose": "Selon flore",
            "reinjection": "Selon flore",
            "grade": "Avis d'experts",
            "allergie": "Selon flore",
            "remarque": "Considérer une antibioprophylaxie individuelle adaptée en cas de parcours de soins prolongé, colonisation à BMR, immunodépression, etc."
        },
        "Lambeau à distance à pédicule ou vascularisation transitoire (lambeau inguinal, Colson, thénarien, deltopectoral, frontal, scalpant)": {
            "molecule": "Antibioprophylaxie adaptée à la flore du site opératoire et au risque du patient",
            "dose": "Selon flore",
            "reinjection": "Selon flore",
            "grade": "Avis d'experts",
            "allergie": "Selon flore",
            "remarque": "Considérer une antibioprophylaxie individuelle adaptée en cas de parcours de soins prolongé, colonisation à BMR, immunodépression, etc."
        }
    }
},

    "Gynécologie & Obstétrique": {
        "CHIRURGIE DU SEIN": {
            "Chirurgie sénologique carcinologique": {
                "Tumorectomie mammaire sans curage": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Tumorectomie mammaire avec ganglion sentinelle": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Tumorectomie mammaire avec curage axillaire": {"molecule": "Céfazoline", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"},
                "Mastectomie*, sans ou avec curage, sans ou avec reconstruction immédiate": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"}
            },
            "Chirurgie sénologique esthétique/reconstruction": {
                "Mastoplastie unilatérale ou bilatérale de réduction": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Mastopexie pour ptose simple": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Ablation d'implant prothétique mammaire, sans ou avec capsulectomie": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"},
                "Mastoplastie ou reconstruction avec pose d'implant ou lambeau": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"},
                "Changement d'implant prothétique mammaire": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"},
                "Chirurgie du mamelon ou de la plaque aréolo-mamelonnaire": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Autogreffe de tissu adipeux < 200 cm³ au niveau du sein ET chirurgie <2h": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Autogreffe de tissus adipeux >= 200 cm³ et/ou chirurgie >2h": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"}
            }
        },
        "CHIRURGIE DE L’UTERUS, ANNEXES, VULVE, PMA, IVG": {
            "Chirurgie des annexes et des paramètres par voie coelioscopique ou robotique": {
                "Coelioscopie diagnostique": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Ligature ou déligature de trompe, détorsion d'annexe": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Plastie tubaire, fimbrioplastie, salpingectomie": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "NB: ATB (Céfazoline) si endométriose/antécédents infectieux"},
                "Drilling ovarien, kystectomie ovarienne, transposition ovarienne": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Ponction de kyste": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Ablation de dispositif intra-utérin ayant migré (par coelioscopie)": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Annexectomie / Ovariectomie": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Débulking ovarien": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Curage pelvien et/ou lombo-aortique": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Omentectomie": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Résection de lésions endométriosiques avec atteinte rectale": {"molecule": "Céfazoline + Métronidazole", "dose": "2g + 1g IVL", "reinjection": "1g (Cefaz) si > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg"}
            },
            "Chirurgie des annexes et des paramètres par voie laparotomique": {
                "Chirurgie tubaire": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Annexectomie, ovariectomie": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Curage pelvien et/ou lombo-aortique": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Omentectomie": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Ablation de dispositif intra-utérin ayant migré": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"},
                "Exérèse de lésions endométriosiques de la cloison rectovaginale": {"molecule": "Céfazoline + Métronidazole", "dose": "2g + 1g IVL", "reinjection": "1g (Cefaz) si > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg"}
            },
            "Chirurgie de l'utérus par voie laparotomique, coelioscopique ou robotique": {
                "Hysterectomie totale sans ou avec annexectomie": {"molecule": "Céfoxitine (Alternative: Céfazoline + Metro)", "dose": "2 g IVL", "reinjection": "1g si durée > 2h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg"},
                "Colpo-hysterectomie / Colpo-trachélectomie élargie": {"molecule": "Céfoxitine", "dose": "2 g IVL", "reinjection": "1g si durée > 2h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg"},
                "Hysterectomie subtotale sans ou avec annexectomie": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Myomectomie": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Cerclage de l'isthme utérin en dehors de la grossesse": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Hystérorraphie, hystéroplastie": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Colpectomie subtotale ou totale": {"molecule": "Céfoxitine", "dose": "2 g IVL", "reinjection": "1g si durée > 2h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg"},
                "Chirurgie du prolapsus toutes voies d'abord": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"},
                "Hystéropexie / Promontofixation": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"},
                "Colpo-périnéorraphie": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"}
            },
            "Chirurgie de l'utérus par voie vaginale": {
                "Conisation, curetage, destruction muqueuse par thermocontact": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Cerclage de l'isthme utérin par abord vaginal": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Destruction lésions col, exérèse lésion pédiculée": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Hysterectomie avec et sans annexectomie": {"molecule": "Céfoxitine", "dose": "2 g IVL", "reinjection": "1g si durée > 2h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg"}
            },
            "Hystéroscopie": {
                "Hystéroscopie diagnostique": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 1", "allergie": "N/A"},
                "Pose de dispositif intra-utérin": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Destruction muqueuse (thermocontact) / Abrasion / Curetage": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 1", "allergie": "N/A"},
                "Exérèse de polype / Biopsie endomètre": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 1", "allergie": "N/A"},
                "Résection de myome de l'utérus": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 1", "allergie": "N/A"},
                "Ablation dispositif / corps étranger": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 1", "allergie": "N/A"}
            },
            "Chirurgie vulvaire superficielle": {
                "Exérèse glande Bartholin / Adhérences": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 2", "allergie": "N/A"},
                "Vulvectomie partielle sans curage": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 2", "allergie": "N/A"},
                "Vulvo-périnéoplastie / Nymphoplastie": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 2", "allergie": "N/A"},
                "Périnéotomie médiane sans lambeau": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 2", "allergie": "N/A"},
                "Destruction lésions périnéales / Amputation clitoris": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 2", "allergie": "N/A"}
            },
            "Chirurgie vulvaire profonde et/ou carcinologique": {
                "Vulvectomie partielle avec curage lymphonodal inguinal": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"},
                "Vulvectomie totale sans ou avec curage": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"},
                "Périnéotomie médiane avec lambeau cutané périnéal": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"}
            },
            "Chirurgie vaginale": {
                "Chirurgie de l'hymen / Résection de cloison": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Destruction de lésions vaginales": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"}
            },
            "Avortement, grossesse arrêtée": {
                "Révision cavité après avortement": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 2", "allergie": "N/A"},
                "Évacuation utérus gravide (aspiration/curetage)": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 2", "allergie": "ATB curative si infection suspectée"}
            },
            "Procréation médicalement assistée": {
                "Prélèvement d'ovocytes (voie transvaginale ou coelioscopie)": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 1", "allergie": "NB: ATB (Céfazoline) si endométriose/antécédents infectieux"},
                "Transfert intra-utérin d'embryon": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "GRADE 1", "allergie": "NB: ATB (Céfazoline) si endométriose/antécédents infectieux"}
            },
            "Embolisation": {
                "Embolisation de fibromes utérins": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Embolisation de varices pelviennes (sans abord chirurgical)": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"}
            }
        },

        # --- GRANDE CATÉGORIE 3 ---
        "CHIRURGIE OBSTETRICALE": {
            "Césarienne": {
                "Accouchement par césarienne programmée ou en urgence": {"molecule": "Céfazoline (Alternative: Aucune validée)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"},
                "Suture du corps de l'utérus pour rupture obstétricale": {"molecule": "Céfazoline (Alternative: Aucune validée)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "GRADE 2", "allergie": "Clindamycine 900 mg IVL"}
            },
            "Cerclage du col utérin": {
                "Cerclage du col de l'utérus au cours de la grossesse": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"},
                "Ablation de cerclage du col de l'utérus": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"}
            },
            "Embolisation": {
                "Embolisation pour hémorragie du post-partum": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"}
            },
            "Tamponnement utérin": {
                "Tamponnement intra-utérin pour hémorragie obstétricale": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "Dose unique", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"}
            },
            "Délivrance artificielle / révision utérine": {
                "Révision de la cavité de l'utérus / Extraction manuelle": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "Dose unique", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"}
            },
            "Curetage post-partum": {
                "Curetage de la cavité de l'utérus à visée thérapeutique": {"molecule": "PAS D'ANTIBIOPROPHYLAXIE", "dose": "N/A", "reinjection": "N/A", "grade": "Avis d'experts", "allergie": "N/A"}
            },
            "Hysterectomie d'hémostase": {
                "Hysterectomie pour complications obstétricales": {"molecule": "Céfoxitine", "dose": "2 g IVL", "reinjection": "1g si durée > 2h", "grade": "Avis d'experts", "allergie": "Clindamycine 900mg + Gentamicine 6-7mg/kg"}
            },
            "Ligatures vasculaires": {
                "Ligature des artères iliaques / pédicules vasculaires pour hémorragie": {"molecule": "Céfazoline (Alternative: Céfuroxime)", "dose": "2 g IVL", "reinjection": "1g si durée > 4h", "grade": "Avis d'experts", "allergie": "Clindamycine 900 mg IVL"}
            }
        }
    }
}# =============================================================================
# 4. CONFIGURATION DES ICÔNES & COULEURS
# =============================================================================

# Icônes pour les spécialités
SPEC_ICONS_FLET = {
    "Neurochirurgie & Neuroradiologie": ft.Icons.PSYCHOLOGY,
    "ORL (Oto-Rhino-Laryngologie)": ft.Icons.HEARING,
    "Stomatologie & Chirurgie Maxillo-Faciale": ft.Icons.BRUSH, 
    "Ophtalmologie": ft.Icons.VISIBILITY,
    "Chirurgie Thoracique & Pneumologie": ft.Icons.AIR,
    "Cardiaque & Vasculaire": ft.Icons.FAVORITE,
    "Orthopédie & Traumato": ft.Icons.ACCESSIBILITY_NEW,
    "Chirurgie Digestive": ft.Icons.FASTFOOD,
    "Urologie": ft.Icons.WATER_DROP,
    "Chirurgie Plastique, Reconstructrice & Esthétique": ft.Icons.FACE,
    "Gynécologie & Obstétrique": ft.Icons.PREGNANT_WOMAN,
    "Chirurgie d'Affirmation de Genre": ft.Icons.TRANSGENDER,
    "Chirurgie des Brûlés": ft.Icons.LOCAL_FIRE_DEPARTMENT
}

# Couleurs pour les spécialités
SPEC_COLORS_FLET = {
    "Neurochirurgie & Neuroradiologie": ft.Colors.PURPLE,
    "ORL (Oto-Rhino-Laryngologie)": ft.Colors.TEAL,
    "Stomatologie & Chirurgie Maxillo-Faciale": ft.Colors.BLUE_GREY,
    "Ophtalmologie": ft.Colors.BLUE,
    "Chirurgie Thoracique & Pneumologie": ft.Colors.CYAN,
    "Cardiaque & Vasculaire": ft.Colors.RED,
    "Orthopédie & Traumato": ft.Colors.ORANGE,
    "Chirurgie Digestive": ft.Colors.GREEN,
    "Urologie": ft.Colors.INDIGO,
    "Chirurgie Plastique, Reconstructrice & Esthétique": ft.Colors.RED_ACCENT,
    "Gynécologie & Obstétrique": ft.Colors.PINK,
    "Chirurgie d'Affirmation de Genre": ft.Colors.CYAN,
    "Chirurgie des Brûlés": ft.Colors.DEEP_ORANGE
}

# Émojis pour les catégories (comme dans votre script Tkinter)
# Émojis pour les catégories et sous-catégories
CATEGORY_ICONS = {
    # --- NEUROCHIRURGIE ---
    "Craniotomie": "🧠",
    "Chirurgie intracrânienne par voie trans-sphénoïdale ou trans-labyrinthique": "👃",
    "Dérivation ventriculaire externe": "⚡",
    "Dérivation ventriculaire interne": "🔄",
    "Plaies cranio-cérébrales et fracture de la base du crâne": "🤕",
    "Chirurgie du rachis": "🦴",
    "Électrode de stimulation cérébrale ou médullaire et pose de stimulateur": "🔋",
    "Neuroradiologie interventionnelle": "☢️",

    # --- ORL ---
    "Chirurgie rhino-sinusienne": "👃",
    "Chirurgie carcinologique cervico-faciale": "🧣",
    "Chirurgie du cou et de la thyroïde": "🦋",
    "Chirurgie amygdalienne et adénoïdectomie": "👅",
    "Chirurgie des glandes salivaires": "💧",
    "Laryngoscopie en suspension": "🔦",
    "Chirurgie otologique": "👂",

    # --- STOMATO ---
    "Chirurgie orthognatique": "💀",
    "Chirurgie alvéolo-dentaire": "🦷",
    "Traumatologie maxillo-faciale": "🤕",

    # --- OPHTALMO ---
    "Chirurgie du globe oculaire": "👁️",
    "Chirurgie péri-oculaire": "👓",

    # --- THORACIQUE ---
    "Chirurgie d'exérèse pulmonaire (par thoracotomie ou cervico-thoracotomie...)": "✂️",
    "Chirurgies médiastinales, pleurales, pariétales (y compris voies thoracoscopiques...)": "🫁",
    "Chirurgie des voies aériennes sous-glottiques": "🗣️",
    "Chirurgie œsophagienne (avec ou sans plastie colique)": "🥖",
    "Radiologie interventionnelle des voies respiratoires ou du poumon": "📡",
    "Pose de prothèse endo-bronchique, trachéale ou mise en place de valves unidirectionnelle": "🔭",
    "Endoscopie thérapeutique : dilatation, laser": "🔦",
    "Transplantation mono ou bipulmonaire": "🫀",

    # --- CARDIO & VASCULAIRE ---
    "Chirurgie cardiaque": "❤️",
    "Transplantation cardiaque et assistance circulatoire de longue durée": "🔄",
    "Assistance circulatoire de courte durée": "🩺",
    "Cardiologie structurelle": "🏗️",
    "Rythmologie interventionnelle": "⚡",
    "Chirurgie vasculaire": "🩺",
    "Radiologie vasculaire": "📡",

    # --- ORTHOPÉDIE (Grandes Catégories) ---
    "CHIRURGIE ORTHOPEDIQUE PROGRAMMEE": "📅",
    "TRAUMATOLOGIE": "🚑",
    # --- ORTHOPÉDIE (Sous-Catégories) ---
    "Chirurgie du membre inférieur": "🦵",
    "Chirurgie de l'épaule et du coude": "💪",
    "Chirurgie de la main": "✋",
    "Fractures fermées": "🦴",
    "Fractures ouvertes (hors main)": "💥",
    "Plaie des parties molles (hors main)": "🩹",
    "Traumatisme de la main": "🖐️",

        # --- DIGESTIF (Grandes Catégories) ---
    "CHIRURGIE ŒSO-GASTRIQUE, DE L’INTESTIN GRELE, COLORECTALE ET PROCTOLOGIQUE": "🥖",
    "CHIRURGIE HEPATO-BILIAIRE, SPLENIQUE ET PANCREATIQUE": "🤢",
    "CHIRURGIE DE PAROI": "🧱",
    "ENDOSCOPIE DIGESTIVE": "📷",
    "RADIOLOGIE INTERVENTIONNELLE DIGESTIVE": "🎯",

    # --- DIGESTIF (Sous-Catégories visibles dans l'app) ---
    "Chirurgie œsophagienne": "🧵",
    "Chirurgie gastrique non bariatrique": "🥘",
    "Chirurgie bariatrique": "⚖️",
    "Chirurgie de l'intestin grêle": "➰",
    "Chirurgie colorectale et appendiculaire": "💩",
    "Chirurgie proctologique": "⭕",
    "Chirurgie de la vésicule biliaire et des voies biliaires": "🟢",
    "Chirurgie des kystes hépatiques": "🧫",
    "Hépatectomie sans chirurgie des voies biliaires": "🧬",
    "Splénectomie": "🧬",
    "Chirurgie pancréatique": "🍬",
    "Transplantation hépatique et pancréatique": "🔄",
    "Chirurgie de paroi": "🧱",
    "Endoscopie digestive": "📷",
    "Radiologie interventionnelle digestive": "🎯",


    # --- UROLOGIE (CORRIGÉ) ---
    "Chirurgie de la Prostate": "🌰",
    "Chirurgie de la prostate": "🌰", # Doublon de sécurité (minuscule)
    "Chirurgie de la Vessie": "🎈",
    "Chirurgie de la vessie": "🎈",   # Doublon de sécurité (minuscule)
    "Chirurgie des organes génitaux de l'homme": "🍆",
    "Chirurgie des voies excrétrices": "💧",
    "Cathéter de dialyse intrapéritonéale": "💉",
    "Chirurgies du rein": "🥔",

    # --- PLASTIQUE ---
    "Chirurgie mammaire plastique ou carcinologique": "🍈",
    "Chirurgie de silhouette": "👙",
    "Chirurgie de la tête et du cou": "👤",
    "Chirurgie de la face avec reconstruction par lambeau": "🎭",
    "Chirurgie générale et carcinologique": "🧬",

    # --- AFFIRMATION DE GENRE ---
    "Prothèses pénienne et testiculaire": "🍆",
    "Vaginoplastie": "🌸",
    "Phalloplastie": "🍌",
    "Métoïdioplastie": "⚧️",
    "Chondro-laryngoplastie": "🗣️",

    # --- BRÛLÉS ---
    "Pansements et soins de brûlure": "🩹",
    "Incisions de décharge": "🔪",
    "Excision et couverture": "🧬",
    "Chirurgie complexe": "⚕️",

    # --- GYNÉCO (Grandes Catégories) ---
    "CHIRURGIE DU SEIN": "🍈",
    "CHIRURGIE DE L’UTERUS, ANNEXES, VULVE, PMA, IVG": "♀️",
    "CHIRURGIE OBSTETRICALE": "👶",
    # --- GYNÉCO (Sous-Catégories) ---
    "Chirurgie sénologique carcinologique": "🎗️",
    "Chirurgie sénologique esthétique/reconstruction": "✨",
    "Chirurgie des annexes et des paramètres par voie coelioscopique ou robotique": "🥚",
    "Chirurgie des annexes et des paramètres par voie laparotomique": "🔪",
    "Chirurgie de l'utérus par voie laparotomique, coelioscopique ou robotique": "🤖",
    "Chirurgie de l'utérus par voie vaginale": "🔽",
    "Hystéroscopie": "🔍",
    "Chirurgie vulvaire superficielle": "🌸",
    "Chirurgie vulvaire profonde et/ou carcinologique": "🦀",
    "Chirurgie vaginale": "⭕",
    "Avortement, grossesse arrêtée": "🛑",
    "Procréation médicalement assistée": "🧪",
    "Embolisation": "🎯",
    "Césarienne": "👶",
    "Cerclage du col utérin": "💍",
    "Embolisation (Obstétrique)": "🩸",
    "Tamponnement utérin": "🎈",
    "Délivrance artificielle / révision utérine": "✋",
    "Curetage post-partum": "🥄",
    "Hysterectomie d'hémostase": "🆘",
    "Ligatures vasculaires": "🎗️"
}# =============================================================================
# 5. APPLICATION FLET
# =============================================================================
# ==================== GESTION DES FAVORIS ====================
def load_favorites(page):
    """Charge les favoris depuis le stockage local"""
    fav_json = page.client_storage.get("favorites")
    if fav_json:
        try:
            return json.loads(fav_json)
        except:
            return []
    return []

def save_favorites(page, favorites):
    """Sauvegarde les favoris dans le stockage local"""
    page.client_storage.set("favorites", json.dumps(favorites))

def add_to_favorites(page, spec, cat, act_name, data):
    """Ajoute un acte aux favoris"""
    favorites = load_favorites(page)
    fav_key = f"{spec}||{cat}||{act_name}"
    for fav in favorites:
        if f"{fav['specialty']}||{fav['category']}||{fav['act_name']}" == fav_key:
            return False
    favorites.append({
        "specialty": spec,
        "category": cat,
        "act_name": act_name,
        "data": data
    })
    save_favorites(page, favorites)
    return True

def remove_from_favorites(page, spec, cat, act_name):
    """Retire un acte des favoris"""
    favorites = load_favorites(page)
    fav_key = f"{spec}||{cat}||{act_name}"
    favorites = [f for f in favorites if f"{f['specialty']}||{f['category']}||{fav['act_name']}" != fav_key]
    save_favorites(page, favorites)

def is_favorite(page, spec, cat, act_name):
    """Vérifie si un acte est dans les favoris"""
    favorites = load_favorites(page)
    fav_key = f"{spec}||{cat}||{act_name}"
    for fav in favorites:
        if f"{fav['specialty']}||{fav['category']}||{fav['act_name']}" == fav_key:
            return True
    return False



def remove_from_favorites(page, spec, cat, act_name):
    """Retire un acte des favoris"""
    favorites = load_favorites(page)
    fav_key = f"{spec}||{cat}||{act_name}"
    favorites = [f for f in favorites if f"{f['specialty']}||{f['category']}||{f['act_name']}" != fav_key]
    save_favorites(page, favorites)

def is_favorite(page, spec, cat, act_name):
    """Vérifie si un acte est dans les favoris"""
    favorites = load_favorites(page)
    fav_key = f"{spec}||{cat}||{act_name}"
    for fav in favorites:
        if f"{fav['specialty']}||{fav['category']}||{fav['act_name']}" == fav_key:
            return True
    return False


# ==================== RECHERCHE D'ACTES ====================
def search_acts(query: str):
    """
    Recherche un acte/intervention dans toutes les spécialités SFAR_DATA.
    Retourne une liste de dictionnaires avec:
      - specialty
      - category
      - act_name
      - data (données SFAR_DATA)
      - path (chemin texte pour affichage)
    """
    if not query or len(query) < 2:
        return []

    q = query.lower().strip()
    results = []

    for specialty, categories in SFAR_DATA.items():
        for category, acts in categories.items():
            # Exemple de structure:
            #   acts = { "Acte A": {...}, "Acte B": {...} }
            # ou    acts = { "Sous-cat": { "Acte": {...}, ... }, ... }
            first_key = next(iter(acts))

            # Cas 1 : catégorie "plate" (actes directement avec "molecule")
            if isinstance(acts[first_key], dict) and "molecule" in acts[first_key]:
                for act_name, act_data in acts.items():
                    if q in act_name.lower():
                        results.append(
                            {
                                "specialty": specialty,
                                "category": category,
                                "act_name": act_name,
                                "data": act_data,
                                "path": f"{specialty} > {category}",
                            }
                        )
            # Cas 2 : catégories imbriquées (sous-catégories)
            else:
                for subcat, subacts in acts.items():
                    for act_name, act_data in subacts.items():
                        if q in act_name.lower():
                            results.append(
                                {
                                    "specialty": specialty,
                                    "category": category,
                                    "act_name": act_name,
                                    "data": act_data,
                                    "path": f"{specialty} > {category} > {subcat}",
                                }
                            )

    return results

def main(page: ft.Page):
    # Configuration de la page
    page.title = "ATB SFAR 2024"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE_GREY)
    page.padding = 0
    
    # --- DIALOGUES ---
    def open_about_dlg(e):
        dlg_about = ft.AlertDialog(
            title=ft.Text("À propos"),
            content=ft.Container(
                height=300,
                padding=10,
                content=ft.Column([
                    ft.Text("ATB SFAR 2024", weight=ft.FontWeight.BOLD, size=18, color=ft.Colors.BLUE_GREY_900),
                    ft.Text("Version 2.0 (Finale)", size=14, italic=True),
                    ft.Divider(),
                    ft.Text("Développé par :", size=12, color=ft.Colors.GREY),
                    ft.Text("ILYES", weight=ft.FontWeight.BOLD, size=16),
                    ft.Divider(),
                    ft.Text("Contact :", size=12, color=ft.Colors.GREY),
                    ft.Container(
                        content=ft.Text("giftformenow@gmail.com", color=ft.Colors.BLUE_ACCENT, italic=True),
                        on_click=lambda _: page.launch_url("mailto:giftformenow@gmail.com")
                    ),
                    ft.Divider(),
                    ft.Text("Références :", size=12, color=ft.Colors.GREY),
                    ft.Text("Basé sur les RFE 2024 de la SFAR", weight=ft.FontWeight.BOLD),
                    ft.Container(
                        content=ft.Text("Site web : sfar.org", color=ft.Colors.BLUE, italic=True),
                        on_click=lambda _: page.launch_url("https://sfar.org")
                    )
                ], spacing=5, scroll=ft.ScrollMode.AUTO)
            ),
            actions=[ft.TextButton("Fermer", on_click=lambda e: page.close(dlg_about))]
        )
        page.open(dlg_about)

    def open_reco_dlg(e):
        col_recos = ft.Column(spacing=15, scroll=ft.ScrollMode.AUTO)
        
        for k, v in RFE_GENERALES.items():
            # Utilisation de Markdown pour bien structurer la Question, la Reco et l'Argumentaire
            content_md = f"""
**QUESTION :**
{v['question']}

**RECOMMANDATION :**
{v['reco']}

---
**Argumentaire (Résumé) :**
*{v['argumentaire']}*
"""
            col_recos.controls.append(
                ft.ExpansionTile(
                    title=ft.Text(v["titre"], weight=ft.FontWeight.BOLD, size=15),
                    subtitle=ft.Text(v["grade"], italic=True, color=ft.Colors.ORANGE_800, size=12),
                    controls=[
                        ft.Container(
                            bgcolor=ft.Colors.BLUE_50,
                            padding=15,
                            border_radius=5,
                            content=ft.Markdown(
                                content_md,
                                selectable=True,
                                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB
                            )
                        )
                    ]
                )
            )

        dlg_reco = ft.AlertDialog(
            title=ft.Text("Recommandations Générales (SFAR 2024)", weight=ft.FontWeight.BOLD),
            content=ft.Container(
                width=600,  # Largeur augmentée pour une meilleure lecture des textes longs
                height=500,
                content=col_recos
            ),
            actions=[ft.TextButton("Fermer", on_click=lambda e: page.close(dlg_reco))]
        )
        page.open(dlg_reco)

    def open_spec_info_dlg(spec_name):
        # Récupération du texte info depuis SPECIALTY_INFO
        info_text = SPECIALTY_INFO.get(spec_name, "Pas d'informations spécifiques.")
        
        dlg_info = ft.AlertDialog(
            title=ft.Text(f"Infos : {spec_name}"),
            content=ft.Container(
                width=500,
                height=500,  # 👈 AJOUT : Hauteur fixe
                content=ft.Column([  # 👈 MODIF : Wrap dans Column
                    ft.Markdown(
                        info_text, 
                        selectable=True,
                        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB
                    )
                ], scroll=ft.ScrollMode.AUTO),  # 👈 AJOUT : Scroll activé
            ),
            actions=[ft.TextButton("Fermer", on_click=lambda e: page.close(dlg_info))]
        )
        page.open(dlg_info)

    navigation_origin = {"last": "/"}
    
    # --- NAVIGATION ---
    def route_change(route):
        page.views.clear()
        
                # PAGE 1: ACCUEIL
        if page.route == "/":
                # ----- SECTION FAVORIS (masquée sur la page d'accueil) -----
            fav_section = ft.Column(spacing=10, visible=False)

            # ----- GRID DES SPÉCIALITÉS -----
            grid_view = ft.GridView(
                expand=True,
                runs_count=2,
                max_extent=200,
                child_aspect_ratio=1.2,
                spacing=10,
                run_spacing=10,
                padding=10,
            )

            for spec in SFAR_DATA.keys():
                color = SPEC_COLORS_FLET.get(spec, ft.Colors.BLUE)
                icon = SPEC_ICONS_FLET.get(spec, ft.Icons.MEDICAL_SERVICES)

                tile = ft.Container(
                    bgcolor=color,
                    border_radius=10,
                    padding=10,
                    ink=True,
                    on_click=lambda e, s=spec: page.go(f"/cat/{s}"),
                    content=ft.Column(
                        [
                            ft.Icon(icon, color=ft.Colors.WHITE, size=40),
                            ft.Text(
                                spec,
                                color=ft.Colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=13,
                                text_align=ft.TextAlign.CENTER,
                                no_wrap=False,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                )
                grid_view.controls.append(tile)

                       # ----- RECHERCHE D'ACTES (UI) -----
            search_results_col = ft.Column(spacing=10, visible=False)
            suggestions_col = ft.Column(spacing=2, visible=False)

            def update_suggestions(query: str):
                nonlocal suggestions_col
                q = (query or "").strip()
                suggestions_col.controls.clear()

                # Moins de 3 lettres → pas de suggestions
                if len(q) < 3:
                    suggestions_col.visible = False
                    page.update()
                    return

                results = search_acts(q)
                if not results:
                    suggestions_col.visible = False
                    page.update()
                    return

                for result in results[:8]:  # max 8 suggestions
                    color = SPEC_COLORS_FLET.get(result["specialty"], ft.Colors.BLUE)
                    data = result["data"]
                    is_pas_atb = "PAS D'ANTIBIO" in data.get("molecule", "")
                    icon_mol = ft.Icons.BLOCK if is_pas_atb else ft.Icons.CHECK_CIRCLE

                    def make_suggestion_click(r):
                        def handler(e):
                            navigation_origin["last"] = page.route
                            page.go(
                                f"/detail/{r['specialty']}/{r['category']}/{urllib.parse.quote(r['act_name'])}"
                            )

                        return handler


                    suggestions_col.controls.append(
                        ft.Container(
                            padding=5,
                            ink=True,
                            on_click=make_suggestion_click(result),
                            content=ft.Row(
                                [
                                    ft.Icon(icon_mol, size=16, color=ft.Colors.GREY_700),
                                    ft.Text(
                                        result["act_name"],
                                        size=13,
                                        weight=ft.FontWeight.BOLD,
                                        expand=True,
                                        no_wrap=True,
                                    ),
                                    ft.Text(
                                        result["specialty"],
                                        size=11,
                                        color=ft.Colors.GREY_600,
                                    ),
                                ]
                            ),
                        )
                    )

                suggestions_col.visible = True
                page.update()

            def perform_search(query: str):
                nonlocal search_results_col, grid_view, fav_section, suggestions_col


                if not query or len(query.strip()) < 2:
                    # Réinitialiser l'affichage
                    search_results_col.visible = False
                    search_results_col.controls.clear()
                    suggestions_col.visible = False
                    suggestions_col.controls.clear()
                    grid_view.visible = True
                    fav_section.visible = False
                    page.update()
                    return


                results = search_acts(query)
                search_results_col.controls.clear()

                if not results:
                    search_results_col.controls.append(
                        ft.Container(
                            padding=20,
                            content=ft.Column(
                                [
                                    ft.Icon(
                                        ft.Icons.SEARCH_OFF,
                                        size=60,
                                        color=ft.Colors.GREY_400,
                                    ),
                                    ft.Text(
                                        "Aucun résultat trouvé",
                                        size=16,
                                        color=ft.Colors.GREY_600,
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        )
                    )
                else:
                    search_results_col.controls.append(
                        ft.Container(
                            padding=10,
                            content=ft.Text(
                                f"🔍 {len(results)} résultat(s) trouvé(s)",
                                weight=ft.FontWeight.BOLD,
                                size=16,
                            ),
                        )
                    )

                    for result in results[:20]:  # Limiter l'affichage à 20 résultats
                        color = SPEC_COLORS_FLET.get(
                            result["specialty"], ft.Colors.BLUE
                        )
                        data = result["data"]
                        is_pas_atb = "PAS D'ANTIBIO" in data.get("molecule", "")
                        icon_mol = (
                            ft.Icons.BLOCK if is_pas_atb else ft.Icons.CHECK_CIRCLE
                        )
                        color_mol = (
                            ft.Colors.RED if is_pas_atb else ft.Colors.GREEN_700
                        )

                        def make_result_click(r):
                            def handler(e):
                                navigation_origin["last"] = page.route
                                page.go(
                                    f"/detail/{r['specialty']}/{r['category']}/{urllib.parse.quote(r['act_name'])}"
                                )

                            return handler



                        card = ft.Card(
                            elevation=2,
                            content=ft.Container(
                                padding=15,
                                bgcolor=color,
                                border_radius=8,
                                ink=True,
                                on_click=make_result_click(result),
                                content=ft.Column(
                                    [
                                        ft.Row(
                                            [
                                                ft.Icon(
                                                    icon_mol,
                                                    color=ft.Colors.WHITE,
                                                    size=20,
                                                ),
                                                ft.Text(
                                                    result["act_name"],
                                                    color=ft.Colors.WHITE,
                                                    weight=ft.FontWeight.BOLD,
                                                    size=14,
                                                    expand=True,
                                                    no_wrap=False,
                                                ),
                                            ]
                                        ),
                                        ft.Text(
                                            result["path"],
                                            color=ft.Colors.WHITE70,
                                            size=12,
                                            italic=True,
                                        ),
                                        ft.Divider(
                                            color=ft.Colors.WHITE30,
                                            height=5,
                                        ),
                                        ft.Text(
                                            f"💊 {data.get('molecule', '')[:60]}...",
                                            color=ft.Colors.WHITE,
                                            size=12,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        ft.Text(
                                            f"💉 {data.get('dose', '')}",
                                            color=ft.Colors.WHITE,
                                            size=11,
                                        ),
                                    ],
                                    spacing=5,
                                ),
                            ),
                        )
                        search_results_col.controls.append(card)

                search_results_col.visible = True
                grid_view.visible = False
                fav_section.visible = False
                page.update()

            def clear_search(e):
                search_field.value = ""
                perform_search("")

            search_field = ft.TextField(
                hint_text="🔍 Rechercher un acte ou une intervention...",
                expand=True,
                border_radius=10,
                filled=True,
                bgcolor=ft.Colors.WHITE,
                text_size=14,
                on_change=lambda e: update_suggestions(e.control.value),
                on_submit=lambda e: perform_search(e.control.value),
            )


            search_bar = ft.Container(
                padding=15,
                content=ft.Row(
                    [
                        search_field,
                        ft.IconButton(
                            icon=ft.Icons.SEARCH,
                            icon_color=ft.Colors.BLUE_GREY_800,
                            tooltip="Rechercher",
                            on_click=lambda e: perform_search(search_field.value),
                        ),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color=ft.Colors.RED,
                            tooltip="Effacer",
                            on_click=clear_search,
                        ),
                    ]
                ),
            )

            main_content = ft.Column(
                [
                    search_results_col,  # masqué par défaut
                    fav_section,
                    grid_view,
                ],
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            )

            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(
                            title=ft.Text(
                                "ATB SFAR 2024",
                                weight=ft.FontWeight.BOLD,
                            ),
                            bgcolor=ft.Colors.BLUE_GREY_800,
                            color=ft.Colors.WHITE,
                            actions=[
                                ft.IconButton(
                                    ft.Icons.STAR,
                                    tooltip="Mes Favoris",
                                    on_click=lambda e: page.go("/favoris"),
                                ),
                                ft.IconButton(
                                    ft.Icons.INFO_OUTLINE,
                                    tooltip="À propos",
                                    on_click=open_about_dlg),
                                ft.IconButton(
                                    ft.Icons.MENU_BOOK,
                                    tooltip="Recos Générales",
                                    on_click=open_reco_dlg),
                            ],
                        ),
                        search_bar,
                        suggestions_col,
                        ft.Container(
                            padding=15,
                            content=ft.Text(
                                "Choisissez une spécialité :",
                                weight=ft.FontWeight.BOLD,
                                size=16,
                            ),
                        ),
                        main_content,
                    ],
                )
            )

                
                # PAGE FAVORIS
        elif page.route == "/favoris":
            favorites = load_favorites(page)
            
            if not favorites:
                content = ft.Container(
                    padding=50,
                    alignment=ft.alignment.center,
                    content=ft.Column([
                        ft.Icon(ft.Icons.STAR_BORDER, size=80, color=ft.Colors.GREY_400),
                        ft.Text("Aucun favori pour le moment", size=20, color=ft.Colors.GREY_600, text_align=ft.TextAlign.CENTER),
                        ft.Text("Cliquez sur l'étoile ⭐ d'un acte pour l'ajouter", size=14, color=ft.Colors.GREY_500, text_align=ft.TextAlign.CENTER)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
                )
            else:
                # Liste visuelle des favoris
                fav_list = ft.Column(scroll=ft.ScrollMode.AUTO, spacing=10, expand=True)

                for fav in favorites:
                    color = SPEC_COLORS_FLET.get(fav["specialty"], ft.Colors.BLUE)

                    def make_click_handler(f):
                        def handler(e):
                            navigation_origin["last"] = page.route  # généralement "/favoris"
                            page.go(
                                f"/detail/{f['specialty']}/{f['category']}/{f['act_name']}"
                            )
                        return handler




                    def make_remove_fav(f):
                        def handler(e):
                            # Supprime des favoris (stockage local)
                            remove_from_favorites(page, f["specialty"], f["category"], f["act_name"])
                            # Retire visuellement la carte
                            fav_list.controls.remove(e.control.parent.parent)  # on enlève le Container du favori
                            page.update()
                        return handler


                    fav_card = ft.Container(
                        padding=15,
                        bgcolor=color,
                        border_radius=8,
                        ink=True,
                        animate_opacity=300,
                        opacity=1.0,
                        on_click=make_click_handler(fav),
                        content=ft.Row(
                            [
                                ft.Text(
                                    fav["act_name"],
                                    color=ft.Colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    size=18,
                                    expand=True,
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    icon_color=ft.Colors.WHITE,
                                    icon_size=24,
                                    tooltip="Retirer des favoris",
                                    on_click=make_remove_fav(fav),

                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                    )
                    fav_list.controls.append(fav_card)

                content = fav_list

            
            page.views.append(
                ft.View(
                    "/favoris",
                    [
                        ft.AppBar(
                            title=ft.Text("⭐ Mes Favoris", weight=ft.FontWeight.BOLD),
                            bgcolor=ft.Colors.AMBER,
                            color=ft.Colors.WHITE,
                            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
                        ),
                        ft.Container(padding=15, content=content)
                    ]
                )
            )


        # PAGE 2: CATÉGORIES
        elif page.route.startswith("/cat/"):
            route_spec = page.route.split("/")[2]
            spec_name = next((k for k in SFAR_DATA.keys() if k == route_spec), route_spec)
            
            color = SPEC_COLORS_FLET.get(spec_name, ft.Colors.BLUE)
            
            lv = ft.ListView(expand=True, spacing=10, padding=15)
            categories = SFAR_DATA.get(spec_name, {})
            
            for cat in categories.keys():
                emoji = CATEGORY_ICONS.get(cat, "📂")

                def open_cat_detail(e, s=spec_name, c=cat):
                    navigation_origin["last"] = page.route  # mémorise la page /cat/...
                    page.go(f"/detail/{s}/{c}")

                card = ft.Container(
                    bgcolor=color,
                    border_radius=8,
                    padding=15,
                    ink=True,
                    on_click=open_cat_detail,
                    content=ft.Row(
                        [
                            ft.Text(emoji, size=30),
                            ft.VerticalDivider(width=10, color=ft.Colors.TRANSPARENT),
                            ft.Text(
                                cat,
                                color=ft.Colors.WHITE,
                                weight=ft.FontWeight.BOLD,
                                size=16,
                                expand=True,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                )
                lv.controls.append(card)


            page.views.append(
                ft.View(
                    f"/cat/{spec_name}",
                    [
                        ft.AppBar(
                            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/")),
                            title=ft.Text(spec_name, size=16), 
                            bgcolor=color, 
                            color=ft.Colors.WHITE,
                            actions=[
                                # Bouton Infos Spécialité
                                ft.IconButton(ft.Icons.INFO, tooltip="Infos Spécialité", on_click=lambda e: open_spec_info_dlg(spec_name)),
                                ft.IconButton(ft.Icons.INFO_OUTLINE, on_click=open_about_dlg),
                                ft.IconButton(ft.Icons.MENU_BOOK, on_click=open_reco_dlg)
                            ]
                        ),
                        ft.Container(padding=15, content=ft.Text("Sélectionnez une catégorie :", size=16, weight=ft.FontWeight.W_500)),
                        lv
                    ]
                )
            )

        # PAGE 3: DÉTAIL
        elif page.route.startswith("/detail/"):
            parts = page.route.split("/")
            spec = parts[2]
            cat = parts[3]
            preselected_act = "/".join(parts[4:]) if len(parts) > 4 else None
            color = SPEC_COLORS_FLET.get(spec, ft.Colors.BLUE)
            
            # Récupération des données
            cat_data = SFAR_DATA[spec][cat]
            
            # Vérification : Est-ce une catégorie "plate" ou "avec sous-catégories" ?
            # On regarde le premier élément. Si c'est un dictionnaire qui contient "molecule", c'est plat.
            first_key = next(iter(cat_data))
            is_nested = "molecule" not in cat_data[first_key]
            
            # Conteneur pour les résultats
            res_col = ft.Column(spacing=10)
            # Si un acte est présélectionné, l'afficher directement
            

            # Fonction pour afficher les détails d'un acte
            def show_act_details(data, spec_name, cat_name, act_name):

                is_pas_atb = "PAS D'ANTIBIO" in data["molecule"] or "PAS D'ANTIBIOPROPHYLAXIE" in data["molecule"]
                color_mol = ft.Colors.RED if is_pas_atb else ft.Colors.GREEN_700
                icon_mol = ft.Icons.BLOCK if is_pas_atb else ft.Icons.CHECK_CIRCLE
                
                                # Vérifie si l'acte est dans les favoris
                is_fav = is_favorite(page, spec_name, cat_name, act_name)
                
                def toggle_favorite(e):
                    if is_favorite(page, spec_name, cat_name, act_name):
                        remove_from_favorites(page, spec_name, cat_name, act_name)
                        fav_btn.icon = ft.Icons.STAR_BORDER
                        fav_btn.icon_color = ft.Colors.GREY_400
                        fav_btn.tooltip = "Ajouter aux favoris"
                        page.snack_bar = ft.SnackBar(ft.Text("❌ Retiré des favoris"))
                        page.snack_bar.open = True
                    else:
                        add_to_favorites(page, spec_name, cat_name, act_name, data)
                        fav_btn.icon = ft.Icons.STAR
                        fav_btn.icon_color = ft.Colors.AMBER
                        fav_btn.tooltip = "Retirer des favoris"
                        page.snack_bar = ft.SnackBar(ft.Text("⭐ Ajouté aux favoris"))
                        page.snack_bar.open = True
                    page.update()


                
                # Bouton étoile
                fav_btn = ft.IconButton(
                    icon=ft.Icons.STAR if is_fav else ft.Icons.STAR_BORDER,
                    icon_color=ft.Colors.AMBER if is_fav else ft.Colors.GREY_400,
                    icon_size=30,
                    tooltip="Retirer des favoris" if is_fav else "Ajouter aux favoris",
                    on_click=toggle_favorite
                )
                
                # Liste des éléments de la carte
                card_controls = [

                    ft.Row([
                        ft.Icon(icon_mol, color=color_mol, size=30),
                        ft.Text("MOLÉCULE", weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_700),
                        ft.Container(expand=True),
                        fav_btn
                    ], alignment=ft.MainAxisAlignment.CENTER),

                    ft.Divider(),
                    ft.Text(data["molecule"], size=20, weight=ft.FontWeight.BOLD, color=color_mol, text_align=ft.TextAlign.CENTER),
                    ft.Text(data["dose"], size=16, text_align=ft.TextAlign.CENTER),
                    ft.Divider(),
                    ft.Row([
                        ft.Icon(ft.Icons.TIMELAPSE, color=ft.Colors.ORANGE),
                        ft.Text(f"Réinjection : {data['reinjection']}", size=14, expand=True)
                    ]),
                    ft.Row([
                        ft.Icon(ft.Icons.GRADE, color=ft.Colors.PURPLE),
                        ft.Text(f"Grade : {data['grade']}", size=14, expand=True)
                    ]),
                    ft.Divider(),
                    ft.Row([
                        ft.Icon(ft.Icons.WARNING, color=ft.Colors.RED),
                        ft.Text("Allergie / Remarques :", color=ft.Colors.RED, weight=ft.FontWeight.BOLD)
                    ]),
                    ft.Text(data.get("allergie", "N/A"), size=14, color=ft.Colors.GREY_800)
                ]

                # --- C'EST ICI QUE LA REMARQUE EST AJOUTÉE ---
                if "remarque" in data:
                    card_controls.append(ft.Divider())
                    card_controls.append(
                        ft.Container(
                            bgcolor=ft.Colors.AMBER_50,
                            padding=10,
                            border_radius=5,
                            border=ft.border.all(1, ft.Colors.AMBER_200),
                            content=ft.Row([
                                ft.Icon(ft.Icons.INFO, color=ft.Colors.AMBER_800),
                                ft.Text(data["remarque"], size=13, italic=True, color=ft.Colors.BLUE_GREY_900, expand=True)
                            ], vertical_alignment=ft.CrossAxisAlignment.START)
                        )
                    )
                # ---------------------------------------------

                res_col.controls = [
                    ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                    ft.Card(
                        elevation=4,
                        content=ft.Container(
                            padding=20,
                            content=ft.Column(card_controls)
                        )
                    )
                ]
                page.update()
            # Si un acte est présélectionné, l'afficher directement
            if preselected_act:
                act_name_decoded = urllib.parse.unquote(preselected_act)
                
                if is_nested:
                    for subcat_name, subcat_data in cat_data.items():
                        if act_name_decoded in subcat_data:
                            show_act_details(subcat_data[act_name_decoded], spec, cat, act_name_decoded)
                            break
                else:
                    if act_name_decoded in cat_data:
                        show_act_details(cat_data[act_name_decoded], spec, cat, act_name_decoded)


            # --- UI SI STRUCTURE IMBRIQUÉE (ex: Endoscopie) ---
            if is_nested:
                # Dropdown 2 : Actes (initialement vide)
                dd_acts = ft.Dropdown(
                    label="Sélectionnez l'acte",
                    text_size=16,
                    disabled=True,
                    options=[]
                )

                # Fonction déclenchée quand on choisit une sous-catégorie
                def on_change_subcat(e):
                    subcat = e.control.value
                    if not subcat: return
                    
                    # Mise à jour du 2ème dropdown
                    acts_list = cat_data[subcat]
                    dd_acts.options = [ft.dropdown.Option(k) for k in acts_list.keys()]
                    dd_acts.value = None
                    dd_acts.disabled = False
                    dd_acts.on_change = lambda x: show_act_details(acts_list[x.control.value], spec, cat, x.control.value)
                    
                    # Reset de l'affichage résultat
                    res_col.controls = []
                    page.update()

                # Dropdown 1 : Sous-catégories
                dd_sub = ft.Dropdown(
                    label="Sélectionnez le type",
                    text_size=16,
                    options=[ft.dropdown.Option(k) for k in cat_data.keys()],
                    on_change=on_change_subcat
                )
                
                controls_list = [
                    ft.Text("1. Type d'intervention :", weight=ft.FontWeight.BOLD),
                    dd_sub,
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                    ft.Text("2. Acte précis :", weight=ft.FontWeight.BOLD),
                    dd_acts, 
                    res_col
                ]

            # --- UI SI STRUCTURE STANDARD ---
            else:
                def on_change_simple(e):
                    val = e.control.value
                    if val: show_act_details(cat_data[val], spec, cat, val)


                dd_simple = ft.Dropdown(
                    label="Sélectionnez l'acte chirurgical",
                    text_size=16,
                    options=[ft.dropdown.Option(k) for k in cat_data.keys()],
                    on_change=on_change_simple
                )
                controls_list = [dd_simple, res_col]

            page.views.append(
                ft.View(
                    f"/detail/{spec}/{cat}",
                    [
                        ft.AppBar(
                            leading=ft.IconButton(
                                ft.Icons.ARROW_BACK,
                                on_click=lambda e: page.go(navigation_origin["last"]),
                            ),
                            title=ft.Text(cat, size=16),
                            bgcolor=color,
                            color=ft.Colors.WHITE,
                            actions=[
                                ft.IconButton(ft.Icons.INFO_OUTLINE, on_click=open_about_dlg),
                                ft.IconButton(ft.Icons.MENU_BOOK, on_click=open_reco_dlg),
                            ],
                        ),
                        ft.Container(
                            padding=20,
                            expand=True,  # 👈 IMPORTANT
                            content=ft.Column(
                                controls_list,
                                scroll=ft.ScrollMode.AUTO,  # colonne défilable
                                expand=True,                # prend toute la hauteur dispo
                   