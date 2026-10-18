# PsInitializeThreadRngState

- RVA: `0x0048975C`–`0x004897DE` (길이 `130` bytes)
- VA: `0x000000014048975C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000789BC`
- 디코드: `29`개 명령, `130/130` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004897CC` → [RtlInitializeTRng](RtlInitializeTRng_function_004897E4.md) (function, `0x004897E4`)

### Direct callers
- [KiAllocatePrcbThread](../5B/KiAllocatePrcbThread_function_005B9130.md) at `0x005B934F`
- [KiInitializeAndStartInitialThread](../5C/KiInitializeAndStartInitialThread_function_005C42A4.md) at `0x005C4415`
- [PspAllocateThread](../../page/9E/PspAllocateThread_function_009EF72C.md) at `0x009EFE37`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048975C  48 83 EC 38                     sub rsp, 0x38
00489760  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
00489769  4C 8B C9                        mov r9, rcx
0048976C  4C 8B 81 10 05 00 00            mov r8, qword ptr [rcx + 0x510]
00489773  4C 33 81 08 05 00 00            xor r8, qword ptr [rcx + 0x508]
0048977A  4C 33 81 C0 04 00 00            xor r8, qword ptr [rcx + 0x4c0]
00489781  4C 33 81 F0 00 00 00            xor r8, qword ptr [rcx + 0xf0]
00489788  4C 33 41 28                     xor r8, qword ptr [rcx + 0x28]
0048978C  4C 33 C2                        xor r8, rdx
0048978F  4C 33 C1                        xor r8, rcx
00489792  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00489797  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
004897A0  0F 31                           rdtsc
004897A2  48 C1 E2 20                     shl rdx, 0x20
004897A6  48 0B D0                        or rdx, rax
004897A9  8B 81 40 86 00 00               mov eax, dword ptr [rcx + 0x8640]
004897AF  48 33 D0                        xor rdx, rax
004897B2  48 8D 44 24 20                  lea rax, [rsp + 0x20]
004897B7  48 33 54 24 20                  xor rdx, qword ptr [rsp + 0x20]
004897BC  48 33 D0                        xor rdx, rax
004897BF  48 83 FA 01                     cmp rdx, 1
004897C3  72 12                           jb 0x1404897d7
004897C5  49 8D 89 60 07 00 00            lea rcx, [r9 + 0x760]
004897CC  E8 13 00 00 00                  call 0x1404897e4
004897D1  48 83 C4 38                     add rsp, 0x38
004897D5  C3                              ret
004897D6  CC                              int3
004897D7  BA 01 00 00 00                  mov edx, 1
004897DC  EB E7                           jmp 0x1404897c5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsInitializeThreadRngState(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a3 = (*(unsigned __int64 *)(a1 + 1296)) ^ (*(unsigned __int64 *)(a1 + 1288));
    a3 = (a3) ^ (*(unsigned __int64 *)(a1 + 1216));
    a3 = (a3) ^ (*(unsigned __int64 *)(a1 + 240));
    a3 = (a3) ^ (*(unsigned __int64 *)(a1 + 40));
    a3 = (a3) ^ (*(unsigned __int64 *)(gs_base + (0 + 392)));
    a3 = (a3) ^ (a1);
    v_stack_m18 = a3;
    a2 = (*(unsigned __int64 *)(gs_base + (0 + 392))) << (32);
    a2 = (a2) | (result);
    a2 = (a2) ^ ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34368)));
    a2 = (a2) ^ (v_stack_m18);
    a2 = (a2) ^ (v_stack_m18);
    if (a2 < 1) goto loc_004897D7;
loc_004897C5:
    result = RtlInitializeTRng(a1 + 1888, a2, a3, a1);
    v_rsp = (v_rsp) + (56);
    return result;
loc_004897D7:
    goto loc_004897C5;
}
```

## 5. (Beta) C Style

```c
int64_t PsInitializeThreadRngState(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    a3 = (*(uint64_t *)(arg1 + 0x510)) ^ (*(uint64_t *)(arg1 + 0x508));
    a3 = (a3) ^ (*(uint64_t *)(arg1 + 0x4C0));
    a3 = (a3) ^ (*(uint64_t *)(arg1 + 0xF0));
    a3 = (a3) ^ (*(uint64_t *)(arg1 + 0x28));
    a3 = (a3) ^ (*(uint64_t *)(gs_base + (0 + 0x188)));
    a3 = (a3) ^ (Arg1);
    v_stack_m18 = a3;
    a2 = (*(uint64_t *)(gs_base + (0 + 0x188))) << (32);
    a2 = (a2) | (result);
    a2 = (a2) ^ ((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x8640)));
    a2 = (a2) ^ (v_stack_m18);
    a2 = (a2) ^ (v_stack_m18);
    if (a2 < 1) goto loc_004897D7;
loc_004897C5:
    result = RtlInitializeTRng(Arg1 + 1888, a2, a3, Arg1);
    local_rsp = (local_rsp) + (56);
    return result;
loc_004897D7:
    goto loc_004897C5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0xF0` | `64` | `R` |
| `Arg1` | `+ 0x4C0` | `64` | `R` |
| `Arg1` | `+ 0x508` | `64` | `R` |
| `Arg1` | `+ 0x510` | `64` | `R` |
| `Arg1` | `+ 0x760` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048975C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048975C[BB_0048975C]
  bb_004897C5[BB_004897C5]
  bb_004897D6[BB_004897D6]
  bb_004897D7[BB_004897D7]
  bb_0048975C -->|branch| bb_004897D7
  bb_0048975C -->|fallthrough| bb_004897C5
  bb_004897D6 -->|flow| bb_004897D7
  bb_004897D7 -->|branch| bb_004897C5
```
