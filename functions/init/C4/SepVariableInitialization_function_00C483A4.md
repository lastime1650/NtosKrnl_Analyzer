# SepVariableInitialization

- RVA: `0x00C483A4`–`0x00C4A5C4` (길이 `8,736` bytes)
- VA: `0x0000000140C483A4`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D0768`
- 디코드: `1,647`개 명령, `8,736/8,736` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **167**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **358**

### Outgoing calls
- `0x00C48732` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x00C48748` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48760` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48773` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48786` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48799` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C487AC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C487BF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C487D2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C4886B` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C4887D` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C4888D` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C4889F` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C488B1` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C488C3` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C488D5` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C488E7` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C48924` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x00C4893D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48951` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48969` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C4897D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48991` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C489A5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C489B9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C489CD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C489E1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C489F5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48A09` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48A1D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48A31` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48A45` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48A54` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x00C48A63` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48A77` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48A8B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48A9F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48AB3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48AC7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48ADB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48AEF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48B03` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48B17` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48B2B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48B3F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48B53` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48B67` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48B7B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48B8F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48BA3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48BB3` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x00C48BC2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48BD6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48BEA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48BFE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48C12` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48C26` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48C3A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48C4E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48C62` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48C76` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48C8A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48C9E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48CB2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48CC6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48CDA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48CEE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48D02` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48D16` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48D26` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x00C48D3C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48D50` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48D64` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48D78` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48D8C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48DA0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48DB4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48DC8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48DDC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48DF0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48E04` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48E18` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48E2C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48E3C` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (function, `0x009CA4D0`)
- `0x00C48E4B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48E5F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48E73` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48E87` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48E9B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48EAF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48EC3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48ED7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C48EEB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C493D4` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C493EA` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C493FE` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49411` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49424` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49437` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C4944A` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C4945D` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49470` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49483` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49497` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C494AB` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C494BF` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C494D3` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C494E7` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C494FB` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C4950F` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49523` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49537` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49549` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C4955B` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C4956D` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49583` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49597` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C495AA` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C495BD` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C495D0` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C495E3` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C495F4` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49605` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49615` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49625` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49636` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C49648` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49664` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C4967A` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49690` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C496A6` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C496BC` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C496D2` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C496E8` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C496FE` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C4970E` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C4989F` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C498C0` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C498DF` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C498FE` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49920` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49942` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49964` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49986` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C499A8` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C499CA` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C499EC` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49A0E` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49A30` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49A52` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49A74` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49A96` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49AB8` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49ADA` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49AFC` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49B1E` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49B3D` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49B5C` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49C38` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (function, `0x009EB720`)
- `0x00C49C5D` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49C7C` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49C9B` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49CBA` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (function, `0x00474DC0`)
- `0x00C49CC7` → [SepInitSystemDacls](SepInitSystemDacls_function_00C478DC.md) (function, `0x00C478DC`)
- `0x00C4A51D` → [Feature_AgenticAppContainerBfsSupport__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_AgenticAppContainerBfsSupport__private_IsEnabledDeviceUsageNoInline_function_006061DC.md) (function, `0x006061DC`)
- `0x00C4A575` → [SepInitializeSharedSidMap](../../page/7A/SepInitializeSharedSidMap_function_007A3270.md) (function, `0x007A3270`)
- `0x00C4A57E` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)

### Direct callers
- [SepInitializationPhase0](SepInitializationPhase0_function_00C4A790.md) at `0x00C4A796`

### Static image references
- `0x00C483C0` → RVA `0x00C7CA50` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C483D8` → RVA `0x00C7CA80` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C483EB` → RVA `0x00C7CA90` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C483F6` → RVA `0x00C7CAC0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C48404` → RVA `0x00C7C980` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C48412` → RVA `0x00C7C9B0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C48420` → RVA `0x00C7CA00` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C4842E` → RVA `0x00C7CA20` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C4843C` → RVA `0x00C7CD30` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C4844A` → RVA `0x00C7CD50` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C48458` → RVA `0x00C7CD80` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C48466` → RVA `0x00C7CDB0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C48474` → RVA `0x00C7CCC0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C48482` → RVA `0x00C7CCE0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C48490` → RVA `0x00C7CD00` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C4849E` → RVA `0x00C7CD20` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C484AC` → RVA `0x00C7CBF0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C484BA` → RVA `0x00C7CC30` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C484C8` → RVA `0x00C7CC60` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C484D3` → RVA `0x00C7CC90` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C484DE` → RVA `0x00C7CAF0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C484E9` → RVA `0x00C7CB20` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C484F4` → RVA `0x00C7CB60` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C48502` → RVA `0x00C7CBA0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C48510` → RVA `0x00C7CDD0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C4851B` → RVA `0x00C7CE10` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C48526` → RVA `0x00B4B15C` (`PAGE`; read)
- `0x00C48620` → RVA `0x00B4B160` (`PAGE`; read)
- `0x00C4862C` → RVA `0x00B4B164` (`PAGE`; read)
- `0x00C48636` → RVA `0x00B4B168` (`PAGE`; read)
- `0x00C48642` → RVA `0x00B4B14C` (`PAGE`; read)
- `0x00C4864C` → RVA `0x00B4B150` (`PAGE`; read)
- `0x00C48658` → RVA `0x00B4B154` (`PAGE`; read)
- `0x00C48664` → RVA `0x00B4B158` (`PAGE`; read)
- `0x00C48672` → RVA `0x00B4B17C` (`PAGE`; read)
- `0x00C4867E` → RVA `0x00B4B180` (`PAGE`; read)
- `0x00C4868C` → RVA `0x00B4B184` (`PAGE`; read)
- `0x00C48698` → RVA `0x00B4B188` (`PAGE`; read)
- `0x00C486A6` → RVA `0x00B4B16C` (`PAGE`; read)
- `0x00C486B0` → RVA `0x00B4B170` (`PAGE`; read)
- `0x00C486BC` → RVA `0x00B4B174` (`PAGE`; read)
- `0x00C486C8` → RVA `0x00B4B178` (`PAGE`; read)
- `0x00C486D6` → RVA `0x00FC6B20` (`ALMOSTRO`; read)
- `0x00C4871B` → RVA `0x00E67BF0` (`.data`; write)
- `0x00C48721` → RVA `0x00E67BF1` (`.data`; write)
- `0x00C4872C` → RVA `0x00E67D00` (`.data`; write)
- `0x00C48752` → RVA `0x00FD9B78` (`PAGEDATA`; write)
- `0x00C48768` → RVA `0x00E67D40` (`.data`; write)
- `0x00C4877B` → RVA `0x00E67CE8` (`.data`; write)
- `0x00C4878E` → RVA `0x00E67D38` (`.data`; write)
- `0x00C487A1` → RVA `0x00E67D30` (`.data`; write)
- `0x00C487B4` → RVA `0x00E67D48` (`.data`; write)
- `0x00C487C7` → RVA `0x00E67D50` (`.data`; write)
- `0x00C487D7` → RVA `0x00FD9B78` (`PAGEDATA`; read)
- `0x00C487E1` → RVA `0x00E67CF0` (`.data`; write)
- `0x00C487F5` → RVA `0x00E67D48` (`.data`; read)
- `0x00C4880A` → RVA `0x00E67D50` (`.data`; read)
- `0x00C4881A` → RVA `0x00E67D40` (`.data`; read)
- `0x00C4882A` → RVA `0x00E67CE8` (`.data`; read)
- `0x00C4883A` → RVA `0x00E67D38` (`.data`; read)
- `0x00C48853` → RVA `0x00E67D30` (`.data`; read)
- `0x00C48945` → RVA `0x00FD9E58` (`PAGEDATA`; write)
- `0x00C4895A` → RVA `0x00FD9D48` (`PAGEDATA`; write)
- `0x00C48971` → RVA `0x00E67D20` (`.data`; write)
- `0x00C48985` → RVA `0x00E67D28` (`.data`; write)
- `0x00C48999` → RVA `0x00E67B80` (`.data`; write)
- `0x00C489AD` → RVA `0x00E67CF8` (`.data`; write)
- `0x00C489C1` → RVA `0x00FD9CA0` (`PAGEDATA`; write)
- `0x00C489D5` → RVA `0x00E67D58` (`.data`; write)
- `0x00C489E9` → RVA `0x00FD9CA8` (`PAGEDATA`; write)
- `0x00C489FD` → RVA `0x00FD9B10` (`PAGEDATA`; write)
- `0x00C48A11` → RVA `0x00FD9AC8` (`PAGEDATA`; write)
- `0x00C48A25` → RVA `0x00FD9B58` (`PAGEDATA`; write)
- `0x00C48A39` → RVA `0x00FD9BA8` (`PAGEDATA`; write)
- `0x00C48A4D` → RVA `0x00FD9C28` (`PAGEDATA`; write)
- `0x00C48A6B` → RVA `0x00FD9A68` (`PAGEDATA`; write)
- `0x00C48A7F` → RVA `0x00FD9BD8` (`PAGEDATA`; write)
- `0x00C48A93` → RVA `0x00FD9CE0` (`PAGEDATA`; write)
- `0x00C48AA7` → RVA `0x00FD9CE8` (`PAGEDATA`; write)
- `0x00C48ABB` → RVA `0x00FD9CD0` (`PAGEDATA`; write)
- `0x00C48ACF` → RVA `0x00FD9CD8` (`PAGEDATA`; write)
- `0x00C48AE3` → RVA `0x00FD9CF0` (`PAGEDATA`; write)
- `0x00C48AF4` → RVA `0x00FD9CF8` (`PAGEDATA`; write)
- `0x00C48B0B` → RVA `0x00F05818` (`.data`; write)
- `0x00C48B1F` → RVA `0x00F05878` (`.data`; write)
- `0x00C48B33` → RVA `0x00F05820` (`.data`; write)
- `0x00C48B47` → RVA `0x00F05838` (`.data`; write)
- `0x00C48B5B` → RVA `0x00F05840` (`.data`; write)
- `0x00C48B6F` → RVA `0x00E67D18` (`.data`; write)
- `0x00C48B83` → RVA `0x00E67D08` (`.data`; write)
- `0x00C48B97` → RVA `0x00E67D60` (`.data`; write)
- `0x00C48BAC` → RVA `0x00E67BC0` (`.data`; write)
- `0x00C48BCA` → RVA `0x00F057A0` (`.data`; write)
- `0x00C48BDE` → RVA `0x00F057C8` (`.data`; write)
- `0x00C48BF2` → RVA `0x00F057D0` (`.data`; write)
- `0x00C48C06` → RVA `0x00F057B8` (`.data`; write)
- `0x00C48C1A` → RVA `0x00F057C0` (`.data`; write)
- `0x00C48C2E` → RVA `0x00F057E8` (`.data`; write)
- `0x00C48C3F` → RVA `0x00F057F0` (`.data`; write)
- `0x00C48C56` → RVA `0x00F057D8` (`.data`; write)
- `0x00C48C6A` → RVA `0x00F057E0` (`.data`; write)
- `0x00C48C7E` → RVA `0x00F05808` (`.data`; write)
- `0x00C48C92` → RVA `0x00F05810` (`.data`; write)
- `0x00C48CA6` → RVA `0x00F057F8` (`.data`; write)
- `0x00C48CBA` → RVA `0x00F05800` (`.data`; write)
- `0x00C48CCE` → RVA `0x00F05770` (`.data`; write)
- `0x00C48CE2` → RVA `0x00F05778` (`.data`; write)
- `0x00C48CF6` → RVA `0x00F05760` (`.data`; write)
- `0x00C48D0A` → RVA `0x00F05768` (`.data`; write)
- `0x00C48D1F` → RVA `0x00F05788` (`.data`; write)
- `0x00C48D44` → RVA `0x00E67D10` (`.data`; write)
- `0x00C48D58` → RVA `0x00E67BB8` (`.data`; write)
- `0x00C48D6C` → RVA `0x00F05828` (`.data`; write)
- `0x00C48D7D` → RVA `0x00F05830` (`.data`; write)
- `0x00C48D94` → RVA `0x00F05858` (`.data`; write)
- `0x00C48DA8` → RVA `0x00F04F50` (`.data`; write)
- `0x00C48DBC` → RVA `0x00F04F58` (`.data`; write)
- `0x00C48DD0` → RVA `0x00F05860` (`.data`; write)
- `0x00C48DE4` → RVA `0x00F05848` (`.data`; write)
- `0x00C48DF8` → RVA `0x00F05850` (`.data`; write)
- `0x00C48E0C` → RVA `0x00F05798` (`.data`; write)
- `0x00C48E20` → RVA `0x00F05790` (`.data`; write)
- `0x00C48E35` → RVA `0x00F05780` (`.data`; write)
- `0x00C48E53` → RVA `0x00F05868` (`.data`; write)
- `0x00C48E67` → RVA `0x00F05870` (`.data`; write)
- `0x00C48E7B` → RVA `0x00F057A8` (`.data`; write)
- `0x00C48E8F` → RVA `0x00F057B0` (`.data`; write)
- `0x00C48EA3` → RVA `0x00E67BD8` (`.data`; write)
- `0x00C48EB7` → RVA `0x00E67BE0` (`.data`; write)
- `0x00C48EC8` → RVA `0x00E67BC8` (`.data`; write)
- `0x00C48EDF` → RVA `0x00E67BD0` (`.data`; write)
- `0x00C48EF0` → RVA `0x00FD9E58` (`PAGEDATA`; read)
- `0x00C48EFA` → RVA `0x00E67BE8` (`.data`; write)
- `0x00C48F0D` → RVA `0x00FD9D48` (`PAGEDATA`; read)
- `0x00C48F24` → RVA `0x00E67D20` (`.data`; read)
- `0x00C48F39` → RVA `0x00E67D28` (`.data`; read)
- `0x00C48F4D` → RVA `0x00E67B80` (`.data`; read)
- `0x00C48F61` → RVA `0x00FD9CA0` (`PAGEDATA`; read)
- `0x00C48F75` → RVA `0x00E67CF8` (`.data`; read)
- `0x00C48F89` → RVA `0x00E67D58` (`.data`; read)
- `0x00C48F9D` → RVA `0x00FD9CA8` (`PAGEDATA`; read)
- `0x00C48FB1` → RVA `0x00FD9B10` (`PAGEDATA`; read)
- `0x00C48FC5` → RVA `0x00FD9AC8` (`PAGEDATA`; read)
- `0x00C48FDA` → RVA `0x00FD9B58` (`PAGEDATA`; read)
- `0x00C48FEF` → RVA `0x00FD9BA8` (`PAGEDATA`; read)
- `0x00C49004` → RVA `0x00FD9C28` (`PAGEDATA`; read)
- `0x00C49019` → RVA `0x00FD9A68` (`PAGEDATA`; read)
- `0x00C4902E` → RVA `0x00FD9BD8` (`PAGEDATA`; read)
- `0x00C49043` → RVA `0x00FD9CE0` (`PAGEDATA`; read)
- `0x00C49058` → RVA `0x00FD9CE8` (`PAGEDATA`; read)
- `0x00C4906D` → RVA `0x00FD9CD0` (`PAGEDATA`; read)
- `0x00C49082` → RVA `0x00FD9CD8` (`PAGEDATA`; read)
- `0x00C49092` → RVA `0x00FD9CF0` (`PAGEDATA`; read)
- `0x00C490A2` → RVA `0x00FD9CF8` (`PAGEDATA`; read)
- `0x00C490B2` → RVA `0x00F05818` (`.data`; read)
- `0x00C490C7` → RVA `0x00F05878` (`.data`; read)
- `0x00C490DB` → RVA `0x00F05820` (`.data`; read)
- `0x00C490EF` → RVA `0x00F05838` (`.data`; read)
- `0x00C49103` → RVA `0x00F05840` (`.data`; read)
- `0x00C49117` → RVA `0x00E67D18` (`.data`; read)
- `0x00C4912B` → RVA `0x00E67D08` (`.data`; read)
- `0x00C4913F` → RVA `0x00E67D60` (`.data`; read)
- `0x00C4914F` → RVA `0x00E67BC0` (`.data`; read)
- `0x00C4915F` → RVA `0x00F057A0` (`.data`; read)
- `0x00C4916C` → RVA `0x00F057C8` (`.data`; read)
- `0x00C49179` → RVA `0x00F057D0` (`.data`; read)
- `0x00C49186` → RVA `0x00F057B8` (`.data`; read)
- `0x00C49193` → RVA `0x00F057C0` (`.data`; read)
- `0x00C491A0` → RVA `0x00F057E8` (`.data`; read)
- `0x00C491AD` → RVA `0x00F057F0` (`.data`; read)
- `0x00C491BA` → RVA `0x00F057D8` (`.data`; read)
- `0x00C491C7` → RVA `0x00F057E0` (`.data`; read)
- `0x00C491D4` → RVA `0x00F05808` (`.data`; read)
- `0x00C491E1` → RVA `0x00F05810` (`.data`; read)
- `0x00C491EE` → RVA `0x00F057F8` (`.data`; read)
- `0x00C491FB` → RVA `0x00F05800` (`.data`; read)
- `0x00C49208` → RVA `0x00F05770` (`.data`; read)
- `0x00C49215` → RVA `0x00F05778` (`.data`; read)
- `0x00C49222` → RVA `0x00F05760` (`.data`; read)
- `0x00C4922F` → RVA `0x00F05768` (`.data`; read)
- `0x00C4923C` → RVA `0x00F05788` (`.data`; read)
- `0x00C49249` → RVA `0x00E67D10` (`.data`; read)
- `0x00C49259` → RVA `0x00F05828` (`.data`; read)
- `0x00C49270` → RVA `0x00F05830` (`.data`; read)
- `0x00C49287` → RVA `0x00F05858` (`.data`; read)
- `0x00C4929E` → RVA `0x00F04F50` (`.data`; read)
- `0x00C492B5` → RVA `0x00F04F58` (`.data`; read)
- `0x00C492CC` → RVA `0x00F05860` (`.data`; read)
- `0x00C492E3` → RVA `0x00F05848` (`.data`; read)
- `0x00C492FA` → RVA `0x00F05850` (`.data`; read)
- `0x00C49311` → RVA `0x00E67BB8` (`.data`; read)
- `0x00C49328` → RVA `0x00F05798` (`.data`; read)
- `0x00C49335` → RVA `0x00F05790` (`.data`; read)
- `0x00C49342` → RVA `0x00F05780` (`.data`; read)
- `0x00C4934F` → RVA `0x00F05870` (`.data`; read)
- `0x00C4935C` → RVA `0x00F05868` (`.data`; read)
- `0x00C49373` → RVA `0x00F057B0` (`.data`; read)
- `0x00C49380` → RVA `0x00F057A8` (`.data`; read)
- `0x00C4938D` → RVA `0x00E67BD8` (`.data`; read)
- `0x00C4939D` → RVA `0x00E67BC8` (`.data`; read)
- `0x00C493AA` → RVA `0x00E67BE0` (`.data`; read)
- `0x00C493B7` → RVA `0x00E67BD0` (`.data`; read)
- `0x00C49B4A` → RVA `0x00E67BE8` (`.data`; read)
- `0x00C49CDA` → RVA `0x00FD9B80` (`PAGEDATA`; write)
- `0x00C49CE8` → RVA `0x00FD9BC8` (`PAGEDATA`; write)
- `0x00C49D01` → RVA `0x00FD9AD0` (`PAGEDATA`; write)
- `0x00C49D1A` → RVA `0x00FD9B70` (`PAGEDATA`; write)
- `0x00C49D2F` → RVA `0x00FDA008` (`PAGEDATA`; write)
- `0x00C49D44` → RVA `0x00FD9A78` (`PAGEDATA`; write)
- `0x00C49D67` → RVA `0x00FD9B00` (`PAGEDATA`; write)
- `0x00C49D8A` → RVA `0x00FD9B38` (`PAGEDATA`; write)
- `0x00C49D9F` → RVA `0x00FD9B20` (`PAGEDATA`; write)
- `0x00C49DBD` → RVA `0x00FD9D40` (`PAGEDATA`; write)
- `0x00C49DD2` → RVA `0x00FD9AE8` (`PAGEDATA`; write)
- `0x00C49DE7` → RVA `0x00FD9B48` (`PAGEDATA`; write)
- `0x00C49DFC` → RVA `0x00FD9BE0` (`PAGEDATA`; write)
- `0x00C49E11` → RVA `0x00FD9B08` (`PAGEDATA`; write)
- `0x00C49E26` → RVA `0x00FD9BD0` (`PAGEDATA`; write)
- `0x00C49E39` → RVA `0x00FD9AC0` (`PAGEDATA`; write)
- `0x00C49E4C` → RVA `0x00FD9AE0` (`PAGEDATA`; write)
- `0x00C49E5F` → RVA `0x00FD9B30` (`PAGEDATA`; write)
- `0x00C49E72` → RVA `0x00FD9A80` (`PAGEDATA`; write)
- `0x00C49EB3` → RVA `0x00FD9C10` (`PAGEDATA`; write)
- `0x00C49ECC` → RVA `0x00FD9AB8` (`PAGEDATA`; write)
- `0x00C49ED3` → RVA `0x00FD9D50` (`PAGEDATA`; write)
- `0x00C49EDA` → RVA `0x00FD9E60` (`PAGEDATA`; write)
- `0x00C49EE1` → RVA `0x00FD9F40` (`PAGEDATA`; write)
- `0x00C49EE8` → RVA `0x00FD9FF8` (`PAGEDATA`; write)
- `0x00C49EEF` → RVA `0x00FD9D60` (`PAGEDATA`; write)
- `0x00C49EFD` → RVA `0x00FDA1A8` (`PAGEDATA`; write)
- `0x00C49F0B` → RVA `0x00FDA1B0` (`PAGEDATA`; write)
- `0x00C49F19` → RVA `0x00FDA1B8` (`PAGEDATA`; write)
- `0x00C49F27` → RVA `0x00FDA1C0` (`PAGEDATA`; write)
- `0x00C49F35` → RVA `0x00FDA1C8` (`PAGEDATA`; write)
- `0x00C49F3C` → RVA `0x00E67CF0` (`.data`; read)
- `0x00C49F43` → RVA `0x00FDA2F0` (`PAGEDATA`; write)
- `0x00C49F51` → RVA `0x00FDA1D0` (`PAGEDATA`; write)
- `0x00C49F5F` → RVA `0x00FDA1D8` (`PAGEDATA`; write)
- `0x00C49F6D` → RVA `0x00FDA1E0` (`PAGEDATA`; write)
- `0x00C49F7B` → RVA `0x00FDA1E8` (`PAGEDATA`; write)
- `0x00C49F89` → RVA `0x00FDA1F0` (`PAGEDATA`; write)
- `0x00C49F97` → RVA `0x00FDA1F8` (`PAGEDATA`; write)
- `0x00C49FA5` → RVA `0x00FDA240` (`PAGEDATA`; write)
- `0x00C49FB3` → RVA `0x00FDA248` (`PAGEDATA`; write)
- `0x00C49FC1` → RVA `0x00FDA250` (`PAGEDATA`; write)
- `0x00C49FCF` → RVA `0x00FDA270` (`PAGEDATA`; write)
- `0x00C49FDD` → RVA `0x00FDA278` (`PAGEDATA`; write)
- `0x00C49FEB` → RVA `0x00FDA2C0` (`PAGEDATA`; write)
- `0x00C49FF9` → RVA `0x00FDA200` (`PAGEDATA`; write)
- `0x00C4A007` → RVA `0x00FDA208` (`PAGEDATA`; write)
- `0x00C4A015` → RVA `0x00FDA210` (`PAGEDATA`; write)
- `0x00C4A023` → RVA `0x00FDA218` (`PAGEDATA`; write)
- `0x00C4A031` → RVA `0x00FDA220` (`PAGEDATA`; write)
- `0x00C4A03F` → RVA `0x00FDA228` (`PAGEDATA`; write)
- `0x00C4A04D` → RVA `0x00FDA230` (`PAGEDATA`; write)
- `0x00C4A0BD` → RVA `0x00FDA238` (`PAGEDATA`; write)
- `0x00C4A0D9` → RVA `0x00FDA2C8` (`PAGEDATA`; write)
- `0x00C4A0E7` → RVA `0x00FDA2D0` (`PAGEDATA`; write)
- `0x00C4A0EE` → RVA `0x00FD9D68` (`PAGEDATA`; write)
- `0x00C4A0F5` → RVA `0x00FD9E68` (`PAGEDATA`; write)
- `0x00C4A0FC` → RVA `0x00FD9C98` (`PAGEDATA`; write)
- `0x00C4A103` → RVA `0x00FD9D58` (`PAGEDATA`; write)
- `0x00C4A10A` → RVA `0x00FD9B28` (`PAGEDATA`; write)
- `0x00C4A111` → RVA `0x00FD9E50` (`PAGEDATA`; write)
- `0x00C4A118` → RVA `0x00FD9D70` (`PAGEDATA`; write)
- `0x00C4A11F` → RVA `0x00FD9F48` (`PAGEDATA`; write)
- `0x00C4A126` → RVA `0x00FD9E70` (`PAGEDATA`; write)
- `0x00C4A134` → RVA `0x00FDA2D8` (`PAGEDATA`; write)
- `0x00C4A142` → RVA `0x00FDA2E0` (`PAGEDATA`; write)
- `0x00C4A150` → RVA `0x00FDA2E8` (`PAGEDATA`; write)
- `0x00C4A15E` → RVA `0x00FDA2F8` (`PAGEDATA`; write)
- `0x00C4A16C` → RVA `0x00FDA300` (`PAGEDATA`; write)
- `0x00C4A17A` → RVA `0x00FDA308` (`PAGEDATA`; write)
- `0x00C4A188` → RVA `0x00FDA310` (`PAGEDATA`; write)
- `0x00C4A196` → RVA `0x00FDA320` (`PAGEDATA`; write)
- `0x00C4A1A8` → RVA `0x00FDA0F4` (`PAGEDATA`; write)
- `0x00C4A1BA` → RVA `0x00FDA0FC` (`PAGEDATA`; write)
- `0x00C4A1CC` → RVA `0x00FDA104` (`PAGEDATA`; write)
- `0x00C4A1DE` → RVA `0x00FDA10C` (`PAGEDATA`; write)
- `0x00C4A1EE` → RVA `0x00FDA114` (`PAGEDATA`; write)
- `0x00C4A1FE` → RVA `0x00FDA11C` (`PAGEDATA`; write)
- `0x00C4A20E` → RVA `0x00FDA124` (`PAGEDATA`; write)
- `0x00C4A21E` → RVA `0x00FDA12C` (`PAGEDATA`; write)
- `0x00C4A22E` → RVA `0x00FDA134` (`PAGEDATA`; write)
- `0x00C4A23E` → RVA `0x00FDA13C` (`PAGEDATA`; write)
- `0x00C4A24E` → RVA `0x00FDA144` (`PAGEDATA`; write)
- `0x00C4A25E` → RVA `0x00FDA14C` (`PAGEDATA`; write)
- `0x00C4A26E` → RVA `0x00FDA154` (`PAGEDATA`; write)
- `0x00C4A27E` → RVA `0x00FDA15C` (`PAGEDATA`; write)
- `0x00C4A28E` → RVA `0x00FDA164` (`PAGEDATA`; write)
- `0x00C4A29D` → RVA `0x00FDA16C` (`PAGEDATA`; write)
- `0x00C4A2A4` → RVA `0x00FDA0F0` (`PAGEDATA`; write)
- `0x00C4A2AE` → RVA `0x00FDA0F8` (`PAGEDATA`; write)
- `0x00C4A2B8` → RVA `0x00FDA100` (`PAGEDATA`; write)
- `0x00C4A2C2` → RVA `0x00FDA108` (`PAGEDATA`; write)
- `0x00C4A2CC` → RVA `0x00FDA110` (`PAGEDATA`; write)
- `0x00C4A2D6` → RVA `0x00FDA118` (`PAGEDATA`; write)
- `0x00C4A2E0` → RVA `0x00FDA120` (`PAGEDATA`; write)
- `0x00C4A2EA` → RVA `0x00FDA128` (`PAGEDATA`; write)
- `0x00C4A2F4` → RVA `0x00FDA130` (`PAGEDATA`; write)
- `0x00C4A2FE` → RVA `0x00FDA138` (`PAGEDATA`; write)
- `0x00C4A308` → RVA `0x00FDA140` (`PAGEDATA`; write)
- `0x00C4A312` → RVA `0x00FDA148` (`PAGEDATA`; write)
- `0x00C4A31C` → RVA `0x00FDA150` (`PAGEDATA`; write)
- `0x00C4A326` → RVA `0x00FDA158` (`PAGEDATA`; write)
- `0x00C4A330` → RVA `0x00FDA160` (`PAGEDATA`; write)
- `0x00C4A33A` → RVA `0x00FDA168` (`PAGEDATA`; write)
- `0x00C4A344` → RVA `0x00FDA170` (`PAGEDATA`; write)
- `0x00C4A356` → RVA `0x00FDA174` (`PAGEDATA`; write)
- `0x00C4A365` → RVA `0x00FDA17C` (`PAGEDATA`; write)
- `0x00C4A374` → RVA `0x00FDA184` (`PAGEDATA`; write)
- `0x00C4A383` → RVA `0x00FDA18C` (`PAGEDATA`; write)
- `0x00C4A392` → RVA `0x00FDA194` (`PAGEDATA`; write)
- `0x00C4A3D5` → RVA `0x00FDA31C` (`PAGEDATA`; write)
- `0x00C4A3E2` → RVA `0x00FDA328` (`PAGEDATA`; write)
- `0x00C4A3F0` → RVA `0x00FDA330` (`PAGEDATA`; write)
- `0x00C4A3FE` → RVA `0x00FDA338` (`PAGEDATA`; write)
- `0x00C4A40C` → RVA `0x00FDA340` (`PAGEDATA`; write)
- `0x00C4A413` → RVA `0x00FDA178` (`PAGEDATA`; write)
- `0x00C4A41D` → RVA `0x00FDA180` (`PAGEDATA`; write)
- `0x00C4A427` → RVA `0x00FDA188` (`PAGEDATA`; write)
- `0x00C4A431` → RVA `0x00FDA190` (`PAGEDATA`; write)
- `0x00C4A43B` → RVA `0x00FDA198` (`PAGEDATA`; write)
- `0x00C4A445` → RVA `0x00FDA19C` (`PAGEDATA`; write)
- `0x00C4A44C` → RVA `0x00FDA1A0` (`PAGEDATA`; write)
- `0x00C4A456` → RVA `0x00FDA1A4` (`PAGEDATA`; write)
- `0x00C4A45D` → RVA `0x00FDA258` (`PAGEDATA`; write)
- `0x00C4A467` → RVA `0x00FDA25C` (`PAGEDATA`; write)
- `0x00C4A46E` → RVA `0x00FDA260` (`PAGEDATA`; write)
- `0x00C4A478` → RVA `0x00FDA264` (`PAGEDATA`; write)
- `0x00C4A47F` → RVA `0x00FDA268` (`PAGEDATA`; write)
- `0x00C4A489` → RVA `0x00FDA26C` (`PAGEDATA`; write)
- `0x00C4A48F` → RVA `0x00FDA280` (`PAGEDATA`; write)
- `0x00C4A499` → RVA `0x00FDA284` (`PAGEDATA`; write)
- `0x00C4A49F` → RVA `0x00FDA288` (`PAGEDATA`; write)
- `0x00C4A4A9` → RVA `0x00FDA28C` (`PAGEDATA`; write)
- `0x00C4A4AF` → RVA `0x00FDA290` (`PAGEDATA`; write)
- `0x00C4A4B9` → RVA `0x00FDA294` (`PAGEDATA`; write)
- `0x00C4A4C0` → RVA `0x00FDA298` (`PAGEDATA`; write)
- `0x00C4A4CA` → RVA `0x00FDA29C` (`PAGEDATA`; write)
- `0x00C4A4D1` → RVA `0x00FDA2A0` (`PAGEDATA`; write)
- `0x00C4A4DB` → RVA `0x00FDA2A4` (`PAGEDATA`; write)
- `0x00C4A4E2` → RVA `0x00FDA2A8` (`PAGEDATA`; write)
- `0x00C4A4EC` → RVA `0x00FDA2AC` (`PAGEDATA`; write)
- `0x00C4A4F3` → RVA `0x00FDA2B0` (`PAGEDATA`; write)
- `0x00C4A4FD` → RVA `0x00FDA2B4` (`PAGEDATA`; write)
- `0x00C4A503` → RVA `0x00FDA2B8` (`PAGEDATA`; write)
- `0x00C4A50D` → RVA `0x00FDA2BC` (`PAGEDATA`; write)
- `0x00C4A513` → RVA `0x00FDA318` (`PAGEDATA`; write)
- `0x00C4A52F` → RVA `0x00FDA348` (`PAGEDATA`; write)
- `0x00C4A536` → RVA `0x00FDA0F0` (`PAGEDATA`; read)
- `0x00C4A542` → RVA `0x00FD9AA0` (`PAGEDATA`; write)
- `0x00C4A54B` → RVA `0x00F0FEB8` (`.data`; read)
- `0x00C4A567` → RVA `0x00F0FE88` (`.data`; write)
- `0x00C4A56E` → RVA `0x00F0FE80` (`.data`; write)
- `0x00C4A587` → RVA `0x00F04D20` (`.data`; read)
- `0x00C4A59B` → RVA `0x00F04D10` (`.data`; write)
- `0x00C4A5A2` → RVA `0x00F04D08` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **166**
  - `0x00C48732` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`INIT` → `PAGE`)
  - `0x00C48748` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48760` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48773` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48786` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48799` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C487AC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C487BF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C487D2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C4886B` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C4887D` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C4888D` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C4889F` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C488B1` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C488C3` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C488D5` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C488E7` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C48924` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`INIT` → `PAGE`)
  - `0x00C4893D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48951` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48969` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C4897D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48991` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C489A5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C489B9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C489CD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C489E1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C489F5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48A09` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48A1D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48A31` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48A45` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48A54` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`INIT` → `PAGE`)
  - `0x00C48A63` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48A77` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48A8B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48A9F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48AB3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48AC7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48ADB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48AEF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48B03` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48B17` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48B2B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48B3F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48B53` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48B67` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48B7B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48B8F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48BA3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48BB3` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`INIT` → `PAGE`)
  - `0x00C48BC2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48BD6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48BEA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48BFE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48C12` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48C26` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48C3A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48C4E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48C62` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48C76` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48C8A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48C9E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48CB2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48CC6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48CDA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48CEE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48D02` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48D16` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48D26` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`INIT` → `PAGE`)
  - `0x00C48D3C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48D50` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48D64` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48D78` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48D8C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48DA0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48DB4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48DC8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48DDC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48DF0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48E04` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48E18` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48E2C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48E3C` → [RtlLengthRequiredSid](../../page/9C/RtlLengthRequiredSid_function_009CA4D0.md) (`INIT` → `PAGE`)
  - `0x00C48E4B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48E5F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48E73` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48E87` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48E9B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48EAF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48EC3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48ED7` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C48EEB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C493D4` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C493EA` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C493FE` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49411` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49424` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49437` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C4944A` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C4945D` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49470` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49483` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49497` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C494AB` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C494BF` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C494D3` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C494E7` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C494FB` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C4950F` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49523` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49537` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49549` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C4955B` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C4956D` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49583` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49597` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C495AA` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C495BD` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C495D0` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C495E3` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C495F4` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49605` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49615` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49625` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49636` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C49648` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49664` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C4967A` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49690` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C496A6` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C496BC` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C496D2` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C496E8` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C496FE` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C4970E` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C4989F` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C498C0` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C498DF` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C498FE` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49920` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49942` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49964` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49986` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C499A8` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C499CA` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C499EC` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49A0E` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49A30` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49A52` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49A74` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49A96` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49AB8` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49ADA` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49AFC` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49B1E` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49B3D` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49B5C` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49C38` → [RtlInitializeSid](../../page/9E/RtlInitializeSid_function_009EB720.md) (`INIT` → `PAGE`)
  - `0x00C49C5D` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49C7C` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49C9B` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C49CBA` → [RtlDeriveCapabilitySidsFromName](../../text/47/RtlDeriveCapabilitySidsFromName_function_00474DC0.md) (`INIT` → `.text`)
  - `0x00C4A51D` → [Feature_AgenticAppContainerBfsSupport__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_AgenticAppContainerBfsSupport__private_IsEnabledDeviceUsageNoInline_function_006061DC.md) (`INIT` → `.text`)
  - `0x00C4A575` → [SepInitializeSharedSidMap](../../page/7A/SepInitializeSharedSidMap_function_007A3270.md) (`INIT` → `PAGE`)
  - `0x00C4A57E` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C483A4  40 55                           push rbp
00C483A6  53                              push rbx
00C483A7  56                              push rsi
00C483A8  57                              push rdi
00C483A9  41 54                           push r12
00C483AB  41 55                           push r13
00C483AD  41 56                           push r14
00C483AF  41 57                           push r15
00C483B1  48 8D AC 24 18 FE FF FF         lea rbp, [rsp - 0x1e8]
00C483B9  48 81 EC E8 02 00 00            sub rsp, 0x2e8
00C483C0  48 8D 05 89 46 03 00            lea rax, [rip + 0x34689]
00C483C7  48 C7 45 58 22 00 24 00         mov qword ptr [rbp + 0x58], 0x240022
00C483CF  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00C483D3  BA 40 00 00 00                  mov edx, 0x40
00C483D8  48 8D 05 A1 46 03 00            lea rax, [rip + 0x346a1]
00C483DF  48 C7 45 68 0E 00 10 00         mov qword ptr [rbp + 0x68], 0x10000e
00C483E7  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00C483EB  48 8D 05 9E 46 03 00            lea rax, [rip + 0x3469e]
00C483F2  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
00C483F6  48 8D 05 C3 46 03 00            lea rax, [rip + 0x346c3]
00C483FD  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00C48404  48 8D 05 75 45 03 00            lea rax, [rip + 0x34575]
00C4840B  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
00C48412  48 8D 05 97 45 03 00            lea rax, [rip + 0x34597]
00C48419  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
00C48420  48 8D 05 D9 45 03 00            lea rax, [rip + 0x345d9]
00C48427  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00C4842E  48 8D 05 EB 45 03 00            lea rax, [rip + 0x345eb]
00C48435  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00C4843C  48 8D 05 ED 48 03 00            lea rax, [rip + 0x348ed]
00C48443  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
00C4844A  48 8D 05 FF 48 03 00            lea rax, [rip + 0x348ff]
00C48451  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
00C48458  48 8D 05 21 49 03 00            lea rax, [rip + 0x34921]
00C4845F  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
00C48466  48 8D 05 43 49 03 00            lea rax, [rip + 0x34943]
00C4846D  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
00C48474  48 8D 05 45 48 03 00            lea rax, [rip + 0x34845]
00C4847B  48 89 85 10 01 00 00            mov qword ptr [rbp + 0x110], rax
00C48482  48 8D 05 57 48 03 00            lea rax, [rip + 0x34857]
00C48489  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
00C48490  48 8D 05 69 48 03 00            lea rax, [rip + 0x34869]
00C48497  48 89 85 30 01 00 00            mov qword ptr [rbp + 0x130], rax
00C4849E  48 8D 05 7B 48 03 00            lea rax, [rip + 0x3487b]
00C484A5  48 89 85 40 01 00 00            mov qword ptr [rbp + 0x140], rax
00C484AC  48 8D 05 3D 47 03 00            lea rax, [rip + 0x3473d]
00C484B3  48 89 85 50 01 00 00            mov qword ptr [rbp + 0x150], rax
00C484BA  48 8D 05 6F 47 03 00            lea rax, [rip + 0x3476f]
00C484C1  48 89 85 60 01 00 00            mov qword ptr [rbp + 0x160], rax
00C484C8  48 8D 05 91 47 03 00            lea rax, [rip + 0x34791]
00C484CF  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00C484D3  48 8D 05 B6 47 03 00            lea rax, [rip + 0x347b6]
00C484DA  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00C484DE  48 8D 05 0B 46 03 00            lea rax, [rip + 0x3460b]
00C484E5  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00C484E9  48 8D 05 30 46 03 00            lea rax, [rip + 0x34630]
00C484F0  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00C484F4  48 8D 05 65 46 03 00            lea rax, [rip + 0x34665]
00C484FB  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
00C48502  48 8D 05 97 46 03 00            lea rax, [rip + 0x34697]
00C48509  48 89 85 80 01 00 00            mov qword ptr [rbp + 0x180], rax
00C48510  48 8D 05 B9 48 03 00            lea rax, [rip + 0x348b9]
00C48517  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00C4851B  48 8D 05 EE 48 03 00            lea rax, [rip + 0x348ee]
00C48522  48 89 45 00                     mov qword ptr [rbp], rax
00C48526  8B 05 30 2C F0 FF               mov eax, dword ptr [rip - 0xfd3d0]
00C4852C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00C48530  48 C7 45 48 24 00 26 00         mov qword ptr [rbp + 0x48], 0x260024
00C48538  48 C7 45 78 28 00 2A 00         mov qword ptr [rbp + 0x78], 0x2a0028
00C48540  48 C7 85 88 00 00 00 26 00 28 00  mov qword ptr [rbp + 0x88], 0x280026
00C4854B  48 C7 85 98 00 00 00 4E 00 50 00  mov qword ptr [rbp + 0x98], 0x50004e
00C48556  48 C7 85 A8 00 00 00 12 00 14 00  mov qword ptr [rbp + 0xa8], 0x140012
00C48561  48 C7 85 B8 00 00 00 28 00 2A 00  mov qword ptr [rbp + 0xb8], 0x2a0028
00C4856C  48 C7 85 C8 00 00 00 18 00 1A 00  mov qword ptr [rbp + 0xc8], 0x1a0018
00C48577  48 C7 85 D8 00 00 00 2C 00 2E 00  mov qword ptr [rbp + 0xd8], 0x2e002c
00C48582  48 C7 85 E8 00 00 00 2A 00 2C 00  mov qword ptr [rbp + 0xe8], 0x2c002a
00C4858D  48 C7 85 F8 00 00 00 18 00 1A 00  mov qword ptr [rbp + 0xf8], 0x1a0018
00C48598  48 C7 85 08 01 00 00 1E 00 20 00  mov qword ptr [rbp + 0x108], 0x20001e
00C485A3  48 C7 85 18 01 00 00 18 00 1A 00  mov qword ptr [rbp + 0x118], 0x1a0018
00C485AE  48 C7 85 28 01 00 00 1A 00 1C 00  mov qword ptr [rbp + 0x128], 0x1c001a
00C485B9  48 C7 85 38 01 00 00 0E 00 10 00  mov qword ptr [rbp + 0x138], 0x10000e
00C485C4  48 C7 85 48 01 00 00 36 00 38 00  mov qword ptr [rbp + 0x148], 0x380036
00C485CF  48 C7 85 58 01 00 00 20 00 22 00  mov qword ptr [rbp + 0x158], 0x220020
00C485DA  48 C7 45 08 26 00 28 00         mov qword ptr [rbp + 8], 0x280026
00C485E2  48 C7 45 18 2C 00 2E 00         mov qword ptr [rbp + 0x18], 0x2e002c
00C485EA  48 C7 45 38 28 00 2A 00         mov qword ptr [rbp + 0x38], 0x2a0028
00C485F2  48 C7 45 28 30 00 32 00         mov qword ptr [rbp + 0x28], 0x320030
00C485FA  48 C7 85 68 01 00 00 3E 00 40 00  mov qword ptr [rbp + 0x168], 0x40003e
00C48605  48 C7 85 78 01 00 00 42 00 44 00  mov qword ptr [rbp + 0x178], 0x440042
00C48610  48 C7 45 E8 3A 00 3C 00         mov qword ptr [rbp - 0x18], 0x3c003a
00C48618  48 C7 45 F8 50 00 52 00         mov qword ptr [rbp - 8], 0x520050
00C48620  0F B7 05 39 2B F0 FF            movzx eax, word ptr [rip - 0xfd4c7]
00C48627  66 89 44 24 34                  mov word ptr [rsp + 0x34], ax
00C4862C  8B 05 32 2B F0 FF               mov eax, dword ptr [rip - 0xfd4ce]
00C48632  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00C48636  0F B7 05 2B 2B F0 FF            movzx eax, word ptr [rip - 0xfd4d5]
00C4863D  66 89 44 24 3C                  mov word ptr [rsp + 0x3c], ax
00C48642  8B 05 04 2B F0 FF               mov eax, dword ptr [rip - 0xfd4fc]
00C48648  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00C4864C  0F B7 05 FD 2A F0 FF            movzx eax, word ptr [rip - 0xfd503]
00C48653  66 89 44 24 44                  mov word ptr [rsp + 0x44], ax
00C48658  8B 05 F6 2A F0 FF               mov eax, dword ptr [rip - 0xfd50a]
00C4865E  89 85 40 02 00 00               mov dword ptr [rbp + 0x240], eax
00C48664  0F B7 05 ED 2A F0 FF            movzx eax, word ptr [rip - 0xfd513]
00C4866B  66 89 85 44 02 00 00            mov word ptr [rbp + 0x244], ax
00C48672  8B 05 04 2B F0 FF               mov eax, dword ptr [rip - 0xfd4fc]
00C48678  89 85 30 02 00 00               mov dword ptr [rbp + 0x230], eax
00C4867E  0F B7 05 FB 2A F0 FF            movzx eax, word ptr [rip - 0xfd505]
00C48685  66 89 85 34 02 00 00            mov word ptr [rbp + 0x234], ax
00C4868C  8B 05 F2 2A F0 FF               mov eax, dword ptr [rip - 0xfd50e]
00C48692  89 85 48 02 00 00               mov dword ptr [rbp + 0x248], eax
00C48698  0F B7 05 E9 2A F0 FF            movzx eax, word ptr [rip - 0xfd517]
00C4869F  66 89 85 4C 02 00 00            mov word ptr [rbp + 0x24c], ax
00C486A6  8B 05 C0 2A F0 FF               mov eax, dword ptr [rip - 0xfd540]
00C486AC  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00C486B0  0F B7 05 B9 2A F0 FF            movzx eax, word ptr [rip - 0xfd547]
00C486B7  66 89 44 24 2C                  mov word ptr [rsp + 0x2c], ax
00C486BC  8B 05 B2 2A F0 FF               mov eax, dword ptr [rip - 0xfd54e]
00C486C2  89 85 38 02 00 00               mov dword ptr [rbp + 0x238], eax
00C486C8  0F B7 05 A9 2A F0 FF            movzx eax, word ptr [rip - 0xfd557]
00C486CF  66 89 85 3C 02 00 00            mov word ptr [rbp + 0x23c], ax
00C486D6  48 8B 05 43 E4 37 00            mov rax, qword ptr [rip + 0x37e443]
00C486DD  48 8B 88 F0 00 00 00            mov rcx, qword ptr [rax + 0xf0]
00C486E4  8B 81 84 00 00 00               mov eax, dword ptr [rcx + 0x84]
00C486EA  84 C2                           test dl, al
00C486EC  75 26                           jne 0x140c48714
00C486EE  48 B9 64 02 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000264
00C486F8  83 39 01                        cmp dword ptr [rcx], 1
00C486FB  75 17                           jne 0x140c48714
00C486FD  48 B9 10 03 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000310
00C48707  48 81 39 00 34 08 00            cmp qword ptr [rcx], 0x83400
00C4870E  77 04                           ja 0x140c48714
00C48710  B1 01                           mov cl, 1
00C48712  EB 02                           jmp 0x140c48716
00C48714  32 C9                           xor cl, cl
00C48716  C1 E8 07                        shr eax, 7
00C48719  24 01                           and al, 1
00C4871B  88 0D CF F4 21 00               mov byte ptr [rip + 0x21f4cf], cl
00C48721  88 0D CA F4 21 00               mov byte ptr [rip + 0x21f4ca], cl
00C48727  B9 01 00 00 00                  mov ecx, 1
00C4872C  88 05 CE F5 21 00               mov byte ptr [rip + 0x21f5ce], al
00C48732  E8 99 1D D8 FF                  call 0x1409ca4d0
00C48737  BF 53 65 53 69                  mov edi, 0x69536553
00C4873C  8B D0                           mov edx, eax
00C4873E  44 8B C7                        mov r8d, edi
00C48741  8B D8                           mov ebx, eax
00C48743  B9 20 01 00 00                  mov ecx, 0x120
00C48748  E8 A3 99 F3 FF                  call 0x140b820f0
00C4874D  BE 60 00 00 00                  mov esi, 0x60
00C48752  48 89 05 1F 14 39 00            mov qword ptr [rip + 0x39141f], rax
00C48759  8B CE                           mov ecx, esi
00C4875B  44 8B C7                        mov r8d, edi
00C4875E  8B D3                           mov edx, ebx
00C48760  E8 8B 99 F3 FF                  call 0x140b820f0
00C48765  44 8B C7                        mov r8d, edi
00C48768  48 89 05 D1 F5 21 00            mov qword ptr [rip + 0x21f5d1], rax
00C4876F  8B D3                           mov edx, ebx
00C48771  8B CE                           mov ecx, esi
00C48773  E8 78 99 F3 FF                  call 0x140b820f0
00C48778  44 8B C7                        mov r8d, edi
00C4877B  48 89 05 66 F5 21 00            mov qword ptr [rip + 0x21f566], rax
00C48782  8B D3                           mov edx, ebx
00C48784  8B CE                           mov ecx, esi
00C48786  E8 65 99 F3 FF                  call 0x140b820f0
00C4878B  44 8B C7                        mov r8d, edi
00C4878E  48 89 05 A3 F5 21 00            mov qword ptr [rip + 0x21f5a3], rax
00C48795  8B D3                           mov edx, ebx
00C48797  8B CE                           mov ecx, esi
00C48799  E8 52 99 F3 FF                  call 0x140b820f0
00C4879E  44 8B C7                        mov r8d, edi
00C487A1  48 89 05 88 F5 21 00            mov qword ptr [rip + 0x21f588], rax
00C487A8  8B D3                           mov edx, ebx
00C487AA  8B CE                           mov ecx, esi
00C487AC  E8 3F 99 F3 FF                  call 0x140b820f0
00C487B1  44 8B C7                        mov r8d, edi
00C487B4  48 89 05 8D F5 21 00            mov qword ptr [rip + 0x21f58d], rax
00C487BB  8B D3                           mov edx, ebx
00C487BD  8B CE                           mov ecx, esi
00C487BF  E8 2C 99 F3 FF                  call 0x140b820f0
00C487C4  44 8B C7                        mov r8d, edi
00C487C7  48 89 05 82 F5 21 00            mov qword ptr [rip + 0x21f582], rax
00C487CE  8B D3                           mov edx, ebx
00C487D0  8B CE                           mov ecx, esi
00C487D2  E8 19 99 F3 FF                  call 0x140b820f0
00C487D7  48 8B 0D 9A 13 39 00            mov rcx, qword ptr [rip + 0x39139a]
00C487DE  48 8B F8                        mov rdi, rax
00C487E1  48 89 05 08 F5 21 00            mov qword ptr [rip + 0x21f508], rax
00C487E8  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
00C487EC  48 85 C9                        test rcx, rcx
00C487EF  0F 84 B8 1D 00 00               je 0x140c4a5ad
00C487F5  48 8B 05 4C F5 21 00            mov rax, qword ptr [rip + 0x21f54c]
00C487FC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C48801  48 85 C0                        test rax, rax
00C48804  0F 84 A3 1D 00 00               je 0x140c4a5ad
00C4880A  4C 8B 25 3F F5 21 00            mov r12, qword ptr [rip + 0x21f53f]
00C48811  4D 85 E4                        test r12, r12
00C48814  0F 84 93 1D 00 00               je 0x140c4a5ad
00C4881A  4C 8B 2D 1F F5 21 00            mov r13, qword ptr [rip + 0x21f51f]
00C48821  4D 85 ED                        test r13, r13
00C48824  0F 84 83 1D 00 00               je 0x140c4a5ad
00C4882A  4C 8B 3D B7 F4 21 00            mov r15, qword ptr [rip + 0x21f4b7]
00C48831  4D 85 FF                        test r15, r15
00C48834  0F 84 73 1D 00 00               je 0x140c4a5ad
00C4883A  4C 8B 35 F7 F4 21 00            mov r14, qword ptr [rip + 0x21f4f7]
00C48841  4D 85 F6                        test r14, r14
00C48844  0F 84 63 1D 00 00               je 0x140c4a5ad
00C4884A  48 85 FF                        test rdi, rdi
00C4884D  0F 84 5A 1D 00 00               je 0x140c4a5ad
00C48853  48 8B 35 D6 F4 21 00            mov rsi, qword ptr [rip + 0x21f4d6]
00C4885A  48 85 F6                        test rsi, rsi
00C4885D  0F 84 4A 1D 00 00               je 0x140c4a5ad
00C48863  41 B0 01                        mov r8b, 1
00C48866  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00C4886B  E8 B0 2E DA FF                  call 0x1409eb720
00C48870  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
00C48875  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00C4887A  41 B0 01                        mov r8b, 1
00C4887D  E8 9E 2E DA FF                  call 0x1409eb720
00C48882  41 B0 01                        mov r8b, 1
00C48885  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00C4888A  49 8B CC                        mov rcx, r12
00C4888D  E8 8E 2E DA FF                  call 0x1409eb720
00C48892  41 B0 01                        mov r8b, 1
00C48895  48 8D 95 40 02 00 00            lea rdx, [rbp + 0x240]
00C4889C  49 8B CD                        mov rcx, r13
00C4889F  E8 7C 2E DA FF                  call 0x1409eb720
00C488A4  41 B0 01                        mov r8b, 1
00C488A7  48 8D 95 40 02 00 00            lea rdx, [rbp + 0x240]
00C488AE  49 8B CF                        mov rcx, r15
00C488B1  E8 6A 2E DA FF                  call 0x1409eb720
00C488B6  41 B0 01                        mov r8b, 1
00C488B9  48 8D 95 40 02 00 00            lea rdx, [rbp + 0x240]
00C488C0  49 8B CE                        mov rcx, r14
00C488C3  E8 58 2E DA FF                  call 0x1409eb720
00C488C8  41 B0 01                        mov r8b, 1
00C488CB  48 8D 95 40 02 00 00            lea rdx, [rbp + 0x240]
00C488D2  48 8B CE                        mov rcx, rsi
00C488D5  E8 46 2E DA FF                  call 0x1409eb720
00C488DA  41 B0 01                        mov r8b, 1
00C488DD  48 8D 95 40 02 00 00            lea rdx, [rbp + 0x240]
00C488E4  48 8B CF                        mov rcx, rdi
00C488E7  E8 34 2E DA FF                  call 0x1409eb720
00C488EC  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00C488F0  33 C9                           xor ecx, ecx
00C488F2  89 48 08                        mov dword ptr [rax + 8], ecx
00C488F5  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
00C488FA  89 48 08                        mov dword ptr [rax + 8], ecx
00C488FD  41 89 4C 24 08                  mov dword ptr [r12 + 8], ecx
00C48902  41 89 4D 08                     mov dword ptr [r13 + 8], ecx
00C48906  41 C7 47 08 01 00 00 00         mov dword ptr [r15 + 8], 1
00C4890E  44 8D 79 02                     lea r15d, [rcx + 2]
00C48912  45 89 7E 08                     mov dword ptr [r14 + 8], r15d
00C48916  C7 46 08 03 00 00 00            mov dword ptr [rsi + 8], 3
00C4891D  C7 47 08 04 00 00 00            mov dword ptr [rdi + 8], 4
00C48924  E8 A7 1B D8 FF                  call 0x1409ca4d0
00C48929  41 BE 53 65 53 69               mov r14d, 0x69536553
00C4892F  8B D0                           mov edx, eax
00C48931  41 BD 20 01 00 00               mov r13d, 0x120
00C48937  45 8B C6                        mov r8d, r14d
00C4893A  41 8B CD                        mov ecx, r13d
00C4893D  E8 AE 97 F3 FF                  call 0x140b820f0
00C48942  45 8B C6                        mov r8d, r14d
00C48945  48 89 05 0C 15 39 00            mov qword ptr [rip + 0x39150c], rax
00C4894C  8B D3                           mov edx, ebx
00C4894E  41 8B CD                        mov ecx, r13d
00C48951  E8 9A 97 F3 FF                  call 0x140b820f0
00C48956  45 8D 67 5E                     lea r12d, [r15 + 0x5e]
00C4895A  48 89 05 E7 13 39 00            mov qword ptr [rip + 0x3913e7], rax
00C48961  41 8B CC                        mov ecx, r12d
00C48964  45 8B C6                        mov r8d, r14d
00C48967  8B D3                           mov edx, ebx
00C48969  E8 82 97 F3 FF                  call 0x140b820f0
00C4896E  45 8B C6                        mov r8d, r14d
00C48971  48 89 05 A8 F3 21 00            mov qword ptr [rip + 0x21f3a8], rax
00C48978  8B D3                           mov edx, ebx
00C4897A  41 8B CC                        mov ecx, r12d
00C4897D  E8 6E 97 F3 FF                  call 0x140b820f0
00C48982  45 8B C6                        mov r8d, r14d
00C48985  48 89 05 9C F3 21 00            mov qword ptr [rip + 0x21f39c], rax
00C4898C  8B D3                           mov edx, ebx
00C4898E  41 8B CC                        mov ecx, r12d
00C48991  E8 5A 97 F3 FF                  call 0x140b820f0
00C48996  45 8B C6                        mov r8d, r14d
00C48999  48 89 05 E0 F1 21 00            mov qword ptr [rip + 0x21f1e0], rax
00C489A0  8B D3                           mov edx, ebx
00C489A2  41 8B CC                        mov ecx, r12d
00C489A5  E8 46 97 F3 FF                  call 0x140b820f0
00C489AA  45 8B C6                        mov r8d, r14d
00C489AD  48 89 05 44 F3 21 00            mov qword ptr [rip + 0x21f344], rax
00C489B4  8B D3                           mov edx, ebx
00C489B6  41 8B CD                        mov ecx, r13d
00C489B9  E8 32 97 F3 FF                  call 0x140b820f0
00C489BE  45 8B C6                        mov r8d, r14d
00C489C1  48 89 05 D8 12 39 00            mov qword ptr [rip + 0x3912d8], rax
00C489C8  8B D3                           mov edx, ebx
00C489CA  41 8B CC                        mov ecx, r12d
00C489CD  E8 1E 97 F3 FF                  call 0x140b820f0
00C489D2  45 8B C6                        mov r8d, r14d
00C489D5  48 89 05 7C F3 21 00            mov qword ptr [rip + 0x21f37c], rax
00C489DC  8B D3                           mov edx, ebx
00C489DE  41 8B CD                        mov ecx, r13d
00C489E1  E8 0A 97 F3 FF                  call 0x140b820f0
00C489E6  45 8B C6                        mov r8d, r14d
00C489E9  48 89 05 B8 12 39 00            mov qword ptr [rip + 0x3912b8], rax
00C489F0  8B D3                           mov edx, ebx
00C489F2  41 8B CD                        mov ecx, r13d
00C489F5  E8 F6 96 F3 FF                  call 0x140b820f0
00C489FA  45 8B C6                        mov r8d, r14d
00C489FD  48 89 05 0C 11 39 00            mov qword ptr [rip + 0x39110c], rax
00C48A04  8B D3                           mov edx, ebx
00C48A06  41 8B CD                        mov ecx, r13d
00C48A09  E8 E2 96 F3 FF                  call 0x140b820f0
00C48A0E  45 8B C6                        mov r8d, r14d
00C48A11  48 89 05 B0 10 39 00            mov qword ptr [rip + 0x3910b0], rax
00C48A18  8B D3                           mov edx, ebx
00C48A1A  41 8B CD                        mov ecx, r13d
00C48A1D  E8 CE 96 F3 FF                  call 0x140b820f0
00C48A22  45 8B C6                        mov r8d, r14d
00C48A25  48 89 05 2C 11 39 00            mov qword ptr [rip + 0x39112c], rax
00C48A2C  8B D3                           mov edx, ebx
00C48A2E  41 8B CD                        mov ecx, r13d
00C48A31  E8 BA 96 F3 FF                  call 0x140b820f0
00C48A36  45 8B C6                        mov r8d, r14d
00C48A39  48 89 05 68 11 39 00            mov qword ptr [rip + 0x391168], rax
00C48A40  8B D3                           mov edx, ebx
00C48A42  41 8B CD                        mov ecx, r13d
00C48A45  E8 A6 96 F3 FF                  call 0x140b820f0
00C48A4A  41 8B CF                        mov ecx, r15d
00C48A4D  48 89 05 D4 11 39 00            mov qword ptr [rip + 0x3911d4], rax
00C48A54  E8 77 1A D8 FF                  call 0x1409ca4d0
00C48A59  45 8B C6                        mov r8d, r14d
00C48A5C  8B D0                           mov edx, eax
00C48A5E  41 8B CD                        mov ecx, r13d
00C48A61  8B F0                           mov esi, eax
00C48A63  E8 88 96 F3 FF                  call 0x140b820f0
00C48A68  45 8B C6                        mov r8d, r14d
00C48A6B  48 89 05 F6 0F 39 00            mov qword ptr [rip + 0x390ff6], rax
00C48A72  8B D6                           mov edx, esi
00C48A74  41 8B CD                        mov ecx, r13d
00C48A77  E8 74 96 F3 FF                  call 0x140b820f0
00C48A7C  45 8B C6                        mov r8d, r14d
00C48A7F  48 89 05 52 11 39 00            mov qword ptr [rip + 0x391152], rax
00C48A86  8B D6                           mov edx, esi
00C48A88  41 8B CD                        mov ecx, r13d
00C48A8B  E8 60 96 F3 FF                  call 0x140b820f0
00C48A90  45 8B C6                        mov r8d, r14d
00C48A93  48 89 05 46 12 39 00            mov qword ptr [rip + 0x391246], rax
00C48A9A  8B D6                           mov edx, esi
00C48A9C  41 8B CD                        mov ecx, r13d
00C48A9F  E8 4C 96 F3 FF                  call 0x140b820f0
00C48AA4  45 8B C6                        mov r8d, r14d
00C48AA7  48 89 05 3A 12 39 00            mov qword ptr [rip + 0x39123a], rax
00C48AAE  8B D6                           mov edx, esi
00C48AB0  41 8B CD                        mov ecx, r13d
00C48AB3  E8 38 96 F3 FF                  call 0x140b820f0
00C48AB8  45 8B C6                        mov r8d, r14d
00C48ABB  48 89 05 0E 12 39 00            mov qword ptr [rip + 0x39120e], rax
00C48AC2  8B D6                           mov edx, esi
00C48AC4  41 8B CD                        mov ecx, r13d
00C48AC7  E8 24 96 F3 FF                  call 0x140b820f0
00C48ACC  45 8B C6                        mov r8d, r14d
00C48ACF  48 89 05 02 12 39 00            mov qword ptr [rip + 0x391202], rax
00C48AD6  8B D6                           mov edx, esi
00C48AD8  41 8B CD                        mov ecx, r13d
00C48ADB  E8 10 96 F3 FF                  call 0x140b820f0
00C48AE0  45 8B C6                        mov r8d, r14d
00C48AE3  48 89 05 06 12 39 00            mov qword ptr [rip + 0x391206], rax
00C48AEA  8B D6                           mov edx, esi
00C48AEC  41 8B CD                        mov ecx, r13d
00C48AEF  E8 FC 95 F3 FF                  call 0x140b820f0
00C48AF4  48 89 05 FD 11 39 00            mov qword ptr [rip + 0x3911fd], rax
00C48AFB  45 8B C6                        mov r8d, r14d
00C48AFE  8B D3                           mov edx, ebx
00C48B00  41 8B CC                        mov ecx, r12d
00C48B03  E8 E8 95 F3 FF                  call 0x140b820f0
00C48B08  45 8B C6                        mov r8d, r14d
00C48B0B  48 89 05 06 CD 2B 00            mov qword ptr [rip + 0x2bcd06], rax
00C48B12  8B D3                           mov edx, ebx
00C48B14  41 8B CC                        mov ecx, r12d
00C48B17  E8 D4 95 F3 FF                  call 0x140b820f0
00C48B1C  45 8B C6                        mov r8d, r14d
00C48B1F  48 89 05 52 CD 2B 00            mov qword ptr [rip + 0x2bcd52], rax
00C48B26  8B D3                           mov edx, ebx
00C48B28  41 8B CC                        mov ecx, r12d
00C48B2B  E8 C0 95 F3 FF                  call 0x140b820f0
00C48B30  45 8B C6                        mov r8d, r14d
00C48B33  48 89 05 E6 CC 2B 00            mov qword ptr [rip + 0x2bcce6], rax
00C48B3A  8B D3                           mov edx, ebx
00C48B3C  41 8B CC                        mov ecx, r12d
00C48B3F  E8 AC 95 F3 FF                  call 0x140b820f0
00C48B44  45 8B C6                        mov r8d, r14d
00C48B47  48 89 05 EA CC 2B 00            mov qword ptr [rip + 0x2bccea], rax
00C48B4E  8B D3                           mov edx, ebx
00C48B50  41 8B CC                        mov ecx, r12d
00C48B53  E8 98 95 F3 FF                  call 0x140b820f0
00C48B58  45 8B C6                        mov r8d, r14d
00C48B5B  48 89 05 DE CC 2B 00            mov qword ptr [rip + 0x2bccde], rax
00C48B62  8B D3                           mov edx, ebx
00C48B64  41 8B CC                        mov ecx, r12d
00C48B67  E8 84 95 F3 FF                  call 0x140b820f0
00C48B6C  45 8B C6                        mov r8d, r14d
00C48B6F  48 89 05 A2 F1 21 00            mov qword ptr [rip + 0x21f1a2], rax
00C48B76  8B D3                           mov edx, ebx
00C48B78  41 8B CC                        mov ecx, r12d
00C48B7B  E8 70 95 F3 FF                  call 0x140b820f0
00C48B80  45 8B C6                        mov r8d, r14d
00C48B83  48 89 05 7E F1 21 00            mov qword ptr [rip + 0x21f17e], rax
00C48B8A  8B D6                           mov edx, esi
00C48B8C  41 8B CC                        mov ecx, r12d
00C48B8F  E8 5C 95 F3 FF                  call 0x140b820f0
00C48B94  45 8B C6                        mov r8d, r14d
00C48B97  48 89 05 C2 F1 21 00            mov qword ptr [rip + 0x21f1c2], rax
00C48B9E  8B D6                           mov edx, esi
00C48BA0  41 8B CC                        mov ecx, r12d
00C48BA3  E8 48 95 F3 FF                  call 0x140b820f0
00C48BA8  41 8D 4F 08                     lea ecx, [r15 + 8]
00C48BAC  48 89 05 0D F0 21 00            mov qword ptr [rip + 0x21f00d], rax
00C48BB3  E8 18 19 D8 FF                  call 0x1409ca4d0
00C48BB8  45 8B C6                        mov r8d, r14d
00C48BBB  8B D0                           mov edx, eax
00C48BBD  41 8B CD                        mov ecx, r13d
00C48BC0  8B F8                           mov edi, eax
00C48BC2  E8 29 95 F3 FF                  call 0x140b820f0
00C48BC7  45 8B C6                        mov r8d, r14d
00C48BCA  48 89 05 CF CB 2B 00            mov qword ptr [rip + 0x2bcbcf], rax
00C48BD1  8B D7                           mov edx, edi
00C48BD3  41 8B CD                        mov ecx, r13d
00C48BD6  E8 15 95 F3 FF                  call 0x140b820f0
00C48BDB  45 8B C6                        mov r8d, r14d
00C48BDE  48 89 05 E3 CB 2B 00            mov qword ptr [rip + 0x2bcbe3], rax
00C48BE5  8B D7                           mov edx, edi
00C48BE7  41 8B CD                        mov ecx, r13d
00C48BEA  E8 01 95 F3 FF                  call 0x140b820f0
00C48BEF  45 8B C6                        mov r8d, r14d
00C48BF2  48 89 05 D7 CB 2B 00            mov qword ptr [rip + 0x2bcbd7], rax
00C48BF9  8B D7                           mov edx, edi
00C48BFB  41 8B CD                        mov ecx, r13d
00C48BFE  E8 ED 94 F3 FF                  call 0x140b820f0
00C48C03  45 8B C6                        mov r8d, r14d
00C48C06  48 89 05 AB CB 2B 00            mov qword ptr [rip + 0x2bcbab], rax
00C48C0D  8B D7                           mov edx, edi
00C48C0F  41 8B CD                        mov ecx, r13d
00C48C12  E8 D9 94 F3 FF                  call 0x140b820f0
00C48C17  45 8B C6                        mov r8d, r14d
00C48C1A  48 89 05 9F CB 2B 00            mov qword ptr [rip + 0x2bcb9f], rax
00C48C21  8B D7                           mov edx, edi
00C48C23  41 8B CD                        mov ecx, r13d
00C48C26  E8 C5 94 F3 FF                  call 0x140b820f0
00C48C2B  45 8B C6                        mov r8d, r14d
00C48C2E  48 89 05 B3 CB 2B 00            mov qword ptr [rip + 0x2bcbb3], rax
00C48C35  8B D7                           mov edx, edi
00C48C37  41 8B CD                        mov ecx, r13d
00C48C3A  E8 B1 94 F3 FF                  call 0x140b820f0
00C48C3F  48 89 05 AA CB 2B 00            mov qword ptr [rip + 0x2bcbaa], rax
00C48C46  45 8B C6                        mov r8d, r14d
00C48C49  8B D7                           mov edx, edi
00C48C4B  41 8B CD                        mov ecx, r13d
00C48C4E  E8 9D 94 F3 FF                  call 0x140b820f0
00C48C53  45 8B C6                        mov r8d, r14d
00C48C56  48 89 05 7B CB 2B 00            mov qword ptr [rip + 0x2bcb7b], rax
00C48C5D  8B D7                           mov edx, edi
00C48C5F  41 8B CD                        mov ecx, r13d
00C48C62  E8 89 94 F3 FF                  call 0x140b820f0
00C48C67  45 8B C6                        mov r8d, r14d
00C48C6A  48 89 05 6F CB 2B 00            mov qword ptr [rip + 0x2bcb6f], rax
00C48C71  8B D7                           mov edx, edi
00C48C73  41 8B CD                        mov ecx, r13d
00C48C76  E8 75 94 F3 FF                  call 0x140b820f0
00C48C7B  45 8B C6                        mov r8d, r14d
00C48C7E  48 89 05 83 CB 2B 00            mov qword ptr [rip + 0x2bcb83], rax
00C48C85  8B D7                           mov edx, edi
00C48C87  41 8B CD                        mov ecx, r13d
00C48C8A  E8 61 94 F3 FF                  call 0x140b820f0
00C48C8F  45 8B C6                        mov r8d, r14d
00C48C92  48 89 05 77 CB 2B 00            mov qword ptr [rip + 0x2bcb77], rax
00C48C99  8B D7                           mov edx, edi
00C48C9B  41 8B CD                        mov ecx, r13d
00C48C9E  E8 4D 94 F3 FF                  call 0x140b820f0
00C48CA3  45 8B C6                        mov r8d, r14d
00C48CA6  48 89 05 4B CB 2B 00            mov qword ptr [rip + 0x2bcb4b], rax
00C48CAD  8B D7                           mov edx, edi
00C48CAF  41 8B CD                        mov ecx, r13d
00C48CB2  E8 39 94 F3 FF                  call 0x140b820f0
00C48CB7  45 8B C6                        mov r8d, r14d
00C48CBA  48 89 05 3F CB 2B 00            mov qword ptr [rip + 0x2bcb3f], rax
00C48CC1  8B D7                           mov edx, edi
00C48CC3  41 8B CD                        mov ecx, r13d
00C48CC6  E8 25 94 F3 FF                  call 0x140b820f0
00C48CCB  45 8B C6                        mov r8d, r14d
00C48CCE  48 89 05 9B CA 2B 00            mov qword ptr [rip + 0x2bca9b], rax
00C48CD5  8B D7                           mov edx, edi
00C48CD7  41 8B CD                        mov ecx, r13d
00C48CDA  E8 11 94 F3 FF                  call 0x140b820f0
00C48CDF  45 8B C6                        mov r8d, r14d
00C48CE2  48 89 05 8F CA 2B 00            mov qword ptr [rip + 0x2bca8f], rax
00C48CE9  8B D7                           mov edx, edi
00C48CEB  41 8B CD                        mov ecx, r13d
00C48CEE  E8 FD 93 F3 FF                  call 0x140b820f0
00C48CF3  45 8B C6                        mov r8d, r14d
00C48CF6  48 89 05 63 CA 2B 00            mov qword ptr [rip + 0x2bca63], rax
00C48CFD  8B D7                           mov edx, edi
00C48CFF  41 8B CD                        mov ecx, r13d
00C48D02  E8 E9 93 F3 FF                  call 0x140b820f0
00C48D07  45 8B C6                        mov r8d, r14d
00C48D0A  48 89 05 57 CA 2B 00            mov qword ptr [rip + 0x2bca57], rax
00C48D11  8B D7                           mov edx, edi
00C48D13  41 8B CD                        mov ecx, r13d
00C48D16  E8 D5 93 F3 FF                  call 0x140b820f0
00C48D1B  41 8D 4F 04                     lea ecx, [r15 + 4]
00C48D1F  48 89 05 62 CA 2B 00            mov qword ptr [rip + 0x2bca62], rax
00C48D26  E8 A5 17 D8 FF                  call 0x1409ca4d0
00C48D2B  8B D8                           mov ebx, eax
00C48D2D  45 8B C6                        mov r8d, r14d
00C48D30  8B D0                           mov edx, eax
00C48D32  41 8B CC                        mov ecx, r12d
00C48D35  48 89 9D 90 01 00 00            mov qword ptr [rbp + 0x190], rbx
00C48D3C  E8 AF 93 F3 FF                  call 0x140b820f0
00C48D41  45 8B C6                        mov r8d, r14d
00C48D44  48 89 05 C5 EF 21 00            mov qword ptr [rip + 0x21efc5], rax
00C48D4B  8B D3                           mov edx, ebx
00C48D4D  41 8B CC                        mov ecx, r12d
00C48D50  E8 9B 93 F3 FF                  call 0x140b820f0
00C48D55  45 8B C6                        mov r8d, r14d
00C48D58  48 89 05 59 EE 21 00            mov qword ptr [rip + 0x21ee59], rax
00C48D5F  8B D6                           mov edx, esi
00C48D61  41 8B CC                        mov ecx, r12d
00C48D64  E8 87 93 F3 FF                  call 0x140b820f0
00C48D69  45 8B C6                        mov r8d, r14d
00C48D6C  48 89 05 B5 CA 2B 00            mov qword ptr [rip + 0x2bcab5], rax
00C48D73  8B D6                           mov edx, esi
00C48D75  41 8B CC                        mov ecx, r12d
00C48D78  E8 73 93 F3 FF                  call 0x140b820f0
00C48D7D  48 89 05 AC CA 2B 00            mov qword ptr [rip + 0x2bcaac], rax
00C48D84  45 8B C6                        mov r8d, r14d
00C48D87  8B D6                           mov edx, esi
00C48D89  41 8B CC                        mov ecx, r12d
00C48D8C  E8 5F 93 F3 FF                  call 0x140b820f0
00C48D91  45 8B C6                        mov r8d, r14d
00C48D94  48 89 05 BD CA 2B 00            mov qword ptr [rip + 0x2bcabd], rax
00C48D9B  8B D6                           mov edx, esi
00C48D9D  41 8B CC                        mov ecx, r12d
00C48DA0  E8 4B 93 F3 FF                  call 0x140b820f0
00C48DA5  45 8B C6                        mov r8d, r14d
00C48DA8  48 89 05 A1 C1 2B 00            mov qword ptr [rip + 0x2bc1a1], rax
00C48DAF  8B D6                           mov edx, esi
00C48DB1  41 8B CC                        mov ecx, r12d
00C48DB4  E8 37 93 F3 FF                  call 0x140b820f0
00C48DB9  45 8B C6                        mov r8d, r14d
00C48DBC  48 89 05 95 C1 2B 00            mov qword ptr [rip + 0x2bc195], rax
00C48DC3  8B D6                           mov edx, esi
00C48DC5  41 8B CC                        mov ecx, r12d
00C48DC8  E8 23 93 F3 FF                  call 0x140b820f0
00C48DCD  45 8B C6                        mov r8d, r14d
00C48DD0  48 89 05 89 CA 2B 00            mov qword ptr [rip + 0x2bca89], rax
00C48DD7  8B D6                           mov edx, esi
00C48DD9  41 8B CC                        mov ecx, r12d
00C48DDC  E8 0F 93 F3 FF                  call 0x140b820f0
00C48DE1  45 8B C6                        mov r8d, r14d
00C48DE4  48 89 05 5D CA 2B 00            mov qword ptr [rip + 0x2bca5d], rax
00C48DEB  8B D6                           mov edx, esi
00C48DED  41 8B CC                        mov ecx, r12d
00C48DF0  E8 FB 92 F3 FF                  call 0x140b820f0
00C48DF5  45 8B C6                        mov r8d, r14d
00C48DF8  48 89 05 51 CA 2B 00            mov qword ptr [rip + 0x2bca51], rax
00C48DFF  8B D6                           mov edx, esi
00C48E01  41 8B CD                        mov ecx, r13d
00C48E04  E8 E7 92 F3 FF                  call 0x140b820f0
00C48E09  45 8B C6                        mov r8d, r14d
00C48E0C  48 89 05 85 C9 2B 00            mov qword ptr [rip + 0x2bc985], rax
00C48E13  8B D7                           mov edx, edi
00C48E15  41 8B CD                        mov ecx, r13d
00C48E18  E8 D3 92 F3 FF                  call 0x140b820f0
00C48E1D  45 8B C6                        mov r8d, r14d
00C48E20  48 89 05 69 C9 2B 00            mov qword ptr [rip + 0x2bc969], rax
00C48E27  8B D7                           mov edx, edi
00C48E29  41 8B CD                        mov ecx, r13d
00C48E2C  E8 BF 92 F3 FF                  call 0x140b820f0
00C48E31  41 8D 4F 07                     lea ecx, [r15 + 7]
00C48E35  48 89 05 44 C9 2B 00            mov qword ptr [rip + 0x2bc944], rax
00C48E3C  E8 8F 16 D8 FF                  call 0x1409ca4d0
00C48E41  45 8B C6                        mov r8d, r14d
00C48E44  8B D0                           mov edx, eax
00C48E46  41 8B CD                        mov ecx, r13d
00C48E49  8B D8                           mov ebx, eax
00C48E4B  E8 A0 92 F3 FF                  call 0x140b820f0
00C48E50  45 8B C6                        mov r8d, r14d
00C48E53  48 89 05 0E CA 2B 00            mov qword ptr [rip + 0x2bca0e], rax
00C48E5A  8B D7                           mov edx, edi
00C48E5C  41 8B CD                        mov ecx, r13d
00C48E5F  E8 8C 92 F3 FF                  call 0x140b820f0
00C48E64  45 8B C6                        mov r8d, r14d
00C48E67  48 89 05 02 CA 2B 00            mov qword ptr [rip + 0x2bca02], rax
00C48E6E  8B D3                           mov edx, ebx
00C48E70  41 8B CD                        mov ecx, r13d
00C48E73  E8 78 92 F3 FF                  call 0x140b820f0
00C48E78  45 8B C6                        mov r8d, r14d
00C48E7B  48 89 05 26 C9 2B 00            mov qword ptr [rip + 0x2bc926], rax
00C48E82  8B D7                           mov edx, edi
00C48E84  41 8B CD                        mov ecx, r13d
00C48E87  E8 64 92 F3 FF                  call 0x140b820f0
00C48E8C  45 8B C6                        mov r8d, r14d
00C48E8F  48 89 05 1A C9 2B 00            mov qword ptr [rip + 0x2bc91a], rax
00C48E96  8B D6                           mov edx, esi
00C48E98  41 8B CC                        mov ecx, r12d
00C48E9B  E8 50 92 F3 FF                  call 0x140b820f0
00C48EA0  45 8B C6                        mov r8d, r14d
00C48EA3  48 89 05 2E ED 21 00            mov qword ptr [rip + 0x21ed2e], rax
00C48EAA  8B D7                           mov edx, edi
00C48EAC  41 8B CD                        mov ecx, r13d
00C48EAF  E8 3C 92 F3 FF                  call 0x140b820f0
00C48EB4  45 8B C6                        mov r8d, r14d
00C48EB7  48 89 05 22 ED 21 00            mov qword ptr [rip + 0x21ed22], rax
00C48EBE  8B D7                           mov edx, edi
00C48EC0  41 8B CD                        mov ecx, r13d
00C48EC3  E8 28 92 F3 FF                  call 0x140b820f0
00C48EC8  48 89 05 F9 EC 21 00            mov qword ptr [rip + 0x21ecf9], rax
00C48ECF  45 8B C6                        mov r8d, r14d
00C48ED2  8B D7                           mov edx, edi
00C48ED4  41 8B CD                        mov ecx, r13d
00C48ED7  E8 14 92 F3 FF                  call 0x140b820f0
00C48EDC  45 8B C6                        mov r8d, r14d
00C48EDF  48 89 05 EA EC 21 00            mov qword ptr [rip + 0x21ecea], rax
00C48EE6  8B D7                           mov edx, edi
00C48EE8  41 8B CD                        mov ecx, r13d
00C48EEB  E8 00 92 F3 FF                  call 0x140b820f0
00C48EF0  48 8B 0D 61 0F 39 00            mov rcx, qword ptr [rip + 0x390f61]
00C48EF7  45 33 C0                        xor r8d, r8d
00C48EFA  48 89 05 E7 EC 21 00            mov qword ptr [rip + 0x21ece7], rax
00C48F01  48 8B D0                        mov rdx, rax
00C48F04  48 85 C9                        test rcx, rcx
00C48F07  0F 84 A0 16 00 00               je 0x140c4a5ad
00C48F0D  48 8B 05 34 0E 39 00            mov rax, qword ptr [rip + 0x390e34]
00C48F14  48 89 85 40 02 00 00            mov qword ptr [rbp + 0x240], rax
00C48F1B  48 85 C0                        test rax, rax
00C48F1E  0F 84 89 16 00 00               je 0x140c4a5ad
00C48F24  48 8B 05 F5 ED 21 00            mov rax, qword ptr [rip + 0x21edf5]
00C48F2B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C48F30  48 85 C0                        test rax, rax
00C48F33  0F 84 74 16 00 00               je 0x140c4a5ad
00C48F39  48 8B 05 E8 ED 21 00            mov rax, qword ptr [rip + 0x21ede8]
00C48F40  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00C48F44  48 85 C0                        test rax, rax
00C48F47  0F 84 60 16 00 00               je 0x140c4a5ad
00C48F4D  48 8B 05 2C EC 21 00            mov rax, qword ptr [rip + 0x21ec2c]
00C48F54  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
00C48F58  48 85 C0                        test rax, rax
00C48F5B  0F 84 4C 16 00 00               je 0x140c4a5ad
00C48F61  48 8B 05 38 0D 39 00            mov rax, qword ptr [rip + 0x390d38]
00C48F68  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00C48F6C  48 85 C0                        test rax, rax
00C48F6F  0F 84 38 16 00 00               je 0x140c4a5ad
00C48F75  48 8B 05 7C ED 21 00            mov rax, qword ptr [rip + 0x21ed7c]
00C48F7C  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
00C48F80  48 85 C0                        test rax, rax
00C48F83  0F 84 24 16 00 00               je 0x140c4a5ad
00C48F89  48 8B 05 C8 ED 21 00            mov rax, qword ptr [rip + 0x21edc8]
00C48F90  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00C48F94  48 85 C0                        test rax, rax
00C48F97  0F 84 10 16 00 00               je 0x140c4a5ad
00C48F9D  48 8B 05 04 0D 39 00            mov rax, qword ptr [rip + 0x390d04]
00C48FA4  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
00C48FA8  48 85 C0                        test rax, rax
00C48FAB  0F 84 FC 15 00 00               je 0x140c4a5ad
00C48FB1  48 8B 05 58 0B 39 00            mov rax, qword ptr [rip + 0x390b58]
00C48FB8  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00C48FBC  48 85 C0                        test rax, rax
00C48FBF  0F 84 E8 15 00 00               je 0x140c4a5ad
00C48FC5  48 8B 05 FC 0A 39 00            mov rax, qword ptr [rip + 0x390afc]
00C48FCC  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00C48FD1  48 85 C0                        test rax, rax
00C48FD4  0F 84 D3 15 00 00               je 0x140c4a5ad
00C48FDA  48 8B 05 77 0B 39 00            mov rax, qword ptr [rip + 0x390b77]
00C48FE1  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00C48FE6  48 85 C0                        test rax, rax
00C48FE9  0F 84 BE 15 00 00               je 0x140c4a5ad
00C48FEF  48 8B 05 B2 0B 39 00            mov rax, qword ptr [rip + 0x390bb2]
00C48FF6  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00C48FFB  48 85 C0                        test rax, rax
00C48FFE  0F 84 A9 15 00 00               je 0x140c4a5ad
00C49004  48 8B 05 1D 0C 39 00            mov rax, qword ptr [rip + 0x390c1d]
00C4900B  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00C49010  48 85 C0                        test rax, rax
00C49013  0F 84 94 15 00 00               je 0x140c4a5ad
00C49019  48 8B 05 48 0A 39 00            mov rax, qword ptr [rip + 0x390a48]
00C49020  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00C49025  48 85 C0                        test rax, rax
00C49028  0F 84 7F 15 00 00               je 0x140c4a5ad
00C4902E  48 8B 05 A3 0B 39 00            mov rax, qword ptr [rip + 0x390ba3]
00C49035  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00C4903A  48 85 C0                        test rax, rax
00C4903D  0F 84 6A 15 00 00               je 0x140c4a5ad
00C49043  48 8B 05 96 0C 39 00            mov rax, qword ptr [rip + 0x390c96]
00C4904A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00C4904F  48 85 C0                        test rax, rax
00C49052  0F 84 55 15 00 00               je 0x140c4a5ad
00C49058  48 8B 05 89 0C 39 00            mov rax, qword ptr [rip + 0x390c89]
00C4905F  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00C49064  48 85 C0                        test rax, rax
00C49067  0F 84 40 15 00 00               je 0x140c4a5ad
00C4906D  48 8B 05 5C 0C 39 00            mov rax, qword ptr [rip + 0x390c5c]
00C49074  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00C49079  48 85 C0                        test rax, rax
00C4907C  0F 84 2B 15 00 00               je 0x140c4a5ad
00C49082  4C 8B 25 4F 0C 39 00            mov r12, qword ptr [rip + 0x390c4f]
00C49089  4D 85 E4                        test r12, r12
00C4908C  0F 84 1B 15 00 00               je 0x140c4a5ad
00C49092  4C 8B 2D 57 0C 39 00            mov r13, qword ptr [rip + 0x390c57]
00C49099  4D 85 ED                        test r13, r13
00C4909C  0F 84 0B 15 00 00               je 0x140c4a5ad
00C490A2  4C 8B 3D 4F 0C 39 00            mov r15, qword ptr [rip + 0x390c4f]
00C490A9  4D 85 FF                        test r15, r15
00C490AC  0F 84 FB 14 00 00               je 0x140c4a5ad
00C490B2  48 8B 05 5F C7 2B 00            mov rax, qword ptr [rip + 0x2bc75f]
00C490B9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00C490BE  48 85 C0                        test rax, rax
00C490C1  0F 84 E6 14 00 00               je 0x140c4a5ad
00C490C7  48 8B 05 AA C7 2B 00            mov rax, qword ptr [rip + 0x2bc7aa]
00C490CE  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00C490D2  48 85 C0                        test rax, rax
00C490D5  0F 84 D2 14 00 00               je 0x140c4a5ad
00C490DB  48 8B 05 3E C7 2B 00            mov rax, qword ptr [rip + 0x2bc73e]
00C490E2  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00C490E6  48 85 C0                        test rax, rax
00C490E9  0F 84 BE 14 00 00               je 0x140c4a5ad
00C490EF  48 8B 05 42 C7 2B 00            mov rax, qword ptr [rip + 0x2bc742]
00C490F6  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00C490FA  48 85 C0                        test rax, rax
00C490FD  0F 84 AA 14 00 00               je 0x140c4a5ad
00C49103  48 8B 05 36 C7 2B 00            mov rax, qword ptr [rip + 0x2bc736]
00C4910A  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00C4910E  48 85 C0                        test rax, rax
00C49111  0F 84 96 14 00 00               je 0x140c4a5ad
00C49117  48 8B 05 FA EB 21 00            mov rax, qword ptr [rip + 0x21ebfa]
00C4911E  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00C49122  48 85 C0                        test rax, rax
00C49125  0F 84 82 14 00 00               je 0x140c4a5ad
00C4912B  48 8B 05 D6 EB 21 00            mov rax, qword ptr [rip + 0x21ebd6]
00C49132  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
00C49136  48 85 C0                        test rax, rax
00C49139  0F 84 6E 14 00 00               je 0x140c4a5ad
00C4913F  48 8B 35 1A EC 21 00            mov rsi, qword ptr [rip + 0x21ec1a]
00C49146  48 85 F6                        test rsi, rsi
00C49149  0F 84 5E 14 00 00               je 0x140c4a5ad
00C4914F  48 8B 3D 6A EA 21 00            mov rdi, qword ptr [rip + 0x21ea6a]
00C49156  48 85 FF                        test rdi, rdi
00C49159  0F 84 4E 14 00 00               je 0x140c4a5ad
00C4915F  4C 39 05 3A C6 2B 00            cmp qword ptr [rip + 0x2bc63a], r8
00C49166  0F 84 41 14 00 00               je 0x140c4a5ad
00C4916C  4C 39 05 55 C6 2B 00            cmp qword ptr [rip + 0x2bc655], r8
00C49173  0F 84 34 14 00 00               je 0x140c4a5ad
00C49179  4C 39 05 50 C6 2B 00            cmp qword ptr [rip + 0x2bc650], r8
00C49180  0F 84 27 14 00 00               je 0x140c4a5ad
00C49186  4C 39 05 2B C6 2B 00            cmp qword ptr [rip + 0x2bc62b], r8
00C4918D  0F 84 1A 14 00 00               je 0x140c4a5ad
00C49193  4C 39 05 26 C6 2B 00            cmp qword ptr [rip + 0x2bc626], r8
00C4919A  0F 84 0D 14 00 00               je 0x140c4a5ad
00C491A0  4C 39 05 41 C6 2B 00            cmp qword ptr [rip + 0x2bc641], r8
00C491A7  0F 84 00 14 00 00               je 0x140c4a5ad
00C491AD  4C 39 05 3C C6 2B 00            cmp qword ptr [rip + 0x2bc63c], r8
00C491B4  0F 84 F3 13 00 00               je 0x140c4a5ad
00C491BA  4C 39 05 17 C6 2B 00            cmp qword ptr [rip + 0x2bc617], r8
00C491C1  0F 84 E6 13 00 00               je 0x140c4a5ad
00C491C7  4C 39 05 12 C6 2B 00            cmp qword ptr [rip + 0x2bc612], r8
00C491CE  0F 84 D9 13 00 00               je 0x140c4a5ad
00C491D4  4C 39 05 2D C6 2B 00            cmp qword ptr [rip + 0x2bc62d], r8
00C491DB  0F 84 CC 13 00 00               je 0x140c4a5ad
00C491E1  4C 39 05 28 C6 2B 00            cmp qword ptr [rip + 0x2bc628], r8
00C491E8  0F 84 BF 13 00 00               je 0x140c4a5ad
00C491EE  4C 39 05 03 C6 2B 00            cmp qword ptr [rip + 0x2bc603], r8
00C491F5  0F 84 B2 13 00 00               je 0x140c4a5ad
00C491FB  4C 39 05 FE C5 2B 00            cmp qword ptr [rip + 0x2bc5fe], r8
00C49202  0F 84 A5 13 00 00               je 0x140c4a5ad
00C49208  4C 39 05 61 C5 2B 00            cmp qword ptr [rip + 0x2bc561], r8
00C4920F  0F 84 98 13 00 00               je 0x140c4a5ad
00C49215  4C 39 05 5C C5 2B 00            cmp qword ptr [rip + 0x2bc55c], r8
00C4921C  0F 84 8B 13 00 00               je 0x140c4a5ad
00C49222  4C 39 05 37 C5 2B 00            cmp qword ptr [rip + 0x2bc537], r8
00C49229  0F 84 7E 13 00 00               je 0x140c4a5ad
00C4922F  4C 39 05 32 C5 2B 00            cmp qword ptr [rip + 0x2bc532], r8
00C49236  0F 84 71 13 00 00               je 0x140c4a5ad
00C4923C  4C 39 05 45 C5 2B 00            cmp qword ptr [rip + 0x2bc545], r8
00C49243  0F 84 64 13 00 00               je 0x140c4a5ad
00C49249  4C 8B 35 C0 EA 21 00            mov r14, qword ptr [rip + 0x21eac0]
00C49250  4D 85 F6                        test r14, r14
00C49253  0F 84 54 13 00 00               je 0x140c4a5ad
00C49259  48 8B 05 C8 C5 2B 00            mov rax, qword ptr [rip + 0x2bc5c8]
00C49260  48 89 85 A0 01 00 00            mov qword ptr [rbp + 0x1a0], rax
00C49267  48 85 C0                        test rax, rax
00C4926A  0F 84 3D 13 00 00               je 0x140c4a5ad
00C49270  48 8B 05 B9 C5 2B 00            mov rax, qword ptr [rip + 0x2bc5b9]
00C49277  48 89 85 A8 01 00 00            mov qword ptr [rbp + 0x1a8], rax
00C4927E  48 85 C0                        test rax, rax
00C49281  0F 84 26 13 00 00               je 0x140c4a5ad
00C49287  48 8B 05 CA C5 2B 00            mov rax, qword ptr [rip + 0x2bc5ca]
00C4928E  48 89 85 B0 01 00 00            mov qword ptr [rbp + 0x1b0], rax
00C49295  48 85 C0                        test rax, rax
00C49298  0F 84 0F 13 00 00               je 0x140c4a5ad
00C4929E  48 8B 05 AB BC 2B 00            mov rax, qword ptr [rip + 0x2bbcab]
00C492A5  48 89 85 C0 01 00 00            mov qword ptr [rbp + 0x1c0], rax
00C492AC  48 85 C0                        test rax, rax
00C492AF  0F 84 F8 12 00 00               je 0x140c4a5ad
00C492B5  48 8B 05 9C BC 2B 00            mov rax, qword ptr [rip + 0x2bbc9c]
00C492BC  48 89 85 D8 01 00 00            mov qword ptr [rbp + 0x1d8], rax
00C492C3  48 85 C0                        test rax, rax
00C492C6  0F 84 E1 12 00 00               je 0x140c4a5ad
00C492CC  48 8B 05 8D C5 2B 00            mov rax, qword ptr [rip + 0x2bc58d]
00C492D3  48 89 85 B8 01 00 00            mov qword ptr [rbp + 0x1b8], rax
00C492DA  48 85 C0                        test rax, rax
00C492DD  0F 84 CA 12 00 00               je 0x140c4a5ad
00C492E3  48 8B 05 5E C5 2B 00            mov rax, qword ptr [rip + 0x2bc55e]
00C492EA  48 89 85 C8 01 00 00            mov qword ptr [rbp + 0x1c8], rax
00C492F1  48 85 C0                        test rax, rax
00C492F4  0F 84 B3 12 00 00               je 0x140c4a5ad
00C492FA  48 8B 05 4F C5 2B 00            mov rax, qword ptr [rip + 0x2bc54f]
00C49301  48 89 85 98 01 00 00            mov qword ptr [rbp + 0x198], rax
00C49308  48 85 C0                        test rax, rax
00C4930B  0F 84 9C 12 00 00               je 0x140c4a5ad
00C49311  48 8B 05 A0 E8 21 00            mov rax, qword ptr [rip + 0x21e8a0]
00C49318  48 89 85 88 01 00 00            mov qword ptr [rbp + 0x188], rax
00C4931F  48 85 C0                        test rax, rax
00C49322  0F 84 85 12 00 00               je 0x140c4a5ad
00C49328  4C 39 05 69 C4 2B 00            cmp qword ptr [rip + 0x2bc469], r8
00C4932F  0F 84 78 12 00 00               je 0x140c4a5ad
00C49335  4C 39 05 54 C4 2B 00            cmp qword ptr [rip + 0x2bc454], r8
00C4933C  0F 84 6B 12 00 00               je 0x140c4a5ad
00C49342  4C 39 05 37 C4 2B 00            cmp qword ptr [rip + 0x2bc437], r8
00C49349  0F 84 5E 12 00 00               je 0x140c4a5ad
00C4934F  4C 39 05 1A C5 2B 00            cmp qword ptr [rip + 0x2bc51a], r8
00C49356  0F 84 51 12 00 00               je 0x140c4a5ad
00C4935C  48 8B 05 05 C5 2B 00            mov rax, qword ptr [rip + 0x2bc505]
00C49363  48 89 85 D0 01 00 00            mov qword ptr [rbp + 0x1d0], rax
00C4936A  48 85 C0                        test rax, rax
00C4936D  0F 84 3A 12 00 00               je 0x140c4a5ad
00C49373  4C 39 05 36 C4 2B 00            cmp qword ptr [rip + 0x2bc436], r8
00C4937A  0F 84 2D 12 00 00               je 0x140c4a5ad
00C49380  4C 39 05 21 C4 2B 00            cmp qword ptr [rip + 0x2bc421], r8
00C49387  0F 84 20 12 00 00               je 0x140c4a5ad
00C4938D  48 8B 1D 44 E8 21 00            mov rbx, qword ptr [rip + 0x21e844]
00C49394  48 85 DB                        test rbx, rbx
00C49397  0F 84 10 12 00 00               je 0x140c4a5ad
00C4939D  4C 39 05 24 E8 21 00            cmp qword ptr [rip + 0x21e824], r8
00C493A4  0F 84 03 12 00 00               je 0x140c4a5ad
00C493AA  4C 39 05 2F E8 21 00            cmp qword ptr [rip + 0x21e82f], r8
00C493B1  0F 84 F6 11 00 00               je 0x140c4a5ad
00C493B7  4C 39 05 12 E8 21 00            cmp qword ptr [rip + 0x21e812], r8
00C493BE  0F 84 E9 11 00 00               je 0x140c4a5ad
00C493C4  48 85 D2                        test rdx, rdx
00C493C7  0F 84 E0 11 00 00               je 0x140c4a5ad
00C493CD  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C493D4  E8 47 23 DA FF                  call 0x1409eb720
00C493D9  48 8B 8D 40 02 00 00            mov rcx, qword ptr [rbp + 0x240]
00C493E0  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C493E7  41 B0 01                        mov r8b, 1
00C493EA  E8 31 23 DA FF                  call 0x1409eb720
00C493EF  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
00C493F4  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C493FB  41 B0 01                        mov r8b, 1
00C493FE  E8 1D 23 DA FF                  call 0x1409eb720
00C49403  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
00C49407  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C4940E  41 B0 01                        mov r8b, 1
00C49411  E8 0A 23 DA FF                  call 0x1409eb720
00C49416  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00C4941A  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C49421  41 B0 01                        mov r8b, 1
00C49424  E8 F7 22 DA FF                  call 0x1409eb720
00C49429  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
00C4942D  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C49434  41 B0 01                        mov r8b, 1
00C49437  E8 E4 22 DA FF                  call 0x1409eb720
00C4943C  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
00C49440  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C49447  41 B0 01                        mov r8b, 1
00C4944A  E8 D1 22 DA FF                  call 0x1409eb720
00C4944F  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
00C49453  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C4945A  41 B0 01                        mov r8b, 1
00C4945D  E8 BE 22 DA FF                  call 0x1409eb720
00C49462  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
00C49466  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C4946D  41 B0 01                        mov r8b, 1
00C49470  E8 AB 22 DA FF                  call 0x1409eb720
00C49475  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
00C49479  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C49480  41 B0 01                        mov r8b, 1
00C49483  E8 98 22 DA FF                  call 0x1409eb720
00C49488  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00C4948D  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C49494  41 B0 01                        mov r8b, 1
00C49497  E8 84 22 DA FF                  call 0x1409eb720
00C4949C  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00C494A1  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C494A8  41 B0 01                        mov r8b, 1
00C494AB  E8 70 22 DA FF                  call 0x1409eb720
00C494B0  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00C494B5  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C494BC  41 B0 01                        mov r8b, 1
00C494BF  E8 5C 22 DA FF                  call 0x1409eb720
00C494C4  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00C494C9  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C494D0  41 B0 01                        mov r8b, 1
00C494D3  E8 48 22 DA FF                  call 0x1409eb720
00C494D8  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00C494DD  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C494E4  41 B0 02                        mov r8b, 2
00C494E7  E8 34 22 DA FF                  call 0x1409eb720
00C494EC  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00C494F1  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C494F8  41 B0 02                        mov r8b, 2
00C494FB  E8 20 22 DA FF                  call 0x1409eb720
00C49500  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00C49505  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C4950C  41 B0 02                        mov r8b, 2
00C4950F  E8 0C 22 DA FF                  call 0x1409eb720
00C49514  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00C49519  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C49520  41 B0 02                        mov r8b, 2
00C49523  E8 F8 21 DA FF                  call 0x1409eb720
00C49528  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00C4952D  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C49534  41 B0 02                        mov r8b, 2
00C49537  E8 E4 21 DA FF                  call 0x1409eb720
00C4953C  41 B0 02                        mov r8b, 2
00C4953F  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C49546  49 8B CC                        mov rcx, r12
00C49549  E8 D2 21 DA FF                  call 0x1409eb720
00C4954E  41 B0 02                        mov r8b, 2
00C49551  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C49558  49 8B CD                        mov rcx, r13
00C4955B  E8 C0 21 DA FF                  call 0x1409eb720
00C49560  41 B0 02                        mov r8b, 2
00C49563  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C4956A  49 8B CF                        mov rcx, r15
00C4956D  E8 AE 21 DA FF                  call 0x1409eb720
00C49572  48 8B 8D 88 01 00 00            mov rcx, qword ptr [rbp + 0x188]
00C49579  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C49580  41 B0 06                        mov r8b, 6
00C49583  E8 98 21 DA FF                  call 0x1409eb720
00C49588  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00C4958D  48 8D 95 48 02 00 00            lea rdx, [rbp + 0x248]
00C49594  41 B0 01                        mov r8b, 1
00C49597  E8 84 21 DA FF                  call 0x1409eb720
00C4959C  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00C495A0  48 8D 95 48 02 00 00            lea rdx, [rbp + 0x248]
00C495A7  41 B0 01                        mov r8b, 1
00C495AA  E8 71 21 DA FF                  call 0x1409eb720
00C495AF  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00C495B3  48 8D 95 48 02 00 00            lea rdx, [rbp + 0x248]
00C495BA  41 B0 01                        mov r8b, 1
00C495BD  E8 5E 21 DA FF                  call 0x1409eb720
00C495C2  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00C495C6  48 8D 95 48 02 00 00            lea rdx, [rbp + 0x248]
00C495CD  41 B0 01                        mov r8b, 1
00C495D0  E8 4B 21 DA FF                  call 0x1409eb720
00C495D5  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00C495D9  48 8D 95 48 02 00 00            lea rdx, [rbp + 0x248]
00C495E0  41 B0 01                        mov r8b, 1
00C495E3  E8 38 21 DA FF                  call 0x1409eb720
00C495E8  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00C495EC  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
00C495F1  41 B0 01                        mov r8b, 1
00C495F4  E8 27 21 DA FF                  call 0x1409eb720
00C495F9  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
00C495FD  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
00C49602  41 B0 01                        mov r8b, 1
00C49605  E8 16 21 DA FF                  call 0x1409eb720
00C4960A  41 B0 02                        mov r8b, 2
00C4960D  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
00C49612  48 8B CE                        mov rcx, rsi
00C49615  E8 06 21 DA FF                  call 0x1409eb720
00C4961A  41 B0 02                        mov r8b, 2
00C4961D  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
00C49622  48 8B CF                        mov rcx, rdi
00C49625  E8 F6 20 DA FF                  call 0x1409eb720
00C4962A  4C 8B 85 90 01 00 00            mov r8, qword ptr [rbp + 0x190]
00C49631  33 D2                           xor edx, edx
00C49633  49 8B CE                        mov rcx, r14
00C49636  E8 05 D6 A7 FF                  call 0x1406c6c40
00C4963B  41 B0 06                        mov r8b, 6
00C4963E  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C49645  49 8B CE                        mov rcx, r14
00C49648  E8 D3 20 DA FF                  call 0x1409eb720
00C4964D  48 8B 8D 98 01 00 00            mov rcx, qword ptr [rbp + 0x198]
00C49654  48 8D 95 38 02 00 00            lea rdx, [rbp + 0x238]
00C4965B  41 BE 02 00 00 00               mov r14d, 2
00C49661  45 8A C6                        mov r8b, r14b
00C49664  E8 B7 20 DA FF                  call 0x1409eb720
00C49669  48 8B 8D A0 01 00 00            mov rcx, qword ptr [rbp + 0x1a0]
00C49670  48 8D 95 38 02 00 00            lea rdx, [rbp + 0x238]
00C49677  45 8A C6                        mov r8b, r14b
00C4967A  E8 A1 20 DA FF                  call 0x1409eb720
00C4967F  48 8B 8D A8 01 00 00            mov rcx, qword ptr [rbp + 0x1a8]
00C49686  48 8D 95 38 02 00 00            lea rdx, [rbp + 0x238]
00C4968D  45 8A C6                        mov r8b, r14b
00C49690  E8 8B 20 DA FF                  call 0x1409eb720
00C49695  48 8B 8D B0 01 00 00            mov rcx, qword ptr [rbp + 0x1b0]
00C4969C  48 8D 95 38 02 00 00            lea rdx, [rbp + 0x238]
00C496A3  45 8A C6                        mov r8b, r14b
00C496A6  E8 75 20 DA FF                  call 0x1409eb720
00C496AB  48 8B 8D C0 01 00 00            mov rcx, qword ptr [rbp + 0x1c0]
00C496B2  48 8D 95 38 02 00 00            lea rdx, [rbp + 0x238]
00C496B9  45 8A C6                        mov r8b, r14b
00C496BC  E8 5F 20 DA FF                  call 0x1409eb720
00C496C1  48 8B 8D D8 01 00 00            mov rcx, qword ptr [rbp + 0x1d8]
00C496C8  48 8D 95 38 02 00 00            lea rdx, [rbp + 0x238]
00C496CF  45 8A C6                        mov r8b, r14b
00C496D2  E8 49 20 DA FF                  call 0x1409eb720
00C496D7  48 8B 8D B8 01 00 00            mov rcx, qword ptr [rbp + 0x1b8]
00C496DE  48 8D 95 38 02 00 00            lea rdx, [rbp + 0x238]
00C496E5  45 8A C6                        mov r8b, r14b
00C496E8  E8 33 20 DA FF                  call 0x1409eb720
00C496ED  48 8B 8D C8 01 00 00            mov rcx, qword ptr [rbp + 0x1c8]
00C496F4  48 8D 95 38 02 00 00            lea rdx, [rbp + 0x238]
00C496FB  45 8A C6                        mov r8b, r14b
00C496FE  E8 1D 20 DA FF                  call 0x1409eb720
00C49703  45 8A C6                        mov r8b, r14b
00C49706  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
00C4970B  48 8B CB                        mov rcx, rbx
00C4970E  E8 0D 20 DA FF                  call 0x1409eb720
00C49713  48 8B 85 40 02 00 00            mov rax, qword ptr [rbp + 0x240]
00C4971A  45 8D 56 1E                     lea r10d, [r14 + 0x1e]
00C4971E  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
00C49723  45 8D 5E 01                     lea r11d, [r14 + 1]
00C49727  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
00C4972C  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00C49731  C7 40 08 01 00 00 00            mov dword ptr [rax + 8], 1
00C49738  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
00C4973D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00C49742  44 89 70 08                     mov dword ptr [rax + 8], r14d
00C49746  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00C4974A  44 89 58 08                     mov dword ptr [rax + 8], r11d
00C4974E  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
00C49752  C7 40 08 04 00 00 00            mov dword ptr [rax + 8], 4
00C49759  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00C4975D  C7 40 08 06 00 00 00            mov dword ptr [rax + 8], 6
00C49764  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
00C49768  C7 40 08 0A 00 00 00            mov dword ptr [rax + 8], 0xa
00C4976F  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00C49773  C7 40 08 12 00 00 00            mov dword ptr [rax + 8], 0x12
00C4977A  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00C4977E  C7 40 08 0B 00 00 00            mov dword ptr [rax + 8], 0xb
00C49785  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00C49789  C7 40 08 0C 00 00 00            mov dword ptr [rax + 8], 0xc
00C49790  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00C49795  C7 40 08 07 00 00 00            mov dword ptr [rax + 8], 7
00C4979C  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00C497A1  C7 40 08 13 00 00 00            mov dword ptr [rax + 8], 0x13
00C497A8  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00C497AD  C7 40 08 14 00 00 00            mov dword ptr [rax + 8], 0x14
00C497B4  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00C497B9  C7 40 08 11 00 00 00            mov dword ptr [rax + 8], 0x11
00C497C0  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00C497C5  45 89 51 08                     mov dword ptr [r9 + 8], r10d
00C497C9  45 89 50 08                     mov dword ptr [r8 + 8], r10d
00C497CD  44 89 52 08                     mov dword ptr [rdx + 8], r10d
00C497D1  44 89 51 08                     mov dword ptr [rcx + 8], r10d
00C497D5  44 89 50 08                     mov dword ptr [rax + 8], r10d
00C497D9  45 89 54 24 08                  mov dword ptr [r12 + 8], r10d
00C497DE  45 89 55 08                     mov dword ptr [r13 + 8], r10d
00C497E2  45 89 57 08                     mov dword ptr [r15 + 8], r10d
00C497E6  41 C7 41 0C 20 02 00 00         mov dword ptr [r9 + 0xc], 0x220
00C497EE  41 C7 40 0C 21 02 00 00         mov dword ptr [r8 + 0xc], 0x221
00C497F6  C7 42 0C 22 02 00 00            mov dword ptr [rdx + 0xc], 0x222
00C497FD  C7 41 0C 23 02 00 00            mov dword ptr [rcx + 0xc], 0x223
00C49804  C7 40 0C 24 02 00 00            mov dword ptr [rax + 0xc], 0x224
00C4980B  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00C49810  41 C7 44 24 0C 25 02 00 00      mov dword ptr [r12 + 0xc], 0x225
00C49819  41 BC 00 20 00 00               mov r12d, 0x2000
00C4981F  41 C7 45 0C 26 02 00 00         mov dword ptr [r13 + 0xc], 0x226
00C49827  41 C7 47 0C 27 02 00 00         mov dword ptr [r15 + 0xc], 0x227
00C4982F  41 BF 00 10 00 00               mov r15d, 0x1000
00C49835  83 60 08 00                     and dword ptr [rax + 8], 0
00C49839  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00C4983D  44 89 78 08                     mov dword ptr [rax + 8], r15d
00C49841  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00C49845  44 89 60 08                     mov dword ptr [rax + 8], r12d
00C49849  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00C4984D  C7 40 08 00 30 00 00            mov dword ptr [rax + 8], 0x3000
00C49854  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
00C49858  C7 40 08 00 40 00 00            mov dword ptr [rax + 8], 0x4000
00C4985F  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00C49863  44 89 70 08                     mov dword ptr [rax + 8], r14d
00C49867  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
00C4986B  44 89 58 08                     mov dword ptr [rax + 8], r11d
00C4986F  44 89 76 08                     mov dword ptr [rsi + 8], r14d
00C49873  C7 46 0C 01 00 00 00            mov dword ptr [rsi + 0xc], 1
00C4987A  44 89 77 08                     mov dword ptr [rdi + 8], r14d
00C4987E  44 89 77 0C                     mov dword ptr [rdi + 0xc], r14d
00C49882  44 89 5B 08                     mov dword ptr [rbx + 8], r11d
00C49886  C7 43 0C 00 00 01 00            mov dword ptr [rbx + 0xc], 0x10000
00C4988D  4C 8B 05 0C BF 2B 00            mov r8, qword ptr [rip + 0x2bbf0c]
00C49894  48 8B 95 D0 01 00 00            mov rdx, qword ptr [rbp + 0x1d0]
00C4989B  48 8D 4D 58                     lea rcx, [rbp + 0x58]
00C4989F  E8 1C B5 82 FF                  call 0x140474dc0
00C498A4  33 FF                           xor edi, edi
00C498A6  85 C0                           test eax, eax
00C498A8  0F 88 FF 0C 00 00               js 0x140c4a5ad
00C498AE  4C 8B 05 13 BF 2B 00            mov r8, qword ptr [rip + 0x2bbf13]
00C498B5  48 8D 4D 68                     lea rcx, [rbp + 0x68]
00C498B9  48 8B 15 A8 BF 2B 00            mov rdx, qword ptr [rip + 0x2bbfa8]
00C498C0  E8 FB B4 82 FF                  call 0x140474dc0
00C498C5  85 C0                           test eax, eax
00C498C7  0F 88 E0 0C 00 00               js 0x140c4a5ad
00C498CD  4C 8B 05 FC BE 2B 00            mov r8, qword ptr [rip + 0x2bbefc]
00C498D4  48 8D 4D 48                     lea rcx, [rbp + 0x48]
00C498D8  48 8B 15 89 BF 2B 00            mov rdx, qword ptr [rip + 0x2bbf89]
00C498DF  E8 DC B4 82 FF                  call 0x140474dc0
00C498E4  85 C0                           test eax, eax
00C498E6  0F 88 C1 0C 00 00               js 0x140c4a5ad
00C498EC  4C 8B 05 C5 BE 2B 00            mov r8, qword ptr [rip + 0x2bbec5]
00C498F3  48 8D 4D 78                     lea rcx, [rbp + 0x78]
00C498F7  48 8B 15 6A BF 2B 00            mov rdx, qword ptr [rip + 0x2bbf6a]
00C498FE  E8 BD B4 82 FF                  call 0x140474dc0
00C49903  85 C0                           test eax, eax
00C49905  0F 88 A2 0C 00 00               js 0x140c4a5ad
00C4990B  4C 8B 05 AE BE 2B 00            mov r8, qword ptr [rip + 0x2bbeae]
00C49912  48 8D 8D 88 00 00 00            lea rcx, [rbp + 0x88]
00C49919  48 8B 15 48 BF 2B 00            mov rdx, qword ptr [rip + 0x2bbf48]
00C49920  E8 9B B4 82 FF                  call 0x140474dc0
00C49925  85 C0                           test eax, eax
00C49927  0F 88 80 0C 00 00               js 0x140c4a5ad
00C4992D  4C 8B 05 B4 BE 2B 00            mov r8, qword ptr [rip + 0x2bbeb4]
00C49934  48 8D 8D 98 00 00 00            lea rcx, [rbp + 0x98]
00C4993B  48 8B 15 26 BF 2B 00            mov rdx, qword ptr [rip + 0x2bbf26]
00C49942  E8 79 B4 82 FF                  call 0x140474dc0
00C49947  85 C0                           test eax, eax
00C49949  0F 88 5E 0C 00 00               js 0x140c4a5ad
00C4994F  4C 8B 05 9A BE 2B 00            mov r8, qword ptr [rip + 0x2bbe9a]
00C49956  48 8D 8D A8 00 00 00            lea rcx, [rbp + 0xa8]
00C4995D  48 8B 15 04 BF 2B 00            mov rdx, qword ptr [rip + 0x2bbf04]
00C49964  E8 57 B4 82 FF                  call 0x140474dc0
00C49969  85 C0                           test eax, eax
00C4996B  0F 88 3C 0C 00 00               js 0x140c4a5ad
00C49971  4C 8B 05 60 BE 2B 00            mov r8, qword ptr [rip + 0x2bbe60]
00C49978  48 8D 8D B8 00 00 00            lea rcx, [rbp + 0xb8]
00C4997F  48 8B 15 E2 BE 2B 00            mov rdx, qword ptr [rip + 0x2bbee2]
00C49986  E8 35 B4 82 FF                  call 0x140474dc0
00C4998B  85 C0                           test eax, eax
00C4998D  0F 88 1A 0C 00 00               js 0x140c4a5ad
00C49993  4C 8B 05 46 BE 2B 00            mov r8, qword ptr [rip + 0x2bbe46]
00C4999A  48 8D 8D C8 00 00 00            lea rcx, [rbp + 0xc8]
00C499A1  48 8B 15 C0 BE 2B 00            mov rdx, qword ptr [rip + 0x2bbec0]
00C499A8  E8 13 B4 82 FF                  call 0x140474dc0
00C499AD  85 C0                           test eax, eax
00C499AF  0F 88 F8 0B 00 00               js 0x140c4a5ad
00C499B5  4C 8B 05 4C BE 2B 00            mov r8, qword ptr [rip + 0x2bbe4c]
00C499BC  48 8D 8D D8 00 00 00            lea rcx, [rbp + 0xd8]
00C499C3  48 8B 15 9E BE 2B 00            mov rdx, qword ptr [rip + 0x2bbe9e]
00C499CA  E8 F1 B3 82 FF                  call 0x140474dc0
00C499CF  85 C0                           test eax, eax
00C499D1  0F 88 D6 0B 00 00               js 0x140c4a5ad
00C499D7  4C 8B 05 32 BE 2B 00            mov r8, qword ptr [rip + 0x2bbe32]
00C499DE  48 8D 8D E8 00 00 00            lea rcx, [rbp + 0xe8]
00C499E5  48 8B 15 7C BE 2B 00            mov rdx, qword ptr [rip + 0x2bbe7c]
00C499EC  E8 CF B3 82 FF                  call 0x140474dc0
00C499F1  85 C0                           test eax, eax
00C499F3  0F 88 B4 0B 00 00               js 0x140c4a5ad
00C499F9  4C 8B 05 F8 BD 2B 00            mov r8, qword ptr [rip + 0x2bbdf8]
00C49A00  48 8D 8D F8 00 00 00            lea rcx, [rbp + 0xf8]
00C49A07  48 8B 15 5A BE 2B 00            mov rdx, qword ptr [rip + 0x2bbe5a]
00C49A0E  E8 AD B3 82 FF                  call 0x140474dc0
00C49A13  85 C0                           test eax, eax
00C49A15  0F 88 92 0B 00 00               js 0x140c4a5ad
00C49A1B  4C 8B 05 DE BD 2B 00            mov r8, qword ptr [rip + 0x2bbdde]
00C49A22  48 8D 8D 08 01 00 00            lea rcx, [rbp + 0x108]
00C49A29  48 8B 15 38 BE 2B 00            mov rdx, qword ptr [rip + 0x2bbe38]
00C49A30  E8 8B B3 82 FF                  call 0x140474dc0
00C49A35  85 C0                           test eax, eax
00C49A37  0F 88 70 0B 00 00               js 0x140c4a5ad
00C49A3D  4C 8B 05 2C BD 2B 00            mov r8, qword ptr [rip + 0x2bbd2c]
00C49A44  48 8D 8D 18 01 00 00            lea rcx, [rbp + 0x118]
00C49A4B  48 8B 15 16 BE 2B 00            mov rdx, qword ptr [rip + 0x2bbe16]
00C49A52  E8 69 B3 82 FF                  call 0x140474dc0
00C49A57  85 C0                           test eax, eax
00C49A59  0F 88 4E 0B 00 00               js 0x140c4a5ad
00C49A5F  4C 8B 05 12 BD 2B 00            mov r8, qword ptr [rip + 0x2bbd12]
00C49A66  48 8D 8D 28 01 00 00            lea rcx, [rbp + 0x128]
00C49A6D  48 8B 15 F4 BD 2B 00            mov rdx, qword ptr [rip + 0x2bbdf4]
00C49A74  E8 47 B3 82 FF                  call 0x140474dc0
00C49A79  85 C0                           test eax, eax
00C49A7B  0F 88 2C 0B 00 00               js 0x140c4a5ad
00C49A81  4C 8B 05 D8 BC 2B 00            mov r8, qword ptr [rip + 0x2bbcd8]
00C49A88  48 8D 8D 38 01 00 00            lea rcx, [rbp + 0x138]
00C49A8F  48 8B 15 D2 BD 2B 00            mov rdx, qword ptr [rip + 0x2bbdd2]
00C49A96  E8 25 B3 82 FF                  call 0x140474dc0
00C49A9B  85 C0                           test eax, eax
00C49A9D  0F 88 0A 0B 00 00               js 0x140c4a5ad
00C49AA3  4C 8B 05 BE BC 2B 00            mov r8, qword ptr [rip + 0x2bbcbe]
00C49AAA  48 8D 8D 48 01 00 00            lea rcx, [rbp + 0x148]
00C49AB1  48 8B 15 B0 BD 2B 00            mov rdx, qword ptr [rip + 0x2bbdb0]
00C49AB8  E8 03 B3 82 FF                  call 0x140474dc0
00C49ABD  85 C0                           test eax, eax
00C49ABF  0F 88 E8 0A 00 00               js 0x140c4a5ad
00C49AC5  4C 8B 05 BC BC 2B 00            mov r8, qword ptr [rip + 0x2bbcbc]
00C49ACC  48 8D 8D 58 01 00 00            lea rcx, [rbp + 0x158]
00C49AD3  48 8B 15 8E BD 2B 00            mov rdx, qword ptr [rip + 0x2bbd8e]
00C49ADA  E8 E1 B2 82 FF                  call 0x140474dc0
00C49ADF  85 C0                           test eax, eax
00C49AE1  0F 88 C6 0A 00 00               js 0x140c4a5ad
00C49AE7  4C 8B 05 F2 E0 21 00            mov r8, qword ptr [rip + 0x21e0f2]
00C49AEE  48 8D 8D 68 01 00 00            lea rcx, [rbp + 0x168]
00C49AF5  48 8B 15 6C BD 2B 00            mov rdx, qword ptr [rip + 0x2bbd6c]
00C49AFC  E8 BF B2 82 FF                  call 0x140474dc0
00C49B01  85 C0                           test eax, eax
00C49B03  0F 88 A4 0A 00 00               js 0x140c4a5ad
00C49B09  4C 8B 05 B8 E0 21 00            mov r8, qword ptr [rip + 0x21e0b8]
00C49B10  48 8D 8D 78 01 00 00            lea rcx, [rbp + 0x178]
00C49B17  48 8B 15 4A BD 2B 00            mov rdx, qword ptr [rip + 0x2bbd4a]
00C49B1E  E8 9D B2 82 FF                  call 0x140474dc0
00C49B23  85 C0                           test eax, eax
00C49B25  0F 88 82 0A 00 00               js 0x140c4a5ad
00C49B2B  4C 8B 05 9E E0 21 00            mov r8, qword ptr [rip + 0x21e09e]
00C49B32  48 8D 4D E8                     lea rcx, [rbp - 0x18]
00C49B36  48 8B 15 2B BD 2B 00            mov rdx, qword ptr [rip + 0x2bbd2b]
00C49B3D  E8 7E B2 82 FF                  call 0x140474dc0
00C49B42  85 C0                           test eax, eax
00C49B44  0F 88 63 0A 00 00               js 0x140c4a5ad
00C49B4A  4C 8B 05 97 E0 21 00            mov r8, qword ptr [rip + 0x21e097]
00C49B51  48 8D 4D F8                     lea rcx, [rbp - 8]
00C49B55  48 8B 15 0C BD 2B 00            mov rdx, qword ptr [rip + 0x2bbd0c]
00C49B5C  E8 5F B2 82 FF                  call 0x140474dc0
00C49B61  85 C0                           test eax, eax
00C49B63  0F 88 44 0A 00 00               js 0x140c4a5ad
00C49B69  48 8B 05 A0 E1 21 00            mov rax, qword ptr [rip + 0x21e1a0]
00C49B70  48 8D 95 30 02 00 00            lea rdx, [rbp + 0x230]
00C49B77  48 8B 1D 1A BC 2B 00            mov rbx, qword ptr [rip + 0x2bbc1a]
00C49B7E  B9 00 04 00 00                  mov ecx, 0x400
00C49B83  45 8A C6                        mov r8b, r14b
00C49B86  C7 40 08 54 00 00 00            mov dword ptr [rax + 8], 0x54
00C49B8D  48 8B 05 BC BC 2B 00            mov rax, qword ptr [rip + 0x2bbcbc]
00C49B94  48 89 78 08                     mov qword ptr [rax + 8], rdi
00C49B98  48 8B 05 89 BC 2B 00            mov rax, qword ptr [rip + 0x2bbc89]
00C49B9F  89 48 08                        mov dword ptr [rax + 8], ecx
00C49BA2  44 89 60 0C                     mov dword ptr [rax + 0xc], r12d
00C49BA6  48 8B 05 83 BC 2B 00            mov rax, qword ptr [rip + 0x2bbc83]
00C49BAD  89 48 08                        mov dword ptr [rax + 8], ecx
00C49BB0  44 89 78 0C                     mov dword ptr [rax + 0xc], r15d
00C49BB4  48 8B 05 9D BC 2B 00            mov rax, qword ptr [rip + 0x2bbc9d]
00C49BBB  89 48 08                        mov dword ptr [rax + 8], ecx
00C49BBE  89 48 0C                        mov dword ptr [rax + 0xc], ecx
00C49BC1  B9 00 02 00 00                  mov ecx, 0x200
00C49BC6  48 8B 05 83 B3 2B 00            mov rax, qword ptr [rip + 0x2bb383]
00C49BCD  89 48 08                        mov dword ptr [rax + 8], ecx
00C49BD0  C7 40 0C 00 06 00 00            mov dword ptr [rax + 0xc], 0x600
00C49BD7  48 8B 05 7A B3 2B 00            mov rax, qword ptr [rip + 0x2bb37a]
00C49BDE  89 48 08                        mov dword ptr [rax + 8], ecx
00C49BE1  44 89 60 0C                     mov dword ptr [rax + 0xc], r12d
00C49BE5  48 8B 05 74 BC 2B 00            mov rax, qword ptr [rip + 0x2bbc74]
00C49BEC  89 48 08                        mov dword ptr [rax + 8], ecx
00C49BEF  44 89 78 0C                     mov dword ptr [rax + 0xc], r15d
00C49BF3  48 8B 05 4E BC 2B 00            mov rax, qword ptr [rip + 0x2bbc4e]
00C49BFA  89 48 08                        mov dword ptr [rax + 8], ecx
00C49BFD  48 8B CB                        mov rcx, rbx
00C49C00  C7 40 0C 00 08 00 00            mov dword ptr [rax + 0xc], 0x800
00C49C07  48 8B 05 AA DF 21 00            mov rax, qword ptr [rip + 0x21dfaa]
00C49C0E  C7 40 08 50 00 00 00            mov dword ptr [rax + 8], 0x50
00C49C15  C7 40 0C B5 89 FB 38            mov dword ptr [rax + 0xc], 0x38fb89b5
00C49C1C  C7 40 10 19 84 C2 CB            mov dword ptr [rax + 0x10], 0xcbc28419
00C49C23  C7 40 14 5C 6C 23 6D            mov dword ptr [rax + 0x14], 0x6d236c5c
00C49C2A  C7 40 18 57 00 77 6E            mov dword ptr [rax + 0x18], 0x6e770057
00C49C31  C7 40 1C C0 02 64 87            mov dword ptr [rax + 0x1c], 0x876402c0
00C49C38  E8 E3 1A DA FF                  call 0x1409eb720
00C49C3D  4C 8B 05 4C BB 2B 00            mov r8, qword ptr [rip + 0x2bbb4c]
00C49C44  48 8D 4D 08                     lea rcx, [rbp + 8]
00C49C48  48 8B 15 19 BC 2B 00            mov rdx, qword ptr [rip + 0x2bbc19]
00C49C4F  C7 43 08 20 00 00 00            mov dword ptr [rbx + 8], 0x20
00C49C56  C7 43 0C 45 02 00 00            mov dword ptr [rbx + 0xc], 0x245
00C49C5D  E8 5E B1 82 FF                  call 0x140474dc0
00C49C62  85 C0                           test eax, eax
00C49C64  0F 88 43 09 00 00               js 0x140c4a5ad
00C49C6A  4C 8B 05 0F BB 2B 00            mov r8, qword ptr [rip + 0x2bbb0f]
00C49C71  48 8D 4D 18                     lea rcx, [rbp + 0x18]
00C49C75  48 8B 15 EC BB 2B 00            mov rdx, qword ptr [rip + 0x2bbbec]
00C49C7C  E8 3F B1 82 FF                  call 0x140474dc0
00C49C81  85 C0                           test eax, eax
00C49C83  0F 88 24 09 00 00               js 0x140c4a5ad
00C49C89  4C 8B 05 E0 BB 2B 00            mov r8, qword ptr [rip + 0x2bbbe0]
00C49C90  48 8D 4D 28                     lea rcx, [rbp + 0x28]
00C49C94  48 8B 15 CD BB 2B 00            mov rdx, qword ptr [rip + 0x2bbbcd]
00C49C9B  E8 20 B1 82 FF                  call 0x140474dc0
00C49CA0  85 C0                           test eax, eax
00C49CA2  0F 88 05 09 00 00               js 0x140c4a5ad
00C49CA8  4C 8B 05 01 BB 2B 00            mov r8, qword ptr [rip + 0x2bbb01]
00C49CAF  48 8D 4D 38                     lea rcx, [rbp + 0x38]
00C49CB3  48 8B 15 EE BA 2B 00            mov rdx, qword ptr [rip + 0x2bbaee]
00C49CBA  E8 01 B1 82 FF                  call 0x140474dc0
00C49CBF  85 C0                           test eax, eax
00C49CC1  0F 88 E6 08 00 00               js 0x140c4a5ad
00C49CC7  E8 10 DC FF FF                  call 0x140c478dc
00C49CCC  41 8B C6                        mov eax, r14d
00C49CCF  48 C7 85 38 02 00 00 03 00 00 00  mov qword ptr [rbp + 0x238], 3
00C49CDA  48 89 05 9F FE 38 00            mov qword ptr [rip + 0x38fe9f], rax
00C49CE1  48 8B 85 38 02 00 00            mov rax, qword ptr [rbp + 0x238]
00C49CE8  48 89 05 D9 FE 38 00            mov qword ptr [rip + 0x38fed9], rax
00C49CEF  48 C7 85 40 02 00 00 04 00 00 00  mov qword ptr [rbp + 0x240], 4
00C49CFA  48 8B 85 40 02 00 00            mov rax, qword ptr [rbp + 0x240]
00C49D01  48 89 05 C8 FD 38 00            mov qword ptr [rip + 0x38fdc8], rax
00C49D08  48 C7 85 48 02 00 00 05 00 00 00  mov qword ptr [rbp + 0x248], 5
00C49D13  48 8B 85 48 02 00 00            mov rax, qword ptr [rbp + 0x248]
00C49D1A  48 89 05 4F FE 38 00            mov qword ptr [rip + 0x38fe4f], rax
00C49D21  48 C7 44 24 40 06 00 00 00      mov qword ptr [rsp + 0x40], 6
00C49D2A  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00C49D2F  48 89 05 D2 02 39 00            mov qword ptr [rip + 0x3902d2], rax
00C49D36  48 C7 44 24 38 07 00 00 00      mov qword ptr [rsp + 0x38], 7
00C49D3F  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00C49D44  48 89 05 2D FD 38 00            mov qword ptr [rip + 0x38fd2d], rax
00C49D4B  48 C7 44 24 20 18 00 00 00      mov qword ptr [rsp + 0x20], 0x18
00C49D54  4C 8B 64 24 20                  mov r12, qword ptr [rsp + 0x20]
00C49D59  48 C7 44 24 30 08 00 00 00      mov qword ptr [rsp + 0x30], 8
00C49D62  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00C49D67  48 89 05 92 FD 38 00            mov qword ptr [rip + 0x38fd92], rax
00C49D6E  48 C7 44 24 20 19 00 00 00      mov qword ptr [rsp + 0x20], 0x19
00C49D77  4C 8B 7C 24 20                  mov r15, qword ptr [rsp + 0x20]
00C49D7C  48 C7 44 24 28 09 00 00 00      mov qword ptr [rsp + 0x28], 9
00C49D85  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
00C49D8A  48 89 05 A7 FD 38 00            mov qword ptr [rip + 0x38fda7], rax
00C49D91  48 C7 44 24 48 0A 00 00 00      mov qword ptr [rsp + 0x48], 0xa
00C49D9A  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
00C49D9F  48 89 05 7A FD 38 00            mov qword ptr [rip + 0x38fd7a], rax
00C49DA6  48 C7 44 24 20 1A 00 00 00      mov qword ptr [rsp + 0x20], 0x1a
00C49DAF  48 C7 44 24 50 0F 00 00 00      mov qword ptr [rsp + 0x50], 0xf
00C49DB8  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00C49DBD  48 89 05 7C FF 38 00            mov qword ptr [rip + 0x38ff7c], rax
00C49DC4  48 C7 44 24 58 0E 00 00 00      mov qword ptr [rsp + 0x58], 0xe
00C49DCD  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00C49DD2  48 89 05 0F FD 38 00            mov qword ptr [rip + 0x38fd0f], rax
00C49DD9  48 C7 44 24 60 0B 00 00 00      mov qword ptr [rsp + 0x60], 0xb
00C49DE2  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00C49DE7  48 89 05 5A FD 38 00            mov qword ptr [rip + 0x38fd5a], rax
00C49DEE  48 C7 44 24 68 0C 00 00 00      mov qword ptr [rsp + 0x68], 0xc
00C49DF7  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00C49DFC  48 89 05 DD FD 38 00            mov qword ptr [rip + 0x38fddd], rax
00C49E03  48 C7 44 24 70 0D 00 00 00      mov qword ptr [rsp + 0x70], 0xd
00C49E0C  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00C49E11  48 89 05 F0 FC 38 00            mov qword ptr [rip + 0x38fcf0], rax
00C49E18  48 C7 44 24 78 10 00 00 00      mov qword ptr [rsp + 0x78], 0x10
00C49E21  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
00C49E26  48 89 05 A3 FD 38 00            mov qword ptr [rip + 0x38fda3], rax
00C49E2D  48 C7 45 80 11 00 00 00         mov qword ptr [rbp - 0x80], 0x11
00C49E35  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00C49E39  48 89 05 80 FC 38 00            mov qword ptr [rip + 0x38fc80], rax
00C49E40  48 C7 45 88 12 00 00 00         mov qword ptr [rbp - 0x78], 0x12
00C49E48  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
00C49E4C  48 89 05 8D FC 38 00            mov qword ptr [rip + 0x38fc8d], rax
00C49E53  48 C7 45 90 13 00 00 00         mov qword ptr [rbp - 0x70], 0x13
00C49E5B  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
00C49E5F  48 89 05 CA FC 38 00            mov qword ptr [rip + 0x38fcca], rax
00C49E66  48 C7 45 98 14 00 00 00         mov qword ptr [rbp - 0x68], 0x14
00C49E6E  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
00C49E72  48 89 05 07 FC 38 00            mov qword ptr [rip + 0x38fc07], rax
00C49E79  4C 89 B5 30 02 00 00            mov qword ptr [rbp + 0x230], r14
00C49E80  4C 8B 74 24 20                  mov r14, qword ptr [rsp + 0x20]
00C49E85  48 C7 44 24 20 1B 00 00 00      mov qword ptr [rsp + 0x20], 0x1b
00C49E8E  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
00C49E93  48 C7 45 A0 15 00 00 00         mov qword ptr [rbp - 0x60], 0x15
00C49E9B  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
00C49E9F  48 C7 45 A8 16 00 00 00         mov qword ptr [rbp - 0x58], 0x16
00C49EA7  48 C7 45 B0 17 00 00 00         mov qword ptr [rbp - 0x50], 0x17
00C49EAF  4C 8B 6D B0                     mov r13, qword ptr [rbp - 0x50]
00C49EB3  48 89 05 56 FD 38 00            mov qword ptr [rip + 0x38fd56], rax
00C49EBA  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
00C49EBE  48 C7 44 24 20 1C 00 00 00      mov qword ptr [rsp + 0x20], 0x1c
00C49EC7  48 8B 7C 24 20                  mov rdi, qword ptr [rsp + 0x20]
00C49ECC  48 89 05 E5 FB 38 00            mov qword ptr [rip + 0x38fbe5], rax
00C49ED3  4C 89 2D 76 FE 38 00            mov qword ptr [rip + 0x38fe76], r13
00C49EDA  4C 89 25 7F FF 38 00            mov qword ptr [rip + 0x38ff7f], r12
00C49EE1  4C 89 3D 58 00 39 00            mov qword ptr [rip + 0x390058], r15
00C49EE8  4C 89 35 09 01 39 00            mov qword ptr [rip + 0x390109], r14
00C49EEF  48 89 35 6A FE 38 00            mov qword ptr [rip + 0x38fe6a], rsi
00C49EF6  4C 8B 2D 7B FC 38 00            mov r13, qword ptr [rip + 0x38fc7b]
00C49EFD  4C 89 2D A4 02 39 00            mov qword ptr [rip + 0x3902a4], r13
00C49F04  4C 8B 2D 3D DE 21 00            mov r13, qword ptr [rip + 0x21de3d]
00C49F0B  4C 89 2D 9E 02 39 00            mov qword ptr [rip + 0x39029e], r13
00C49F12  4C 8B 2D 37 DE 21 00            mov r13, qword ptr [rip + 0x21de37]
00C49F19  4C 89 2D 98 02 39 00            mov qword ptr [rip + 0x390298], r13
00C49F20  4C 8B 2D 19 DE 21 00            mov r13, qword ptr [rip + 0x21de19]
00C49F27  4C 89 2D 92 02 39 00            mov qword ptr [rip + 0x390292], r13
00C49F2E  4C 8B 2D B3 DD 21 00            mov r13, qword ptr [rip + 0x21ddb3]
00C49F35  4C 89 2D 8C 02 39 00            mov qword ptr [rip + 0x39028c], r13
00C49F3C  4C 8B 2D AD DD 21 00            mov r13, qword ptr [rip + 0x21ddad]
00C49F43  4C 89 2D A6 03 39 00            mov qword ptr [rip + 0x3903a6], r13
00C49F4A  4C 8B 2D 07 FF 38 00            mov r13, qword ptr [rip + 0x38ff07]
00C49F51  4C 89 2D 78 02 39 00            mov qword ptr [rip + 0x390278], r13
00C49F58  4C 8B 2D E9 FD 38 00            mov r13, qword ptr [rip + 0x38fde9]
00C49F5F  4C 89 2D 72 02 39 00            mov qword ptr [rip + 0x390272], r13
00C49F66  4C 8B 2D B3 DD 21 00            mov r13, qword ptr [rip + 0x21ddb3]
00C49F6D  4C 89 2D 6C 02 39 00            mov qword ptr [rip + 0x39026c], r13
00C49F74  4C 8B 2D AD DD 21 00            mov r13, qword ptr [rip + 0x21ddad]
00C49F7B  4C 89 2D 66 02 39 00            mov qword ptr [rip + 0x390266], r13
00C49F82  4C 8B 2D F7 DB 21 00            mov r13, qword ptr [rip + 0x21dbf7]
00C49F89  4C 89 2D 60 02 39 00            mov qword ptr [rip + 0x390260], r13
00C49F90  4C 8B 2D C1 DD 21 00            mov r13, qword ptr [rip + 0x21ddc1]
00C49F97  4C 89 2D 5A 02 39 00            mov qword ptr [rip + 0x39025a], r13
00C49F9E  4C 8B 2D 03 FD 38 00            mov r13, qword ptr [rip + 0x38fd03]
00C49FA5  4C 89 2D 94 02 39 00            mov qword ptr [rip + 0x390294], r13
00C49FAC  4C 8B 2D 5D FB 38 00            mov r13, qword ptr [rip + 0x38fb5d]
00C49FB3  4C 89 2D 8E 02 39 00            mov qword ptr [rip + 0x39028e], r13
00C49FBA  4C 8B 2D 07 FB 38 00            mov r13, qword ptr [rip + 0x38fb07]
00C49FC1  4C 89 2D 88 02 39 00            mov qword ptr [rip + 0x390288], r13
00C49FC8  4C 8B 2D 89 FB 38 00            mov r13, qword ptr [rip + 0x38fb89]
00C49FCF  4C 89 2D 9A 02 39 00            mov qword ptr [rip + 0x39029a], r13
00C49FD6  4C 8B 2D CB FB 38 00            mov r13, qword ptr [rip + 0x38fbcb]
00C49FDD  4C 89 2D 94 02 39 00            mov qword ptr [rip + 0x390294], r13
00C49FE4  4C 8B 2D 3D FC 38 00            mov r13, qword ptr [rip + 0x38fc3d]
00C49FEB  4C 89 2D CE 02 39 00            mov qword ptr [rip + 0x3902ce], r13
00C49FF2  4C 8B 2D 6F FA 38 00            mov r13, qword ptr [rip + 0x38fa6f]
00C49FF9  4C 89 2D 00 02 39 00            mov qword ptr [rip + 0x390200], r13
00C4A000  4C 8B 2D D1 FB 38 00            mov r13, qword ptr [rip + 0x38fbd1]
00C4A007  4C 89 2D FA 01 39 00            mov qword ptr [rip + 0x3901fa], r13
00C4A00E  4C 8B 2D CB FC 38 00            mov r13, qword ptr [rip + 0x38fccb]
00C4A015  4C 89 2D F4 01 39 00            mov qword ptr [rip + 0x3901f4], r13
00C4A01C  4C 8B 2D C5 FC 38 00            mov r13, qword ptr [rip + 0x38fcc5]
00C4A023  4C 89 2D EE 01 39 00            mov qword ptr [rip + 0x3901ee], r13
00C4A02A  4C 8B 2D 9F FC 38 00            mov r13, qword ptr [rip + 0x38fc9f]
00C4A031  4C 89 2D E8 01 39 00            mov qword ptr [rip + 0x3901e8], r13
00C4A038  4C 8B 2D 99 FC 38 00            mov r13, qword ptr [rip + 0x38fc99]
00C4A03F  4C 89 2D E2 01 39 00            mov qword ptr [rip + 0x3901e2], r13
00C4A046  4C 8B 2D A3 FC 38 00            mov r13, qword ptr [rip + 0x38fca3]
00C4A04D  4C 89 2D DC 01 39 00            mov qword ptr [rip + 0x3901dc], r13
00C4A054  4C 8B 2D 9D FC 38 00            mov r13, qword ptr [rip + 0x38fc9d]
00C4A05B  48 C7 44 24 20 1D 00 00 00      mov qword ptr [rsp + 0x20], 0x1d
00C4A064  48 8B 5C 24 20                  mov rbx, qword ptr [rsp + 0x20]
00C4A069  48 C7 44 24 20 1E 00 00 00      mov qword ptr [rsp + 0x20], 0x1e
00C4A072  4C 8B 5C 24 20                  mov r11, qword ptr [rsp + 0x20]
00C4A077  48 C7 44 24 20 1F 00 00 00      mov qword ptr [rsp + 0x20], 0x1f
00C4A080  4C 8B 54 24 20                  mov r10, qword ptr [rsp + 0x20]
00C4A085  48 C7 44 24 20 20 00 00 00      mov qword ptr [rsp + 0x20], 0x20
00C4A08E  4C 8B 4C 24 20                  mov r9, qword ptr [rsp + 0x20]
00C4A093  48 C7 44 24 20 21 00 00 00      mov qword ptr [rsp + 0x20], 0x21
00C4A09C  4C 8B 44 24 20                  mov r8, qword ptr [rsp + 0x20]
00C4A0A1  48 C7 44 24 20 22 00 00 00      mov qword ptr [rsp + 0x20], 0x22
00C4A0AA  48 8B 54 24 20                  mov rdx, qword ptr [rsp + 0x20]
00C4A0AF  48 C7 44 24 20 23 00 00 00      mov qword ptr [rsp + 0x20], 0x23
00C4A0B8  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
00C4A0BD  4C 89 2D 74 01 39 00            mov qword ptr [rip + 0x390174], r13
00C4A0C4  4C 8B 2D 4D B7 2B 00            mov r13, qword ptr [rip + 0x2bb74d]
00C4A0CB  48 C7 44 24 20 24 00 00 00      mov qword ptr [rsp + 0x20], 0x24
00C4A0D4  48 8B 44 24 20                  mov rax, qword ptr [rsp + 0x20]
00C4A0D9  4C 89 2D E8 01 39 00            mov qword ptr [rip + 0x3901e8], r13
00C4A0E0  4C 8B 2D 91 B7 2B 00            mov r13, qword ptr [rip + 0x2bb791]
00C4A0E7  4C 89 2D E2 01 39 00            mov qword ptr [rip + 0x3901e2], r13
00C4A0EE  48 89 3D 73 FC 38 00            mov qword ptr [rip + 0x38fc73], rdi
00C4A0F5  48 89 1D 6C FD 38 00            mov qword ptr [rip + 0x38fd6c], rbx
00C4A0FC  4C 89 1D 95 FB 38 00            mov qword ptr [rip + 0x38fb95], r11
00C4A103  4C 89 15 4E FC 38 00            mov qword ptr [rip + 0x38fc4e], r10
00C4A10A  4C 89 0D 17 FA 38 00            mov qword ptr [rip + 0x38fa17], r9
00C4A111  4C 89 05 38 FD 38 00            mov qword ptr [rip + 0x38fd38], r8
00C4A118  48 89 15 51 FC 38 00            mov qword ptr [rip + 0x38fc51], rdx
00C4A11F  48 89 0D 22 FE 38 00            mov qword ptr [rip + 0x38fe22], rcx
00C4A126  48 89 05 43 FD 38 00            mov qword ptr [rip + 0x38fd43], rax
00C4A12D  4C 8B 2D EC B6 2B 00            mov r13, qword ptr [rip + 0x2bb6ec]
00C4A134  4C 89 2D 9D 01 39 00            mov qword ptr [rip + 0x39019d], r13
00C4A13B  4C 8B 2D F6 B6 2B 00            mov r13, qword ptr [rip + 0x2bb6f6]
00C4A142  4C 89 2D 97 01 39 00            mov qword ptr [rip + 0x390197], r13
00C4A149  4C 8B 2D F0 B6 2B 00            mov r13, qword ptr [rip + 0x2bb6f0]
00C4A150  4C 89 2D 91 01 39 00            mov qword ptr [rip + 0x390191], r13
00C4A157  4C 8B 2D 02 DC 21 00            mov r13, qword ptr [rip + 0x21dc02]
00C4A15E  4C 89 2D 93 01 39 00            mov qword ptr [rip + 0x390193], r13
00C4A165  4C 8B 2D A4 DB 21 00            mov r13, qword ptr [rip + 0x21dba4]
00C4A16C  4C 89 2D 8D 01 39 00            mov qword ptr [rip + 0x39018d], r13
00C4A173  4C 8B 2D AE B6 2B 00            mov r13, qword ptr [rip + 0x2bb6ae]
00C4A17A  4C 89 2D 87 01 39 00            mov qword ptr [rip + 0x390187], r13
00C4A181  4C 8B 2D 30 DA 21 00            mov r13, qword ptr [rip + 0x21da30]
00C4A188  4C 89 2D 81 01 39 00            mov qword ptr [rip + 0x390181], r13
00C4A18F  4C 8B 2D 42 DA 21 00            mov r13, qword ptr [rip + 0x21da42]
00C4A196  4C 89 2D 83 01 39 00            mov qword ptr [rip + 0x390183], r13
00C4A19D  4C 8B AD 30 02 00 00            mov r13, qword ptr [rbp + 0x230]
00C4A1A4  49 C1 ED 20                     shr r13, 0x20
00C4A1A8  44 89 2D 45 FF 38 00            mov dword ptr [rip + 0x38ff45], r13d
00C4A1AF  4C 8B AD 38 02 00 00            mov r13, qword ptr [rbp + 0x238]
00C4A1B6  49 C1 ED 20                     shr r13, 0x20
00C4A1BA  44 89 2D 3B FF 38 00            mov dword ptr [rip + 0x38ff3b], r13d
00C4A1C1  4C 8B AD 40 02 00 00            mov r13, qword ptr [rbp + 0x240]
00C4A1C8  49 C1 ED 20                     shr r13, 0x20
00C4A1CC  44 89 2D 31 FF 38 00            mov dword ptr [rip + 0x38ff31], r13d
00C4A1D3  4C 8B AD 48 02 00 00            mov r13, qword ptr [rbp + 0x248]
00C4A1DA  49 C1 ED 20                     shr r13, 0x20
00C4A1DE  44 89 2D 27 FF 38 00            mov dword ptr [rip + 0x38ff27], r13d
00C4A1E5  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
00C4A1EA  49 C1 ED 20                     shr r13, 0x20
00C4A1EE  44 89 2D 1F FF 38 00            mov dword ptr [rip + 0x38ff1f], r13d
00C4A1F5  4C 8B 6C 24 38                  mov r13, qword ptr [rsp + 0x38]
00C4A1FA  49 C1 ED 20                     shr r13, 0x20
00C4A1FE  44 89 2D 17 FF 38 00            mov dword ptr [rip + 0x38ff17], r13d
00C4A205  4C 8B 6C 24 30                  mov r13, qword ptr [rsp + 0x30]
00C4A20A  49 C1 ED 20                     shr r13, 0x20
00C4A20E  44 89 2D 0F FF 38 00            mov dword ptr [rip + 0x38ff0f], r13d
00C4A215  4C 8B 6C 24 28                  mov r13, qword ptr [rsp + 0x28]
00C4A21A  49 C1 ED 20                     shr r13, 0x20
00C4A21E  44 89 2D 07 FF 38 00            mov dword ptr [rip + 0x38ff07], r13d
00C4A225  4C 8B 6C 24 48                  mov r13, qword ptr [rsp + 0x48]
00C4A22A  49 C1 ED 20                     shr r13, 0x20
00C4A22E  44 89 2D FF FE 38 00            mov dword ptr [rip + 0x38feff], r13d
00C4A235  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
00C4A23A  49 C1 ED 20                     shr r13, 0x20
00C4A23E  44 89 2D F7 FE 38 00            mov dword ptr [rip + 0x38fef7], r13d
00C4A245  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
00C4A24A  49 C1 ED 20                     shr r13, 0x20
00C4A24E  44 89 2D EF FE 38 00            mov dword ptr [rip + 0x38feef], r13d
00C4A255  4C 8B 6C 24 60                  mov r13, qword ptr [rsp + 0x60]
00C4A25A  49 C1 ED 20                     shr r13, 0x20
00C4A25E  44 89 2D E7 FE 38 00            mov dword ptr [rip + 0x38fee7], r13d
00C4A265  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
00C4A26A  49 C1 ED 20                     shr r13, 0x20
00C4A26E  44 89 2D DF FE 38 00            mov dword ptr [rip + 0x38fedf], r13d
00C4A275  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
00C4A27A  49 C1 ED 20                     shr r13, 0x20
00C4A27E  44 89 2D D7 FE 38 00            mov dword ptr [rip + 0x38fed7], r13d
00C4A285  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
00C4A28A  49 C1 ED 20                     shr r13, 0x20
00C4A28E  44 89 2D CF FE 38 00            mov dword ptr [rip + 0x38fecf], r13d
00C4A295  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
00C4A299  49 C1 ED 20                     shr r13, 0x20
00C4A29D  44 89 2D C8 FE 38 00            mov dword ptr [rip + 0x38fec8], r13d
00C4A2A4  C7 05 42 FE 38 00 02 00 00 00   mov dword ptr [rip + 0x38fe42], 2
00C4A2AE  C7 05 40 FE 38 00 03 00 00 00   mov dword ptr [rip + 0x38fe40], 3
00C4A2B8  C7 05 3E FE 38 00 04 00 00 00   mov dword ptr [rip + 0x38fe3e], 4
00C4A2C2  C7 05 3C FE 38 00 05 00 00 00   mov dword ptr [rip + 0x38fe3c], 5
00C4A2CC  C7 05 3A FE 38 00 06 00 00 00   mov dword ptr [rip + 0x38fe3a], 6
00C4A2D6  C7 05 38 FE 38 00 07 00 00 00   mov dword ptr [rip + 0x38fe38], 7
00C4A2E0  C7 05 36 FE 38 00 08 00 00 00   mov dword ptr [rip + 0x38fe36], 8
00C4A2EA  C7 05 34 FE 38 00 09 00 00 00   mov dword ptr [rip + 0x38fe34], 9
00C4A2F4  C7 05 32 FE 38 00 0A 00 00 00   mov dword ptr [rip + 0x38fe32], 0xa
00C4A2FE  C7 05 30 FE 38 00 0F 00 00 00   mov dword ptr [rip + 0x38fe30], 0xf
00C4A308  C7 05 2E FE 38 00 0E 00 00 00   mov dword ptr [rip + 0x38fe2e], 0xe
00C4A312  C7 05 2C FE 38 00 0B 00 00 00   mov dword ptr [rip + 0x38fe2c], 0xb
00C4A31C  C7 05 2A FE 38 00 0C 00 00 00   mov dword ptr [rip + 0x38fe2a], 0xc
00C4A326  C7 05 28 FE 38 00 0D 00 00 00   mov dword ptr [rip + 0x38fe28], 0xd
00C4A330  C7 05 26 FE 38 00 10 00 00 00   mov dword ptr [rip + 0x38fe26], 0x10
00C4A33A  C7 05 24 FE 38 00 11 00 00 00   mov dword ptr [rip + 0x38fe24], 0x11
00C4A344  C7 05 22 FE 38 00 12 00 00 00   mov dword ptr [rip + 0x38fe22], 0x12
00C4A34E  4C 8B 6D 88                     mov r13, qword ptr [rbp - 0x78]
00C4A352  49 C1 ED 20                     shr r13, 0x20
00C4A356  44 89 2D 17 FE 38 00            mov dword ptr [rip + 0x38fe17], r13d
00C4A35D  4C 8B 6D 90                     mov r13, qword ptr [rbp - 0x70]
00C4A361  49 C1 ED 20                     shr r13, 0x20
00C4A365  44 89 2D 10 FE 38 00            mov dword ptr [rip + 0x38fe10], r13d
00C4A36C  4C 8B 6D 98                     mov r13, qword ptr [rbp - 0x68]
00C4A370  49 C1 ED 20                     shr r13, 0x20
00C4A374  44 89 2D 09 FE 38 00            mov dword ptr [rip + 0x38fe09], r13d
00C4A37B  4C 8B 6D A0                     mov r13, qword ptr [rbp - 0x60]
00C4A37F  49 C1 ED 20                     shr r13, 0x20
00C4A383  44 89 2D 02 FE 38 00            mov dword ptr [rip + 0x38fe02], r13d
00C4A38A  4C 8B 6D A8                     mov r13, qword ptr [rbp - 0x58]
00C4A38E  49 C1 ED 20                     shr r13, 0x20
00C4A392  44 89 2D FB FD 38 00            mov dword ptr [rip + 0x38fdfb], r13d
00C4A399  4C 8B 6D B0                     mov r13, qword ptr [rbp - 0x50]
00C4A39D  49 C1 ED 20                     shr r13, 0x20
00C4A3A1  49 C1 EC 20                     shr r12, 0x20
00C4A3A5  49 C1 EF 20                     shr r15, 0x20
00C4A3A9  49 C1 EE 20                     shr r14, 0x20
00C4A3AD  48 C1 EE 20                     shr rsi, 0x20
00C4A3B1  48 C1 EF 20                     shr rdi, 0x20
00C4A3B5  48 C1 EB 20                     shr rbx, 0x20
00C4A3B9  49 C1 EB 20                     shr r11, 0x20
00C4A3BD  49 C1 EA 20                     shr r10, 0x20
00C4A3C1  49 C1 E9 20                     shr r9, 0x20
00C4A3C5  49 C1 E8 20                     shr r8, 0x20
00C4A3C9  48 C1 EA 20                     shr rdx, 0x20
00C4A3CD  48 C1 E9 20                     shr rcx, 0x20
00C4A3D1  48 C1 E8 20                     shr rax, 0x20
00C4A3D5  89 05 41 FF 38 00               mov dword ptr [rip + 0x38ff41], eax
00C4A3DB  48 8B 05 FE D7 21 00            mov rax, qword ptr [rip + 0x21d7fe]
00C4A3E2  48 89 05 3F FF 38 00            mov qword ptr [rip + 0x38ff3f], rax
00C4A3E9  48 8B 05 D8 D7 21 00            mov rax, qword ptr [rip + 0x21d7d8]
00C4A3F0  48 89 05 39 FF 38 00            mov qword ptr [rip + 0x38ff39], rax
00C4A3F7  48 8B 05 D2 D7 21 00            mov rax, qword ptr [rip + 0x21d7d2]
00C4A3FE  48 89 05 33 FF 38 00            mov qword ptr [rip + 0x38ff33], rax
00C4A405  48 8B 05 DC D7 21 00            mov rax, qword ptr [rip + 0x21d7dc]
00C4A40C  48 89 05 2D FF 38 00            mov qword ptr [rip + 0x38ff2d], rax
00C4A413  C7 05 5B FD 38 00 13 00 00 00   mov dword ptr [rip + 0x38fd5b], 0x13
00C4A41D  C7 05 59 FD 38 00 14 00 00 00   mov dword ptr [rip + 0x38fd59], 0x14
00C4A427  C7 05 57 FD 38 00 15 00 00 00   mov dword ptr [rip + 0x38fd57], 0x15
00C4A431  C7 05 55 FD 38 00 16 00 00 00   mov dword ptr [rip + 0x38fd55], 0x16
00C4A43B  C7 05 53 FD 38 00 17 00 00 00   mov dword ptr [rip + 0x38fd53], 0x17
00C4A445  44 89 2D 50 FD 38 00            mov dword ptr [rip + 0x38fd50], r13d
00C4A44C  C7 05 4A FD 38 00 18 00 00 00   mov dword ptr [rip + 0x38fd4a], 0x18
00C4A456  44 89 25 47 FD 38 00            mov dword ptr [rip + 0x38fd47], r12d
00C4A45D  C7 05 F1 FD 38 00 19 00 00 00   mov dword ptr [rip + 0x38fdf1], 0x19
00C4A467  44 89 3D EE FD 38 00            mov dword ptr [rip + 0x38fdee], r15d
00C4A46E  C7 05 E8 FD 38 00 1A 00 00 00   mov dword ptr [rip + 0x38fde8], 0x1a
00C4A478  44 89 35 E5 FD 38 00            mov dword ptr [rip + 0x38fde5], r14d
00C4A47F  C7 05 DF FD 38 00 1B 00 00 00   mov dword ptr [rip + 0x38fddf], 0x1b
00C4A489  89 35 DD FD 38 00               mov dword ptr [rip + 0x38fddd], esi
00C4A48F  C7 05 E7 FD 38 00 1C 00 00 00   mov dword ptr [rip + 0x38fde7], 0x1c
00C4A499  89 3D E5 FD 38 00               mov dword ptr [rip + 0x38fde5], edi
00C4A49F  C7 05 DF FD 38 00 1D 00 00 00   mov dword ptr [rip + 0x38fddf], 0x1d
00C4A4A9  89 1D DD FD 38 00               mov dword ptr [rip + 0x38fddd], ebx
00C4A4AF  C7 05 D7 FD 38 00 1E 00 00 00   mov dword ptr [rip + 0x38fdd7], 0x1e
00C4A4B9  44 89 1D D4 FD 38 00            mov dword ptr [rip + 0x38fdd4], r11d
00C4A4C0  C7 05 CE FD 38 00 1F 00 00 00   mov dword ptr [rip + 0x38fdce], 0x1f
00C4A4CA  44 89 15 CB FD 38 00            mov dword ptr [rip + 0x38fdcb], r10d
00C4A4D1  C7 05 C5 FD 38 00 20 00 00 00   mov dword ptr [rip + 0x38fdc5], 0x20
00C4A4DB  44 89 0D C2 FD 38 00            mov dword ptr [rip + 0x38fdc2], r9d
00C4A4E2  C7 05 BC FD 38 00 21 00 00 00   mov dword ptr [rip + 0x38fdbc], 0x21
00C4A4EC  44 89 05 B9 FD 38 00            mov dword ptr [rip + 0x38fdb9], r8d
00C4A4F3  C7 05 B3 FD 38 00 22 00 00 00   mov dword ptr [rip + 0x38fdb3], 0x22
00C4A4FD  89 15 B1 FD 38 00               mov dword ptr [rip + 0x38fdb1], edx
00C4A503  C7 05 AB FD 38 00 23 00 00 00   mov dword ptr [rip + 0x38fdab], 0x23
00C4A50D  89 0D A9 FD 38 00               mov dword ptr [rip + 0x38fda9], ecx
00C4A513  C7 05 FB FD 38 00 24 00 00 00   mov dword ptr [rip + 0x38fdfb], 0x24
00C4A51D  E8 BA BC 9B FF                  call 0x1406061dc
00C4A522  33 FF                           xor edi, edi
00C4A524  85 C0                           test eax, eax
00C4A526  74 0E                           je 0x140c4a536
00C4A528  48 8B 05 91 D6 21 00            mov rax, qword ptr [rip + 0x21d691]
00C4A52F  48 89 05 12 FE 38 00            mov qword ptr [rip + 0x38fe12], rax
00C4A536  48 8D 05 B3 FB 38 00            lea rax, [rip + 0x38fbb3]
00C4A53D  BB 05 00 00 00                  mov ebx, 5
00C4A542  48 89 05 57 F5 38 00            mov qword ptr [rip + 0x38f557], rax
00C4A549  8B CB                           mov ecx, ebx
00C4A54B  48 8D 05 66 59 2C 00            lea rax, [rip + 0x2c5966]
00C4A552  40 88 78 08                     mov byte ptr [rax + 8], dil
00C4A556  48 89 38                        mov qword ptr [rax], rdi
00C4A559  48 89 78 E8                     mov qword ptr [rax - 0x18], rdi
00C4A55D  48 8D 40 28                     lea rax, [rax + 0x28]
00C4A561  48 83 E9 01                     sub rcx, 1
00C4A565  75 EB                           jne 0x140c4a552
00C4A567  48 89 3D 1A 59 2C 00            mov qword ptr [rip + 0x2c591a], rdi
00C4A56E  48 89 3D 0B 59 2C 00            mov qword ptr [rip + 0x2c590b], rdi
00C4A575  E8 F6 8C B5 FF                  call 0x1407a3270
00C4A57A  85 C0                           test eax, eax
00C4A57C  78 2F                           js 0x140c4a5ad
00C4A57E  E8 E5 33 98 FF                  call 0x1405cd968
00C4A583  85 C0                           test eax, eax
00C4A585  74 22                           je 0x140c4a5a9
00C4A587  48 8D 0D 92 A7 2B 00            lea rcx, [rip + 0x2ba792]
00C4A58E  48 89 39                        mov qword ptr [rcx], rdi
00C4A591  48 8D 49 28                     lea rcx, [rcx + 0x28]
00C4A595  48 83 EB 01                     sub rbx, 1
00C4A599  75 F3                           jne 0x140c4a58e
00C4A59B  48 89 3D 6E A7 2B 00            mov qword ptr [rip + 0x2ba76e], rdi
00C4A5A2  48 89 3D 5F A7 2B 00            mov qword ptr [rip + 0x2ba75f], rdi
00C4A5A9  B0 01                           mov al, 1
00C4A5AB  EB 02                           jmp 0x140c4a5af
00C4A5AD  32 C0                           xor al, al
00C4A5AF  48 81 C4 E8 02 00 00            add rsp, 0x2e8
00C4A5B6  41 5F                           pop r15
00C4A5B8  41 5E                           pop r14
00C4A5BA  41 5D                           pop r13
00C4A5BC  41 5C                           pop r12
00C4A5BE  5F                              pop rdi
00C4A5BF  5E                              pop rsi
00C4A5C0  5B                              pop rbx
00C4A5C1  5D                              pop rbp
00C4A5C2  C3                              ret
00C4A5C3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepVariableInitialization(void)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned __int16 v_stack_m2E4;
    unsigned int v_stack_m2E8;
    unsigned __int16 v_stack_m2EC;
    unsigned int v_stack_m2F0;
    unsigned __int16 v_stack_m2F4;
    unsigned int v_stack_m2F8;
    unsigned __int16 v_stack_m2FC;
    unsigned int v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned __int16 v_stack_p14;
    unsigned int v_stack_p18;
    unsigned __int16 v_stack_p1C;
    unsigned int v_stack_p20;
    unsigned __int16 v_stack_p24;
    unsigned int v_stack_p8;
    unsigned __int16 v_stack_pC;

    v_rsp = (v_rsp) - (744);
    v_stack_m1D0 = 0x240022ULL;
    v_stack_m1C8 = v_rip + 214665;
    v_stack_m1C0 = 0x10000EULL;
    v_stack_m1B8 = v_rip + 214689;
    v_stack_m1D8 = v_rip + 214686;
    v_stack_m1A8 = v_rip + 214723;
    v_stack_m198 = v_rip + 214389;
    v_stack_m188 = v_rip + 214423;
    v_stack_m178 = v_rip + 214489;
    v_stack_m168 = v_rip + 214507;
    v_stack_m158 = v_rip + 215277;
    v_stack_m148 = v_rip + 215295;
    v_stack_m138 = v_rip + 215329;
    v_stack_m128 = v_rip + 215363;
    v_stack_m118 = v_rip + 215109;
    v_stack_m108 = v_rip + 215127;
    v_stack_mF8 = v_rip + 215145;
    v_stack_mE8 = v_rip + 215163;
    v_stack_mD8 = v_rip + 214845;
    v_stack_mC8 = v_rip + 214895;
    v_stack_m218 = v_rip + 214929;
    v_stack_m208 = v_rip + 214966;
    v_stack_m1E8 = v_rip + 214539;
    v_stack_m1F8 = v_rip + 214576;
    v_stack_mB8 = v_rip + 214629;
    v_stack_mA8 = v_rip + 214679;
    v_stack_m238 = v_rip + 215225;
    v_stack_m228 = v_rip + 215278;
    v_stack_m2F8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 1037264)));
    v_stack_m1E0 = 0x260024ULL;
    v_stack_m1B0 = 0x2A0028ULL;
    v_stack_m1A0 = 0x280026ULL;
    v_stack_m190 = 0x50004EULL;
    v_stack_m180 = 0x140012ULL;
    v_stack_m170 = 0x2A0028ULL;
    v_stack_m160 = 0x1A0018ULL;
    v_stack_m150 = 0x2E002CULL;
    v_stack_m140 = 0x2C002AULL;
    v_stack_m130 = 0x1A0018ULL;
    v_stack_m120 = 0x20001EULL;
    v_stack_m110 = 0x1A0018ULL;
    v_stack_m100 = 0x1C001AULL;
    v_stack_mF0 = 0x10000EULL;
    v_stack_mE0 = 0x380036ULL;
    v_stack_mD0 = 0x220020ULL;
    v_stack_m220 = 0x280026ULL;
    v_stack_m210 = 0x2E002CULL;
    v_stack_m1F0 = 0x2A0028ULL;
    v_stack_m200 = 0x320030ULL;
    v_stack_mC0 = 0x40003EULL;
    v_stack_mB0 = 0x440042ULL;
    v_stack_m240 = 0x3C003AULL;
    v_stack_m230 = 0x520050ULL;
    v_stack_m2F4 = (unsigned __int16)(*(unsigned __int16 *)(v_rip - 1037511));
    v_stack_m2F0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 1037518)));
    v_stack_m2EC = (unsigned __int16)(*(unsigned __int16 *)(v_rip - 1037525));
    v_stack_m2E8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 1037564)));
    v_stack_m2E4 = (unsigned __int16)(*(unsigned __int16 *)(v_rip - 1037571));
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 1037578)));
    v_stack_p1C = (unsigned __int16)(*(unsigned __int16 *)(v_rip - 1037587));
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 1037564)));
    v_stack_pC = (unsigned __int16)(*(unsigned __int16 *)(v_rip - 1037573));
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 1037582)));
    v_stack_p24 = (unsigned __int16)(*(unsigned __int16 *)(v_rip - 1037591));
    v_stack_m300 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 1037632)));
    v_stack_m2FC = (unsigned __int16)(*(unsigned __int16 *)(v_rip - 1037639));
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 1037646)));
    v_stack_p14 = (unsigned __int16)(*(unsigned __int16 *)(v_rip - 1037655));
    if (((64) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3662915) + 240) + 132))))) != 0) goto loc_00C48714;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3662915) + 240))) != 1) goto loc_00C48714;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3662915) + 240))) > 0x83400ULL) goto loc_00C48714;
    goto loc_00C48716;
loc_00C48714:
    a1 = 0;
loc_00C48716:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3662915) + 240) + 132))) >> (7));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int8 *)(v_rip + 2225359) = 0;
    *(unsigned __int8 *)(v_rip + 2225354) = 0;
    *(unsigned __int8 *)(v_rip + 2225614) = (unsigned __int8)(result);
    result = RtlLengthRequiredSid(1, 64, a3, a4);
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740703) = result;
    result = ExAllocatePool2(96, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2225617) = result;
    result = ExAllocatePool2(96, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2225510) = result;
    result = ExAllocatePool2(96, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2225571) = result;
    result = ExAllocatePool2(96, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2225544) = result;
    result = ExAllocatePool2(96, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2225549) = result;
    result = ExAllocatePool2(96, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2225538) = result;
    result = ExAllocatePool2(96, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2225416) = result;
    v_stack_m270 = *(unsigned __int64 *)(v_rip + 3740570);
    if (*(unsigned __int64 *)(v_rip + 3740570) == 0) goto loc_00C4A5AD;
    v_stack_m308 = *(unsigned __int64 *)(v_rip + 2225484);
    if (*(unsigned __int64 *)(v_rip + 2225484) == 0) goto loc_00C4A5AD;
    if (*(unsigned __int64 *)(v_rip + 2225471) == 0) goto loc_00C4A5AD;
    if (*(unsigned __int64 *)(v_rip + 2225439) == 0) goto loc_00C4A5AD;
    if (*(unsigned __int64 *)(v_rip + 2225335) == 0) goto loc_00C4A5AD;
    if (*(unsigned __int64 *)(v_rip + 2225399) == 0) goto loc_00C4A5AD;
    if (result == 0) goto loc_00C4A5AD;
    if (*(unsigned __int64 *)(v_rip + 2225366) == 0) goto loc_00C4A5AD;
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 3740570), v_stack_m2F8, 1, a4);
    result = RtlInitializeSid(v_stack_m308, v_stack_m2F0, 1, a4);
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 2225471), v_stack_m2E8, 1, a4);
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 2225439), v_stack_p18, 1, a4);
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 2225335), v_stack_p18, 1, a4);
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 2225399), v_stack_p18, 1, a4);
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 2225366), v_stack_p18, 1, a4);
    result = RtlInitializeSid(result, v_stack_p18, 1, a4);
    a1 = 0;
    *(unsigned int *)(v_stack_m270 + 8) = 0;
    *(unsigned int *)(v_stack_m308 + 8) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2225471) + 8) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2225439) + 8) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2225335) + 8) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2225399) + 8) = (unsigned int)(a1 + 2);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2225366) + 8) = 3;
    *(unsigned int *)(result + 8) = 4;
    result = RtlLengthRequiredSid(a1, v_stack_p18, 1, a4);
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740940) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740647) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2225064) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2225052) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2224608) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2224964) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740376) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2225020) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740344) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3739916) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3739824) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3739948) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740008) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740116) = result;
    result = RtlLengthRequiredSid((unsigned int)((unsigned int)(a1 + 2)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3739638) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3739986) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740230) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740218) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740174) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740162) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740166) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 3740157) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870534) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870610) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870502) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870506) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870494) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2224546) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2224510) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2224578) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2224141) = result;
    result = RtlLengthRequiredSid(a1 + 2 + 8, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870223) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870243) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870231) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870187) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870175) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870195) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870186) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870139) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870127) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870147) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870135) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870091) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2870079) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869915) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869903) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869859) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869847) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869858) = result;
    result = RtlLengthRequiredSid(a1 + 2 + 4, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    v_stack_m98 = (unsigned int)((unsigned int)(result));
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2224069) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2223705) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869941) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869932) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869949) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2867617) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2867605) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869897) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869853) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869841) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869637) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869609) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869572) = result;
    result = RtlLengthRequiredSid(a1 + 2 + 7, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869774) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869762) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869542) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2869530) = result;
    result = ExAllocatePool2((unsigned int)((unsigned int)(a1 + 2 + 94)), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2223406) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2223394) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2223353) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    *(unsigned __int64 *)(v_rip + 2223338) = result;
    result = ExAllocatePool2(288, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((unsigned int)(0x69536553ULL))), a4);
    a3 = 0;
    *(unsigned __int64 *)(v_rip + 2223335) = result;
    if (*(unsigned __int64 *)(v_rip + 3739489) == 0) goto loc_00C4A5AD;
    v_stack_p18 = *(unsigned __int64 *)(v_rip + 3739188);
    if (*(unsigned __int64 *)(v_rip + 3739188) == 0) goto loc_00C4A5AD;
    v_stack_m308 = *(unsigned __int64 *)(v_rip + 2223605);
    if (*(unsigned __int64 *)(v_rip + 2223605) == 0) goto loc_00C4A5AD;
    v_stack_m278 = *(unsigned __int64 *)(v_rip + 2223592);
    if (*(unsigned __int64 *)(v_rip + 2223592) == 0) goto loc_00C4A5AD;
    v_stack_m280 = *(unsigned __int64 *)(v_rip + 2223148);
    if (*(unsigned __int64 *)(v_rip + 2223148) == 0) goto loc_00C4A5AD;
    v_stack_m288 = *(unsigned __int64 *)(v_rip + 3738936);
    if (*(unsigned __int64 *)(v_rip + 3738936) == 0) goto loc_00C4A5AD;
    v_stack_m290 = *(unsigned __int64 *)(v_rip + 2223484);
    if (*(unsigned __int64 *)(v_rip + 2223484) == 0) goto loc_00C4A5AD;
    v_stack_m298 = *(unsigned __int64 *)(v_rip + 2223560);
    if (*(unsigned __int64 *)(v_rip + 2223560) == 0) goto loc_00C4A5AD;
    v_stack_m2A0 = *(unsigned __int64 *)(v_rip + 3738884);
    if (*(unsigned __int64 *)(v_rip + 3738884) == 0) goto loc_00C4A5AD;
    v_stack_m2A8 = *(unsigned __int64 *)(v_rip + 3738456);
    if (*(unsigned __int64 *)(v_rip + 3738456) == 0) goto loc_00C4A5AD;
    v_stack_m2B0 = *(unsigned __int64 *)(v_rip + 3738364);
    if (*(unsigned __int64 *)(v_rip + 3738364) == 0) goto loc_00C4A5AD;
    v_stack_m2B8 = *(unsigned __int64 *)(v_rip + 3738487);
    if (*(unsigned __int64 *)(v_rip + 3738487) == 0) goto loc_00C4A5AD;
    v_stack_m2C0 = *(unsigned __int64 *)(v_rip + 3738546);
    if (*(unsigned __int64 *)(v_rip + 3738546) == 0) goto loc_00C4A5AD;
    v_stack_m2C8 = *(unsigned __int64 *)(v_rip + 3738653);
    if (*(unsigned __int64 *)(v_rip + 3738653) == 0) goto loc_00C4A5AD;
    v_stack_m2D0 = *(unsigned __int64 *)(v_rip + 3738184);
    if (*(unsigned __int64 *)(v_rip + 3738184) == 0) goto loc_00C4A5AD;
    v_stack_m2D8 = *(unsigned __int64 *)(v_rip + 3738531);
    if (*(unsigned __int64 *)(v_rip + 3738531) == 0) goto loc_00C4A5AD;
    v_stack_m2E0 = *(unsigned __int64 *)(v_rip + 3738774);
    if (*(unsigned __int64 *)(v_rip + 3738774) == 0) goto loc_00C4A5AD;
    v_stack_m2E8 = *(unsigned __int64 *)(v_rip + 3738761);
    if (*(unsigned __int64 *)(v_rip + 3738761) == 0) goto loc_00C4A5AD;
    v_stack_m2F0 = *(unsigned __int64 *)(v_rip + 3738716);
    if (*(unsigned __int64 *)(v_rip + 3738716) == 0) goto loc_00C4A5AD;
    if (*(unsigned __int64 *)(v_rip + 3738703) == 0) goto loc_00C4A5AD;
    if (*(unsigned __int64 *)(v_rip + 3738711) == 0) goto loc_00C4A5AD;
    if (*(unsigned __int64 *)(v_rip + 3738703) == 0) goto loc_00C4A5AD;
    v_stack_m2F8 = *(unsigned __int64 *)(v_rip + 2869087);
    if (*(unsigned __int64 *)(v_rip + 2869087) == 0) goto loc_00C4A5AD;
    v_stack_m268 = *(unsigned __int64 *)(v_rip + 2869162);
    if (*(unsigned __int64 *)(v_rip + 2869162) == 0) goto loc_00C4A5AD;
    v_stack_m260 = *(unsigned __int64 *)(v_rip + 2869054);
    if (*(unsigned __int64 *)(v_rip + 2869054) == 0) goto loc_00C4A5AD;
    v_stack_m258 = *(unsigned __int64 *)(v_rip + 2869058);
    if (*(unsigned __int64 *)(v_rip + 2869058) == 0) goto loc_00C4A5AD;
    v_stack_m250 = *(unsigned __int64 *)(v_rip + 2869046);
    if (*(unsigned __int64 *)(v_rip + 2869046) == 0) goto loc_00C4A5AD;
    v_stack_m248 = *(unsigned __int64 *)(v_rip + 2223098);
    if (*(unsigned __int64 *)(v_rip + 2223098) == 0) goto loc_00C4A5AD;
    v_stack_m270 = *(unsigned __int64 *)(v_rip + 2223062);
    if (*(unsigned __int64 *)(v_rip + 2223062) == 0) goto loc_00C4A5AD;
    if (*(unsigned __int64 *)(v_rip + 2223130) == 0) goto loc_00C4A5AD;
    if (*(unsigned __int64 *)(v_rip + 2222698) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868794)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868821)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868816)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868779)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868774)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868801)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868796)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868759)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868754)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868781)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868776)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868739)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868734)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868577)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868572)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868535)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868530)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868549)) == 0) goto loc_00C4A5AD;
    if (*(unsigned __int64 *)(v_rip + 2222784) == 0) goto loc_00C4A5AD;
    v_stack_m88 = *(unsigned __int64 *)(v_rip + 2868680);
    if (*(unsigned __int64 *)(v_rip + 2868680) == 0) goto loc_00C4A5AD;
    v_stack_m80 = *(unsigned __int64 *)(v_rip + 2868665);
    if (*(unsigned __int64 *)(v_rip + 2868665) == 0) goto loc_00C4A5AD;
    v_stack_m78 = *(unsigned __int64 *)(v_rip + 2868682);
    if (*(unsigned __int64 *)(v_rip + 2868682) == 0) goto loc_00C4A5AD;
    v_stack_m68 = *(unsigned __int64 *)(v_rip + 2866347);
    if (*(unsigned __int64 *)(v_rip + 2866347) == 0) goto loc_00C4A5AD;
    v_stack_m50 = *(unsigned __int64 *)(v_rip + 2866332);
    if (*(unsigned __int64 *)(v_rip + 2866332) == 0) goto loc_00C4A5AD;
    v_stack_m70 = *(unsigned __int64 *)(v_rip + 2868621);
    if (*(unsigned __int64 *)(v_rip + 2868621) == 0) goto loc_00C4A5AD;
    v_stack_m60 = *(unsigned __int64 *)(v_rip + 2868574);
    if (*(unsigned __int64 *)(v_rip + 2868574) == 0) goto loc_00C4A5AD;
    v_stack_m90 = *(unsigned __int64 *)(v_rip + 2868559);
    if (*(unsigned __int64 *)(v_rip + 2868559) == 0) goto loc_00C4A5AD;
    v_stack_mA0 = *(unsigned __int64 *)(v_rip + 2222240);
    if (*(unsigned __int64 *)(v_rip + 2222240) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868329)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868308)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868279)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868506)) == 0) goto loc_00C4A5AD;
    v_stack_m58 = *(unsigned __int64 *)(v_rip + 2868485);
    if (*(unsigned __int64 *)(v_rip + 2868485) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868278)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2868257)) == 0) goto loc_00C4A5AD;
    if (*(unsigned __int64 *)(v_rip + 2222148) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2222116)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2222127)) == 0) goto loc_00C4A5AD;
    if ((*(unsigned __int64 *)(v_rip + 2222098)) == 0) goto loc_00C4A5AD;
    if (result == 0) goto loc_00C4A5AD;
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 3739489), v_stack_p8, a3, a4);
    result = RtlInitializeSid(v_stack_p18, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m308, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m278, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m280, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m288, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m290, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m298, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2A0, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2A8, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2B0, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2B8, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2C0, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2C8, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2D0, v_stack_p8, 2, a4);
    result = RtlInitializeSid(v_stack_m2D8, v_stack_p8, 2, a4);
    result = RtlInitializeSid(v_stack_m2E0, v_stack_p8, 2, a4);
    result = RtlInitializeSid(v_stack_m2E8, v_stack_p8, 2, a4);
    result = RtlInitializeSid(v_stack_m2F0, v_stack_p8, 2, a4);
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 3738703), v_stack_p8, 2, a4);
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 3738711), v_stack_p8, 2, a4);
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 3738703), v_stack_p8, 2, a4);
    result = RtlInitializeSid(v_stack_mA0, v_stack_p8, 6, a4);
    result = RtlInitializeSid(v_stack_m2F8, v_stack_p20, 1, a4);
    result = RtlInitializeSid(v_stack_m268, v_stack_p20, 1, a4);
    result = RtlInitializeSid(v_stack_m260, v_stack_p20, 1, a4);
    result = RtlInitializeSid(v_stack_m258, v_stack_p20, 1, a4);
    result = RtlInitializeSid(v_stack_m250, v_stack_p20, 1, a4);
    result = RtlInitializeSid(v_stack_m248, v_stack_m300, 1, a4);
    result = RtlInitializeSid(v_stack_m270, v_stack_m300, 1, a4);
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 2223130), v_stack_m300, 2, a4);
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 2222698), v_stack_m300, 2, a4);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_rip + 2222784), a2, v_stack_m98, a4);
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 2222784), v_stack_p8, 6, a4);
    result = RtlInitializeSid(v_stack_m90, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m88, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m80, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m78, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m68, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m50, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m70, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m60, v_stack_p10, 2, a4);
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 2222148), v_stack_m300, 2, a4);
    *(unsigned int *)(v_stack_p18 + 8) = 1;
    *(unsigned int *)(v_stack_m308 + 8) = 2;
    *(unsigned int *)(v_stack_m278 + 8) = (unsigned int)(2 + 1);
    *(unsigned int *)(v_stack_m280 + 8) = 4;
    *(unsigned int *)(v_stack_m288 + 8) = 6;
    *(unsigned int *)(v_stack_m290 + 8) = 10;
    *(unsigned int *)(v_stack_m298 + 8) = 18;
    *(unsigned int *)(v_stack_m2A0 + 8) = 11;
    *(unsigned int *)(v_stack_m2A8 + 8) = 12;
    *(unsigned int *)(v_stack_m2B0 + 8) = 7;
    *(unsigned int *)(v_stack_m2B8 + 8) = 19;
    *(unsigned int *)(v_stack_m2C0 + 8) = 20;
    *(unsigned int *)(v_stack_m2C8 + 8) = 17;
    *(unsigned int *)(v_stack_m2D0 + 8) = (unsigned int)(2 + 30);
    *(unsigned int *)(v_stack_m2D8 + 8) = (unsigned int)(2 + 30);
    *(unsigned int *)(v_stack_m2E0 + 8) = (unsigned int)(2 + 30);
    *(unsigned int *)(v_stack_m2E8 + 8) = (unsigned int)(2 + 30);
    *(unsigned int *)(v_stack_m2F0 + 8) = (unsigned int)(2 + 30);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3738703) + 8) = (unsigned int)(2 + 30);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3738711) + 8) = (unsigned int)(2 + 30);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3738703) + 8) = (unsigned int)(2 + 30);
    *(unsigned int *)(v_stack_m2D0 + 12) = 544;
    *(unsigned int *)(v_stack_m2D8 + 12) = 545;
    *(unsigned int *)(v_stack_m2E0 + 12) = 546;
    *(unsigned int *)(v_stack_m2E8 + 12) = 547;
    *(unsigned int *)(v_stack_m2F0 + 12) = 548;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3738703) + 12) = 549;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3738711) + 12) = 550;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 3738703) + 12) = 551;
    *(unsigned int *)(v_stack_m268 + 8) = (unsigned int)((unsigned int)(0x1000ULL));
    *(unsigned int *)(v_stack_m260 + 8) = (unsigned int)((unsigned int)(0x2000ULL));
    *(unsigned int *)(v_stack_m258 + 8) = 0x3000ULL;
    *(unsigned int *)(v_stack_m250 + 8) = 0x4000ULL;
    *(unsigned int *)(v_stack_m248 + 8) = 2;
    *(unsigned int *)(v_stack_m270 + 8) = (unsigned int)(2 + 1);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2223130) + 8) = 2;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2223130) + 12) = 1;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2222698) + 8) = 2;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2222698) + 12) = 2;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2222148) + 8) = (unsigned int)(2 + 1);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2222148) + 12) = 0x10000ULL;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m1D0, v_stack_m58, *(unsigned __int64 *)(v_rip + 2866956), v_stack_m2D0);
    v_rdi = 0;
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m1C0, *(unsigned __int64 *)(v_rip + 2867112), *(unsigned __int64 *)(v_rip + 2866963), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m1E0, *(unsigned __int64 *)(v_rip + 2867081), *(unsigned __int64 *)(v_rip + 2866940), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m1B0, *(unsigned __int64 *)(v_rip + 2867050), *(unsigned __int64 *)(v_rip + 2866885), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m1A0, *(unsigned __int64 *)(v_rip + 2867016), *(unsigned __int64 *)(v_rip + 2866862), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m190, *(unsigned __int64 *)(v_rip + 2866982), *(unsigned __int64 *)(v_rip + 2866868), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m180, *(unsigned __int64 *)(v_rip + 2866948), *(unsigned __int64 *)(v_rip + 2866842), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m170, *(unsigned __int64 *)(v_rip + 2866914), *(unsigned __int64 *)(v_rip + 2866784), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m160, *(unsigned __int64 *)(v_rip + 2866880), *(unsigned __int64 *)(v_rip + 2866758), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m150, *(unsigned __int64 *)(v_rip + 2866846), *(unsigned __int64 *)(v_rip + 2866764), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m140, *(unsigned __int64 *)(v_rip + 2866812), *(unsigned __int64 *)(v_rip + 2866738), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m130, *(unsigned __int64 *)(v_rip + 2866778), *(unsigned __int64 *)(v_rip + 2866680), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m120, *(unsigned __int64 *)(v_rip + 2866744), *(unsigned __int64 *)(v_rip + 2866654), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m110, *(unsigned __int64 *)(v_rip + 2866710), *(unsigned __int64 *)(v_rip + 2866476), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m100, *(unsigned __int64 *)(v_rip + 2866676), *(unsigned __int64 *)(v_rip + 2866450), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_mF0, *(unsigned __int64 *)(v_rip + 2866642), *(unsigned __int64 *)(v_rip + 2866392), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_mE0, *(unsigned __int64 *)(v_rip + 2866608), *(unsigned __int64 *)(v_rip + 2866366), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_mD0, *(unsigned __int64 *)(v_rip + 2866574), *(unsigned __int64 *)(v_rip + 2866364), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_mC0, *(unsigned __int64 *)(v_rip + 2866540), *(unsigned __int64 *)(v_rip + 2220274), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_mB0, *(unsigned __int64 *)(v_rip + 2866506), *(unsigned __int64 *)(v_rip + 2220216), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m240, *(unsigned __int64 *)(v_rip + 2866475), *(unsigned __int64 *)(v_rip + 2220190), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m230, *(unsigned __int64 *)(v_rip + 2866444), *(unsigned __int64 *)(v_rip + 2220183), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2220448) + 8) = 84;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 2866364) + 8) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2866313) + 8) = (unsigned int)((unsigned int)(0x400ULL));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2866313) + 12) = (unsigned int)((unsigned int)(0x2000ULL));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2866307) + 8) = (unsigned int)((unsigned int)(0x400ULL));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2866307) + 12) = (unsigned int)((unsigned int)(0x1000ULL));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2866333) + 8) = (unsigned int)((unsigned int)(0x400ULL));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2866333) + 12) = (unsigned int)((unsigned int)(0x400ULL));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2864003) + 8) = 512;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2864003) + 12) = 0x600ULL;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2863994) + 8) = 512;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2863994) + 12) = (unsigned int)((unsigned int)(0x2000ULL));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2866292) + 8) = 512;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2866292) + 12) = (unsigned int)((unsigned int)(0x1000ULL));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2866254) + 8) = 512;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2866254) + 12) = 0x800ULL;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2219946) + 8) = 80;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2219946) + 12) = 0x38FB89B5ULL;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2219946) + 16) = 0xCBC28419ULL;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2219946) + 20) = 0x6D236C5CULL;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2219946) + 24) = 0x6E770057ULL;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2219946) + 28) = 0x876402C0ULL;
    result = RtlInitializeSid(*(unsigned __int64 *)(v_rip + 2866202), v_stack_p8, 2, v_stack_m2D0);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2866202) + 8) = 32;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 2866202) + 12) = 581;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m220, *(unsigned __int64 *)(v_rip + 2866201), *(unsigned __int64 *)(v_rip + 2865996), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m210, *(unsigned __int64 *)(v_rip + 2866156), *(unsigned __int64 *)(v_rip + 2865935), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m200, *(unsigned __int64 *)(v_rip + 2866125), *(unsigned __int64 *)(v_rip + 2866144), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m1F0, *(unsigned __int64 *)(v_rip + 2865902), *(unsigned __int64 *)(v_rip + 2865921), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = SepInitSystemDacls(v_stack_m1F0, *(unsigned __int64 *)(v_rip + 2865902), *(unsigned __int64 *)(v_rip + 2865921), v_stack_m2D0);
    v_stack_p10 = 3;
    *(unsigned __int64 *)(v_rip + 3735199) = 2;
    *(unsigned __int64 *)(v_rip + 3735257) = v_stack_p10;
    v_stack_p18 = 4;
    *(unsigned __int64 *)(v_rip + 3734984) = v_stack_p18;
    v_stack_p20 = 5;
    *(unsigned __int64 *)(v_rip + 3735119) = v_stack_p20;
    v_stack_m2E8 = 6;
    *(unsigned __int64 *)(v_rip + 3736274) = v_stack_m2E8;
    v_stack_m2F0 = 7;
    *(unsigned __int64 *)(v_rip + 3734829) = v_stack_m2F0;
    v_stack_m308 = 24;
    v_stack_m2F8 = 8;
    *(unsigned __int64 *)(v_rip + 3734930) = v_stack_m2F8;
    v_stack_m308 = 25;
    v_stack_m300 = 9;
    *(unsigned __int64 *)(v_rip + 3734951) = v_stack_m300;
    v_stack_m2E0 = 10;
    *(unsigned __int64 *)(v_rip + 3734906) = v_stack_m2E0;
    v_stack_m308 = 26;
    v_stack_m2D8 = 15;
    *(unsigned __int64 *)(v_rip + 3735420) = v_stack_m2D8;
    v_stack_m2D0 = 14;
    *(unsigned __int64 *)(v_rip + 3734799) = v_stack_m2D0;
    v_stack_m2C8 = 11;
    *(unsigned __int64 *)(v_rip + 3734874) = v_stack_m2C8;
    v_stack_m2C0 = 12;
    *(unsigned __int64 *)(v_rip + 3735005) = v_stack_m2C0;
    v_stack_m2B8 = 13;
    *(unsigned __int64 *)(v_rip + 3734768) = v_stack_m2B8;
    v_stack_m2B0 = 16;
    *(unsigned __int64 *)(v_rip + 3734947) = v_stack_m2B0;
    v_stack_m2A8 = 17;
    *(unsigned __int64 *)(v_rip + 3734656) = v_stack_m2A8;
    v_stack_m2A0 = 18;
    *(unsigned __int64 *)(v_rip + 3734669) = v_stack_m2A0;
    v_stack_m298 = 19;
    *(unsigned __int64 *)(v_rip + 3734730) = v_stack_m298;
    v_stack_m290 = 20;
    *(unsigned __int64 *)(v_rip + 3734535) = v_stack_m290;
    v_stack_p8 = 2;
    v_stack_m308 = 27;
    v_stack_m288 = 21;
    v_stack_m280 = 22;
    v_stack_m278 = 23;
    *(unsigned __int64 *)(v_rip + 3734870) = v_stack_m288;
    v_stack_m308 = 28;
    *(unsigned __int64 *)(v_rip + 3734501) = v_stack_m280;
    *(unsigned __int64 *)(v_rip + 3735158) = v_stack_m278;
    *(unsigned __int64 *)(v_rip + 3735423) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3735640) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3735817) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3735146) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3736228) = *(unsigned __int64 *)(v_rip + 3734651);
    *(unsigned __int64 *)(v_rip + 3736222) = *(unsigned __int64 *)(v_rip + 2219581);
    *(unsigned __int64 *)(v_rip + 3736216) = *(unsigned __int64 *)(v_rip + 2219575);
    *(unsigned __int64 *)(v_rip + 3736210) = *(unsigned __int64 *)(v_rip + 2219545);
    *(unsigned __int64 *)(v_rip + 3736204) = *(unsigned __int64 *)(v_rip + 2219443);
    *(unsigned __int64 *)(v_rip + 3736486) = *(unsigned __int64 *)(v_rip + 2219437);
    *(unsigned __int64 *)(v_rip + 3736184) = *(unsigned __int64 *)(v_rip + 3735303);
    *(unsigned __int64 *)(v_rip + 3736178) = *(unsigned __int64 *)(v_rip + 3735017);
    *(unsigned __int64 *)(v_rip + 3736172) = *(unsigned __int64 *)(v_rip + 2219443);
    *(unsigned __int64 *)(v_rip + 3736166) = *(unsigned __int64 *)(v_rip + 2219437);
    *(unsigned __int64 *)(v_rip + 3736160) = *(unsigned __int64 *)(v_rip + 2218999);
    *(unsigned __int64 *)(v_rip + 3736154) = *(unsigned __int64 *)(v_rip + 2219457);
    *(unsigned __int64 *)(v_rip + 3736212) = *(unsigned __int64 *)(v_rip + 3734787);
    *(unsigned __int64 *)(v_rip + 3736206) = *(unsigned __int64 *)(v_rip + 3734365);
    *(unsigned __int64 *)(v_rip + 3736200) = *(unsigned __int64 *)(v_rip + 3734279);
    *(unsigned __int64 *)(v_rip + 3736218) = *(unsigned __int64 *)(v_rip + 3734409);
    *(unsigned __int64 *)(v_rip + 3736212) = *(unsigned __int64 *)(v_rip + 3734475);
    *(unsigned __int64 *)(v_rip + 3736270) = *(unsigned __int64 *)(v_rip + 3734589);
    *(unsigned __int64 *)(v_rip + 3736064) = *(unsigned __int64 *)(v_rip + 3734127);
    *(unsigned __int64 *)(v_rip + 3736058) = *(unsigned __int64 *)(v_rip + 3734481);
    *(unsigned __int64 *)(v_rip + 3736052) = *(unsigned __int64 *)(v_rip + 3734731);
    *(unsigned __int64 *)(v_rip + 3736046) = *(unsigned __int64 *)(v_rip + 3734725);
    *(unsigned __int64 *)(v_rip + 3736040) = *(unsigned __int64 *)(v_rip + 3734687);
    *(unsigned __int64 *)(v_rip + 3736034) = *(unsigned __int64 *)(v_rip + 3734681);
    *(unsigned __int64 *)(v_rip + 3736028) = *(unsigned __int64 *)(v_rip + 3734691);
    v_stack_m308 = 29;
    v_stack_m308 = 30;
    v_stack_m308 = 31;
    v_stack_m308 = 32;
    v_stack_m308 = 33;
    v_stack_m308 = 34;
    v_stack_m308 = 35;
    *(unsigned __int64 *)(v_rip + 3735924) = *(unsigned __int64 *)(v_rip + 3734685);
    v_stack_m308 = 36;
    *(unsigned __int64 *)(v_rip + 3736040) = *(unsigned __int64 *)(v_rip + 2864973);
    *(unsigned __int64 *)(v_rip + 3736034) = *(unsigned __int64 *)(v_rip + 2865041);
    *(unsigned __int64 *)(v_rip + 3734643) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3734892) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3734421) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3734606) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3734039) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3734840) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3734609) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3735074) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3734851) = v_stack_m308;
    *(unsigned __int64 *)(v_rip + 3735965) = *(unsigned __int64 *)(v_rip + 2864876);
    *(unsigned __int64 *)(v_rip + 3735959) = *(unsigned __int64 *)(v_rip + 2864886);
    *(unsigned __int64 *)(v_rip + 3735953) = *(unsigned __int64 *)(v_rip + 2864880);
    *(unsigned __int64 *)(v_rip + 3735955) = *(unsigned __int64 *)(v_rip + 2219010);
    *(unsigned __int64 *)(v_rip + 3735949) = *(unsigned __int64 *)(v_rip + 2218916);
    *(unsigned __int64 *)(v_rip + 3735943) = *(unsigned __int64 *)(v_rip + 2864814);
    *(unsigned __int64 *)(v_rip + 3735937) = *(unsigned __int64 *)(v_rip + 2218544);
    *(unsigned __int64 *)(v_rip + 3735939) = *(unsigned __int64 *)(v_rip + 2218562);
    v_r13 = (v_stack_p8) >> (32);
    *(unsigned int *)(v_rip + 3735365) = (unsigned int)(v_r13);
    v_r13 = (v_stack_p10) >> (32);
    *(unsigned int *)(v_rip + 3735355) = (unsigned int)(v_r13);
    v_r13 = (v_stack_p18) >> (32);
    *(unsigned int *)(v_rip + 3735345) = (unsigned int)(v_r13);
    v_r13 = (v_stack_p20) >> (32);
    *(unsigned int *)(v_rip + 3735335) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m2E8) >> (32);
    *(unsigned int *)(v_rip + 3735327) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m2F0) >> (32);
    *(unsigned int *)(v_rip + 3735319) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m2F8) >> (32);
    *(unsigned int *)(v_rip + 3735311) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m300) >> (32);
    *(unsigned int *)(v_rip + 3735303) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m2E0) >> (32);
    *(unsigned int *)(v_rip + 3735295) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m2D8) >> (32);
    *(unsigned int *)(v_rip + 3735287) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m2D0) >> (32);
    *(unsigned int *)(v_rip + 3735279) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m2C8) >> (32);
    *(unsigned int *)(v_rip + 3735271) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m2C0) >> (32);
    *(unsigned int *)(v_rip + 3735263) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m2B8) >> (32);
    *(unsigned int *)(v_rip + 3735255) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m2B0) >> (32);
    *(unsigned int *)(v_rip + 3735247) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m2A8) >> (32);
    *(unsigned int *)(v_rip + 3735240) = (unsigned int)(v_r13);
    *(unsigned int *)(v_rip + 3735106) = 2;
    *(unsigned int *)(v_rip + 3735104) = 3;
    *(unsigned int *)(v_rip + 3735102) = 4;
    *(unsigned int *)(v_rip + 3735100) = 5;
    *(unsigned int *)(v_rip + 3735098) = 6;
    *(unsigned int *)(v_rip + 3735096) = 7;
    *(unsigned int *)(v_rip + 3735094) = 8;
    *(unsigned int *)(v_rip + 3735092) = 9;
    *(unsigned int *)(v_rip + 3735090) = 10;
    *(unsigned int *)(v_rip + 3735088) = 15;
    *(unsigned int *)(v_rip + 3735086) = 14;
    *(unsigned int *)(v_rip + 3735084) = 11;
    *(unsigned int *)(v_rip + 3735082) = 12;
    *(unsigned int *)(v_rip + 3735080) = 13;
    *(unsigned int *)(v_rip + 3735078) = 16;
    *(unsigned int *)(v_rip + 3735076) = 17;
    *(unsigned int *)(v_rip + 3735074) = 18;
    v_r13 = (v_stack_m2A0) >> (32);
    *(unsigned int *)(v_rip + 3735063) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m298) >> (32);
    *(unsigned int *)(v_rip + 3735056) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m290) >> (32);
    *(unsigned int *)(v_rip + 3735049) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m288) >> (32);
    *(unsigned int *)(v_rip + 3735042) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m280) >> (32);
    *(unsigned int *)(v_rip + 3735035) = (unsigned int)(v_r13);
    v_r13 = (v_stack_m278) >> (32);
    v_r12 = (v_stack_m308) >> (32);
    v_r15 = (v_stack_m308) >> (32);
    v_r14 = (v_stack_m308) >> (32);
    v_rsi = (v_stack_m308) >> (32);
    v_rdi = (v_stack_m308) >> (32);
    v_rbx = (v_stack_m308) >> (32);
    v_r11 = (v_stack_m308) >> (32);
    v_r10 = (v_stack_m308) >> (32);
    a4 = (v_stack_m308) >> (32);
    a3 = (v_stack_m308) >> (32);
    a2 = (v_stack_m308) >> (32);
    a1 = (v_stack_m308) >> (32);
    result = (v_stack_m308) >> (32);
    *(unsigned int *)(v_rip + 3735361) = (unsigned int)(result);
    *(unsigned __int64 *)(v_rip + 3735359) = *(unsigned __int64 *)(v_rip + 2217982);
    *(unsigned __int64 *)(v_rip + 3735353) = *(unsigned __int64 *)(v_rip + 2217944);
    *(unsigned __int64 *)(v_rip + 3735347) = *(unsigned __int64 *)(v_rip + 2217938);
    *(unsigned __int64 *)(v_rip + 3735341) = *(unsigned __int64 *)(v_rip + 2217948);
    *(unsigned int *)(v_rip + 3734875) = 19;
    *(unsigned int *)(v_rip + 3734873) = 20;
    *(unsigned int *)(v_rip + 3734871) = 21;
    *(unsigned int *)(v_rip + 3734869) = 22;
    *(unsigned int *)(v_rip + 3734867) = 23;
    *(unsigned int *)(v_rip + 3734864) = (unsigned int)(v_r13);
    *(unsigned int *)(v_rip + 3734858) = 24;
    *(unsigned int *)(v_rip + 3734855) = (unsigned int)(v_r12);
    *(unsigned int *)(v_rip + 3735025) = 25;
    *(unsigned int *)(v_rip + 3735022) = (unsigned int)(v_r15);
    *(unsigned int *)(v_rip + 3735016) = 26;
    *(unsigned int *)(v_rip + 3735013) = (unsigned int)(v_r14);
    *(unsigned int *)(v_rip + 3735007) = 27;
    *(unsigned int *)(v_rip + 3735005) = (unsigned int)(v_rsi);
    *(unsigned int *)(v_rip + 3735015) = 28;
    *(unsigned int *)(v_rip + 3735013) = (unsigned int)(v_rdi);
    *(unsigned int *)(v_rip + 3735007) = 29;
    *(unsigned int *)(v_rip + 3735005) = (unsigned int)(v_rbx);
    *(unsigned int *)(v_rip + 3734999) = 30;
    *(unsigned int *)(v_rip + 3734996) = (unsigned int)(v_r11);
    *(unsigned int *)(v_rip + 3734990) = 31;
    *(unsigned int *)(v_rip + 3734987) = (unsigned int)(v_r10);
    *(unsigned int *)(v_rip + 3734981) = 32;
    *(unsigned int *)(v_rip + 3734978) = (unsigned int)(a4);
    *(unsigned int *)(v_rip + 3734972) = 33;
    *(unsigned int *)(v_rip + 3734969) = (unsigned int)(a3);
    *(unsigned int *)(v_rip + 3734963) = 34;
    *(unsigned int *)(v_rip + 3734961) = (unsigned int)(a2);
    *(unsigned int *)(v_rip + 3734955) = 35;
    *(unsigned int *)(v_rip + 3734953) = (unsigned int)(a1);
    *(unsigned int *)(v_rip + 3735035) = 36;
    result = Feature_AgenticAppContainerBfsSupport__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    v_rdi = 0;
    if ((unsigned int)(result) != 0) {
        result = *(unsigned __int64 *)(v_rip + 2217617);
        *(unsigned __int64 *)(v_rip + 3735058) = result;
    }
    *(unsigned __int64 *)(v_rip + 3732823) = v_rip + 3734451;
loc_00C4A552:
    *(unsigned __int8 *)(v_rip + 2906470 + 8) = 0;
    *(unsigned __int64 *)(v_rip + 2906470) = 0;
    *(unsigned __int64 *)(v_rip + 2906470 - 24) = 0;
    a1 = (5) - (1);
    if (condition_is_not_equal) goto loc_00C4A552;
    *(unsigned __int64 *)(v_rip + 2906394) = 0;
    *(unsigned __int64 *)(v_rip + 2906379) = 0;
    result = SepInitializeSharedSidMap(a1, a2, a3, a4);
    if (sign_flag) goto loc_00C4A5AD;
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00C4A5A9;
loc_00C4A58E:
    *(unsigned __int64 *)(v_rip + 2860946) = 0;
    v_rbx = (5) - (1);
    if (condition_is_not_equal) goto loc_00C4A58E;
    *(unsigned __int64 *)(v_rip + 2860910) = 0;
    *(unsigned __int64 *)(v_rip + 2860895) = 0;
loc_00C4A5A9:
    goto loc_00C4A5AF;
loc_00C4A5AD:
    result = 0;
loc_00C4A5AF:
    v_rsp = (v_rsp) + (744);
    return result;
}
```

## 5. (Beta) C Style

```c
void SepVariableInitialization(void)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint16_t v_stack_m2E4;
    uint32_t v_stack_m2E8;
    uint16_t v_stack_m2EC;
    uint32_t v_stack_m2F0;
    uint16_t v_stack_m2F4;
    uint32_t v_stack_m2F8;
    uint16_t v_stack_m2FC;
    uint32_t v_stack_m300;
    uint64_t v_stack_m308;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint16_t v_stack_p14;
    uint32_t v_stack_p18;
    uint16_t v_stack_p1C;
    uint32_t v_stack_p20;
    uint16_t v_stack_p24;
    uint32_t v_stack_p8;
    uint16_t v_stack_pC;

    local_rsp = (local_rsp) - (744);
    v_stack_m1D0 = 0x240022ULL;
    v_stack_m1C8 = v_rip + 214665;
    v_stack_m1C0 = 0x10000EULL;
    v_stack_m1B8 = v_rip + 214689;
    v_stack_m1D8 = v_rip + 214686;
    v_stack_m1A8 = v_rip + 214723;
    v_stack_m198 = v_rip + 214389;
    v_stack_m188 = v_rip + 214423;
    v_stack_m178 = v_rip + 214489;
    v_stack_m168 = v_rip + 214507;
    v_stack_m158 = v_rip + 215277;
    v_stack_m148 = v_rip + 215295;
    v_stack_m138 = v_rip + 215329;
    v_stack_m128 = v_rip + 215363;
    v_stack_m118 = v_rip + 215109;
    v_stack_m108 = v_rip + 215127;
    v_stack_mF8 = v_rip + 215145;
    v_stack_mE8 = v_rip + 215163;
    v_stack_mD8 = v_rip + 214845;
    v_stack_mC8 = v_rip + 214895;
    v_stack_m218 = v_rip + 214929;
    v_stack_m208 = v_rip + 214966;
    v_stack_m1E8 = v_rip + 214539;
    v_stack_m1F8 = v_rip + 214576;
    v_stack_mB8 = v_rip + 214629;
    v_stack_mA8 = v_rip + 214679;
    v_stack_m238 = v_rip + 215225;
    v_stack_m228 = v_rip + 215278;
    v_stack_m2F8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xFD3D0)));
    v_stack_m1E0 = 0x260024ULL;
    v_stack_m1B0 = 0x2A0028ULL;
    v_stack_m1A0 = 0x280026ULL;
    v_stack_m190 = 0x50004EULL;
    v_stack_m180 = 0x140012ULL;
    v_stack_m170 = 0x2A0028ULL;
    v_stack_m160 = 0x1A0018ULL;
    v_stack_m150 = 0x2E002CULL;
    v_stack_m140 = 0x2C002AULL;
    v_stack_m130 = 0x1A0018ULL;
    v_stack_m120 = 0x20001EULL;
    v_stack_m110 = 0x1A0018ULL;
    v_stack_m100 = 0x1C001AULL;
    v_stack_mF0 = 0x10000EULL;
    v_stack_mE0 = 0x380036ULL;
    v_stack_mD0 = 0x220020ULL;
    v_stack_m220 = 0x280026ULL;
    v_stack_m210 = 0x2E002CULL;
    v_stack_m1F0 = 0x2A0028ULL;
    v_stack_m200 = 0x320030ULL;
    v_stack_mC0 = 0x40003EULL;
    v_stack_mB0 = 0x440042ULL;
    v_stack_m240 = 0x3C003AULL;
    v_stack_m230 = 0x520050ULL;
    v_stack_m2F4 = (uint16_t)(*(uint16_t *)(v_rip - 0xFD4C7));
    v_stack_m2F0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xFD4CE)));
    v_stack_m2EC = (uint16_t)(*(uint16_t *)(v_rip - 0xFD4D5));
    v_stack_m2E8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xFD4FC)));
    v_stack_m2E4 = (uint16_t)(*(uint16_t *)(v_rip - 0xFD503));
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xFD50A)));
    v_stack_p1C = (uint16_t)(*(uint16_t *)(v_rip - 0xFD513));
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xFD4FC)));
    v_stack_pC = (uint16_t)(*(uint16_t *)(v_rip - 0xFD505));
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xFD50E)));
    v_stack_p24 = (uint16_t)(*(uint16_t *)(v_rip - 0xFD517));
    v_stack_m300 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xFD540)));
    v_stack_m2FC = (uint16_t)(*(uint16_t *)(v_rip - 0xFD547));
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0xFD54E)));
    v_stack_p14 = (uint16_t)(*(uint16_t *)(v_rip - 0xFD557));
    if (((64) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x37E443) + 0xF0) + 0x84))))) != 0) goto loc_00C48714;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x37E443) + 0xF0))) != 1) goto loc_00C48714;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x37E443) + 0xF0))) > 0x83400ULL) goto loc_00C48714;
    goto loc_00C48716;
loc_00C48714:
    a1 = 0;
loc_00C48716:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x37E443) + 0xF0) + 0x84))) >> (7));
    result = (uint8_t)((result) & (1));
    *(uint8_t *)(v_rip + 0x21F4CF) = 0;
    *(uint8_t *)(v_rip + 0x21F4CA) = 0;
    *(uint8_t *)(v_rip + 0x21F5CE) = (uint8_t)(result);
    result = RtlLengthRequiredSid(1, 64, a3, a4);
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x39141F) = result;
    result = ExAllocatePool2(96, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F5D1) = result;
    result = ExAllocatePool2(96, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F566) = result;
    result = ExAllocatePool2(96, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F5A3) = result;
    result = ExAllocatePool2(96, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F588) = result;
    result = ExAllocatePool2(96, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F58D) = result;
    result = ExAllocatePool2(96, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F582) = result;
    result = ExAllocatePool2(96, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F508) = result;
    v_stack_m270 = *(uint64_t *)(v_rip + 0x39139A);
    if (*(uint64_t *)(v_rip + 0x39139A) == 0) goto loc_00C4A5AD;
    v_stack_m308 = *(uint64_t *)(v_rip + 0x21F54C);
    if (*(uint64_t *)(v_rip + 0x21F54C) == 0) goto loc_00C4A5AD;
    if (*(uint64_t *)(v_rip + 0x21F53F) == 0) goto loc_00C4A5AD;
    if (*(uint64_t *)(v_rip + 0x21F51F) == 0) goto loc_00C4A5AD;
    if (*(uint64_t *)(v_rip + 0x21F4B7) == 0) goto loc_00C4A5AD;
    if (*(uint64_t *)(v_rip + 0x21F4F7) == 0) goto loc_00C4A5AD;
    if (result == 0) goto loc_00C4A5AD;
    if (*(uint64_t *)(v_rip + 0x21F4D6) == 0) goto loc_00C4A5AD;
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x39139A), v_stack_m2F8, 1, a4);
    result = RtlInitializeSid(v_stack_m308, v_stack_m2F0, 1, a4);
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x21F53F), v_stack_m2E8, 1, a4);
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x21F51F), v_stack_p18, 1, a4);
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x21F4B7), v_stack_p18, 1, a4);
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x21F4F7), v_stack_p18, 1, a4);
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x21F4D6), v_stack_p18, 1, a4);
    result = RtlInitializeSid(result, v_stack_p18, 1, a4);
    a1 = 0;
    *(uint32_t *)(v_stack_m270 + 0x8) = 0;
    *(uint32_t *)(v_stack_m308 + 0x8) = 0;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21F53F) + 0x8) = 0;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21F51F) + 0x8) = 0;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21F4B7) + 0x8) = 1;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21F4F7) + 0x8) = (uint32_t)(a1 + 2);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21F4D6) + 0x8) = 3;
    *(uint32_t *)(result + 0x8) = 4;
    result = RtlLengthRequiredSid(a1, v_stack_p18, 1, a4);
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x39150C) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x3913E7) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F3A8) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F39C) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F1E0) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F344) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x3912D8) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F37C) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x3912B8) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x39110C) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x3910B0) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x39112C) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x391168) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x3911D4) = result;
    result = RtlLengthRequiredSid((uint32_t)((uint32_t)(a1 + 2)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x390FF6) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x391152) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x391246) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x39123A) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x39120E) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x391202) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x391206) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x3911FD) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCD06) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCD52) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCCE6) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCCEA) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCCDE) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F1A2) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F17E) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F1C2) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21F00D) = result;
    result = RtlLengthRequiredSid(a1 + 2 + 8, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCBCF) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCBE3) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCBD7) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCBAB) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCB9F) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCBB3) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCBAA) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCB7B) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCB6F) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCB83) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCB77) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCB4B) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCB3F) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCA9B) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCA8F) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCA63) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCA57) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCA62) = result;
    result = RtlLengthRequiredSid(a1 + 2 + 4, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    v_stack_m98 = (uint32_t)((uint32_t)(result));
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21EFC5) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21EE59) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCAB5) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCAAC) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCABD) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BC1A1) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BC195) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCA89) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCA5D) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCA51) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BC985) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BC969) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BC944) = result;
    result = RtlLengthRequiredSid(a1 + 2 + 7, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCA0E) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BCA02) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BC926) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x2BC91A) = result;
    result = ExAllocatePool2((uint32_t)((uint32_t)(a1 + 2 + 94)), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21ED2E) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21ED22) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21ECF9) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    *(uint64_t *)(v_rip + 0x21ECEA) = result;
    result = ExAllocatePool2(288, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((uint32_t)(0x69536553ULL))), a4);
    a3 = 0;
    *(uint64_t *)(v_rip + 0x21ECE7) = result;
    if (*(uint64_t *)(v_rip + 0x390F61) == 0) goto loc_00C4A5AD;
    v_stack_p18 = *(uint64_t *)(v_rip + 0x390E34);
    if (*(uint64_t *)(v_rip + 0x390E34) == 0) goto loc_00C4A5AD;
    v_stack_m308 = *(uint64_t *)(v_rip + 0x21EDF5);
    if (*(uint64_t *)(v_rip + 0x21EDF5) == 0) goto loc_00C4A5AD;
    v_stack_m278 = *(uint64_t *)(v_rip + 0x21EDE8);
    if (*(uint64_t *)(v_rip + 0x21EDE8) == 0) goto loc_00C4A5AD;
    v_stack_m280 = *(uint64_t *)(v_rip + 0x21EC2C);
    if (*(uint64_t *)(v_rip + 0x21EC2C) == 0) goto loc_00C4A5AD;
    v_stack_m288 = *(uint64_t *)(v_rip + 0x390D38);
    if (*(uint64_t *)(v_rip + 0x390D38) == 0) goto loc_00C4A5AD;
    v_stack_m290 = *(uint64_t *)(v_rip + 0x21ED7C);
    if (*(uint64_t *)(v_rip + 0x21ED7C) == 0) goto loc_00C4A5AD;
    v_stack_m298 = *(uint64_t *)(v_rip + 0x21EDC8);
    if (*(uint64_t *)(v_rip + 0x21EDC8) == 0) goto loc_00C4A5AD;
    v_stack_m2A0 = *(uint64_t *)(v_rip + 0x390D04);
    if (*(uint64_t *)(v_rip + 0x390D04) == 0) goto loc_00C4A5AD;
    v_stack_m2A8 = *(uint64_t *)(v_rip + 0x390B58);
    if (*(uint64_t *)(v_rip + 0x390B58) == 0) goto loc_00C4A5AD;
    v_stack_m2B0 = *(uint64_t *)(v_rip + 0x390AFC);
    if (*(uint64_t *)(v_rip + 0x390AFC) == 0) goto loc_00C4A5AD;
    v_stack_m2B8 = *(uint64_t *)(v_rip + 0x390B77);
    if (*(uint64_t *)(v_rip + 0x390B77) == 0) goto loc_00C4A5AD;
    v_stack_m2C0 = *(uint64_t *)(v_rip + 0x390BB2);
    if (*(uint64_t *)(v_rip + 0x390BB2) == 0) goto loc_00C4A5AD;
    v_stack_m2C8 = *(uint64_t *)(v_rip + 0x390C1D);
    if (*(uint64_t *)(v_rip + 0x390C1D) == 0) goto loc_00C4A5AD;
    v_stack_m2D0 = *(uint64_t *)(v_rip + 0x390A48);
    if (*(uint64_t *)(v_rip + 0x390A48) == 0) goto loc_00C4A5AD;
    v_stack_m2D8 = *(uint64_t *)(v_rip + 0x390BA3);
    if (*(uint64_t *)(v_rip + 0x390BA3) == 0) goto loc_00C4A5AD;
    v_stack_m2E0 = *(uint64_t *)(v_rip + 0x390C96);
    if (*(uint64_t *)(v_rip + 0x390C96) == 0) goto loc_00C4A5AD;
    v_stack_m2E8 = *(uint64_t *)(v_rip + 0x390C89);
    if (*(uint64_t *)(v_rip + 0x390C89) == 0) goto loc_00C4A5AD;
    v_stack_m2F0 = *(uint64_t *)(v_rip + 0x390C5C);
    if (*(uint64_t *)(v_rip + 0x390C5C) == 0) goto loc_00C4A5AD;
    if (*(uint64_t *)(v_rip + 0x390C4F) == 0) goto loc_00C4A5AD;
    if (*(uint64_t *)(v_rip + 0x390C57) == 0) goto loc_00C4A5AD;
    if (*(uint64_t *)(v_rip + 0x390C4F) == 0) goto loc_00C4A5AD;
    v_stack_m2F8 = *(uint64_t *)(v_rip + 0x2BC75F);
    if (*(uint64_t *)(v_rip + 0x2BC75F) == 0) goto loc_00C4A5AD;
    v_stack_m268 = *(uint64_t *)(v_rip + 0x2BC7AA);
    if (*(uint64_t *)(v_rip + 0x2BC7AA) == 0) goto loc_00C4A5AD;
    v_stack_m260 = *(uint64_t *)(v_rip + 0x2BC73E);
    if (*(uint64_t *)(v_rip + 0x2BC73E) == 0) goto loc_00C4A5AD;
    v_stack_m258 = *(uint64_t *)(v_rip + 0x2BC742);
    if (*(uint64_t *)(v_rip + 0x2BC742) == 0) goto loc_00C4A5AD;
    v_stack_m250 = *(uint64_t *)(v_rip + 0x2BC736);
    if (*(uint64_t *)(v_rip + 0x2BC736) == 0) goto loc_00C4A5AD;
    v_stack_m248 = *(uint64_t *)(v_rip + 0x21EBFA);
    if (*(uint64_t *)(v_rip + 0x21EBFA) == 0) goto loc_00C4A5AD;
    v_stack_m270 = *(uint64_t *)(v_rip + 0x21EBD6);
    if (*(uint64_t *)(v_rip + 0x21EBD6) == 0) goto loc_00C4A5AD;
    if (*(uint64_t *)(v_rip + 0x21EC1A) == 0) goto loc_00C4A5AD;
    if (*(uint64_t *)(v_rip + 0x21EA6A) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC63A)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC655)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC650)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC62B)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC626)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC641)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC63C)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC617)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC612)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC62D)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC628)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC603)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC5FE)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC561)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC55C)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC537)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC532)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC545)) == 0) goto loc_00C4A5AD;
    if (*(uint64_t *)(v_rip + 0x21EAC0) == 0) goto loc_00C4A5AD;
    v_stack_m88 = *(uint64_t *)(v_rip + 0x2BC5C8);
    if (*(uint64_t *)(v_rip + 0x2BC5C8) == 0) goto loc_00C4A5AD;
    v_stack_m80 = *(uint64_t *)(v_rip + 0x2BC5B9);
    if (*(uint64_t *)(v_rip + 0x2BC5B9) == 0) goto loc_00C4A5AD;
    v_stack_m78 = *(uint64_t *)(v_rip + 0x2BC5CA);
    if (*(uint64_t *)(v_rip + 0x2BC5CA) == 0) goto loc_00C4A5AD;
    v_stack_m68 = *(uint64_t *)(v_rip + 0x2BBCAB);
    if (*(uint64_t *)(v_rip + 0x2BBCAB) == 0) goto loc_00C4A5AD;
    v_stack_m50 = *(uint64_t *)(v_rip + 0x2BBC9C);
    if (*(uint64_t *)(v_rip + 0x2BBC9C) == 0) goto loc_00C4A5AD;
    v_stack_m70 = *(uint64_t *)(v_rip + 0x2BC58D);
    if (*(uint64_t *)(v_rip + 0x2BC58D) == 0) goto loc_00C4A5AD;
    v_stack_m60 = *(uint64_t *)(v_rip + 0x2BC55E);
    if (*(uint64_t *)(v_rip + 0x2BC55E) == 0) goto loc_00C4A5AD;
    v_stack_m90 = *(uint64_t *)(v_rip + 0x2BC54F);
    if (*(uint64_t *)(v_rip + 0x2BC54F) == 0) goto loc_00C4A5AD;
    v_stack_mA0 = *(uint64_t *)(v_rip + 0x21E8A0);
    if (*(uint64_t *)(v_rip + 0x21E8A0) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC469)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC454)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC437)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC51A)) == 0) goto loc_00C4A5AD;
    v_stack_m58 = *(uint64_t *)(v_rip + 0x2BC505);
    if (*(uint64_t *)(v_rip + 0x2BC505) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC436)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x2BC421)) == 0) goto loc_00C4A5AD;
    if (*(uint64_t *)(v_rip + 0x21E844) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x21E824)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x21E82F)) == 0) goto loc_00C4A5AD;
    if ((*(uint64_t *)(v_rip + 0x21E812)) == 0) goto loc_00C4A5AD;
    if (result == 0) goto loc_00C4A5AD;
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x390F61), v_stack_p8, a3, a4);
    result = RtlInitializeSid(v_stack_p18, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m308, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m278, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m280, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m288, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m290, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m298, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2A0, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2A8, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2B0, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2B8, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2C0, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2C8, v_stack_p8, 1, a4);
    result = RtlInitializeSid(v_stack_m2D0, v_stack_p8, 2, a4);
    result = RtlInitializeSid(v_stack_m2D8, v_stack_p8, 2, a4);
    result = RtlInitializeSid(v_stack_m2E0, v_stack_p8, 2, a4);
    result = RtlInitializeSid(v_stack_m2E8, v_stack_p8, 2, a4);
    result = RtlInitializeSid(v_stack_m2F0, v_stack_p8, 2, a4);
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x390C4F), v_stack_p8, 2, a4);
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x390C57), v_stack_p8, 2, a4);
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x390C4F), v_stack_p8, 2, a4);
    result = RtlInitializeSid(v_stack_mA0, v_stack_p8, 6, a4);
    result = RtlInitializeSid(v_stack_m2F8, v_stack_p20, 1, a4);
    result = RtlInitializeSid(v_stack_m268, v_stack_p20, 1, a4);
    result = RtlInitializeSid(v_stack_m260, v_stack_p20, 1, a4);
    result = RtlInitializeSid(v_stack_m258, v_stack_p20, 1, a4);
    result = RtlInitializeSid(v_stack_m250, v_stack_p20, 1, a4);
    result = RtlInitializeSid(v_stack_m248, v_stack_m300, 1, a4);
    result = RtlInitializeSid(v_stack_m270, v_stack_m300, 1, a4);
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x21EC1A), v_stack_m300, 2, a4);
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x21EA6A), v_stack_m300, 2, a4);
    a2 = 0;
    result = memset(*(uint64_t *)(v_rip + 0x21EAC0), a2, v_stack_m98, a4);
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x21EAC0), v_stack_p8, 6, a4);
    result = RtlInitializeSid(v_stack_m90, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m88, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m80, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m78, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m68, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m50, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m70, v_stack_p10, 2, a4);
    result = RtlInitializeSid(v_stack_m60, v_stack_p10, 2, a4);
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x21E844), v_stack_m300, 2, a4);
    *(uint32_t *)(v_stack_p18 + 0x8) = 1;
    *(uint32_t *)(v_stack_m308 + 0x8) = 2;
    *(uint32_t *)(v_stack_m278 + 0x8) = (uint32_t)(2 + 1);
    *(uint32_t *)(v_stack_m280 + 0x8) = 4;
    *(uint32_t *)(v_stack_m288 + 0x8) = 6;
    *(uint32_t *)(v_stack_m290 + 0x8) = 10;
    *(uint32_t *)(v_stack_m298 + 0x8) = 18;
    *(uint32_t *)(v_stack_m2A0 + 0x8) = 11;
    *(uint32_t *)(v_stack_m2A8 + 0x8) = 12;
    *(uint32_t *)(v_stack_m2B0 + 0x8) = 7;
    *(uint32_t *)(v_stack_m2B8 + 0x8) = 19;
    *(uint32_t *)(v_stack_m2C0 + 0x8) = 20;
    *(uint32_t *)(v_stack_m2C8 + 0x8) = 17;
    *(uint32_t *)(v_stack_m2D0 + 0x8) = (uint32_t)(2 + 30);
    *(uint32_t *)(v_stack_m2D8 + 0x8) = (uint32_t)(2 + 30);
    *(uint32_t *)(v_stack_m2E0 + 0x8) = (uint32_t)(2 + 30);
    *(uint32_t *)(v_stack_m2E8 + 0x8) = (uint32_t)(2 + 30);
    *(uint32_t *)(v_stack_m2F0 + 0x8) = (uint32_t)(2 + 30);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x390C4F) + 0x8) = (uint32_t)(2 + 30);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x390C57) + 0x8) = (uint32_t)(2 + 30);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x390C4F) + 0x8) = (uint32_t)(2 + 30);
    *(uint32_t *)(v_stack_m2D0 + 0xC) = 544;
    *(uint32_t *)(v_stack_m2D8 + 0xC) = 545;
    *(uint32_t *)(v_stack_m2E0 + 0xC) = 546;
    *(uint32_t *)(v_stack_m2E8 + 0xC) = 547;
    *(uint32_t *)(v_stack_m2F0 + 0xC) = 548;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x390C4F) + 0xC) = 549;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x390C57) + 0xC) = 550;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x390C4F) + 0xC) = 551;
    *(uint32_t *)(v_stack_m268 + 0x8) = (uint32_t)((uint32_t)(0x1000ULL));
    *(uint32_t *)(v_stack_m260 + 0x8) = (uint32_t)((uint32_t)(0x2000ULL));
    *(uint32_t *)(v_stack_m258 + 0x8) = 0x3000ULL;
    *(uint32_t *)(v_stack_m250 + 0x8) = 0x4000ULL;
    *(uint32_t *)(v_stack_m248 + 0x8) = 2;
    *(uint32_t *)(v_stack_m270 + 0x8) = (uint32_t)(2 + 1);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21EC1A) + 0x8) = 2;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21EC1A) + 0xC) = 1;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21EA6A) + 0x8) = 2;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21EA6A) + 0xC) = 2;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21E844) + 0x8) = (uint32_t)(2 + 1);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21E844) + 0xC) = 0x10000ULL;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m1D0, v_stack_m58, *(uint64_t *)(v_rip + 0x2BBF0C), v_stack_m2D0);
    local_rdi = 0;
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m1C0, *(uint64_t *)(v_rip + 0x2BBFA8), *(uint64_t *)(v_rip + 0x2BBF13), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m1E0, *(uint64_t *)(v_rip + 0x2BBF89), *(uint64_t *)(v_rip + 0x2BBEFC), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m1B0, *(uint64_t *)(v_rip + 0x2BBF6A), *(uint64_t *)(v_rip + 0x2BBEC5), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m1A0, *(uint64_t *)(v_rip + 0x2BBF48), *(uint64_t *)(v_rip + 0x2BBEAE), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m190, *(uint64_t *)(v_rip + 0x2BBF26), *(uint64_t *)(v_rip + 0x2BBEB4), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m180, *(uint64_t *)(v_rip + 0x2BBF04), *(uint64_t *)(v_rip + 0x2BBE9A), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m170, *(uint64_t *)(v_rip + 0x2BBEE2), *(uint64_t *)(v_rip + 0x2BBE60), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m160, *(uint64_t *)(v_rip + 0x2BBEC0), *(uint64_t *)(v_rip + 0x2BBE46), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m150, *(uint64_t *)(v_rip + 0x2BBE9E), *(uint64_t *)(v_rip + 0x2BBE4C), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m140, *(uint64_t *)(v_rip + 0x2BBE7C), *(uint64_t *)(v_rip + 0x2BBE32), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m130, *(uint64_t *)(v_rip + 0x2BBE5A), *(uint64_t *)(v_rip + 0x2BBDF8), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m120, *(uint64_t *)(v_rip + 0x2BBE38), *(uint64_t *)(v_rip + 0x2BBDDE), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m110, *(uint64_t *)(v_rip + 0x2BBE16), *(uint64_t *)(v_rip + 0x2BBD2C), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m100, *(uint64_t *)(v_rip + 0x2BBDF4), *(uint64_t *)(v_rip + 0x2BBD12), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_mF0, *(uint64_t *)(v_rip + 0x2BBDD2), *(uint64_t *)(v_rip + 0x2BBCD8), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_mE0, *(uint64_t *)(v_rip + 0x2BBDB0), *(uint64_t *)(v_rip + 0x2BBCBE), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_mD0, *(uint64_t *)(v_rip + 0x2BBD8E), *(uint64_t *)(v_rip + 0x2BBCBC), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_mC0, *(uint64_t *)(v_rip + 0x2BBD6C), *(uint64_t *)(v_rip + 0x21E0F2), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_mB0, *(uint64_t *)(v_rip + 0x2BBD4A), *(uint64_t *)(v_rip + 0x21E0B8), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m240, *(uint64_t *)(v_rip + 0x2BBD2B), *(uint64_t *)(v_rip + 0x21E09E), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m230, *(uint64_t *)(v_rip + 0x2BBD0C), *(uint64_t *)(v_rip + 0x21E097), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21E1A0) + 0x8) = 84;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x2BBCBC) + 0x8) = 0;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BBC89) + 0x8) = (uint32_t)((uint32_t)(0x400ULL));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BBC89) + 0xC) = (uint32_t)((uint32_t)(0x2000ULL));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BBC83) + 0x8) = (uint32_t)((uint32_t)(0x400ULL));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BBC83) + 0xC) = (uint32_t)((uint32_t)(0x1000ULL));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BBC9D) + 0x8) = (uint32_t)((uint32_t)(0x400ULL));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BBC9D) + 0xC) = (uint32_t)((uint32_t)(0x400ULL));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BB383) + 0x8) = 512;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BB383) + 0xC) = 0x600ULL;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BB37A) + 0x8) = 512;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BB37A) + 0xC) = (uint32_t)((uint32_t)(0x2000ULL));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BBC74) + 0x8) = 512;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BBC74) + 0xC) = (uint32_t)((uint32_t)(0x1000ULL));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BBC4E) + 0x8) = 512;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BBC4E) + 0xC) = 0x800ULL;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21DFAA) + 0x8) = 80;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21DFAA) + 0xC) = 0x38FB89B5ULL;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21DFAA) + 0x10) = 0xCBC28419ULL;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21DFAA) + 0x14) = 0x6D236C5CULL;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21DFAA) + 0x18) = 0x6E770057ULL;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x21DFAA) + 0x1C) = 0x876402C0ULL;
    result = RtlInitializeSid(*(uint64_t *)(v_rip + 0x2BBC1A), v_stack_p8, 2, v_stack_m2D0);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BBC1A) + 0x8) = 32;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x2BBC1A) + 0xC) = 581;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m220, *(uint64_t *)(v_rip + 0x2BBC19), *(uint64_t *)(v_rip + 0x2BBB4C), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m210, *(uint64_t *)(v_rip + 0x2BBBEC), *(uint64_t *)(v_rip + 0x2BBB0F), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m200, *(uint64_t *)(v_rip + 0x2BBBCD), *(uint64_t *)(v_rip + 0x2BBBE0), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = RtlDeriveCapabilitySidsFromName(v_stack_m1F0, *(uint64_t *)(v_rip + 0x2BBAEE), *(uint64_t *)(v_rip + 0x2BBB01), v_stack_m2D0);
    if (sign_flag) goto loc_00C4A5AD;
    result = SepInitSystemDacls(v_stack_m1F0, *(uint64_t *)(v_rip + 0x2BBAEE), *(uint64_t *)(v_rip + 0x2BBB01), v_stack_m2D0);
    v_stack_p10 = 3;
    *(uint64_t *)(v_rip + 0x38FE9F) = 2;
    *(uint64_t *)(v_rip + 0x38FED9) = v_stack_p10;
    v_stack_p18 = 4;
    *(uint64_t *)(v_rip + 0x38FDC8) = v_stack_p18;
    v_stack_p20 = 5;
    *(uint64_t *)(v_rip + 0x38FE4F) = v_stack_p20;
    v_stack_m2E8 = 6;
    *(uint64_t *)(v_rip + 0x3902D2) = v_stack_m2E8;
    v_stack_m2F0 = 7;
    *(uint64_t *)(v_rip + 0x38FD2D) = v_stack_m2F0;
    v_stack_m308 = 24;
    v_stack_m2F8 = 8;
    *(uint64_t *)(v_rip + 0x38FD92) = v_stack_m2F8;
    v_stack_m308 = 25;
    v_stack_m300 = 9;
    *(uint64_t *)(v_rip + 0x38FDA7) = v_stack_m300;
    v_stack_m2E0 = 10;
    *(uint64_t *)(v_rip + 0x38FD7A) = v_stack_m2E0;
    v_stack_m308 = 26;
    v_stack_m2D8 = 15;
    *(uint64_t *)(v_rip + 0x38FF7C) = v_stack_m2D8;
    v_stack_m2D0 = 14;
    *(uint64_t *)(v_rip + 0x38FD0F) = v_stack_m2D0;
    v_stack_m2C8 = 11;
    *(uint64_t *)(v_rip + 0x38FD5A) = v_stack_m2C8;
    v_stack_m2C0 = 12;
    *(uint64_t *)(v_rip + 0x38FDDD) = v_stack_m2C0;
    v_stack_m2B8 = 13;
    *(uint64_t *)(v_rip + 0x38FCF0) = v_stack_m2B8;
    v_stack_m2B0 = 16;
    *(uint64_t *)(v_rip + 0x38FDA3) = v_stack_m2B0;
    v_stack_m2A8 = 17;
    *(uint64_t *)(v_rip + 0x38FC80) = v_stack_m2A8;
    v_stack_m2A0 = 18;
    *(uint64_t *)(v_rip + 0x38FC8D) = v_stack_m2A0;
    v_stack_m298 = 19;
    *(uint64_t *)(v_rip + 0x38FCCA) = v_stack_m298;
    v_stack_m290 = 20;
    *(uint64_t *)(v_rip + 0x38FC07) = v_stack_m290;
    v_stack_p8 = 2;
    v_stack_m308 = 27;
    v_stack_m288 = 21;
    v_stack_m280 = 22;
    v_stack_m278 = 23;
    *(uint64_t *)(v_rip + 0x38FD56) = v_stack_m288;
    v_stack_m308 = 28;
    *(uint64_t *)(v_rip + 0x38FBE5) = v_stack_m280;
    *(uint64_t *)(v_rip + 0x38FE76) = v_stack_m278;
    *(uint64_t *)(v_rip + 0x38FF7F) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x390058) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x390109) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x38FE6A) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x3902A4) = *(uint64_t *)(v_rip + 0x38FC7B);
    *(uint64_t *)(v_rip + 0x39029E) = *(uint64_t *)(v_rip + 0x21DE3D);
    *(uint64_t *)(v_rip + 0x390298) = *(uint64_t *)(v_rip + 0x21DE37);
    *(uint64_t *)(v_rip + 0x390292) = *(uint64_t *)(v_rip + 0x21DE19);
    *(uint64_t *)(v_rip + 0x39028C) = *(uint64_t *)(v_rip + 0x21DDB3);
    *(uint64_t *)(v_rip + 0x3903A6) = *(uint64_t *)(v_rip + 0x21DDAD);
    *(uint64_t *)(v_rip + 0x390278) = *(uint64_t *)(v_rip + 0x38FF07);
    *(uint64_t *)(v_rip + 0x390272) = *(uint64_t *)(v_rip + 0x38FDE9);
    *(uint64_t *)(v_rip + 0x39026C) = *(uint64_t *)(v_rip + 0x21DDB3);
    *(uint64_t *)(v_rip + 0x390266) = *(uint64_t *)(v_rip + 0x21DDAD);
    *(uint64_t *)(v_rip + 0x390260) = *(uint64_t *)(v_rip + 0x21DBF7);
    *(uint64_t *)(v_rip + 0x39025A) = *(uint64_t *)(v_rip + 0x21DDC1);
    *(uint64_t *)(v_rip + 0x390294) = *(uint64_t *)(v_rip + 0x38FD03);
    *(uint64_t *)(v_rip + 0x39028E) = *(uint64_t *)(v_rip + 0x38FB5D);
    *(uint64_t *)(v_rip + 0x390288) = *(uint64_t *)(v_rip + 0x38FB07);
    *(uint64_t *)(v_rip + 0x39029A) = *(uint64_t *)(v_rip + 0x38FB89);
    *(uint64_t *)(v_rip + 0x390294) = *(uint64_t *)(v_rip + 0x38FBCB);
    *(uint64_t *)(v_rip + 0x3902CE) = *(uint64_t *)(v_rip + 0x38FC3D);
    *(uint64_t *)(v_rip + 0x390200) = *(uint64_t *)(v_rip + 0x38FA6F);
    *(uint64_t *)(v_rip + 0x3901FA) = *(uint64_t *)(v_rip + 0x38FBD1);
    *(uint64_t *)(v_rip + 0x3901F4) = *(uint64_t *)(v_rip + 0x38FCCB);
    *(uint64_t *)(v_rip + 0x3901EE) = *(uint64_t *)(v_rip + 0x38FCC5);
    *(uint64_t *)(v_rip + 0x3901E8) = *(uint64_t *)(v_rip + 0x38FC9F);
    *(uint64_t *)(v_rip + 0x3901E2) = *(uint64_t *)(v_rip + 0x38FC99);
    *(uint64_t *)(v_rip + 0x3901DC) = *(uint64_t *)(v_rip + 0x38FCA3);
    v_stack_m308 = 29;
    v_stack_m308 = 30;
    v_stack_m308 = 31;
    v_stack_m308 = 32;
    v_stack_m308 = 33;
    v_stack_m308 = 34;
    v_stack_m308 = 35;
    *(uint64_t *)(v_rip + 0x390174) = *(uint64_t *)(v_rip + 0x38FC9D);
    v_stack_m308 = 36;
    *(uint64_t *)(v_rip + 0x3901E8) = *(uint64_t *)(v_rip + 0x2BB74D);
    *(uint64_t *)(v_rip + 0x3901E2) = *(uint64_t *)(v_rip + 0x2BB791);
    *(uint64_t *)(v_rip + 0x38FC73) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x38FD6C) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x38FB95) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x38FC4E) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x38FA17) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x38FD38) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x38FC51) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x38FE22) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x38FD43) = v_stack_m308;
    *(uint64_t *)(v_rip + 0x39019D) = *(uint64_t *)(v_rip + 0x2BB6EC);
    *(uint64_t *)(v_rip + 0x390197) = *(uint64_t *)(v_rip + 0x2BB6F6);
    *(uint64_t *)(v_rip + 0x390191) = *(uint64_t *)(v_rip + 0x2BB6F0);
    *(uint64_t *)(v_rip + 0x390193) = *(uint64_t *)(v_rip + 0x21DC02);
    *(uint64_t *)(v_rip + 0x39018D) = *(uint64_t *)(v_rip + 0x21DBA4);
    *(uint64_t *)(v_rip + 0x390187) = *(uint64_t *)(v_rip + 0x2BB6AE);
    *(uint64_t *)(v_rip + 0x390181) = *(uint64_t *)(v_rip + 0x21DA30);
    *(uint64_t *)(v_rip + 0x390183) = *(uint64_t *)(v_rip + 0x21DA42);
    local_r13 = (v_stack_p8) >> (32);
    *(uint32_t *)(v_rip + 0x38FF45) = (uint32_t)(local_r13);
    local_r13 = (v_stack_p10) >> (32);
    *(uint32_t *)(v_rip + 0x38FF3B) = (uint32_t)(local_r13);
    local_r13 = (v_stack_p18) >> (32);
    *(uint32_t *)(v_rip + 0x38FF31) = (uint32_t)(local_r13);
    local_r13 = (v_stack_p20) >> (32);
    *(uint32_t *)(v_rip + 0x38FF27) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m2E8) >> (32);
    *(uint32_t *)(v_rip + 0x38FF1F) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m2F0) >> (32);
    *(uint32_t *)(v_rip + 0x38FF17) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m2F8) >> (32);
    *(uint32_t *)(v_rip + 0x38FF0F) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m300) >> (32);
    *(uint32_t *)(v_rip + 0x38FF07) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m2E0) >> (32);
    *(uint32_t *)(v_rip + 0x38FEFF) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m2D8) >> (32);
    *(uint32_t *)(v_rip + 0x38FEF7) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m2D0) >> (32);
    *(uint32_t *)(v_rip + 0x38FEEF) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m2C8) >> (32);
    *(uint32_t *)(v_rip + 0x38FEE7) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m2C0) >> (32);
    *(uint32_t *)(v_rip + 0x38FEDF) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m2B8) >> (32);
    *(uint32_t *)(v_rip + 0x38FED7) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m2B0) >> (32);
    *(uint32_t *)(v_rip + 0x38FECF) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m2A8) >> (32);
    *(uint32_t *)(v_rip + 0x38FEC8) = (uint32_t)(local_r13);
    *(uint32_t *)(v_rip + 0x38FE42) = 2;
    *(uint32_t *)(v_rip + 0x38FE40) = 3;
    *(uint32_t *)(v_rip + 0x38FE3E) = 4;
    *(uint32_t *)(v_rip + 0x38FE3C) = 5;
    *(uint32_t *)(v_rip + 0x38FE3A) = 6;
    *(uint32_t *)(v_rip + 0x38FE38) = 7;
    *(uint32_t *)(v_rip + 0x38FE36) = 8;
    *(uint32_t *)(v_rip + 0x38FE34) = 9;
    *(uint32_t *)(v_rip + 0x38FE32) = 10;
    *(uint32_t *)(v_rip + 0x38FE30) = 15;
    *(uint32_t *)(v_rip + 0x38FE2E) = 14;
    *(uint32_t *)(v_rip + 0x38FE2C) = 11;
    *(uint32_t *)(v_rip + 0x38FE2A) = 12;
    *(uint32_t *)(v_rip + 0x38FE28) = 13;
    *(uint32_t *)(v_rip + 0x38FE26) = 16;
    *(uint32_t *)(v_rip + 0x38FE24) = 17;
    *(uint32_t *)(v_rip + 0x38FE22) = 18;
    local_r13 = (v_stack_m2A0) >> (32);
    *(uint32_t *)(v_rip + 0x38FE17) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m298) >> (32);
    *(uint32_t *)(v_rip + 0x38FE10) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m290) >> (32);
    *(uint32_t *)(v_rip + 0x38FE09) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m288) >> (32);
    *(uint32_t *)(v_rip + 0x38FE02) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m280) >> (32);
    *(uint32_t *)(v_rip + 0x38FDFB) = (uint32_t)(local_r13);
    local_r13 = (v_stack_m278) >> (32);
    local_r12 = (v_stack_m308) >> (32);
    local_r15 = (v_stack_m308) >> (32);
    local_r14 = (v_stack_m308) >> (32);
    local_rsi = (v_stack_m308) >> (32);
    local_rdi = (v_stack_m308) >> (32);
    local_rbx = (v_stack_m308) >> (32);
    local_r11 = (v_stack_m308) >> (32);
    local_r10 = (v_stack_m308) >> (32);
    a4 = (v_stack_m308) >> (32);
    a3 = (v_stack_m308) >> (32);
    a2 = (v_stack_m308) >> (32);
    a1 = (v_stack_m308) >> (32);
    result = (v_stack_m308) >> (32);
    *(uint32_t *)(v_rip + 0x38FF41) = (uint32_t)(result);
    *(uint64_t *)(v_rip + 0x38FF3F) = *(uint64_t *)(v_rip + 0x21D7FE);
    *(uint64_t *)(v_rip + 0x38FF39) = *(uint64_t *)(v_rip + 0x21D7D8);
    *(uint64_t *)(v_rip + 0x38FF33) = *(uint64_t *)(v_rip + 0x21D7D2);
    *(uint64_t *)(v_rip + 0x38FF2D) = *(uint64_t *)(v_rip + 0x21D7DC);
    *(uint32_t *)(v_rip + 0x38FD5B) = 19;
    *(uint32_t *)(v_rip + 0x38FD59) = 20;
    *(uint32_t *)(v_rip + 0x38FD57) = 21;
    *(uint32_t *)(v_rip + 0x38FD55) = 22;
    *(uint32_t *)(v_rip + 0x38FD53) = 23;
    *(uint32_t *)(v_rip + 0x38FD50) = (uint32_t)(local_r13);
    *(uint32_t *)(v_rip + 0x38FD4A) = 24;
    *(uint32_t *)(v_rip + 0x38FD47) = (uint32_t)(local_r12);
    *(uint32_t *)(v_rip + 0x38FDF1) = 25;
    *(uint32_t *)(v_rip + 0x38FDEE) = (uint32_t)(local_r15);
    *(uint32_t *)(v_rip + 0x38FDE8) = 26;
    *(uint32_t *)(v_rip + 0x38FDE5) = (uint32_t)(local_r14);
    *(uint32_t *)(v_rip + 0x38FDDF) = 27;
    *(uint32_t *)(v_rip + 0x38FDDD) = (uint32_t)(local_rsi);
    *(uint32_t *)(v_rip + 0x38FDE7) = 28;
    *(uint32_t *)(v_rip + 0x38FDE5) = (uint32_t)(local_rdi);
    *(uint32_t *)(v_rip + 0x38FDDF) = 29;
    *(uint32_t *)(v_rip + 0x38FDDD) = (uint32_t)(local_rbx);
    *(uint32_t *)(v_rip + 0x38FDD7) = 30;
    *(uint32_t *)(v_rip + 0x38FDD4) = (uint32_t)(local_r11);
    *(uint32_t *)(v_rip + 0x38FDCE) = 31;
    *(uint32_t *)(v_rip + 0x38FDCB) = (uint32_t)(local_r10);
    *(uint32_t *)(v_rip + 0x38FDC5) = 32;
    *(uint32_t *)(v_rip + 0x38FDC2) = (uint32_t)(a4);
    *(uint32_t *)(v_rip + 0x38FDBC) = 33;
    *(uint32_t *)(v_rip + 0x38FDB9) = (uint32_t)(a3);
    *(uint32_t *)(v_rip + 0x38FDB3) = 34;
    *(uint32_t *)(v_rip + 0x38FDB1) = (uint32_t)(a2);
    *(uint32_t *)(v_rip + 0x38FDAB) = 35;
    *(uint32_t *)(v_rip + 0x38FDA9) = (uint32_t)(a1);
    *(uint32_t *)(v_rip + 0x38FDFB) = 36;
    result = Feature_AgenticAppContainerBfsSupport__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    local_rdi = 0;
    if ((uint32_t)(result) != 0) {
        result = *(uint64_t *)(v_rip + 0x21D691);
        *(uint64_t *)(v_rip + 0x38FE12) = result;
    }
    *(uint64_t *)(v_rip + 0x38F557) = v_rip + 3734451;
loc_00C4A552:
    *(uint8_t *)(v_rip + 0x2C5966 + 0x8) = 0;
    *(uint64_t *)(v_rip + 0x2C5966) = 0;
    *(uint64_t *)(v_rip + 0x2C5966 - 0x18) = 0;
    a1 = (5) - (1);
    if (condition_is_not_equal) goto loc_00C4A552;
    *(uint64_t *)(v_rip + 0x2C591A) = 0;
    *(uint64_t *)(v_rip + 0x2C590B) = 0;
    result = SepInitializeSharedSidMap(a1, a2, a3, a4);
    if (sign_flag) goto loc_00C4A5AD;
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_00C4A5A9;
loc_00C4A58E:
    *(uint64_t *)(v_rip + 0x2BA792) = 0;
    local_rbx = (5) - (1);
    if (condition_is_not_equal) goto loc_00C4A58E;
    *(uint64_t *)(v_rip + 0x2BA76E) = 0;
    *(uint64_t *)(v_rip + 0x2BA75F) = 0;
loc_00C4A5A9:
    goto loc_00C4A5AF;
loc_00C4A5AD:
    result = 0;
loc_00C4A5AF:
    local_rsp = (local_rsp) + (744);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C483A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
