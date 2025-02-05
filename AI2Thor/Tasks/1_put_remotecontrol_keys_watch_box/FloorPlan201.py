"""
Pre-initialization for FloorPlan201 task.
FloorPlan201 does not need any modifications for the task of putting small valuables in a box.
"""

class SceneInitializer:
    def __init__(self) -> None:
        pass
        
    def preinit(self, event, controller):
        """Pre-initialize the environment for the task.
    
        Args:
            event: env.event object
            controller: ai2thor.controller object
    
        Returns:
            event: env.event object
        """
    
        # initialization function - autogenerated
    
        event=controller.step(
        action='PlaceObjectAtPoint',
        objectId='KeyChain|-00.27|+00.70|+03.13',
        position={'x': -0.268202006816864, 'y': 0.7014020085334778, 'z': 3.126955270767212}
        )
                    
        event=controller.step(
        action='PlaceObjectAtPoint',
        objectId='Watch|-02.10|+00.73|-00.06',
        position={'x': -2.1016764640808105, 'y': 0.7336912155151367, 'z': -0.05773969739675522}
        )
                    
        event=controller.step(
        action='PlaceObjectAtPoint',
        objectId='RemoteControl|-02.58|+00.74|-00.15',
        position={'x': -2.5830140113830566, 'y': 0.7350274920463562, 'z': -0.14601318538188934}
        )
                    
        return event
            