# PnpCtxRegOpenCurrentUserKey

- RVA: `0x00AB5E40`–`0x00AB5E6A` (길이 `42` bytes)
- VA: `0x0000000140AB5E40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EDE0`
- 디코드: `13`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AB5E56` → [SysCtxRegOpenCurrentUserKey](../8F/SysCtxRegOpenCurrentUserKey_function_008F455C.md) (function, `0x008F455C`)

### Direct callers
- [CmDeleteCommonClassRegKeyWorker](../82/CmDeleteCommonClassRegKeyWorker_function_008298F8.md) at `0x00829ACF`
- [CmDeleteDeviceInterfaceRegKeyWorker](../82/CmDeleteDeviceInterfaceRegKeyWorker_function_00829E1C.md) at `0x00829FE2`
- [CmDeleteDeviceContainerRegKeyWorker](../82/CmDeleteDeviceContainerRegKeyWorker_function_0082B15C.md) at `0x0082B2F3`
- [CmDeleteDevicePanelRegKeyWorker](../82/CmDeleteDevicePanelRegKeyWorker_function_0082E554.md) at `0x0082E6E7`
- [_CmDeleteDeviceRegKeyWorker](../A9/_CmDeleteDeviceRegKeyWorker_function_00A9200C.md) at `0x00A92251`
- [_CmOpenDevicePanelRegKeyWorker](../A9/_CmOpenDevicePanelRegKeyWorker_function_00A98434.md) at `0x00A9859E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB5E40  48 83 EC 28                     sub rsp, 0x28
00AB5E44  48 8B C1                        mov rax, rcx
00AB5E47  33 C9                           xor ecx, ecx
00AB5E49  48 85 C0                        test rax, rax
00AB5E4C  75 13                           jne 0x140ab5e61
00AB5E4E  33 D2                           xor edx, edx
00AB5E50  41 B8 00 00 00 02               mov r8d, 0x2000000
00AB5E56  E8 01 E7 E3 FF                  call 0x1408f455c
00AB5E5B  48 83 C4 28                     add rsp, 0x28
00AB5E5F  C3                              ret
00AB5E60  CC                              int3
00AB5E61  48 8B 88 E0 00 00 00            mov rcx, qword ptr [rax + 0xe0]
00AB5E68  EB E4                           jmp 0x140ab5e4e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpCtxRegOpenCurrentUserKey(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = 0;
    if (0 != 0) goto loc_00AB5E61;
loc_00AB5E4E:
    a2 = 0;
    result = SysCtxRegOpenCurrentUserKey(a1, a2, (unsigned int)(0x2000000ULL), a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_00AB5E61:
    goto loc_00AB5E4E;
}
```

## 5. (Beta) C Style

```c
int64_t PnpCtxRegOpenCurrentUserKey(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = 0;
    if (0 != 0) goto loc_00AB5E61;
loc_00AB5E4E:
    Arg2 = 0;
    result = SysCtxRegOpenCurrentUserKey(Arg1, Arg2, (uint32_t)(0x2000000ULL), a4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_00AB5E61:
    goto loc_00AB5E4E;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB5E40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB5E40[BB_00AB5E40]
  bb_00AB5E4E[BB_00AB5E4E]
  bb_00AB5E60[BB_00AB5E60]
  bb_00AB5E61[BB_00AB5E61]
  bb_00AB5E40 -->|branch| bb_00AB5E61
  bb_00AB5E40 -->|fallthrough| bb_00AB5E4E
  bb_00AB5E60 -->|flow| bb_00AB5E61
  bb_00AB5E61 -->|branch| bb_00AB5E4E
```
