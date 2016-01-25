from percolation.rdf import NS, a
subClassOf=NS.rdfs.subClassOf
subPropertyOf=NS.rdfs.subPropertyOf
po=NS.po; social=NS.social
def snapshots():
    triples=[
            (po.FacebookEgoFriendshipSnapshot,subClassOf,FacebookSnapshot),
            (po.FacebookEgoFriendshipSnapshot,subClassOf,FriendshipSnapshot),
            (po.FacebookEgoFriendshipSnapshot,subClassOf,EgoSnapshot),

            (po.EgoSnapshot,       subClassOf, po.Snapshot),
            (po.FriendshipSnapshot,subClassOf, po.Snapshot),
            (po.FacebookSnapshot,  subClassOf, po.Snapshot),

            (po.FacebookGroupFriendshipInteractionSnapshot, subClassOf,po.FacebookSnapshot),
            (po.FacebookGroupFriendshipInteractionSnapshot, subClassOf,po.GroupSnapshot),
            (po.FacebookGroupFriendshipInteractionSnapshot, subClassOf,po.FriendshipInteractionSnapshot),

            (po.FacebookGroupFriendshipSnapshot, subClassOf,po.FacebookFriendshipSnapshot),
            (po.FacebookGroupFriendshipInteractionSnapshot, subClassOf,po.FacebookGroupSnapshot),

            (po.FacebookGroupInteractionSnapshot, subClassOf,po.InteractionSnapshot),
            (po.FacebookGroupInteractionSnapshot, subClassOf,po.FacebookGroupSnapshot),

            (po.FriendshipInteractionSnapshot,subClassOf,po.FriendshipSnapshot),
            (po.FriendshipInteractionSnapshot,subClassOf,po.InteractionSnapshot),

            (po.InteractionSnapshot,subClassOf, po.Snapshot),
            (po.GroupSnapshot,subClassOf, po.Snapshot),

            (po.rawFile,NS.rdfs.range, po.File),

            (social.nFacebookParsedFiles,subPropertyOf,social.nParsedFiles),

            ]
