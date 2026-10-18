# PspIsSessionLeaderProcess

- RVA: `0x00A8F728`–`0x00A8F748` (길이 `32` bytes)
- VA: `0x0000000140A8F728`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A8F72F` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- [PsIsSessionLeaderProcess](../../text/4B/PsIsSessionLeaderProcess_function_004B5020.md) at `0x004B5024`
- [PspInitializeSessionGlobals](../70/PspInitializeSessionGlobals_function_007005B8.md) at `0x007005F2`
- [PspInitializeSessionGlobals](../70/PspInitializeSessionGlobals_function_007005B8.md) at `0x0070064D`
- [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A14C2D`
- [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A15B70`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A8F72F` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8F728  48 83 EC 28                     sub rsp, 0x28
00A8F72C  4C 8B C1                        mov r8, rcx
00A8F72F  E8 BC EA 86 FF                  call 0x1402fe1f0
00A8F734  33 D2                           xor edx, edx
00A8F736  4C 3B 80 48 03 00 00            cmp r8, qword ptr [rax + 0x348]
00A8F73D  0F 94 C2                        sete dl
00A8F740  8B C2                           mov eax, edx
00A8F742  48 83 C4 28                     add rsp, 0x28
00A8F746  C3                              ret
00A8F747  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspIsSessionLeaderProcess(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsGetCurrentServerSiloGlobals(a1, a2, a1, a4);
    a2 = 0;
    a2 = (a1 == (*(unsigned __int64 *)(result + 840))) ? 1 : 0;
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(a2);
}
```

## 5. (Beta) C Style

```c
int64_t PspIsSessionLeaderProcess(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsGetCurrentServerSiloGlobals(Arg1, Arg2, Arg1, a4);
    Arg2 = 0;
    Arg2 = (Arg1 == (*(uint64_t *)(result + 0x348))) ? 1 : 0;
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(Arg2);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8F728&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8F728[BB_00A8F728]
  bb_00A8F747[BB_00A8F747]
```
