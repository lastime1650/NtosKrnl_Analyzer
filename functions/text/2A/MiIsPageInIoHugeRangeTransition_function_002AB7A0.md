# MiIsPageInIoHugeRangeTransition

- RVA: `0x002AB7A0`–`0x002AB7DF` (길이 `63` bytes)
- VA: `0x00000001402AB7A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `19`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002AB7A7` → [MiIsPageInHugePfn](MiIsPageInHugePfn_function_002AB770.md) (function, `0x002AB770`)

### Direct callers
- [MiReferenceIoPages](../23/MiReferenceIoPages_function_0023C804.md) at `0x0023CDC3`
- [MiDereferenceIoPages](MiDereferenceIoPages_function_002AB1B0.md) at `0x002AB5C7`
- [MiDereferenceIoHugeRange](../67/MiDereferenceIoHugeRange_function_006753F8.md) at `0x0067540F`
- [MiDeleteStaleCacheMaps](../67/MiDeleteStaleCacheMaps_function_0067B780.md) at `0x0067B9C5`

### Static image references
- `0x002AB7B3` → RVA `0x00E300C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002AB7A0  48 83 EC 28                     sub rsp, 0x28
002AB7A4  48 8B D1                        mov rdx, rcx
002AB7A7  E8 C4 FF FF FF                  call 0x1402ab770
002AB7AC  45 33 C0                        xor r8d, r8d
002AB7AF  85 C0                           test eax, eax
002AB7B1  74 28                           je 0x1402ab7db
002AB7B3  48 8B 0D 06 49 B8 00            mov rcx, qword ptr [rip + 0xb84906]
002AB7BA  48 C1 EA 12                     shr rdx, 0x12
002AB7BE  81 E2 FF FF 3F 00               and edx, 0x3fffff
002AB7C4  48 8B 0C D1                     mov rcx, qword ptr [rcx + rdx*8]
002AB7C8  80 E1 07                        and cl, 7
002AB7CB  80 F9 05                        cmp cl, 5
002AB7CE  41 0F 94 C0                     sete r8b
002AB7D2  41 8B C0                        mov eax, r8d
002AB7D5  48 83 C4 28                     add rsp, 0x28
002AB7D9  C3                              ret
002AB7DA  CC                              int3
002AB7DB  33 C0                           xor eax, eax
002AB7DD  EB F6                           jmp 0x1402ab7d5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiIsPageInIoHugeRangeTransition(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiIsPageInHugePfn(a1, a1, a3, a4);
    a3 = 0;
    if ((unsigned int)(result) == 0) goto loc_002AB7DB;
    a2 = (a1) >> (18);
    a2 = (unsigned int)((a2) & (0x3FFFFFULL));
    a1 = (unsigned __int8)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12077318) + a2 * 8)) & (7));
    a3 = (((unsigned __int8)(a1)) == 5) ? 1 : 0;
loc_002AB7D5:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(a3);
loc_002AB7DB:
    result = 0;
    goto loc_002AB7D5;
}
```

## 5. (Beta) C Style

```c
int64_t MiIsPageInIoHugeRangeTransition(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiIsPageInHugePfn(Arg1, Arg1, Arg3, a4);
    Arg3 = 0;
    if ((uint32_t)(result) == 0) goto loc_002AB7DB;
    Arg2 = (Arg1) >> (18);
    Arg2 = (uint32_t)((Arg2) & (0x3FFFFFULL));
    Arg1 = (uint8_t)((*(uint64_t *)(*(uint64_t *)(v_rip + 0xB84906) + Arg2 * 8)) & (7));
    Arg3 = (((uint8_t)(Arg1)) == 5) ? 1 : 0;
loc_002AB7D5:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(Arg3);
loc_002AB7DB:
    result = 0;
    goto loc_002AB7D5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002AB7A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002AB7A0[BB_002AB7A0]
  bb_002AB7B3[BB_002AB7B3]
  bb_002AB7D5[BB_002AB7D5]
  bb_002AB7DA[BB_002AB7DA]
  bb_002AB7DB[BB_002AB7DB]
  bb_002AB7A0 -->|branch| bb_002AB7DB
  bb_002AB7A0 -->|fallthrough| bb_002AB7B3
  bb_002AB7B3 -->|flow| bb_002AB7D5
  bb_002AB7DA -->|flow| bb_002AB7DB
  bb_002AB7DB -->|branch| bb_002AB7D5
```
