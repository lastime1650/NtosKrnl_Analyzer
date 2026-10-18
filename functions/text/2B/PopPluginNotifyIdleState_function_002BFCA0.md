# PopPluginNotifyIdleState

- RVA: `0x002BFCA0`–`0x002BFD2D` (길이 `141` bytes)
- VA: `0x00000001402BFCA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E540`
- 디코드: `42`개 명령, `141/141` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002BFCE8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x002BFD22` → [PopFxAddLogEntry](../39/PopFxAddLogEntry_function_00390B94.md) (function, `0x00390B94`)

### Direct callers
- [PopPepStartComponentIdleStateChangeActivity](PopPepStartComponentIdleStateChangeActivity_function_002BE7C0.md) at `0x002BE8FB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002BFCA0  4C 8B DC                        mov r11, rsp
002BFCA3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
002BFCA7  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
002BFCAB  57                              push rdi
002BFCAC  48 83 EC 40                     sub rsp, 0x40
002BFCB0  48 8B 41 48                     mov rax, qword ptr [rcx + 0x48]
002BFCB4  33 F6                           xor esi, esi
002BFCB6  4C 8B 51 40                     mov r10, qword ptr [rcx + 0x40]
002BFCBA  8B FA                           mov edi, edx
002BFCBC  89 74 24 32                     mov dword ptr [rsp + 0x32], esi
002BFCC0  48 8B D9                        mov rbx, rcx
002BFCC3  66 89 74 24 36                  mov word ptr [rsp + 0x36], si
002BFCC8  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
002BFCCC  8D 4E 13                        lea ecx, [rsi + 0x13]
002BFCCF  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
002BFCD3  49 8D 53 D8                     lea rdx, [r11 - 0x28]
002BFCD7  45 89 43 E4                     mov dword ptr [r11 - 0x1c], r8d
002BFCDB  45 88 4B E8                     mov byte ptr [r11 - 0x18], r9b
002BFCDF  40 88 74 24 31                  mov byte ptr [rsp + 0x31], sil
002BFCE4  49 8B 42 60                     mov rax, qword ptr [r10 + 0x60]
002BFCE8  E8 E3 AD 3F 00                  call 0x1406baad0
002BFCED  0F B6 4C 24 31                  movzx ecx, byte ptr [rsp + 0x31]
002BFCF2  8D 56 01                        lea edx, [rsi + 1]
002BFCF5  84 C0                           test al, al
002BFCF7  0F 44 CA                        cmove ecx, edx
002BFCFA  88 4C 24 31                     mov byte ptr [rsp + 0x31], cl
002BFCFE  84 C9                           test cl, cl
002BFD00  74 13                           je 0x1402bfd15
002BFD02  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
002BFD07  8A C1                           mov al, cl
002BFD09  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
002BFD0E  48 83 C4 40                     add rsp, 0x40
002BFD12  5F                              pop rdi
002BFD13  C3                              ret
002BFD14  CC                              int3
002BFD15  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
002BFD19  45 33 C9                        xor r9d, r9d
002BFD1C  8B D7                           mov edx, edi
002BFD1E  45 8D 41 12                     lea r8d, [r9 + 0x12]
002BFD22  E8 6D 0E 0D 00                  call 0x140390b94
002BFD27  8A 4C 24 31                     mov cl, byte ptr [rsp + 0x31]
002BFD2B  EB D5                           jmp 0x1402bfd02
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPluginNotifyIdleState(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int16 v_stack_m12;
    unsigned int v_stack_m16;
    unsigned __int8 v_stack_m17;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p31;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (64);
    v_rsi = 0;
    v_stack_m16 = 0;
    v_stack_m12 = 0;
    *(unsigned __int64 *)(v_rsp - 40) = *(unsigned __int64 *)(a1 + 72);
    v_stack_m20 = a2;
    *(unsigned int *)(v_rsp - 28) = a3;
    *(unsigned __int8 *)(v_rsp - 24) = (unsigned __int8)(a4);
    v_stack_m17 = 0;
    result = guard_dispatch_icall(v_rsi + 19, v_rsp - 40, a3, a4);
    a1 = v_stack_m17;
    if ((unsigned __int8)(result) == 0) { a1 = (unsigned int)(v_rsi + 1); }
    v_stack_m17 = (unsigned __int8)(a1);
    if ((unsigned __int8)(a1) == 0) goto loc_002BFD15;
loc_002BFD02:
    v_rsp = (v_rsp) + (64);
    return (unsigned __int8)(a1);
loc_002BFD15:
    a4 = 0;
    result = PopFxAddLogEntry(*(unsigned __int64 *)(v_stack_p8 + 48), (unsigned int)((unsigned int)((unsigned int)(a2))), a4 + 18, a4);
    goto loc_002BFD02;
}
```

## 5. (Beta) C Style

```c
int64_t PopPluginNotifyIdleState(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint16_t v_stack_m12;
    uint32_t v_stack_m16;
    uint8_t v_stack_m17;
    uint32_t v_stack_m20;
    uint64_t v_stack_p10;
    uint8_t v_stack_p31;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (64);
    local_rsi = 0;
    v_stack_m16 = 0;
    v_stack_m12 = 0;
    *(uint64_t *)(local_rsp - 0x28) = *(uint64_t *)(arg1 + 0x48);
    v_stack_m20 = Arg2;
    *(uint32_t *)(local_rsp - 0x1C) = Arg3;
    *(uint8_t *)(local_rsp - 0x18) = (uint8_t)(Arg4);
    v_stack_m17 = 0;
    result = guard_dispatch_icall(local_rsi + 19, local_rsp - 40, Arg3, Arg4);
    Arg1 = v_stack_m17;
    if ((uint8_t)(result) == 0) { Arg1 = (uint32_t)(local_rsi + 1); }
    v_stack_m17 = (uint8_t)(Arg1);
    if ((uint8_t)(Arg1) == 0) goto loc_002BFD15;
loc_002BFD02:
    local_rsp = (local_rsp) + (64);
    return (uint8_t)(Arg1);
loc_002BFD15:
    Arg4 = 0;
    result = PopFxAddLogEntry(*(uint64_t *)(v_stack_p8 + 0x30), (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4 + 18, Arg4);
    goto loc_002BFD02;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002BFCA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002BFCA0[BB_002BFCA0]
  bb_002BFD02[BB_002BFD02]
  bb_002BFD14[BB_002BFD14]
  bb_002BFD15[BB_002BFD15]
  bb_002BFCA0 -->|branch| bb_002BFD15
  bb_002BFCA0 -->|fallthrough| bb_002BFD02
  bb_002BFD14 -->|flow| bb_002BFD15
  bb_002BFD15 -->|branch| bb_002BFD02
```
