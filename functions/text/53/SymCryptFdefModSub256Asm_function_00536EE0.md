# SymCryptFdefModSub256Asm

- RVA: `0x00536EE0`–`0x00536F51` (길이 `113` bytes)
- VA: `0x0000000140536EE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3520`
- 디코드: `30`개 명령, `113/113` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00536EE0  48 56                           push rsi
00536EE2  57                              push rdi
00536EE3  48 81 C1 80 00 00 00            add rcx, 0x80
00536EEA  48 8B 02                        mov rax, qword ptr [rdx]
00536EED  49 2B 00                        sub rax, qword ptr [r8]
00536EF0  4C 8B 52 08                     mov r10, qword ptr [rdx + 8]
00536EF4  4D 1B 50 08                     sbb r10, qword ptr [r8 + 8]
00536EF8  4C 8B 5A 10                     mov r11, qword ptr [rdx + 0x10]
00536EFC  4D 1B 58 10                     sbb r11, qword ptr [r8 + 0x10]
00536F00  48 8B 72 18                     mov rsi, qword ptr [rdx + 0x18]
00536F04  49 1B 70 18                     sbb rsi, qword ptr [r8 + 0x18]
00536F08  48 C7 C2 00 00 00 00            mov rdx, 0
00536F0F  48 0F 42 11                     cmovb rdx, qword ptr [rcx]
00536F13  49 C7 C0 00 00 00 00            mov r8, 0
00536F1A  4C 0F 42 41 08                  cmovb r8, qword ptr [rcx + 8]
00536F1F  48 C7 C7 00 00 00 00            mov rdi, 0
00536F26  48 0F 42 79 10                  cmovb rdi, qword ptr [rcx + 0x10]
00536F2B  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
00536F2F  48 0F 43 CA                     cmovae rcx, rdx
00536F33  48 03 C2                        add rax, rdx
00536F36  4D 13 D0                        adc r10, r8
00536F39  4C 13 DF                        adc r11, rdi
00536F3C  48 13 F1                        adc rsi, rcx
00536F3F  49 89 01                        mov qword ptr [r9], rax
00536F42  4D 89 51 08                     mov qword ptr [r9 + 8], r10
00536F46  4D 89 59 10                     mov qword ptr [r9 + 0x10], r11
00536F4A  49 89 71 18                     mov qword ptr [r9 + 0x18], rsi
00536F4E  5F                              pop rdi
00536F4F  5E                              pop rsi
00536F50  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefModSub256Asm(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rdi;

    a1 = (a1) + (128);
    result = (*(unsigned __int64 *)(a2)) - (*(unsigned __int64 *)(a3));
    a2 = 0;
    if (condition_is_below) { a2 = *(unsigned __int64 *)(a1); }
    a3 = 0;
    if (condition_is_below) { a3 = *(unsigned __int64 *)(a1 + 8); }
    v_rdi = 0;
    if (condition_is_below) { v_rdi = *(unsigned __int64 *)(a1 + 16); }
    a1 = *(unsigned __int64 *)(a1 + 24);
    if (condition_is_above_or_equal) { a1 = a2; }
    result = (result) + (a2);
    *(unsigned __int64 *)(a4) = result;
    *(unsigned __int64 *)(a4 + 8) = *(unsigned __int64 *)(a2 + 8);
    *(unsigned __int64 *)(a4 + 16) = *(unsigned __int64 *)(a2 + 16);
    *(unsigned __int64 *)(a4 + 24) = *(unsigned __int64 *)(a2 + 24);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefModSub256Asm(void *Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rdi;

    Arg1 = (Arg1) + (128);
    result = (*(uint64_t *)(arg2)) - (*(uint64_t *)(arg3));
    Arg2 = 0;
    if (condition_is_below) { Arg2 = *(uint64_t *)(arg1); }
    Arg3 = 0;
    if (condition_is_below) { Arg3 = *(uint64_t *)(arg1 + 0x8); }
    local_rdi = 0;
    if (condition_is_below) { local_rdi = *(uint64_t *)(arg1 + 0x10); }
    Arg1 = *(uint64_t *)(arg1 + 0x18);
    if (condition_is_above_or_equal) { Arg1 = Arg2; }
    result = (result) + (Arg2);
    *(uint64_t *)(arg4) = result;
    *(uint64_t *)(arg4 + 0x8) = *(uint64_t *)(arg2 + 0x8);
    *(uint64_t *)(arg4 + 0x10) = *(uint64_t *)(arg2 + 0x10);
    *(uint64_t *)(arg4 + 0x18) = *(uint64_t *)(arg2 + 0x18);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x18` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x8` | `64` | `W` |
| `Arg4` | `+ 0x10` | `64` | `W` |
| `Arg4` | `+ 0x18` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00536EE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00536EE0[BB_00536EE0]
```
