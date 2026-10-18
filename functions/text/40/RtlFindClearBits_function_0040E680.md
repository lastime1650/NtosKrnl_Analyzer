# RtlFindClearBits

- RVA: `0x0040E680`–`0x0040E6B6` (길이 `54` bytes)
- VA: `0x000000014040E680`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009B988`
- 디코드: `17`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiReserveBestDriverRange](../../page/7F/MiReserveBestDriverRange_function_007F92E0.md) at `0x007F9317`
- [MiReserveBestDriverRange](../../page/7F/MiReserveBestDriverRange_function_007F92E0.md) at `0x007F93A4`
- [MiReserveExistingDriverPtes](../../page/AF/MiReserveExistingDriverPtes_function_00AF84DC.md) at `0x00AF853C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0040E6B0` → [sub_0040E9FC](Unknown_function_0040E9FC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0040E680  40 56                           push rsi
0040E682  41 54                           push r12
0040E684  41 55                           push r13
0040E686  41 56                           push r14
0040E688  48 83 EC 18                     sub rsp, 0x18
0040E68C  44 8B 29                        mov r13d, dword ptr [rcx]
0040E68F  45 33 DB                        xor r11d, r11d
0040E692  45 3B C5                        cmp r8d, r13d
0040E695  45 8B F3                        mov r14d, r11d
0040E698  45 8B E0                        mov r12d, r8d
0040E69B  8B F2                           mov esi, edx
0040E69D  45 0F 42 F0                     cmovb r14d, r8d
0040E6A1  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
0040E6A5  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
0040E6AA  45 8D 4D FF                     lea r9d, [r13 - 1]
0040E6AE  85 D2                           test edx, edx
0040E6B0  0F 84 46 03 00 00               je 0x14040e9fc
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall RtlFindClearBits(__int64 a1, int a2, int a3)
{
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (24);
    v_r11 = 0;
    v_r14 = 0;
    if (a3 < ((unsigned int)((unsigned int)(*(unsigned int *)(a1))))) { v_r14 = a3; }
    v_stack_p8 = *(unsigned __int64 *)(a1 + 8);
}
```

## 5. (Beta) C Style

```c
void RtlFindClearBits(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (24);
    local_r11 = 0;
    local_r14 = 0;
    if (Arg3 < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))))) { local_r14 = Arg3; }
    v_stack_p8 = *(uint64_t *)(arg1 + 0x8);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0040E680&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0040E680[BB_0040E680]
```
