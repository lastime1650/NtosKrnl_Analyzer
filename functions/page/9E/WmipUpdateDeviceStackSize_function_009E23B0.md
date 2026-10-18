# WmipUpdateDeviceStackSize

- RVA: `0x009E23B0`–`0x009E23F8` (길이 `72` bytes)
- VA: `0x00000001409E23B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A3E24`
- 디코드: `21`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009E23CD` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x009E23E7` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (function, `0x00396810`)

### Direct callers
- [WmipForwardWmiIrp](WmipForwardWmiIrp_function_009E0DB4.md) at `0x009E0FDA`
- [WmipRegisterDevice](WmipRegisterDevice_function_009E2808.md) at `0x009E288E`

### Static image references
- `0x009E23BE` → RVA `0x00EFFA60` (`.data`; read)
- `0x009E23D2` → RVA `0x00EFFA98` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009E23CD` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x009E23E7` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009E23B0  40 53                           push rbx
009E23B2  48 83 EC 30                     sub rsp, 0x30
009E23B6  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
009E23BC  8A D9                           mov bl, cl
009E23BE  48 8D 0D 9B D6 51 00            lea rcx, [rip + 0x51d69b]
009E23C5  45 33 C9                        xor r9d, r9d
009E23C8  45 33 C0                        xor r8d, r8d
009E23CB  33 D2                           xor edx, edx
009E23CD  E8 DE C2 82 FF                  call 0x14020e6b0
009E23D2  48 8B 05 BF D6 51 00            mov rax, qword ptr [rip + 0x51d6bf]
009E23D9  38 58 4C                        cmp byte ptr [rax + 0x4c], bl
009E23DC  7C 15                           jl 0x1409e23f3
009E23DE  33 D2                           xor edx, edx
009E23E0  48 8D 0D 79 D6 51 00            lea rcx, [rip + 0x51d679]
009E23E7  E8 24 44 9B FF                  call 0x140396810
009E23EC  48 83 C4 30                     add rsp, 0x30
009E23F0  5B                              pop rbx
009E23F1  C3                              ret
009E23F2  CC                              int3
009E23F3  88 58 4C                        mov byte ptr [rax + 0x4c], bl
009E23F6  EB E6                           jmp 0x1409e23de
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WmipUpdateDeviceStackSize(unsigned __int8 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 5363355, a2, a3, a4);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 5363391) + 76)) < a1) goto loc_009E23F3;
loc_009E23DE:
    a2 = 0;
    result = KeReleaseMutex(v_rip + 5363321, a2, a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
loc_009E23F3:
    *(unsigned __int8 *)(result + 76) = a1;
    goto loc_009E23DE;
}
```

## 5. (Beta) C Style

```c
int64_t WmipUpdateDeviceStackSize(uint8_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 5363355, Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0x51D6BF) + 0x4C)) < Arg1) goto loc_009E23F3;
loc_009E23DE:
    Arg2 = 0;
    result = KeReleaseMutex(v_rip + 5363321, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (48);
    return result;
loc_009E23F3:
    *(uint8_t *)(result + 0x4C) = Arg1;
    goto loc_009E23DE;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009E23B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009E23B0[BB_009E23B0]
  bb_009E23DE[BB_009E23DE]
  bb_009E23F2[BB_009E23F2]
  bb_009E23F3[BB_009E23F3]
  bb_009E23B0 -->|branch| bb_009E23F3
  bb_009E23B0 -->|fallthrough| bb_009E23DE
  bb_009E23F2 -->|flow| bb_009E23F3
  bb_009E23F3 -->|branch| bb_009E23DE
```
