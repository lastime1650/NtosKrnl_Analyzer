# Feature_PrefetchQueueWorkerProactivelyForProcessExit__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0034A690`–`0x0034A6C2` (길이 `50` bytes)
- VA: `0x000000014034A690`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063CEC`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0034A6BB` → [Feature_PrefetchQueueWorkerProactivelyForProcessExit__private_IsEnabledFallback](../4F/Feature_PrefetchQueueWorkerProactivelyForProcessExit__private_IsEnabledFallback_function_004FD22C.md) (function, `0x004FD22C`)

### Direct callers
- [MiQueuePageAccessLog](MiQueuePageAccessLog_function_00348EB0.md) at `0x00348F1A`
- [MiQueuePageAccessLog](MiQueuePageAccessLog_function_00348EB0.md) at `0x00348F58`
- [PfpReturnAccessBuffer](../48/PfpReturnAccessBuffer_function_00488A80.md) at `0x00488AD3`
- [PfpReturnAccessBuffer](../48/PfpReturnAccessBuffer_function_00488A80.md) at `0x00488B15`
- [MiAllocatePfnRepurposeLogDispatch](../48/MiAllocatePfnRepurposeLogDispatch_function_00488BD0.md) at `0x00488CFC`
- [MiAllocatePfnRepurposeLogDispatch](../48/MiAllocatePfnRepurposeLogDispatch_function_00488BD0.md) at `0x00488D3E`

### Static image references
- `0x0034A69A` → RVA `0x00FC4AB0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0034A690  48 83 EC 28                     sub rsp, 0x28
0034A694  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0034A69A  8B 05 10 A4 C7 00               mov eax, dword ptr [rip + 0xc7a410]
0034A6A0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0034A6A4  A8 10                           test al, 0x10
0034A6A6  74 09                           je 0x14034a6b1
0034A6A8  83 E0 01                        and eax, 1
0034A6AB  48 83 C4 28                     add rsp, 0x28
0034A6AF  C3                              ret
0034A6B0  CC                              int3
0034A6B1  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0034A6B6  BA 03 00 00 00                  mov edx, 3
0034A6BB  E8 6C 2B 1B 00                  call 0x1404fd22c
0034A6C0  EB E9                           jmp 0x14034a6ab
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_PrefetchQueueWorkerProactivelyForProcessExit__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13083664)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 13083664)))) & (16)) == 0) goto loc_0034A6B1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 13083664))) & (1));
loc_0034A6AB:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0034A6B1:
    result = Feature_PrefetchQueueWorkerProactivelyForProcessExit__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_0034A6AB;
}
```

## 5. (Beta) C Style

```c
void Feature_PrefetchQueueWorkerProactivelyForProcessExit__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC7A410)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC7A410)))) & (16)) == 0) goto loc_0034A6B1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xC7A410))) & (1));
loc_0034A6AB:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0034A6B1:
    result = Feature_PrefetchQueueWorkerProactivelyForProcessExit__private_IsEnabledFallback(v_stack_p30, 3, a3, a4);
    goto loc_0034A6AB;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0034A690&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0034A690[BB_0034A690]
  bb_0034A6A8[BB_0034A6A8]
  bb_0034A6AB[BB_0034A6AB]
  bb_0034A6B0[BB_0034A6B0]
  bb_0034A6B1[BB_0034A6B1]
  bb_0034A690 -->|branch| bb_0034A6B1
  bb_0034A690 -->|fallthrough| bb_0034A6A8
  bb_0034A6A8 -->|flow| bb_0034A6AB
  bb_0034A6B0 -->|flow| bb_0034A6B1
  bb_0034A6B1 -->|branch| bb_0034A6AB
```
