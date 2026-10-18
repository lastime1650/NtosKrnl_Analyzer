# MiLogMapFileEvent

- RVA: `0x0097E0FC`–`0x0097E153` (길이 `87` bytes)
- VA: `0x000000014097E0FC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009757C`
- 디코드: `24`개 명령, `87/87` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0097E12C` → [MiFillMapFileInfo](MiFillMapFileInfo_function_0097E15C.md) (function, `0x0097E15C`)
- `0x0097E14C` → [MiLogPerfMemoryEvent](../../text/23/MiLogPerfMemoryEvent_function_002369C8.md) (function, `0x002369C8`)

### Direct callers
- [MiUnmapVad](../88/MiUnmapVad_function_00889280.md) at `0x00889378`
- [MiMapViewOfImageSection](MiMapViewOfImageSection_function_0097E92C.md) at `0x0097F4DC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0097E14C` → [MiLogPerfMemoryEvent](../../text/23/MiLogPerfMemoryEvent_function_002369C8.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0097E0FC  40 53                           push rbx
0097E0FE  48 83 EC 60                     sub rsp, 0x60
0097E102  8B 41 30                        mov eax, dword ptr [rcx + 0x30]
0097E105  0F 57 C0                        xorps xmm0, xmm0
0097E108  24 70                           and al, 0x70
0097E10A  0F B7 DA                        movzx ebx, dx
0097E10D  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
0097E112  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
0097E117  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
0097E11C  3C 10                           cmp al, 0x10
0097E11E  75 07                           jne 0x14097e127
0097E120  48 83 C4 60                     add rsp, 0x60
0097E124  5B                              pop rbx
0097E125  C3                              ret
0097E126  CC                              int3
0097E127  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
0097E12C  E8 2B 00 00 00                  call 0x14097e15c
0097E131  41 B9 2C 00 00 00               mov r9d, 0x2c
0097E137  C7 44 24 20 03 19 50 00         mov dword ptr [rsp + 0x20], 0x501903
0097E13F  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
0097E144  BA 00 80 00 00                  mov edx, 0x8000
0097E149  0F B7 CB                        movzx ecx, bx
0097E14C  E8 77 88 8B FF                  call 0x1402369c8
0097E151  EB CD                           jmp 0x14097e120
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLogMapFileEvent(__int64 a1, unsigned __int16 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p30;

    v_rsp = (v_rsp) - (96);
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(a1 + 48))) & (112));
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm0;
    v_stack_m18 = v_xmm0;
    if (((unsigned __int8)(result)) != 16) goto loc_0097E127;
loc_0097E120:
    v_rsp = (v_rsp) + (96);
    return result;
loc_0097E127:
    result = MiFillMapFileInfo(a1, v_stack_p30, a3, a4);
    v_stack_p20 = 0x501903ULL;
    result = MiLogPerfMemoryEvent(a2, (unsigned int)(0x8000ULL), v_stack_p30, 44);
    goto loc_0097E120;
}
```

## 5. (Beta) C Style

```c
int64_t MiLogMapFileEvent(void *Arg1, uint16_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_p20;
    uint64_t v_stack_p30;

    local_rsp = (local_rsp) - (96);
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x30))) & (112));
    v_stack_m38 = v_xmm0;
    v_stack_m28 = v_xmm0;
    v_stack_m18 = v_xmm0;
    if (((uint8_t)(result)) != 16) goto loc_0097E127;
loc_0097E120:
    local_rsp = (local_rsp) + (96);
    return result;
loc_0097E127:
    result = MiFillMapFileInfo(Arg1, v_stack_p30, a3, a4);
    v_stack_p20 = 0x501903ULL;
    result = MiLogPerfMemoryEvent(Arg2, (uint32_t)(0x8000ULL), v_stack_p30, 44);
    goto loc_0097E120;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0097E0FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0097E0FC[BB_0097E0FC]
  bb_0097E120[BB_0097E120]
  bb_0097E126[BB_0097E126]
  bb_0097E127[BB_0097E127]
  bb_0097E0FC -->|branch| bb_0097E127
  bb_0097E0FC -->|fallthrough| bb_0097E120
  bb_0097E126 -->|flow| bb_0097E127
  bb_0097E127 -->|branch| bb_0097E120
```
