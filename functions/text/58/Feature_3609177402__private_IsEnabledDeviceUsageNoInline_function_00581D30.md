# Feature_3609177402__private_IsEnabledDeviceUsageNoInline

- RVA: `0x00581D30`–`0x00581D62` (길이 `50` bytes)
- VA: `0x0000000140581D30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00581D57` → [Feature_3609177402__private_IsEnabledFallback](Feature_3609177402__private_IsEnabledFallback_function_00581D68.md) (function, `0x00581D68`)

### Direct callers
- [FsRtlUninitializeOplock](../4E/FsRtlUninitializeOplock_function_004E42C0.md) at `0x004E4419`
- [FsRtlUninitializeOplock](../4E/FsRtlUninitializeOplock_function_004E42C0.md) at `0x004E444D`
- [FsRtlpCancelWaitingIrp](../4E/FsRtlpCancelWaitingIrp_function_004E4698.md) at `0x004E46D1`
- [FsRtlpCancelWaitingIrp](../4E/FsRtlpCancelWaitingIrp_function_004E4698.md) at `0x004E46F4`
- [FsRtlpCancelWaitingIrp](../4E/FsRtlpCancelWaitingIrp_function_004E4698.md) at `0x004E494B`
- [FsRtlpWaitOnIrp](../4E/FsRtlpWaitOnIrp_function_004E7998.md) at `0x004E7BAD`
- [FsRtlpCancelWaitingIrp$fin$0](../6D/FsRtlpCancelWaitingIrp_fin_0_function_006D5210.md) at `0x006D52B5`
- [FsRtlpAllocateOplock](../../page/9F/FsRtlpAllocateOplock_function_009F1C74.md) at `0x009F1D16`
- [FsRtlpAllocateOplock$fin$0](../../page/B1/FsRtlpAllocateOplock_fin_0_function_00B10E21.md) at `0x00B10E3B`

### Static image references
- `0x00581D3A` → RVA `0x00FC4720` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00581D30  48 83 EC 28                     sub rsp, 0x28
00581D34  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00581D3A  8B 05 E0 29 A4 00               mov eax, dword ptr [rip + 0xa429e0]
00581D40  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00581D44  A8 10                           test al, 0x10
00581D46  74 05                           je 0x140581d4d
00581D48  83 E0 01                        and eax, 1
00581D4B  EB 0F                           jmp 0x140581d5c
00581D4D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00581D52  BA 03 00 00 00                  mov edx, 3
00581D57  E8 0C 00 00 00                  call 0x140581d68
00581D5C  48 83 C4 28                     add rsp, 0x28
00581D60  C3                              ret
00581D61  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_3609177402__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10758624)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10758624)))) & (16)) == 0) goto loc_00581D4D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10758624))) & (1));
    goto loc_00581D5C;
loc_00581D4D:
    result = Feature_3609177402__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00581D5C:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_3609177402__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA429E0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA429E0)))) & (16)) == 0) goto loc_00581D4D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA429E0))) & (1));
    goto loc_00581D5C;
loc_00581D4D:
    result = Feature_3609177402__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00581D5C:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00581D30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00581D30[BB_00581D30]
  bb_00581D48[BB_00581D48]
  bb_00581D4D[BB_00581D4D]
  bb_00581D5C[BB_00581D5C]
  bb_00581D61[BB_00581D61]
  bb_00581D30 -->|branch| bb_00581D4D
  bb_00581D30 -->|fallthrough| bb_00581D48
  bb_00581D48 -->|branch| bb_00581D5C
  bb_00581D4D -->|flow| bb_00581D5C
```
