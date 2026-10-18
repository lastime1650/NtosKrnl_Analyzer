# MiFinalizeKernelScpForSystemImage

- RVA: `0x00AA02F8`–`0x00AA0340` (길이 `72` bytes)
- VA: `0x0000000140AA02F8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B95C`
- 디코드: `23`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AA0310` → [MiMapKernelScp](../../text/4D/MiMapKernelScp_function_004DCAD4.md) (function, `0x004DCAD4`)
- `0x00AA031D` → [MiMarkKernelImageRetpolineBits](MiMarkKernelImageRetpolineBits_function_00AA0348.md) (function, `0x00AA0348`)
- `0x00AA0339` → [MiLogRetpolineImageLoadEvents](../A9/MiLogRetpolineImageLoadEvents_function_00A996F0.md) (function, `0x00A996F0`)

### Direct callers
- [MmLoadSystemImageEx](../99/MmLoadSystemImageEx_function_00999B8C.md) at `0x00999FBC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AA0310` → [MiMapKernelScp](../../text/4D/MiMapKernelScp_function_004DCAD4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA02F8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AA02FD  57                              push rdi
00AA02FE  48 83 EC 20                     sub rsp, 0x20
00AA0302  8B 51 40                        mov edx, dword ptr [rcx + 0x40]
00AA0305  48 8B D9                        mov rbx, rcx
00AA0308  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00AA030C  48 C1 EA 0C                     shr rdx, 0xc
00AA0310  E8 BF C7 A3 FF                  call 0x1404dcad4
00AA0315  BA 01 00 00 00                  mov edx, 1
00AA031A  48 8B CB                        mov rcx, rbx
00AA031D  E8 26 00 00 00                  call 0x140aa0348
00AA0322  8B F8                           mov edi, eax
00AA0324  85 C0                           test eax, eax
00AA0326  79 0E                           jns 0x140aa0336
00AA0328  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00AA032D  8B C7                           mov eax, edi
00AA032F  48 83 C4 20                     add rsp, 0x20
00AA0333  5F                              pop rdi
00AA0334  C3                              ret
00AA0335  CC                              int3
00AA0336  48 8B CB                        mov rcx, rbx
00AA0339  E8 B2 93 FF FF                  call 0x140a996f0
00AA033E  EB E8                           jmp 0x140aa0328
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFinalizeKernelScpForSystemImage(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a2 = ((unsigned int)(*(unsigned int *)(a1 + 64))) >> (12);
    result = MiMapKernelScp(*(unsigned __int64 *)(a1 + 48), a2, a3, a4);
    result = MiMarkKernelImageRetpolineBits(a1, 1, a3, a4);
    if (!sign_flag) goto loc_00AA0336;
loc_00AA0328:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00AA0336:
    result = MiLogRetpolineImageLoadEvents(v_stack_p8, 1, a3, a4);
    goto loc_00AA0328;
}
```

## 5. (Beta) C Style

```c
int64_t MiFinalizeKernelScpForSystemImage(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    a2 = ((uint32_t)(*(uint32_t *)(arg1 + 0x40))) >> (12);
    result = MiMapKernelScp(*(uint64_t *)(arg1 + 0x30), a2, a3, a4);
    result = MiMarkKernelImageRetpolineBits(Arg1, 1, a3, a4);
    if (!sign_flag) goto loc_00AA0336;
loc_00AA0328:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00AA0336:
    result = MiLogRetpolineImageLoadEvents(v_stack_p8, 1, a3, a4);
    goto loc_00AA0328;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA02F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA02F8[BB_00AA02F8]
  bb_00AA0328[BB_00AA0328]
  bb_00AA0335[BB_00AA0335]
  bb_00AA0336[BB_00AA0336]
  bb_00AA02F8 -->|branch| bb_00AA0336
  bb_00AA02F8 -->|fallthrough| bb_00AA0328
  bb_00AA0335 -->|flow| bb_00AA0336
  bb_00AA0336 -->|branch| bb_00AA0328
```
