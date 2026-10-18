# Feature_218004792__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0064F3EC`–`0x0064F41E` (길이 `50` bytes)
- VA: `0x000000014064F3EC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0064F413` → [Feature_218004792__private_IsEnabledFallback](Feature_218004792__private_IsEnabledFallback_function_0064F424.md) (function, `0x0064F424`)

### Direct callers
- [EtwpFreePlaceholderList](../46/EtwpFreePlaceholderList_function_0046CF3C.md) at `0x0046CF45`
- [EtwpFreePlaceholderList](../46/EtwpFreePlaceholderList_function_0046CF3C.md) at `0x0046CF57`
- [EtwpInitializeCompression](../4E/EtwpInitializeCompression_function_004EC774.md) at `0x004EC853`
- [EtwpCompressBuffer](../65/EtwpCompressBuffer_function_00652DBC.md) at `0x00652DF7`
- [EtwpCompressPendingBuffers](../65/EtwpCompressPendingBuffers_function_00653140.md) at `0x006531AE`
- [EtwpCompressionDpc](../65/EtwpCompressionDpc_function_00653290.md) at `0x006532A4`
- [EtwpGetPlaceholderBuffer](../65/EtwpGetPlaceholderBuffer_function_00653694.md) at `0x0065369D`
- [EtwpInsertPlaceholderBuffer](../65/EtwpInsertPlaceholderBuffer_function_00653718.md) at `0x00653729`
- [EtwpRotateCompressionTarget](../65/EtwpRotateCompressionTarget_function_00653868.md) at `0x006538BB`
- [EtwpFreeTraceBufferPool](../../page/9C/EtwpFreeTraceBufferPool_function_009C1A74.md) at `0x009C1BE7`

### Static image references
- `0x0064F3F6` → RVA `0x00FC4BC8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064F3EC  48 83 EC 28                     sub rsp, 0x28
0064F3F0  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0064F3F6  8B 05 CC 57 97 00               mov eax, dword ptr [rip + 0x9757cc]
0064F3FC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0064F400  A8 10                           test al, 0x10
0064F402  74 05                           je 0x14064f409
0064F404  83 E0 01                        and eax, 1
0064F407  EB 0F                           jmp 0x14064f418
0064F409  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0064F40E  BA 03 00 00 00                  mov edx, 3
0064F413  E8 0C 00 00 00                  call 0x14064f424
0064F418  48 83 C4 28                     add rsp, 0x28
0064F41C  C3                              ret
0064F41D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_218004792__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9918412)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9918412)))) & (16)) == 0) goto loc_0064F409;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9918412))) & (1));
    goto loc_0064F418;
loc_0064F409:
    result = Feature_218004792__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0064F418:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_218004792__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9757CC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9757CC)))) & (16)) == 0) goto loc_0064F409;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9757CC))) & (1));
    goto loc_0064F418;
loc_0064F409:
    result = Feature_218004792__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0064F418:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064F3EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064F3EC[BB_0064F3EC]
  bb_0064F404[BB_0064F404]
  bb_0064F409[BB_0064F409]
  bb_0064F418[BB_0064F418]
  bb_0064F41D[BB_0064F41D]
  bb_0064F3EC -->|branch| bb_0064F409
  bb_0064F3EC -->|fallthrough| bb_0064F404
  bb_0064F404 -->|branch| bb_0064F418
  bb_0064F409 -->|flow| bb_0064F418
```
