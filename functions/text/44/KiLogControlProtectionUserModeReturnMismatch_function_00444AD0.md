# KiLogControlProtectionUserModeReturnMismatch

- RVA: `0x00444AD0`–`0x00444B26` (길이 `86` bytes)
- VA: `0x0000000140444AD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073EA0`
- 디코드: `25`개 명령, `86/86` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00444AFD` → [KiShouldLogUserModeReturnMismatch](../../page/A4/KiShouldLogUserModeReturnMismatch_function_00A46E10.md) (function, `0x00A46E10`)
- `0x00444B1F` → [EtwTimLogControlProtectionUserModeReturnMismatch](../../page/7B/EtwTimLogControlProtectionUserModeReturnMismatch_function_007BA9D4.md) (function, `0x007BA9D4`)

### Direct callers
- [KiProcessControlProtection](KiProcessControlProtection_function_00444750.md) at `0x00444A7B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00444AFD` → [KiShouldLogUserModeReturnMismatch](../../page/A4/KiShouldLogUserModeReturnMismatch_function_00A46E10.md) (`.text` → `PAGE`)
  - `0x00444B1F` → [EtwTimLogControlProtectionUserModeReturnMismatch](../../page/7B/EtwTimLogControlProtectionUserModeReturnMismatch_function_007BA9D4.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00444AD0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00444AD5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00444ADA  57                              push rdi
00444ADB  48 83 EC 20                     sub rsp, 0x20
00444ADF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00444AE8  49 8B D8                        mov rbx, r8
00444AEB  4D 8B 40 08                     mov r8, qword ptr [r8 + 8]
00444AEF  8B F9                           mov edi, ecx
00444AF1  8B D1                           mov edx, ecx
00444AF3  48 8B B0 20 02 00 00            mov rsi, qword ptr [rax + 0x220]
00444AFA  48 8B CE                        mov rcx, rsi
00444AFD  E8 0E 23 60 00                  call 0x140a46e10
00444B02  84 C0                           test al, al
00444B04  75 11                           jne 0x140444b17
00444B06  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00444B0B  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00444B10  48 83 C4 20                     add rsp, 0x20
00444B14  5F                              pop rdi
00444B15  C3                              ret
00444B16  CC                              int3
00444B17  4C 8B C3                        mov r8, rbx
00444B1A  48 8B D6                        mov rdx, rsi
00444B1D  8B CF                           mov ecx, edi
00444B1F  E8 B0 5E 37 00                  call 0x1407ba9d4
00444B24  EB E0                           jmp 0x140444b06
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiLogControlProtectionUserModeReturnMismatch(int a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = KiShouldLogUserModeReturnMismatch(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), (unsigned int)(a1), *(unsigned __int64 *)(a3 + 8), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00444B17;
loc_00444B06:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00444B17:
    result = EtwTimLogControlProtectionUserModeReturnMismatch((unsigned int)((unsigned int)((unsigned int)(a1))), v_stack_p10, v_stack_p8, a4);
    goto loc_00444B06;
}
```

## 5. (Beta) C Style

```c
int64_t KiLogControlProtectionUserModeReturnMismatch(int32_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = KiShouldLogUserModeReturnMismatch(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), (uint32_t)(Arg1), *(uint64_t *)(arg3 + 0x8), a4);
    if ((uint8_t)(result) != 0) goto loc_00444B17;
loc_00444B06:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00444B17:
    result = EtwTimLogControlProtectionUserModeReturnMismatch((uint32_t)((uint32_t)((uint32_t)(Arg1))), v_stack_p10, v_stack_p8, a4);
    goto loc_00444B06;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00444AD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00444AD0[BB_00444AD0]
  bb_00444B06[BB_00444B06]
  bb_00444B16[BB_00444B16]
  bb_00444B17[BB_00444B17]
  bb_00444AD0 -->|branch| bb_00444B17
  bb_00444AD0 -->|fallthrough| bb_00444B06
  bb_00444B16 -->|flow| bb_00444B17
  bb_00444B17 -->|branch| bb_00444B06
```
