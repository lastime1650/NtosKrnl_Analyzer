# Feature_Test52061194__private_IsEnabledNoReportingNoInline

- RVA: `0x00445C10`–`0x00445C3F` (길이 `47` bytes)
- VA: `0x0000000140445C10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C74`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00445C38` → [Feature_Test52061194__private_IsEnabledFallback](../4F/Feature_Test52061194__private_IsEnabledFallback_function_004F750C.md) (function, `0x004F750C`)

### Direct callers
- [HalpScanForProfilingCorruptionInternal](HalpScanForProfilingCorruptionInternal_function_00445A64.md) at `0x00445AAB`
- [HalpPerfInterrupt](HalpPerfInterrupt_function_00445B70.md) at `0x00445B84`
- [HalpCollectProfileOwnershipStatusInternal](../54/HalpCollectProfileOwnershipStatusInternal_function_00546E7C.md) at `0x00546F1F`
- [HalpCollectSamplingProfileCorruptionStatusInternal](../54/HalpCollectSamplingProfileCorruptionStatusInternal_function_0054715C.md) at `0x005471AF`

### Static image references
- `0x00445C1A` → RVA `0x00FC46D0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00445C10  48 83 EC 28                     sub rsp, 0x28
00445C14  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00445C1A  8B 05 B0 EA B7 00               mov eax, dword ptr [rip + 0xb7eab0]
00445C20  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00445C24  A8 02                           test al, 2
00445C26  74 09                           je 0x140445c31
00445C28  83 E0 01                        and eax, 1
00445C2B  48 83 C4 28                     add rsp, 0x28
00445C2F  C3                              ret
00445C30  CC                              int3
00445C31  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00445C36  33 D2                           xor edx, edx
00445C38  E8 CF 18 0B 00                  call 0x1404f750c
00445C3D  EB EC                           jmp 0x140445c2b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Test52061194__private_IsEnabledNoReportingNoInline(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12053168)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12053168)))) & (2)) == 0) goto loc_00445C31;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12053168))) & (1));
loc_00445C2B:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00445C31:
    a2 = 0;
    result = Feature_Test52061194__private_IsEnabledFallback(v_stack_p30, a2, a3, a4);
    goto loc_00445C2B;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_Test52061194__private_IsEnabledNoReportingNoInline(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB7EAB0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB7EAB0)))) & (2)) == 0) goto loc_00445C31;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB7EAB0))) & (1));
loc_00445C2B:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00445C31:
    Arg2 = 0;
    result = Feature_Test52061194__private_IsEnabledFallback(v_stack_p30, Arg2, a3, a4);
    goto loc_00445C2B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00445C10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00445C10[BB_00445C10]
  bb_00445C28[BB_00445C28]
  bb_00445C2B[BB_00445C2B]
  bb_00445C30[BB_00445C30]
  bb_00445C31[BB_00445C31]
  bb_00445C10 -->|branch| bb_00445C31
  bb_00445C10 -->|fallthrough| bb_00445C28
  bb_00445C28 -->|flow| bb_00445C2B
  bb_00445C30 -->|flow| bb_00445C31
  bb_00445C31 -->|branch| bb_00445C2B
```
