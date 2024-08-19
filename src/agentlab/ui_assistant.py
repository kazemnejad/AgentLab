from browsergym.experiments.loop import ExpArgs, EnvArgs

from agentlab.agents.generic_agent.agent_configs import FLAGS_GPT_4o_VISION
from agentlab.agents.generic_agent.generic_agent import GenericAgentArgs
from agentlab.experiments.exp_utils import RESULTS_DIR
from agentlab.llm.llm_configs import CHAT_MODEL_ARGS_DICT

start_url = "https://www.google.com"

exp_args = ExpArgs(
    agent_args=GenericAgentArgs(
        chat_model_args=CHAT_MODEL_ARGS_DICT["openai/gpt-4o-2024-05-13"],
        flags=FLAGS_GPT_4o_VISION,
    ),
    env_args=EnvArgs(
        task_name="openended",
        max_steps=100,
        task_seed=None,
        task_kwargs={
            "start_url": start_url,
        },
        headless=False,
        record_video=True,
        wait_for_user_message=True,
        viewport={"width": 1500, "height": 1280},
        slow_mo=1000,
    ),
    enable_debug=True,
)

exp_args.prepare(RESULTS_DIR / "ui_assistant_logs")
exp_args.run()
