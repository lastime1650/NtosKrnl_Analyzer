# Feature_3043197241__private_IsEnabledDeviceUsageNoInline

- RVA: `0x00596C38`–`0x00596C6A` (길이 `50` bytes)
- VA: `0x0000000140596C38`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00596C5F` → [Feature_3043197241__private_IsEnabledFallback](Feature_3043197241__private_IsEnabledFallback_function_00596C70.md) (function, `0x00596C70`)

### Direct callers
- [IopSynchronousServiceTail](../../page/8E/IopSynchronousServiceTail_function_008EB440.md) at `0x008EB49F`

### Static image references
- `0x00596C42` → RVA `0x00FC47B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00596C38  48 83 EC 28                     sub rsp, 0x28
00596C3C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00596C42  8B 05 68 DB A2 00               mov eax, dword ptr [rip + 0xa2db68]
00596C48  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00596C4C  A8 10                           test al, 0x10
00596C4E  74 05                           je 0x140596c55
00596C50  83 E0 01                        and eax, 1
00596C53  EB 0F                           jmp 0x140596c64
00596C55  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00596C5A  BA 03 00 00 00                  mov edx, 3
00596C5F  E8 0C 00 00 00                  call 0x140596c70
00596C64  48 83 C4 28                     add rsp, 0x28
00596C68  C3                              ret
00596C69  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_3043197241__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10673000)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10673000)))) & (16)) == 0) goto loc_00596C55;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10673000))) & (1));
    goto loc_00596C64;
loc_00596C55:
    result = Feature_3043197241__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00596C64:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_3043197241__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA2DB68)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA2DB68)))) & (16)) == 0) goto loc_00596C55;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA2DB68))) & (1));
    goto loc_00596C64;
loc_00596C55:
    result = Feature_3043197241__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00596C64:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00596C38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00596C38[BB_00596C38]
  bb_00596C50[BB_00596C50]
  bb_00596C55[BB_00596C55]
  bb_00596C64[BB_00596C64]
  bb_00596C69[BB_00596C69]
  bb_00596C38 -->|branch| bb_00596C55
  bb_00596C38 -->|fallthrough| bb_00596C50
  bb_00596C50 -->|branch| bb_00596C64
  bb_00596C55 -->|flow| bb_00596C64
```
