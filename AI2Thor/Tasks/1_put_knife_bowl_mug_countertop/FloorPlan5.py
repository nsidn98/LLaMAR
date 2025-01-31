"""
Pre-initialization for FloorPlan5 task.
FloorPlan5 does not need any modifications for the task
of putting the butter knife, mug, and bowl in the countertop.
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
        objectId='ButterKnife|-00.70|+00.90|+00.11',
        position={'x': -0.7003003358840942, 'y': 0.3591325044631958, 'z': -0.8372991651296616}
        )
                    
        event=controller.step(
        action='PlaceObjectAtPoint',
        objectId='Bowl|-00.51|+01.12|+00.54',
        position={'x': 0.024953889846801802, 'y': 0.5823627471923828, 'z': -1.1234981179237364}
        )
                    
        event=controller.step(
        action='PlaceObjectAtPoint',
        objectId='Mug|+00.13|+01.12|+00.57',
        position={'x': 1.1909943729639054, 'y': 0.5778025150299072, 'z': 1.0420002698898316}
        )
                    
        return event
            